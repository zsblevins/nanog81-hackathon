# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

from . import path_selection_group
class path_selection_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/path-selection-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
  """
  __slots__ = ('_path_helper', '_extmethods', '__path_selection_group',)

  _yang_name = 'path-selection-groups'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['network-instances', 'network-instance', 'policy-forwarding', 'path-selection-groups']

  def _get_path_selection_group(self):
    """
    Getter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing utils.
    """
    return self.__path_selection_group
      
  def _set_path_selection_group(self, v, load=False):
    """
    Setter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_selection_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_selection_group() directly.

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing utils.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_selection_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__path_selection_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_selection_group(self):
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  path_selection_group = __builtin__.property(_get_path_selection_group, _set_path_selection_group)


  _pyangbind_elements = OrderedDict([('path_selection_group', path_selection_group), ])


from . import path_selection_group
class path_selection_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/path-selection-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
  """
  __slots__ = ('_path_helper', '_extmethods', '__path_selection_group',)

  _yang_name = 'path-selection-groups'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['network-instances', 'network-instance', 'policy-forwarding', 'path-selection-groups']

  def _get_path_selection_group(self):
    """
    Getter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing utils.
    """
    return self.__path_selection_group
      
  def _set_path_selection_group(self, v, load=False):
    """
    Setter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_selection_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_selection_group() directly.

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing utils.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_selection_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__path_selection_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_selection_group(self):
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  path_selection_group = __builtin__.property(_get_path_selection_group, _set_path_selection_group)


  _pyangbind_elements = OrderedDict([('path_selection_group', path_selection_group), ])


from . import path_selection_group
class path_selection_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/path-selection-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
  """
  __slots__ = ('_path_helper', '_extmethods', '__path_selection_group',)

  _yang_name = 'path-selection-groups'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['network-instances', 'network-instance', 'policy-forwarding', 'path-selection-groups']

  def _get_path_selection_group(self):
    """
    Getter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing logic.
    """
    return self.__path_selection_group
      
  def _set_path_selection_group(self, v, load=False):
    """
    Setter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_selection_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_selection_group() directly.

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing logic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_selection_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__path_selection_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_selection_group(self):
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  path_selection_group = __builtin__.property(_get_path_selection_group, _set_path_selection_group)


  _pyangbind_elements = OrderedDict([('path_selection_group', path_selection_group), ])


from . import path_selection_group
class path_selection_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/path-selection-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
  """
  __slots__ = ('_path_helper', '_extmethods', '__path_selection_group',)

  _yang_name = 'path-selection-groups'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['network-instances', 'network-instance', 'policy-forwarding', 'path-selection-groups']

  def _get_path_selection_group(self):
    """
    Getter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing logic.
    """
    return self.__path_selection_group
      
  def _set_path_selection_group(self, v, load=False):
    """
    Setter method for path_selection_group, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups/path_selection_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_selection_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_selection_group() directly.

    YANG Description: A path selection group is a set of forwarding resources,
which are grouped as eligible paths for a particular
policy-based forwarding rule. A policy rule may select a
path-selection-group as the egress for a particular type of
traffic (e.g., DSCP value). The system then utilises its
standard forwarding lookup mechanism to select from the
paths that are specified within the group - for IP packets,
the destination IP address is used such that the packet is
routed to the entity within the path-selection-group that
corresponds to the next-hop for the destination IP address
of the packet; for L2 packets, the selection is based on the
destination MAC address. If multiple paths within the
selection group are eligible to be used for forwarding,
the packets are load-balanced between them according to
the system's usual load balancing logic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_selection_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__path_selection_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_selection_group(self):
    self.__path_selection_group = YANGDynClass(base=YANGListType("group_id",path_selection_group.path_selection_group, yang_name="path-selection-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-id', extensions=None), is_container='list', yang_name="path-selection-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  path_selection_group = __builtin__.property(_get_path_selection_group, _set_path_selection_group)


  _pyangbind_elements = OrderedDict([('path_selection_group', path_selection_group), ])


