import json
from pyangbind.lib import pybindJSON, xpathhelper
import ocbind


def _create_interface(name, description):
    path = f'/interfaces/interface[name={name}]'
    ph = xpathhelper.YANGPathHelper()
    intf_model = ocbind.openconfig_interfaces(path_helper=ph)
    intf_model.interfaces.interface.add(name)
    intf = intf_model.interfaces.interface[name]

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
    intf.routed_vlan.config.vlan = num
    intf.routed_vlan.ipv4.addresses.address.add(ip)
    intf.routed_vlan.ipv4.addresses.address[ip].config.prefix_length = prefixlen
    return path, name, pybindJSON.dumps(intf, mode='ietf')


def create_access_interface(name, description, vlan):
    path, intf = _create_interface(name, description)
    intf.ethernet.switched_vlan.config.access_vlan = vlan
    return path, name, pybindJSON.dumps(intf, mode='ietf')


def create_bgp_neighbor(neighbor_ip, neighbor_as, description):
    ph = xpathhelper.YANGPathHelper()
    # Drill down to BGP neighbor model
    network_instances = ocbind.openconfig_network_instance(path_helper=ph)
    network_instances.network_instances.network_instance.add('default')
    network_instance = network_instances.network_instances.network_instance['default']
    network_instance.protocols.protocol.add('BGP BGP')
    bgp_model = network_instance.protocols.protocol['BGP BGP'].bgp

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
