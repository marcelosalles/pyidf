from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class LoadProfilePlant(DataObject):
    """ Corresponds to IDD object `LoadProfile:Plant`
        Used to simulate a scheduled plant loop demand profile.  Load and flow rate are
        specified using schedules. Positive values are heating loads, and negative values are
        cooling loads. The actual load met is dependent on the performance of the supply
        loop components.
    """
    schema = {'min-fields': 0, 'name': u'LoadProfile:Plant', 'pyname': u'LoadProfilePlant', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'inlet node name', {'name': u'Inlet Node Name', 'pyname': u'inlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'outlet node name', {'name': u'Outlet Node Name', 'pyname': u'outlet_node_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'node'}), (u'load schedule name', {'name': u'Load Schedule Name', 'pyname': u'load_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'peak flow rate', {'name': u'Peak Flow Rate', 'pyname': u'peak_flow_rate', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm3/s'}), (u'flow rate fraction schedule name', {'name': u'Flow Rate Fraction Schedule Name', 'pyname': u'flow_rate_fraction_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Non'}

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Outlet Node Name"] = value

    @property
    def load_schedule_name(self):
        """Get load_schedule_name

        Returns:
            str: the value of `load_schedule_name` or None if not set
        """
        return self["Load Schedule Name"]

    @load_schedule_name.setter
    def load_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Load Schedule Name`
        Schedule values are load in [W]

        Args:
            value (str): value for IDD Field `Load Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Load Schedule Name"] = value

    @property
    def peak_flow_rate(self):
        """Get peak_flow_rate

        Returns:
            float: the value of `peak_flow_rate` or None if not set
        """
        return self["Peak Flow Rate"]

    @peak_flow_rate.setter
    def peak_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Peak Flow Rate`

        Args:
            value (float): value for IDD Field `Peak Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Peak Flow Rate"] = value

    @property
    def flow_rate_fraction_schedule_name(self):
        """Get flow_rate_fraction_schedule_name

        Returns:
            str: the value of `flow_rate_fraction_schedule_name` or None if not set
        """
        return self["Flow Rate Fraction Schedule Name"]

    @flow_rate_fraction_schedule_name.setter
    def flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Flow Rate Fraction Schedule Name`

        Args:
            value (str): value for IDD Field `Flow Rate Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Flow Rate Fraction Schedule Name"] = value