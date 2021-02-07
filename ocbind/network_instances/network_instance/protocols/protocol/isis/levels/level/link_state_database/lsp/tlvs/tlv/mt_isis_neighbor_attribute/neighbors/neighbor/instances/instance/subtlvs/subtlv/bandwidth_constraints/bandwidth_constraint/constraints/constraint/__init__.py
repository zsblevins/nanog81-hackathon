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

from . import state
class constraint(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints/constraint. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint_id','__state',)

  _yang_name = 'constraint'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints', 'constraint']

  def _get_constraint_id(self):
    """
    Getter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)

    YANG Description: Reference to the unique ID for the BCN level.
    """
    return self.__constraint_id
      
  def _set_constraint_id(self, v, load=False):
    """
    Setter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint_id() directly.

    YANG Description: Reference to the unique ID for the BCN level.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__constraint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint_id(self):
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)

    YANG Description: Operational state parameters of the BCN level
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters of the BCN level
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  constraint_id = __builtin__.property(_get_constraint_id)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('constraint_id', constraint_id), ('state', state), ])


from . import state
class constraint(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints/constraint. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint_id','__state',)

  _yang_name = 'constraint'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints', 'constraint']

  def _get_constraint_id(self):
    """
    Getter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)

    YANG Description: Reference to the unique ID for the BCN level.
    """
    return self.__constraint_id
      
  def _set_constraint_id(self, v, load=False):
    """
    Setter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint_id() directly.

    YANG Description: Reference to the unique ID for the BCN level.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__constraint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint_id(self):
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)

    YANG Description: Operational state parameters of the BCN level
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters of the BCN level
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  constraint_id = __builtin__.property(_get_constraint_id)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('constraint_id', constraint_id), ('state', state), ])


from . import state
class constraint(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints/constraint. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint_id','__state',)

  _yang_name = 'constraint'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints', 'constraint']

  def _get_constraint_id(self):
    """
    Getter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)

    YANG Description: Reference to the unique ID for the BCN level.
    """
    return self.__constraint_id
      
  def _set_constraint_id(self, v, load=False):
    """
    Setter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint_id() directly.

    YANG Description: Reference to the unique ID for the BCN level.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__constraint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint_id(self):
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)

    YANG Description: Operational state parameters of the BCN level
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters of the BCN level
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  constraint_id = __builtin__.property(_get_constraint_id)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('constraint_id', constraint_id), ('state', state), ])


from . import state
class constraint(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints/constraint. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint_id','__state',)

  _yang_name = 'constraint'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints', 'constraint']

  def _get_constraint_id(self):
    """
    Getter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)

    YANG Description: Reference to the unique ID for the BCN level.
    """
    return self.__constraint_id
      
  def _set_constraint_id(self, v, load=False):
    """
    Setter method for constraint_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/constraint_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint_id() directly.

    YANG Description: Reference to the unique ID for the BCN level.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__constraint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint_id(self):
    self.__constraint_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="constraint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)

    YANG Description: Operational state parameters of the BCN level
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters of the BCN level
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  constraint_id = __builtin__.property(_get_constraint_id)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = OrderedDict([('constraint_id', constraint_id), ('state', state), ])


