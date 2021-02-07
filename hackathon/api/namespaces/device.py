"""Config namespace."""

from flask_restx import Namespace, Resource, fields  # type: ignore
from netaddr import IPNetwork

from hackathon.models.device import DeviceModel, ValidationError

api = Namespace("device", description="Device operations")

device_model = api.model(
    "Device",
    {
        "id": fields.Integer(
            readonly=True, description="The device unique identifier"
        ),
        "hostname": fields.String(required=True, description="Device hostname"),
        "role": fields.String(required=True, description="Device role"),
        "management_ip": fields.String(required=True, description="Device management IP"),
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
        # Create TOR
        DeviceModel.create(hostname=api.payload['hostname'], management_ip=api.payload['management_ip'], role='tor')

        p2p_prefix = IPNetwork(api.payload['cross_connect_net'])
        if p2p_prefix.prefixlen != 31:
            api.abort(400, 'Expected a /31 for the cross connect')

        core_ip = str(p2p_prefix[0])
        core_net = f'{p2p_prefix[0]}/31'
        tor_ip = str(p2p_prefix[1])
        tor_net = f'{p2p_prefix[1]}/31'

        # Add P2P links on both devices
        DeviceModel.add_p2p_interface(
            hostname=api.payload['hostname'],
            name='Ethernet1',
            remote_host=api.payload['core_hostname'],
            remote_port=api.payload['core_port'],
            ip_address=tor_net
        )

        DeviceModel.add_p2p_interface(
            hostname=api.payload['core_hostname'],
            name=api.payload['core_port'],
            remote_host=api.payload['hostname'],
            remote_port='Ethernet1',
            ip_address=core_net
        )

        # Add BGP Neighbors
        DeviceModel.add_bgp_neighbor(
            hostname=api.payload['hostname'],
            neighbor_ip=core_ip,
            neighbor_as=64512,
            neighbor_hostname=api.payload['core_hostname']
        )

        DeviceModel.add_bgp_neighbor(
            hostname=api.payload['core_hostname'],
            neighbor_ip=tor_ip,
            neighbor_as=api.payload['asn'],
            neighbor_hostname=api.payload['hostname']
        )

        # Sync config on both devices
        DeviceModel.sync(api.payload['hostname'])
        DeviceModel.sync(api.payload['core_hostname'])
