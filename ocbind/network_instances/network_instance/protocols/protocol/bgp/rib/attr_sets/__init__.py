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

from . import attr_set
class attr_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of path attribute sets
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_set',)

  _yang_name = 'attr-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets']

  def _get_attr_set(self):
    """
    Getter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    return self.__attr_set
      
  def _set_attr_set(self, v, load=False):
    """
    Setter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_set() directly.

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__attr_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_set(self):
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  attr_set = __builtin__.property(_get_attr_set)


  _pyangbind_elements = OrderedDict([('attr_set', attr_set), ])


from . import attr_set
class attr_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of path attribute sets
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_set',)

  _yang_name = 'attr-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets']

  def _get_attr_set(self):
    """
    Getter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    return self.__attr_set
      
  def _set_attr_set(self, v, load=False):
    """
    Setter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_set() directly.

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__attr_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_set(self):
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  attr_set = __builtin__.property(_get_attr_set)


  _pyangbind_elements = OrderedDict([('attr_set', attr_set), ])


from . import attr_set
class attr_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of path attribute sets
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_set',)

  _yang_name = 'attr-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets']

  def _get_attr_set(self):
    """
    Getter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    return self.__attr_set
      
  def _set_attr_set(self, v, load=False):
    """
    Setter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_set() directly.

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__attr_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_set(self):
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  attr_set = __builtin__.property(_get_attr_set)


  _pyangbind_elements = OrderedDict([('attr_set', attr_set), ])


from . import attr_set
class attr_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/attr-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the list of path attribute sets
  """
  __slots__ = ('_path_helper', '_extmethods', '__attr_set',)

  _yang_name = 'attr-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'attr-sets']

  def _get_attr_set(self):
    """
    Getter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    return self.__attr_set
      
  def _set_attr_set(self, v, load=False):
    """
    Setter method for attr_set, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/attr_sets/attr_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attr_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attr_set() directly.

    YANG Description: List of path attributes that may be in use by multiple
routes in the table
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attr_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__attr_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attr_set(self):
    self.__attr_set = YANGDynClass(base=YANGListType("index",attr_set.attr_set, yang_name="attr-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="attr-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  attr_set = __builtin__.property(_get_attr_set)


  _pyangbind_elements = OrderedDict([('attr_set', attr_set), ])


