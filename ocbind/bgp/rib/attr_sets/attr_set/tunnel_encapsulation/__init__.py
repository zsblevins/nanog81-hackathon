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

from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-multiprotocol - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-structure - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-peer-group - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-neighbor - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


from . import tunnels
class tunnel_encapsulation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-global - based on the path /bgp/rib/attr-sets/attr-set/tunnel-encapsulation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Tunnel Encapsulation attribute specifies a set of
tunnels to a remote destination. The attribute is TLV
based and allows description of a tunnel type, and the
relevant information to create the tunnel to the remote
destination.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tunnels',)

  _yang_name = 'tunnel-encapsulation'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

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
      return ['bgp', 'rib', 'attr-sets', 'attr-set', 'tunnel-encapsulation']

  def _get_tunnels(self):
    """
    Getter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    return self.__tunnels
      
  def _set_tunnels(self, v, load=False):
    """
    Setter method for tunnels, mapped from YANG variable /bgp/rib/attr_sets/attr_set/tunnel_encapsulation/tunnels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnels() directly.

    YANG Description: Surrounding container for the set of tunnels included
within the tunnel encapsulation attribute.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)""",
        })

    self.__tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnels(self):
    self.__tunnels = YANGDynClass(base=tunnels.tunnels, is_container='container', yang_name="tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=False)

  tunnels = __builtin__.property(_get_tunnels)


  _pyangbind_elements = OrderedDict([('tunnels', tunnels), ])


