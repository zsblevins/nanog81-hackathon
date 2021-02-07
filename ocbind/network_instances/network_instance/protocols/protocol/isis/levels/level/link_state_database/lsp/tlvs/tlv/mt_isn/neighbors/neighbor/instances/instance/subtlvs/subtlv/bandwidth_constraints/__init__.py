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

from . import bandwidth_constraint
class bandwidth_constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines bandwidth-constraints. For DS-TE,
the existing Maximum Reservable link bandwidth parameter
is retained, but its semantics is generalized and
interpreted as the aggregate bandwidth constraint across
all Class-Types
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_constraint',)

  _yang_name = 'bandwidth-constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'mt-isn', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints']

  def _get_bandwidth_constraint(self):
    """
    Getter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    return self.__bandwidth_constraint
      
  def _set_bandwidth_constraint(self, v, load=False):
    """
    Setter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_constraint() directly.

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_constraint(self):
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_constraint = __builtin__.property(_get_bandwidth_constraint)


  _pyangbind_elements = OrderedDict([('bandwidth_constraint', bandwidth_constraint), ])


from . import bandwidth_constraint
class bandwidth_constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines bandwidth-constraints. For DS-TE,
the existing Maximum Reservable link bandwidth parameter
is retained, but its semantics is generalized and
interpreted as the aggregate bandwidth constraint across
all Class-Types
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_constraint',)

  _yang_name = 'bandwidth-constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'mt-isn', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints']

  def _get_bandwidth_constraint(self):
    """
    Getter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    return self.__bandwidth_constraint
      
  def _set_bandwidth_constraint(self, v, load=False):
    """
    Setter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_constraint() directly.

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_constraint(self):
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_constraint = __builtin__.property(_get_bandwidth_constraint)


  _pyangbind_elements = OrderedDict([('bandwidth_constraint', bandwidth_constraint), ])


from . import bandwidth_constraint
class bandwidth_constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines bandwidth-constraints. For DS-TE,
the existing Maximum Reservable link bandwidth parameter
is retained, but its semantics is generalized and
interpreted as the aggregate bandwidth constraint across
all Class-Types
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_constraint',)

  _yang_name = 'bandwidth-constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isn', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints']

  def _get_bandwidth_constraint(self):
    """
    Getter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    return self.__bandwidth_constraint
      
  def _set_bandwidth_constraint(self, v, load=False):
    """
    Setter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_constraint() directly.

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_constraint(self):
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_constraint = __builtin__.property(_get_bandwidth_constraint)


  _pyangbind_elements = OrderedDict([('bandwidth_constraint', bandwidth_constraint), ])


from . import bandwidth_constraint
class bandwidth_constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines bandwidth-constraints. For DS-TE,
the existing Maximum Reservable link bandwidth parameter
is retained, but its semantics is generalized and
interpreted as the aggregate bandwidth constraint across
all Class-Types
  """
  __slots__ = ('_path_helper', '_extmethods', '__bandwidth_constraint',)

  _yang_name = 'bandwidth-constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-isn', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints']

  def _get_bandwidth_constraint(self):
    """
    Getter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    return self.__bandwidth_constraint
      
  def _set_bandwidth_constraint(self, v, load=False):
    """
    Setter method for bandwidth_constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_constraint() directly.

    YANG Description: List of the Bandwidth Constraints sub-TLV instances
present in the TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__bandwidth_constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_constraint(self):
    self.__bandwidth_constraint = YANGDynClass(base=YANGListType("model_id",bandwidth_constraint.bandwidth_constraint, yang_name="bandwidth-constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='model-id', extensions=None), is_container='list', yang_name="bandwidth-constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  bandwidth_constraint = __builtin__.property(_get_bandwidth_constraint)


  _pyangbind_elements = OrderedDict([('bandwidth_constraint', bandwidth_constraint), ])

