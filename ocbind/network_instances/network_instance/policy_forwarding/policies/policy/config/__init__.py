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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration options relating to the forwarding
policy.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policy_id',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'config']

  def _get_policy_id(self):
    """
    Getter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    return self.__policy_id
      
  def _set_policy_id(self, v, load=False):
    """
    Setter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_id() directly.

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__policy_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_id(self):
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  policy_id = __builtin__.property(_get_policy_id, _set_policy_id)


  _pyangbind_elements = OrderedDict([('policy_id', policy_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration options relating to the forwarding
policy.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policy_id',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'config']

  def _get_policy_id(self):
    """
    Getter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    return self.__policy_id
      
  def _set_policy_id(self, v, load=False):
    """
    Setter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_id() directly.

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__policy_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_id(self):
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  policy_id = __builtin__.property(_get_policy_id, _set_policy_id)


  _pyangbind_elements = OrderedDict([('policy_id', policy_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration options relating to the forwarding
policy.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policy_id',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'config']

  def _get_policy_id(self):
    """
    Getter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    return self.__policy_id
      
  def _set_policy_id(self, v, load=False):
    """
    Setter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_id() directly.

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__policy_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_id(self):
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  policy_id = __builtin__.property(_get_policy_id, _set_policy_id)


  _pyangbind_elements = OrderedDict([('policy_id', policy_id), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration options relating to the forwarding
policy.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policy_id',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'policies', 'policy', 'config']

  def _get_policy_id(self):
    """
    Getter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    return self.__policy_id
      
  def _set_policy_id(self, v, load=False):
    """
    Setter method for policy_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/config/policy_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy_id() directly.

    YANG Description: A unique name identifying the forwarding policy. This name is
used when applying the policy to a particular interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__policy_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy_id(self):
    self.__policy_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="policy-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  policy_id = __builtin__.property(_get_policy_id, _set_policy_id)


  _pyangbind_elements = OrderedDict([('policy_id', policy_id), ])


