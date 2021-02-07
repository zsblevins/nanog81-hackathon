"""Config namespace."""

from flask_restx import Namespace, Resource, fields  # type: ignore

from hackathon.models.device import DeviceModel, ValidationError
from hackathon.tasks import add_vlan, provision_tor, update_access_port

api = Namespace("device", description="Device operations")

config_model = api.model(
    "Config",
    {
        "path": fields.String(required=True, description="OpenConfig Path"),
        "key": fields.String(required=True, description="Short key"),
        "schema": fields.String(required=True, description="OpenConfig Value")
    }
)

device_model = api.model(
    "Device",
    {
        "id": fields.Integer(
            readonly=True, description="The device unique identifier"
        ),
        "hostname": fields.String(required=True, description="Device hostname"),
        "role": fields.String(required=True, description="Device role"),
        "management_ip": fields.String(required=True, description="Device management IP"),
        "configs": fields.List(fields.Nested(config_model))
    },
)


@api.route("/")
class DeviceList(Resource):
    """Shows a list of all devices, and lets you POST to add new ones."""

    @api.marshal_list_with(device_model)
    def get(self):
        """List all devices."""
        return DeviceModel.all()

    @api.expect(device_model, validate=True)
    @api.marshal_with(device_model, code=201, mask=None)
    def post(self):
        """Create a new config."""
        try:
            device = DeviceModel.create(**api.payload)
            return device, 201
        except ValidationError as e:
            api.abort(400, e)


provision_tor_model = api.model(
    "ProvisionTor",
    {
        "hostname": fields.String(required=True, description="TOR hostname"),
        "management_ip": fields.String(required=True, description="TOR management IP"),
        "asn": fields.Integer(required=True, description="TOR ASN"),
        "cross_connect_net": fields.String(required=True, description="Core - TOR /31"),
        "core_hostname": fields.String(required=True, description="Core Router Hostname"),
        "core_port": fields.String(required=True, description="Core Router Port")
    },
)


@api.route("/provision_tor")
class ProvisionTOR(Resource):
    @api.expect(provision_tor_model, validate=True)
    def post(self):
        """Provision a new TOR device."""
        try:
            provision_tor(**api.payload)
            return 201
        except ValidationError as e:
            api.abort(400, e)


add_vlan_model = api.model(
    "AddVLAN",
    {
        "hostname": fields.String(required=True, description="TOR hostname"),
        "num": fields.Integer(required=True, description="VLAN Number"),
        "prefix": fields.String(required=True, description="VLAN IPv4 Prefix"),
        "description": fields.String(required=True, description="VLAN Description")
    }
)


@api.route("/add_vlan")
class AddVLAN(Resource):
    @api.expect(add_vlan_model, validate=True)
    def post(self):
        """Add a new SVI to a device."""
        try:
            add_vlan(**api.payload)
            return 201
        except ValidationError as e:
            api.abort(400, e)


port_flip_model = api.model(
    "EditAccessVlan",
    {
        "hostname": fields.String(required=True, description="TOR hostname"),
        "vlan": fields.Integer(required=True, description="Access VLAN"),
        "port": fields.String(required=True, description="Access Port"),
        "description": fields.String(required=False, description="Port Description")
    }
)


@api.route("/set_access_vlan")
class EditAccessVLAN(Resource):
    @api.expect(port_flip_model, validate=True)
    def post(self):
        """Set VLAN on Access Port."""
        try:
            update_access_port(**api.payload)
            return 201
        except ValidationError as e:
            api.abort(400, e)
