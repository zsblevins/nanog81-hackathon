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

from . import candidate_secondary_path
class candidate_secondary_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of candidate secondary paths which may be used
for this primary path. When secondary paths are specified
in the list the path of the secondary LSP in use must be
restricted to those path options referenced. The
priority of the secondary paths is specified within the
list. Higher priority values are less preferred - that is
to say that a path with priority 0 is the most preferred
path. In the case that the list is empty, any secondary
path option may be utilised when the current primary path
is in use.
  """
  __slots__ = ('_path_helper', '_extmethods', '__candidate_secondary_path',)

  _yang_name = 'candidate-secondary-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'constrained-path', 'tunnels', 'tunnel', 'p2p-tunnel-attributes', 'p2p-primary-path', 'p2p-primary-path', 'candidate-secondary-paths']

  def _get_candidate_secondary_path(self):
    """
    Getter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    return self.__candidate_secondary_path
      
  def _set_candidate_secondary_path(self, v, load=False):
    """
    Setter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_candidate_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_candidate_secondary_path() directly.

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """candidate_secondary_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__candidate_secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_candidate_secondary_path(self):
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  candidate_secondary_path = __builtin__.property(_get_candidate_secondary_path, _set_candidate_secondary_path)


  _pyangbind_elements = OrderedDict([('candidate_secondary_path', candidate_secondary_path), ])


from . import candidate_secondary_path
class candidate_secondary_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of candidate secondary paths which may be used
for this primary path. When secondary paths are specified
in the list the path of the secondary LSP in use must be
restricted to those path options referenced. The
priority of the secondary paths is specified within the
list. Higher priority values are less preferred - that is
to say that a path with priority 0 is the most preferred
path. In the case that the list is empty, any secondary
path option may be utilised when the current primary path
is in use.
  """
  __slots__ = ('_path_helper', '_extmethods', '__candidate_secondary_path',)

  _yang_name = 'candidate-secondary-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'constrained-path', 'tunnels', 'tunnel', 'p2p-tunnel-attributes', 'p2p-primary-path', 'p2p-primary-path', 'candidate-secondary-paths']

  def _get_candidate_secondary_path(self):
    """
    Getter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    return self.__candidate_secondary_path
      
  def _set_candidate_secondary_path(self, v, load=False):
    """
    Setter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_candidate_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_candidate_secondary_path() directly.

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """candidate_secondary_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__candidate_secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_candidate_secondary_path(self):
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  candidate_secondary_path = __builtin__.property(_get_candidate_secondary_path, _set_candidate_secondary_path)


  _pyangbind_elements = OrderedDict([('candidate_secondary_path', candidate_secondary_path), ])


from . import candidate_secondary_path
class candidate_secondary_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of candidate secondary paths which may be used
for this primary path. When secondary paths are specified
in the list the path of the secondary LSP in use must be
restricted to those path options referenced. The
priority of the secondary paths is specified within the
list. Higher priority values are less preferred - that is
to say that a path with priority 0 is the most preferred
path. In the case that the list is empty, any secondary
path option may be utilised when the current primary path
is in use.
  """
  __slots__ = ('_path_helper', '_extmethods', '__candidate_secondary_path',)

  _yang_name = 'candidate-secondary-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'constrained-path', 'tunnels', 'tunnel', 'p2p-tunnel-attributes', 'p2p-primary-path', 'p2p-primary-path', 'candidate-secondary-paths']

  def _get_candidate_secondary_path(self):
    """
    Getter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    return self.__candidate_secondary_path
      
  def _set_candidate_secondary_path(self, v, load=False):
    """
    Setter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_candidate_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_candidate_secondary_path() directly.

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """candidate_secondary_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__candidate_secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_candidate_secondary_path(self):
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  candidate_secondary_path = __builtin__.property(_get_candidate_secondary_path, _set_candidate_secondary_path)


  _pyangbind_elements = OrderedDict([('candidate_secondary_path', candidate_secondary_path), ])


from . import candidate_secondary_path
class candidate_secondary_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-primary-path/p2p-primary-path/candidate-secondary-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of candidate secondary paths which may be used
for this primary path. When secondary paths are specified
in the list the path of the secondary LSP in use must be
restricted to those path options referenced. The
priority of the secondary paths is specified within the
list. Higher priority values are less preferred - that is
to say that a path with priority 0 is the most preferred
path. In the case that the list is empty, any secondary
path option may be utilised when the current primary path
is in use.
  """
  __slots__ = ('_path_helper', '_extmethods', '__candidate_secondary_path',)

  _yang_name = 'candidate-secondary-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'lsps', 'constrained-path', 'tunnels', 'tunnel', 'p2p-tunnel-attributes', 'p2p-primary-path', 'p2p-primary-path', 'candidate-secondary-paths']

  def _get_candidate_secondary_path(self):
    """
    Getter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    return self.__candidate_secondary_path
      
  def _set_candidate_secondary_path(self, v, load=False):
    """
    Setter method for candidate_secondary_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_primary_path/p2p_primary_path/candidate_secondary_paths/candidate_secondary_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_candidate_secondary_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_candidate_secondary_path() directly.

    YANG Description: List of secondary paths which may be utilised when the
current primary path is in use
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """candidate_secondary_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__candidate_secondary_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_candidate_secondary_path(self):
    self.__candidate_secondary_path = YANGDynClass(base=YANGListType("secondary_path",candidate_secondary_path.candidate_secondary_path, yang_name="candidate-secondary-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='secondary-path', extensions=None), is_container='list', yang_name="candidate-secondary-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  candidate_secondary_path = __builtin__.property(_get_candidate_secondary_path, _set_candidate_secondary_path)


  _pyangbind_elements = OrderedDict([('candidate_secondary_path', candidate_secondary_path), ])


