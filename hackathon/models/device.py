"""Config models model."""

from netaddr import AddrFormatError, IPAddress
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from hackathon.models import Base
from hackathon.models.util import session_read, session_write
from hackathon.utils.gnmi import GNMIClient
from hackathon.utils.openconfig import create_access_interface, create_bgp_neighbor, create_p2p_interface, create_svi, \
    initialize_bgp, redistribute_connected_bgp


class ValidationError(Exception):
    """Validation Error."""


class DeviceModel(Base):  # type: ignore
    """ORM Device object."""

    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(255), unique=True, nullable=False)
    management_ip = Column(String(255), unique=True, nullable=False)
    role = Column(String, nullable=False)
    configs = relationship("ConfigModel")

    @staticmethod
    @session_write
    def create(hostname, management_ip, role, session=None):
        """Create a new device."""
        try:
            IPAddress(management_ip)
        except AddrFormatError:
            raise ValidationError('Invalid management IP')
        device = DeviceModel(hostname=hostname, management_ip=management_ip, role=role)
        session.add(device)
        return device

    def neighbors(self):
        return {config.key: config.schema for config in self.configs if 'BGP' in config.path}

    def interfaces(self):
        return {config.key: config.schema for config in self.configs if 'interfaces' in config.path}

    def vlans(self):
        return {config.key: config.schema for config in self.configs if config.key.startswith('Vlan')}

    @staticmethod
    @session_read
    def get(device_id=None, hostname=None, session=None):
        if device_id:
            return session.query(DeviceModel).get(device_id)
        else:
            return session.query(DeviceModel).filter_by(hostname=hostname).first()

    @staticmethod
    @session_read
    def all(session=None):
        return session.query(DeviceModel).all()

    def add_p2p_interface(self, name, remote_host, remote_port, ip_address):
        description = f'{remote_host} {remote_port}'
        ip, prefixlen = ip_address.split('/')
        path, key, schema = create_p2p_interface(name, description, ip, prefixlen)
        self.configs.append(ConfigModel(
            device=self,
            path=path,
            key=key,
            schema=schema
        ))

    def add_vlan(self, num, description, ip_address):
        ip, prefixlen = ip_address.split('/')
        path, key, schema = create_svi(num, description, ip, prefixlen)
        self.configs.append(ConfigModel(
            device=self,
            path=path,
            key=key,
            schema=schema
        ))

    def add_access_port(self, name, vlan, description=None):
        description = description or "HOST"
        path, key, schema = create_access_interface(name, description, vlan)
        self.configs.append(ConfigModel(
            device=self,
            path=path,
            key=key,
            schema=schema
        ))

    def initialize_bgp(self, asn):
        path, key, schema = initialize_bgp(asn)
        self.configs.append(ConfigModel(
            device=self,
            path=path,
            key=key,
            schema=schema
        ))

        path, key, schema = redistribute_connected_bgp()
        self.configs.append(ConfigModel(
            device=self,
            path=path,
            key=key,
            schema=schema
        ))

    def add_bgp_neighbor(self, neighbor_ip, neighbor_as, neighbor_hostname):
        path, key, schema = create_bgp_neighbor(neighbor_ip, neighbor_as, neighbor_hostname)
        self.configs.append(ConfigModel(
            device=self,
            path=path,
            key=key,
            schema=schema
        ))

    def sync(self):
        client = GNMIClient(host=self.management_ip)
        for config in self.configs:
            client.set(config.path, config.schema)


class ConfigModel(Base):
    """ORM Config Model"""

    __tablename__ = 'config'
    device_id = Column(Integer, ForeignKey('device.id'), primary_key=True)
    path = Column(String(255), primary_key=True)
    key = Column(String(255))
    schema = Column(Text, nullable=False)
    device = relationship("DeviceModel")
