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

from . import condition
class conditional(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/next-hop-groups/next-hop-group/conditional. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: When a system selects a next-hop-group based on conditions
in addition to those specified in the referencing table entries
(for example, DSCP is used in addition to the IPv4 destination
prefix), these conditions are specified in the conditions list.
Where such conditions exist, the next-hop-group MUST only
specify next-hop-groups under the conditional list, and therefore
MUST NOT specify any corresponding next-hops. The
next-hop-groups that are referenced by any conditions MUST
reference only next-hops and therefore MUST NOT be conditional
themselves.
  """
  __slots__ = ('_path_helper', '_extmethods', '__condition',)

  _yang_name = 'conditional'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hop-groups', 'next-hop-group', 'conditional']

  def _get_condition(self):
    """
    Getter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    return self.__condition
      
  def _set_condition(self, v, load=False):
    """
    Setter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_condition is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_condition() directly.

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """condition must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__condition = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_condition(self):
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  condition = __builtin__.property(_get_condition)


  _pyangbind_elements = OrderedDict([('condition', condition), ])


from . import condition
class conditional(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/next-hop-groups/next-hop-group/conditional. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: When a system selects a next-hop-group based on conditions
in addition to those specified in the referencing table entries
(for example, DSCP is used in addition to the IPv4 destination
prefix), these conditions are specified in the conditions list.
Where such conditions exist, the next-hop-group MUST only
specify next-hop-groups under the conditional list, and therefore
MUST NOT specify any corresponding next-hops. The
next-hop-groups that are referenced by any conditions MUST
reference only next-hops and therefore MUST NOT be conditional
themselves.
  """
  __slots__ = ('_path_helper', '_extmethods', '__condition',)

  _yang_name = 'conditional'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hop-groups', 'next-hop-group', 'conditional']

  def _get_condition(self):
    """
    Getter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    return self.__condition
      
  def _set_condition(self, v, load=False):
    """
    Setter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_condition is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_condition() directly.

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """condition must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__condition = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_condition(self):
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  condition = __builtin__.property(_get_condition)


  _pyangbind_elements = OrderedDict([('condition', condition), ])


from . import condition
class conditional(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/next-hop-groups/next-hop-group/conditional. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: When a system selects a next-hop-group based on conditions
in addition to those specified in the referencing table entries
(for example, DSCP is used in addition to the IPv4 destination
prefix), these conditions are specified in the conditions list.
Where such conditions exist, the next-hop-group MUST only
specify next-hop-groups under the conditional list, and therefore
MUST NOT specify any corresponding next-hops. The
next-hop-groups that are referenced by any conditions MUST
reference only next-hops and therefore MUST NOT be conditional
themselves.
  """
  __slots__ = ('_path_helper', '_extmethods', '__condition',)

  _yang_name = 'conditional'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hop-groups', 'next-hop-group', 'conditional']

  def _get_condition(self):
    """
    Getter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    return self.__condition
      
  def _set_condition(self, v, load=False):
    """
    Setter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_condition is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_condition() directly.

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """condition must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__condition = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_condition(self):
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  condition = __builtin__.property(_get_condition)


  _pyangbind_elements = OrderedDict([('condition', condition), ])


from . import condition
class conditional(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/next-hop-groups/next-hop-group/conditional. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: When a system selects a next-hop-group based on conditions
in addition to those specified in the referencing table entries
(for example, DSCP is used in addition to the IPv4 destination
prefix), these conditions are specified in the conditions list.
Where such conditions exist, the next-hop-group MUST only
specify next-hop-groups under the conditional list, and therefore
MUST NOT specify any corresponding next-hops. The
next-hop-groups that are referenced by any conditions MUST
reference only next-hops and therefore MUST NOT be conditional
themselves.
  """
  __slots__ = ('_path_helper', '_extmethods', '__condition',)

  _yang_name = 'conditional'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'next-hop-groups', 'next-hop-group', 'conditional']

  def _get_condition(self):
    """
    Getter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    return self.__condition
      
  def _set_condition(self, v, load=False):
    """
    Setter method for condition, mapped from YANG variable /network_instances/network_instance/afts/next_hop_groups/next_hop_group/conditional/condition (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_condition is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_condition() directly.

    YANG Description: A conditional next-hop-group that is used by the AFT
entry. The conditions that are specified within the
group are logically ANDed together. If a condition
is a leaf-list field its contents are logically ORed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """condition must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__condition = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_condition(self):
    self.__condition = YANGDynClass(base=YANGListType("id",condition.condition, yang_name="condition", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="condition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  condition = __builtin__.property(_get_condition)


  _pyangbind_elements = OrderedDict([('condition', condition), ])

