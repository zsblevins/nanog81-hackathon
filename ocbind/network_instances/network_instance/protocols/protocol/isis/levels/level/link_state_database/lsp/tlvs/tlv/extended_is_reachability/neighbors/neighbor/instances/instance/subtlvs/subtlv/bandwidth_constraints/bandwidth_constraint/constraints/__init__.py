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

from . import constraint
class constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Constraints contained within the Bandwidth
Constraints sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint',)

  _yang_name = 'constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'extended-is-reachability', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints']

  def _get_constraint(self):
    """
    Getter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    return self.__constraint
      
  def _set_constraint(self, v, load=False):
    """
    Setter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint() directly.

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint(self):
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  constraint = __builtin__.property(_get_constraint)


  _pyangbind_elements = OrderedDict([('constraint', constraint), ])


from . import constraint
class constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-models/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Constraints contained within the Bandwidth
Constraints sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint',)

  _yang_name = 'constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-models', 'lsp', 'tlvs', 'tlv', 'extended-is-reachability', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints']

  def _get_constraint(self):
    """
    Getter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    return self.__constraint
      
  def _set_constraint(self, v, load=False):
    """
    Setter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint() directly.

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint(self):
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  constraint = __builtin__.property(_get_constraint)


  _pyangbind_elements = OrderedDict([('constraint', constraint), ])


from . import constraint
class constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Constraints contained within the Bandwidth
Constraints sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint',)

  _yang_name = 'constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'extended-is-reachability', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints']

  def _get_constraint(self):
    """
    Getter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    return self.__constraint
      
  def _set_constraint(self, v, load=False):
    """
    Setter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint() directly.

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint(self):
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  constraint = __builtin__.property(_get_constraint)


  _pyangbind_elements = OrderedDict([('constraint', constraint), ])


from . import constraint
class constraints(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-is-reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth-constraints/bandwidth-constraint/constraints. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Constraints contained within the Bandwidth
Constraints sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__constraint',)

  _yang_name = 'constraints'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'extended-is-reachability', 'neighbors', 'neighbor', 'instances', 'instance', 'subtlvs', 'subtlv', 'bandwidth-constraints', 'bandwidth-constraint', 'constraints']

  def _get_constraint(self):
    """
    Getter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    return self.__constraint
      
  def _set_constraint(self, v, load=False):
    """
    Setter method for constraint, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_is_reachability/neighbors/neighbor/instances/instance/subtlvs/subtlv/bandwidth_constraints/bandwidth_constraint/constraints/constraint (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constraint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constraint() directly.

    YANG Description: List of the constraints within the Bandwidth
Constraints sub-TLV. The BC0 level is indicated by
the constraint-id leaf being set to 0, with BCN
being indicated by constraint-id N.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constraint must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__constraint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constraint(self):
    self.__constraint = YANGDynClass(base=YANGListType("constraint_id",constraint.constraint, yang_name="constraint", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='constraint-id', extensions=None), is_container='list', yang_name="constraint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  constraint = __builtin__.property(_get_constraint)


  _pyangbind_elements = OrderedDict([('constraint', constraint), ])

