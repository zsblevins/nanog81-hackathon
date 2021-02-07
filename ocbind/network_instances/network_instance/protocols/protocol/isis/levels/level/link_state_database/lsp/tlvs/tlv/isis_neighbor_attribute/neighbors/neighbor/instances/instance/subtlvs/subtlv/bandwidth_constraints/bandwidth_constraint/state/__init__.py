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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
22.
  """
  __slots__ = ('_path_helper', '_extmethods', '__model_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'state']

  def _get_model_id(self):
    """
    Getter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    return self.__model_id
      
  def _set_model_id(self, v, load=False):
    """
    Setter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_model_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_model_id() directly.

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """model_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__model_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_model_id(self):
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  model_id = __builtin__.property(_get_model_id)


  _pyangbind_elements = OrderedDict([('model_id', model_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
22.
  """
  __slots__ = ('_path_helper', '_extmethods', '__model_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'state']

  def _get_model_id(self):
    """
    Getter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    return self.__model_id
      
  def _set_model_id(self, v, load=False):
    """
    Setter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_model_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_model_id() directly.

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """model_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__model_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_model_id(self):
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  model_id = __builtin__.property(_get_model_id)


  _pyangbind_elements = OrderedDict([('model_id', model_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
22.
  """
  __slots__ = ('_path_helper', '_extmethods', '__model_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'state']

  def _get_model_id(self):
    """
    Getter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    return self.__model_id
      
  def _set_model_id(self, v, load=False):
    """
    Setter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_model_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_model_id() directly.

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """model_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__model_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_model_id(self):
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  model_id = __builtin__.property(_get_model_id)


  _pyangbind_elements = OrderedDict([('model_id', model_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/isis-neighbor-attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS Extended Reachability sub-TLV
22.
  """
  __slots__ = ('_path_helper', '_extmethods', '__model_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'isis-neighbor-attribute', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'state']

  def _get_model_id(self):
    """
    Getter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    return self.__model_id
      
  def _set_model_id(self, v, load=False):
    """
    Setter method for model_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/isis_neighbor_attribute/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/state/model_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_model_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_model_id() directly.

    YANG Description: Identifier for the Bandwidth Constraints  Model
currently in use by the LSR initiating the IGP
advertisement.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """model_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__model_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_model_id(self):
    self.__model_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="model-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)

  model_id = __builtin__.property(_get_model_id)


  _pyangbind_elements = OrderedDict([('model_id', model_id), ])


