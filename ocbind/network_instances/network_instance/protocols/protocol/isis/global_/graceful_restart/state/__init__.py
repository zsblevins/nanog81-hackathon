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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/graceful-restart/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS graceful-restart.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__helper_only',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'graceful-restart', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_helper_only(self):
    """
    Getter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    return self.__helper_only
      
  def _set_helper_only(self, v, load=False):
    """
    Setter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_only() directly.

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_only must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_only(self):
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  helper_only = __builtin__.property(_get_helper_only)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('helper_only', helper_only), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/graceful-restart/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS graceful-restart.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__helper_only',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'graceful-restart', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_helper_only(self):
    """
    Getter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    return self.__helper_only
      
  def _set_helper_only(self, v, load=False):
    """
    Setter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_only() directly.

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_only must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_only(self):
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  helper_only = __builtin__.property(_get_helper_only)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('helper_only', helper_only), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/graceful-restart/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS graceful-restart.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__helper_only',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'graceful-restart', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_helper_only(self):
    """
    Getter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    return self.__helper_only
      
  def _set_helper_only(self, v, load=False):
    """
    Setter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_only() directly.

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_only must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_only(self):
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  helper_only = __builtin__.property(_get_helper_only)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('helper_only', helper_only), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/graceful-restart/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS graceful-restart.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__helper_only',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'graceful-restart', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_helper_only(self):
    """
    Getter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    return self.__helper_only
      
  def _set_helper_only(self, v, load=False):
    """
    Setter method for helper_only, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/graceful_restart/state/helper_only (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_helper_only() directly.

    YANG Description: Enable or disable the IS-IS graceful restart helper function. When
this leaf is set, the local system does not utilise the IS-IS
graceful restart procedures during its own restart, but supports
retaining forwarding information during a remote speaker's restart.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """helper_only must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_helper_only(self):
    self.__helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  helper_only = __builtin__.property(_get_helper_only)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('helper_only', helper_only), ])


