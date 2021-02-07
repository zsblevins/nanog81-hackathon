"""Config models model."""

from netaddr import AddrFormatError, IPAddress
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from hackathon.models import Base, session
from hackathon.utils.gnmi import GNMIClient
from hackathon.utils.openconfig import create_access_interface, create_bgp_neighbor, create_p2p_interface, create_svi


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
    def create(hostname, management_ip, role):
        """Create a new device."""
        try:
            IPAddress(management_ip)
        except AddrFormatError:
            raise ValidationError('Invalid management IP')
        device = DeviceModel(hostname=hostname, management_ip=management_ip, role=role)
        session.add(device)
        session.commit()

    def neighbors(self):
        return {config.key: config.schema for config in self.configs.all() if 'BGP' in config.path}

    def interfaces(self):
        return {config.key: config.schema for config in self.configs.all() if 'interfaces' in config.path}

    def vlans(self):
        return {config.key: config.schema for config in self.configs.all() if config.key.startswith('Vlan')}

    @staticmethod
    def get(device_id):
        return session.query(DeviceModel).get(device_id)

    @staticmethod
    def all():
        return session.query(DeviceModel).all()

    @staticmethod
    def add_p2p_interface(hostname, name, remote_host, remote_port, ip_address):
        device = session.query(DeviceModel).filter_by(hostname=hostname).first()
        description = f'{remote_host} {remote_port}'
        ip, prefixlen = ip_address.split('/')
        path, key, schema = create_p2p_interface(name, description, ip, prefixlen)
        session.merge(ConfigModel(
            device=device,
            path=path,
            key=key,
            schema=schema
        ))
        session.commit()

    @staticmethod
    def add_vlan(hostname, num, description, ip_address):
        device = session.query(DeviceModel).filter_by(hostname=hostname).first()
        ip, prefixlen = ip_address.split('/')
        path, key, schema = create_svi(num, description, ip, prefixlen)
        session.merge(ConfigModel(
            device=device,
            path=path,
            key=key,
            schema=schema
        ))
        session.commit()

    @staticmethod
    def add_access_port(hostname, name, vlan, description=None):
        device = session.query(DeviceModel).filter_by(hostname=hostname).first()
        description = description or "HOST"
        path, key, schema = create_access_interface(name, description, vlan)
        session.merge(ConfigModel(
            device=device,
            path=path,
            key=key,
            schema=schema
        ))
        session.commit()

    @staticmethod
    def add_bgp_neighbor(hostname, neighbor_ip, neighbor_as, neighbor_hostname):
        device = session.query(DeviceModel).filter_by(hostname=hostname).first()
        path, key, schema = create_bgp_neighbor(neighbor_ip, neighbor_as, neighbor_hostname)
        session.merge(ConfigModel(
            device=device,
            path=path,
            key=key,
            schema=schema
        ))
        session.commit()

    @staticmethod
    def sync(hostname):
        device = session.query(DeviceModel).filter_by(hostname=hostname).first()
        client = GNMIClient(host=device.management_ip)
        for config in device.configs:
            client.set(config.path, config.schema)


class ConfigModel(Base):
    """ORM Config Model"""

    __tablename__ = 'config'
    device_id = Column(Integer, ForeignKey('device.id'), primary_key=True)
    path = Column(String(255), primary_key=True)
    key = Column(String(255))
    schema = Column(Text, nullable=False)
    device = relationship("DeviceModel")
