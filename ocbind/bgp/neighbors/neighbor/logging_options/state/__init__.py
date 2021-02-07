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
  from YANG module openconfig-bgp - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-multiprotocol - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-structure - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-peer-group - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-neighbor - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-global - based on the path /bgp/neighbors/neighbor/logging-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to logging for the BGP neighbor
or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__log_neighbor_state_changes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

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
      return ['bgp', 'neighbors', 'neighbor', 'logging-options', 'state']

  def _get_log_neighbor_state_changes(self):
    """
    Getter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    return self.__log_neighbor_state_changes
      
  def _set_log_neighbor_state_changes(self, v, load=False):
    """
    Setter method for log_neighbor_state_changes, mapped from YANG variable /bgp/neighbors/neighbor/logging_options/state/log_neighbor_state_changes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_neighbor_state_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_neighbor_state_changes() directly.

    YANG Description: Configure logging of peer state changes.  Default is
to enable logging of peer state changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_neighbor_state_changes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__log_neighbor_state_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_neighbor_state_changes(self):
    self.__log_neighbor_state_changes = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="log-neighbor-state-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  log_neighbor_state_changes = __builtin__.property(_get_log_neighbor_state_changes)


  _pyangbind_elements = OrderedDict([('log_neighbor_state_changes', log_neighbor_state_changes), ])


