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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/subscription/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to RSVP
subscription options
  """
  __slots__ = ('_path_helper', '_extmethods', '__subscription','__calculated_absolute_subscription_bw',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'subscription', 'state']

  def _get_subscription(self):
    """
    Getter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    return self.__subscription
      
  def _set_subscription(self, v, load=False):
    """
    Setter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscription is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscription() directly.

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscription must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__subscription = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscription(self):
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)


  def _get_calculated_absolute_subscription_bw(self):
    """
    Getter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    return self.__calculated_absolute_subscription_bw
      
  def _set_calculated_absolute_subscription_bw(self, v, load=False):
    """
    Setter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_calculated_absolute_subscription_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_calculated_absolute_subscription_bw() directly.

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """calculated_absolute_subscription_bw must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__calculated_absolute_subscription_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_calculated_absolute_subscription_bw(self):
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

  subscription = __builtin__.property(_get_subscription)
  calculated_absolute_subscription_bw = __builtin__.property(_get_calculated_absolute_subscription_bw)


  _pyangbind_elements = OrderedDict([('subscription', subscription), ('calculated_absolute_subscription_bw', calculated_absolute_subscription_bw), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/subscription/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to RSVP
subscription options
  """
  __slots__ = ('_path_helper', '_extmethods', '__subscription','__calculated_absolute_subscription_bw',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'subscription', 'state']

  def _get_subscription(self):
    """
    Getter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    return self.__subscription
      
  def _set_subscription(self, v, load=False):
    """
    Setter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscription is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscription() directly.

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscription must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__subscription = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscription(self):
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)


  def _get_calculated_absolute_subscription_bw(self):
    """
    Getter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    return self.__calculated_absolute_subscription_bw
      
  def _set_calculated_absolute_subscription_bw(self, v, load=False):
    """
    Setter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_calculated_absolute_subscription_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_calculated_absolute_subscription_bw() directly.

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """calculated_absolute_subscription_bw must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__calculated_absolute_subscription_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_calculated_absolute_subscription_bw(self):
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

  subscription = __builtin__.property(_get_subscription)
  calculated_absolute_subscription_bw = __builtin__.property(_get_calculated_absolute_subscription_bw)


  _pyangbind_elements = OrderedDict([('subscription', subscription), ('calculated_absolute_subscription_bw', calculated_absolute_subscription_bw), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/subscription/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to RSVP
subscription options
  """
  __slots__ = ('_path_helper', '_extmethods', '__subscription','__calculated_absolute_subscription_bw',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'subscription', 'state']

  def _get_subscription(self):
    """
    Getter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    return self.__subscription
      
  def _set_subscription(self, v, load=False):
    """
    Setter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscription is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscription() directly.

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscription must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__subscription = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscription(self):
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)


  def _get_calculated_absolute_subscription_bw(self):
    """
    Getter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    return self.__calculated_absolute_subscription_bw
      
  def _set_calculated_absolute_subscription_bw(self, v, load=False):
    """
    Setter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_calculated_absolute_subscription_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_calculated_absolute_subscription_bw() directly.

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """calculated_absolute_subscription_bw must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__calculated_absolute_subscription_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_calculated_absolute_subscription_bw(self):
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

  subscription = __builtin__.property(_get_subscription)
  calculated_absolute_subscription_bw = __builtin__.property(_get_calculated_absolute_subscription_bw)


  _pyangbind_elements = OrderedDict([('subscription', subscription), ('calculated_absolute_subscription_bw', calculated_absolute_subscription_bw), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/subscription/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to RSVP
subscription options
  """
  __slots__ = ('_path_helper', '_extmethods', '__subscription','__calculated_absolute_subscription_bw',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'rsvp-te', 'interface-attributes', 'interface', 'subscription', 'state']

  def _get_subscription(self):
    """
    Getter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    return self.__subscription
      
  def _set_subscription(self, v, load=False):
    """
    Setter method for subscription, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/subscription (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscription is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscription() directly.

    YANG Description: percentage of the interface bandwidth that
RSVP can reserve
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscription must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__subscription = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscription(self):
    self.__subscription = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="subscription", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=False)


  def _get_calculated_absolute_subscription_bw(self):
    """
    Getter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    return self.__calculated_absolute_subscription_bw
      
  def _set_calculated_absolute_subscription_bw(self, v, load=False):
    """
    Setter method for calculated_absolute_subscription_bw, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/subscription/state/calculated_absolute_subscription_bw (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_calculated_absolute_subscription_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_calculated_absolute_subscription_bw() directly.

    YANG Description: The calculated absolute value of the bandwidth
which is reservable to RSVP-TE on the interface
prior to any adjustments that may be made from
external sources.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """calculated_absolute_subscription_bw must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__calculated_absolute_subscription_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_calculated_absolute_subscription_bw(self):
    self.__calculated_absolute_subscription_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="calculated-absolute-subscription-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

  subscription = __builtin__.property(_get_subscription)
  calculated_absolute_subscription_bw = __builtin__.property(_get_calculated_absolute_subscription_bw)


  _pyangbind_elements = OrderedDict([('subscription', subscription), ('calculated_absolute_subscription_bw', calculated_absolute_subscription_bw), ])

