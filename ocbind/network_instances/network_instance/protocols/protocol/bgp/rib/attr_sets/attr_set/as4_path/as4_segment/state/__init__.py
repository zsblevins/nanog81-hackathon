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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/as4-path/as4-segment/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Opstate data for AS-PATH segments
  """
  __slots__ = ('_path_helper', '_extmethods', '__type','__member',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'as4-path', 'as4-segment', 'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)

    YANG Description: The type of AS-PATH segment
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with oc-bgpt:as-path-segment-type""",
          'defined-type': "oc-bgpt:as-path-segment-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)


  def _get_member(self):
    """
    Getter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    return self.__member
      
  def _set_member(self, v, load=False):
    """
    Setter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member() directly.

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)""",
        })

    self.__member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member(self):
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

  type = __builtin__.property(_get_type)
  member = __builtin__.property(_get_member)


  _pyangbind_elements = OrderedDict([('type', type), ('member', member), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/as4-path/as4-segment/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Opstate data for AS-PATH segments
  """
  __slots__ = ('_path_helper', '_extmethods', '__type','__member',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'as4-path', 'as4-segment', 'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)

    YANG Description: The type of AS-PATH segment
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with oc-bgpt:as-path-segment-type""",
          'defined-type': "oc-bgpt:as-path-segment-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)


  def _get_member(self):
    """
    Getter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    return self.__member
      
  def _set_member(self, v, load=False):
    """
    Setter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member() directly.

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)""",
        })

    self.__member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member(self):
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

  type = __builtin__.property(_get_type)
  member = __builtin__.property(_get_member)


  _pyangbind_elements = OrderedDict([('type', type), ('member', member), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/as4-path/as4-segment/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Opstate data for AS-PATH segments
  """
  __slots__ = ('_path_helper', '_extmethods', '__type','__member',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'as4-path', 'as4-segment', 'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)

    YANG Description: The type of AS-PATH segment
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with oc-bgpt:as-path-segment-type""",
          'defined-type': "oc-bgpt:as-path-segment-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)


  def _get_member(self):
    """
    Getter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    return self.__member
      
  def _set_member(self, v, load=False):
    """
    Setter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member() directly.

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)""",
        })

    self.__member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member(self):
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

  type = __builtin__.property(_get_type)
  member = __builtin__.property(_get_member)


  _pyangbind_elements = OrderedDict([('type', type), ('member', member), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets/attr-set/as4-path/as4-segment/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Opstate data for AS-PATH segments
  """
  __slots__ = ('_path_helper', '_extmethods', '__type','__member',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets', 'attr-set', 'as4-path', 'as4-segment', 'state']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)

    YANG Description: The type of AS-PATH segment
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/type (oc-bgpt:as-path-segment-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with oc-bgpt:as-path-segment-type""",
          'defined-type': "oc-bgpt:as-path-segment-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'AS_SEQ': {}, 'AS_SET': {}, 'AS_CONFED_SEQUENCE': {}, 'AS_CONFED_SET': {}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgpt:as-path-segment-type', is_config=False)


  def _get_member(self):
    """
    Getter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    return self.__member
      
  def _set_member(self, v, load=False):
    """
    Setter method for member, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set/as4_path/as4_segment/state/member (oc-inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member() directly.

    YANG Description: List of the AS numbers in the AS-PATH segment
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member must be of a type compatible with oc-inet:as-number""",
          'defined-type': "oc-inet:as-number",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)""",
        })

    self.__member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member(self):
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:as-number', is_config=False)

  type = __builtin__.property(_get_type)
  member = __builtin__.property(_get_member)


  _pyangbind_elements = OrderedDict([('type', type), ('member', member), ])


