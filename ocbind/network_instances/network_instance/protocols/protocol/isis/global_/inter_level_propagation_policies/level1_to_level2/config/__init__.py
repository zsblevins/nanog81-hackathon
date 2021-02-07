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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/inter-level-propagation-policies/level1-to-level2/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the propagation
of prefixes from IS-IS Level 1 to Level 2.
  """
  __slots__ = ('_path_helper', '_extmethods', '__import_policy','__default_import_policy',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'inter-level-propagation-policies', 'level1-to-level2', 'config']

  def _get_import_policy(self):
    """
    Getter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    return self.__import_policy
      
  def _set_import_policy(self, v, load=False):
    """
    Setter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_policy() directly.

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_policy(self):
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_default_import_policy(self):
    """
    Getter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    return self.__default_import_policy
      
  def _set_default_import_policy(self, v, load=False):
    """
    Setter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_import_policy() directly.

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_import_policy must be of a type compatible with default-policy-type""",
          'defined-type': "openconfig-network-instance:default-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)""",
        })

    self.__default_import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_import_policy(self):
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

  import_policy = __builtin__.property(_get_import_policy, _set_import_policy)
  default_import_policy = __builtin__.property(_get_default_import_policy, _set_default_import_policy)


  _pyangbind_elements = OrderedDict([('import_policy', import_policy), ('default_import_policy', default_import_policy), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/inter-level-propagation-policies/level1-to-level2/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the propagation
of prefixes from IS-IS Level 1 to Level 2.
  """
  __slots__ = ('_path_helper', '_extmethods', '__import_policy','__default_import_policy',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'inter-level-propagation-policies', 'level1-to-level2', 'config']

  def _get_import_policy(self):
    """
    Getter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    return self.__import_policy
      
  def _set_import_policy(self, v, load=False):
    """
    Setter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_policy() directly.

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_policy(self):
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_default_import_policy(self):
    """
    Getter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    return self.__default_import_policy
      
  def _set_default_import_policy(self, v, load=False):
    """
    Setter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_import_policy() directly.

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_import_policy must be of a type compatible with default-policy-type""",
          'defined-type': "openconfig-network-instance:default-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)""",
        })

    self.__default_import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_import_policy(self):
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

  import_policy = __builtin__.property(_get_import_policy, _set_import_policy)
  default_import_policy = __builtin__.property(_get_default_import_policy, _set_default_import_policy)


  _pyangbind_elements = OrderedDict([('import_policy', import_policy), ('default_import_policy', default_import_policy), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/inter-level-propagation-policies/level1-to-level2/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the propagation
of prefixes from IS-IS Level 1 to Level 2.
  """
  __slots__ = ('_path_helper', '_extmethods', '__import_policy','__default_import_policy',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'inter-level-propagation-policies', 'level1-to-level2', 'config']

  def _get_import_policy(self):
    """
    Getter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    return self.__import_policy
      
  def _set_import_policy(self, v, load=False):
    """
    Setter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_policy() directly.

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_policy(self):
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_default_import_policy(self):
    """
    Getter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    return self.__default_import_policy
      
  def _set_default_import_policy(self, v, load=False):
    """
    Setter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_import_policy() directly.

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_import_policy must be of a type compatible with default-policy-type""",
          'defined-type': "openconfig-network-instance:default-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)""",
        })

    self.__default_import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_import_policy(self):
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

  import_policy = __builtin__.property(_get_import_policy, _set_import_policy)
  default_import_policy = __builtin__.property(_get_default_import_policy, _set_default_import_policy)


  _pyangbind_elements = OrderedDict([('import_policy', import_policy), ('default_import_policy', default_import_policy), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/inter-level-propagation-policies/level1-to-level2/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the propagation
of prefixes from IS-IS Level 1 to Level 2.
  """
  __slots__ = ('_path_helper', '_extmethods', '__import_policy','__default_import_policy',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'inter-level-propagation-policies', 'level1-to-level2', 'config']

  def _get_import_policy(self):
    """
    Getter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    return self.__import_policy
      
  def _set_import_policy(self, v, load=False):
    """
    Setter method for import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/import_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_policy() directly.

    YANG Description: list of policy names in sequence to be applied on
receiving a routing update in the current context, e.g.,
for the current peer group, neighbor, address family,
etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_policy(self):
    self.__import_policy = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_default_import_policy(self):
    """
    Getter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    return self.__default_import_policy
      
  def _set_default_import_policy(self, v, load=False):
    """
    Setter method for default_import_policy, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/inter_level_propagation_policies/level1_to_level2/config/default_import_policy (default-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_import_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_import_policy() directly.

    YANG Description: explicitly set a default policy if no policy definition
in the import policy chain is satisfied.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_import_policy must be of a type compatible with default-policy-type""",
          'defined-type': "openconfig-network-instance:default-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)""",
        })

    self.__default_import_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_import_policy(self):
    self.__default_import_policy = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'ACCEPT_ROUTE': {}, 'REJECT_ROUTE': {}},), default=six.text_type("REJECT_ROUTE"), is_leaf=True, yang_name="default-import-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='default-policy-type', is_config=True)

  import_policy = __builtin__.property(_get_import_policy, _set_import_policy)
  default_import_policy = __builtin__.property(_get_default_import_policy, _set_default_import_policy)


  _pyangbind_elements = OrderedDict([('import_policy', import_policy), ('default_import_policy', default_import_policy), ])


