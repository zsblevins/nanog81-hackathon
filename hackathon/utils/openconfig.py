import json
from pyangbind.lib import pybindJSON, xpathhelper
import ocbind

from hackathon.utils.gnmi import GNMIClient


def _create_interface(name, description):
    path = f'/interfaces/interface[name={name}]'
    ph = xpathhelper.YANGPathHelper()
    intf_model = ocbind.openconfig_interfaces(path_helper=ph)
    intf_model.interfaces.interface.add(name)
    intf = intf_model.interfaces.interface[name]

    intf.config.name = name
    intf.config.description = description
    intf.config.enabled = 'true'
    return path, intf


def create_p2p_interface(name, description, ip, prefixlen):
    path, intf = _create_interface(name, description)
    intf.subinterfaces.subinterface.add(0)
    subintf = intf.subinterfaces.subinterface[0]
    subintf.config.enabled = 'true'
    subintf.ipv4.config.enabled = 'true'
    subintf.ipv4.addresses.address.add(ip)
    v4_addr = subintf.ipv4.addresses.address[ip]
    v4_addr.config.ip = ip
    v4_addr.config.prefix_length = prefixlen

    schema = json.loads(pybindJSON.dumps(intf, mode='ietf'))
    # Arista needs an augment, hacking it in
    for subint in schema['openconfig-interfaces:subinterfaces']['subinterface']:
        for address in subint['openconfig-if-ip:ipv4']['addresses']['address']:
            address['config']['arista-intf-augments:addr-type'] = 'PRIMARY'

    return path, name, json.dumps(schema, indent=4)


def create_svi(num, description, ip, prefixlen):
    name = f'Vlan{num}'
    path, intf = _create_interface(name, description)
    intf.config.type = 'l3ipvlan'
    intf.routed_vlan.config.vlan = f'Vlan{num}'
    intf.routed_vlan.ipv4.config.enabled = 'true'
    intf.routed_vlan.ipv4.addresses.address.add(ip)
    v4_addr = intf.routed_vlan.ipv4.addresses.address[ip]
    v4_addr.config.ip = ip
    v4_addr.config.prefix_length = prefixlen

    schema = json.loads(pybindJSON.dumps(intf, mode='ietf'))
    # Arista needs an augment, hacking it in
    for address in schema['openconfig-vlan:routed-vlan']['openconfig-if-ip:ipv4']['addresses']['address']:
        address['config']['arista-intf-augments:addr-type'] = 'PRIMARY'

    return path, name, json.dumps(schema, indent=4)


def create_access_interface(name, description, vlan):
    path, intf = _create_interface(name, description)
    intf.ethernet.switched_vlan.config.access_vlan = vlan
    return path, name, pybindJSON.dumps(intf, mode='ietf')


def initialize_bgp(asn):
    ph = xpathhelper.YANGPathHelper()
    bgp_model = ocbind.openconfig_bgp(path_helper=ph).bgp

    path = '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/global/config'
    bgp_model.global_.config.as_ = asn

    return path, 'asn', pybindJSON.dumps(bgp_model.global_.config, mode='ietf')


def redistribute_connected_bgp():
    path = 'network-instances/network-instance[name=default]/table-connections/'
    ph = xpathhelper.YANGPathHelper()
    netinst = ocbind.openconfig_network_instance(path_helper=ph)
    netinst = netinst.network_instances.network_instance.add('default')

    key = ['openconfig-policy-types:DIRECTLY_CONNECTED', 'openconfig-policy-types:BGP', 'openconfig-types:IPV4']
    connections = netinst.table_connections
    tcv4 = connections.table_connection.add(' '.join(key))
    tcv4.config.address_family = key[2]
    tcv4.config.dst_protocol = key[1]
    tcv4.config.src_protocol = key[0]

    key[2] = 'openconfig-types:IPV6'
    tcv6 = connections.table_connection.add(' '.join(key))
    tcv6.config.address_family = key[2]
    tcv6.config.dst_protocol = key[1]
    tcv6.config.src_protocol = key[0]

    return path, 'redistribute_connected', pybindJSON.dumps(connections, mode='ietf')


def create_bgp_neighbor(neighbor_ip, neighbor_as, description):
    ph = xpathhelper.YANGPathHelper()
    bgp_model = ocbind.openconfig_bgp(path_helper=ph).bgp

    # Create neighbor
    bgp_model.neighbors.neighbor.add(neighbor_ip)
    neighbor = bgp_model.neighbors.neighbor[neighbor_ip]
    neighbor.config.neighbor_address = neighbor_ip
    neighbor.config.peer_as = neighbor_as
    neighbor.config.description = description
    neighbor.config.enabled = 'true'

    path = '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor'
    path = f'{path}[neighbor-address={neighbor_ip}]'
    return path, neighbor_ip, pybindJSON.dumps(neighbor, mode='ietf')


def validate_neighbor(host, expected_remote_host, expected_remote_port):
    client = GNMIClient(host)
    output = client.get('/lldp/interfaces')
    interfaces = output[0]['updates'][0]['values']['lldp/interfaces']['openconfig-lldp:interface']
    neighbors = list()
    for intf in interfaces:
        if 'neighbors' in intf:
            for neighbor in intf['neighbors']['neighbor']:
                neighbors.append((neighbor['state']['system-name'], neighbor['state']['port-id']))

    if (expected_remote_host, expected_remote_port) in neighbors:
        return True
    return False
