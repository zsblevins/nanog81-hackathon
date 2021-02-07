"""Miscellaneous tasks."""
import logging

from netaddr import AddrFormatError, IPNetwork

from hackathon.models import get_session
from hackathon.models.device import DeviceModel, ValidationError
from hackathon.models.util import session_write
from hackathon.utils.openconfig import validate_bgp_state, validate_lldp_neighbor

LOG = logging.getLogger(__name__)

@session_write
def initialize_lab(include_tor2=False, session=None):
    devices = [
        {
            'hostname': 'core-rtr1',
            'management_ip': '192.168.123.2',
            'role': 'core'
        },
        {
            'hostname': 'core-rtr2',
            'management_ip': '192.168.123.3',
            'role': 'core'
        },
        {
            'hostname': 'tor1',
            'management_ip': '192.168.123.4',
            'role': 'tor'
        }
    ]
    if include_tor2:
        devices.append(
            {
                'hostname': 'tor2',
                'management_ip': '192.168.123.5',
                'role': 'tor'
            }
        )

    for device in devices:
        DeviceModel.create(**device, session=session)
    session.commit()

    # core-rtr1
    device = DeviceModel.get(hostname='core-rtr1', session=session)
    device.initialize_bgp(64512)
    device.add_p2p_interface(
        name='Ethernet1',
        remote_host='core-rtr2',
        remote_port='Ethernet1',
        ip_address='10.0.0.0/31'
    )
    device.add_bgp_neighbor(
        neighbor_ip='10.0.0.1',
        neighbor_as=64512,
        neighbor_hostname='core-rtr2'
    )

    device.add_p2p_interface(
        name='Ethernet9',
        remote_host='tor1',
        remote_port='Ethernet1',
        ip_address='10.0.1.0/31'
    )
    device.add_bgp_neighbor(
        neighbor_ip='10.0.1.1',
        neighbor_as=64513,
        neighbor_hostname='tor1'
    )
    device.sync()

    # core-rtr2
    device = DeviceModel.get(hostname='core-rtr2', session=session)
    device.initialize_bgp(64512)
    device.add_p2p_interface(
        name='Ethernet1',
        remote_host='core-rtr1',
        remote_port='Ethernet1',
        ip_address='10.0.0.1/31'
    )
    device.add_bgp_neighbor(
        neighbor_ip='10.0.0.0',
        neighbor_as=64512,
        neighbor_hostname='core-rtr1'
    )

    device.add_p2p_interface(
        name='Ethernet9',
        remote_host='tor2',
        remote_port='Ethernet1',
        ip_address='10.0.1.2/31'
    )
    device.add_bgp_neighbor(
        neighbor_ip='10.0.1.3',
        neighbor_as=64514,
        neighbor_hostname='tor2'
    )
    device.sync()

    # tor1
    device = DeviceModel.get(hostname='tor1', session=session)
    device.initialize_bgp(64513)
    device.add_p2p_interface(
        name='Ethernet1',
        remote_host='core-rtr1',
        remote_port='Ethernet9',
        ip_address='10.0.1.1/31'
    )
    device.add_bgp_neighbor(
        neighbor_ip='10.0.1.0',
        neighbor_as=64512,
        neighbor_hostname='core-rtr1'
    )

    device.add_vlan(num=101, description='prod-1', ip_address='11.0.1.1/24')
    device.add_access_port('Ethernet9', 101, 'host1')
    device.sync()

    if include_tor2:
        device = DeviceModel.get(hostname='tor2', session=session)
        device.initialize_bgp(64514)
        device.add_p2p_interface(
            name='Ethernet1',
            remote_host='core-rtr2',
            remote_port='Ethernet9',
            ip_address='10.0.1.3/31'
        )
        device.add_bgp_neighbor(
            neighbor_ip='10.0.1.2',
            neighbor_as=64512,
            neighbor_hostname='core-rtr2'
        )

        device.add_vlan(num=102, description='prod-2', ip_address='11.0.2.1/24')
        device.add_access_port('Ethernet9', 102, 'host2')
        device.sync()


def provision_tor(hostname, management_ip, asn, cross_connect_net, core_hostname, core_port):
    session = get_session()
    try:
        DeviceModel.create(hostname=hostname, management_ip=management_ip, role='tor', session=session)
        session.commit()
        tor = DeviceModel.get(hostname=hostname, session=session)
        core = DeviceModel.get(hostname=core_hostname, session=session)
        tor.initialize_bgp(asn)

        p2p_prefix = IPNetwork(cross_connect_net)
        if p2p_prefix.prefixlen != 31:
            raise ValidationError('Expected a /31.')

        core_ip = str(p2p_prefix[0])
        core_net = f'{p2p_prefix[0]}/31'
        tor_ip = str(p2p_prefix[1])
        tor_net = f'{p2p_prefix[1]}/31'

        # Add P2P links on both devices
        tor.add_p2p_interface(
            name='Ethernet1',
            remote_host=core_hostname,
            remote_port=core_port,
            ip_address=tor_net,
        )

        core.add_p2p_interface(
            name=core_port,
            remote_host=hostname,
            remote_port='Ethernet1',
            ip_address=core_net,
        )

        tor.sync()
        core.sync()

        # Validate LLDP
        if validate_lldp_neighbor(tor.management_ip, core_hostname, core_port):
            LOG.debug('TOR LLDP Neighbor confirmed')
        else:
            LOG.error('TOR LLDP Validation Failed')

        if validate_lldp_neighbor(core.management_ip, hostname, 'Ethernet1'):
            LOG.debug('Core LLDP Neighbor confirmed')
        else:
            LOG.error('Core LLDP Validation Failed')

        # Add BGP Neighbors
        tor.add_bgp_neighbor(
            neighbor_ip=core_ip,
            neighbor_as=64512,
            neighbor_hostname=core_hostname,
        )

        core.add_bgp_neighbor(
            neighbor_ip=tor_ip,
            neighbor_as=asn,
            neighbor_hostname=hostname,
        )

        # Sync config on both devices
        tor.sync()
        core.sync()

        # Validate BGP
        if validate_bgp_state(tor.management_ip, core_ip):
            LOG.debug('BGP Established')
        else:
            LOG.debug('BGP Not Established')

    except Exception as exc:
        session.rollback()
        # Resync affected device after rollback
        DeviceModel.get(hostname=core_hostname, session=session).sync()
        raise exc
    finally:
        session.close()


@session_write
def add_vlan(hostname, num, prefix, description, session=None):
    device = DeviceModel.get(hostname=hostname, session=session)
    try:
        net = IPNetwork(prefix)
    except AddrFormatError:
        raise ValidationError('Invalid VLAN Subnet')
    if net.network == net.ip:
        # Allow them to pass prefix or svi IP
        prefix = f'{net.network + 1}/{net.prefixlen}'
    device.add_vlan(num, description, prefix)
    device.sync()


@session_write
def update_access_port(hostname, port, vlan, description=None, session=None):
    if port in ['Ethernet1', 'Ethernet21']:
        raise ValidationError('Ethernet1 and Ethernet21 are reserved.')

    device = DeviceModel.get(hostname=hostname, session=session)
    device.add_access_port(port, vlan, description)
    device.sync()
