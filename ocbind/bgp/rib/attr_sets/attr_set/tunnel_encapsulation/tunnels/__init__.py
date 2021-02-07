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

from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-multiprotocol - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-structure - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-peer-group - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-neighbor - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])


from . import tunnel
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-global - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnel',)

  _yang_name = 'tunnels'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation', 'tunnels']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.

    YANG Description: List of the tunnels that are specified within the
attribute. Keyed on the type of tunnel that the
TLV describes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType("type",tunnel.tunnel, yang_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='list', is_config=False)

  tunnel = __builtin__.property(_get_tunnel)


  _pyangbind_elements = OrderedDict([('tunnel', tunnel), ])

