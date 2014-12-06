from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class GroundHeatTransferSlabXface(DataObject):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:XFACE`
        This is only needed when using manual gridding (not recommended)
        XFACE: X Direction cell face coordinates: m
    """
    schema = {'min-fields': 0, 'name': u'GroundHeatTransfer:Slab:XFACE', 'pyname': u'GroundHeatTransferSlabXface', 'format': None, 'fields': OrderedDict(), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}


class GroundHeatTransferSlabYface(DataObject):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:YFACE`
        This is only needed when using manual gridding (not recommended)
        YFACE: Y Direction cell face coordinates: m,
    """
    schema = {'min-fields': 0, 'name': u'GroundHeatTransfer:Slab:YFACE', 'pyname': u'GroundHeatTransferSlabYface', 'format': None, 'fields': OrderedDict(), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}


class GroundHeatTransferSlabZface(DataObject):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:ZFACE`
        This is only needed when usuing manual gridding (not recommended)
        ZFACE: Z Direction cell face coordinates: m
    """
    schema = {'min-fields': 0, 'name': u'GroundHeatTransfer:Slab:ZFACE', 'pyname': u'GroundHeatTransferSlabZface', 'format': None, 'fields': OrderedDict(), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}


class GroundHeatTransferBasementXface(DataObject):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:XFACE`
        This is only needed when using manual gridding (not recommended)
        XFACE: X Direction cell face coordinates: m
    """
    schema = {'min-fields': 0, 'name': u'GroundHeatTransfer:Basement:XFACE', 'pyname': u'GroundHeatTransferBasementXface', 'format': None, 'fields': OrderedDict(), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}


class GroundHeatTransferBasementYface(DataObject):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:YFACE`
        This is only needed when using manual gridding (not recommended)
        YFACE: Y Direction cell face coordinates: m
    """
    schema = {'min-fields': 0, 'name': u'GroundHeatTransfer:Basement:YFACE', 'pyname': u'GroundHeatTransferBasementYface', 'format': None, 'fields': OrderedDict(), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}


class GroundHeatTransferBasementZface(DataObject):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:ZFACE`
        This is only needed when using manual gridding (not recommended)
        ZFACE: Z Direction cell face coordinates: m
    """
    schema = {'min-fields': 0, 'name': u'GroundHeatTransfer:Basement:ZFACE', 'pyname': u'GroundHeatTransferBasementZface', 'format': None, 'fields': OrderedDict(), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}


class RoomAirModelType(DataObject):
    """ Corresponds to IDD object `RoomAirModelType`
        Selects the type of room air model to be used in a given zone. If no RoomAirModelType
        object is specified then the default Mixing model (all zone air at the same
        temperature) will be used.
    """
    schema = {'min-fields': 0, 'name': u'RoomAirModelType', 'pyname': u'RoomAirModelType', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'room-air modeling type', {'name': u'Room-Air Modeling Type', 'pyname': u'roomair_modeling_type', 'default': u'Mixing', 'required-field': True, 'autosizable': False, 'accepted-values': [u'Mixing', u'UserDefined', u'OneNodeDisplacementVentilation', u'ThreeNodeDisplacementVentilation', u'CrossVentilation', u'UnderFloorAirDistributionInterior', u'UnderFloorAirDistributionExterior'], 'autocalculatable': False, 'type': 'alpha'}), (u'air temperature coupling strategy', {'name': u'Air Temperature Coupling Strategy', 'pyname': u'air_temperature_coupling_strategy', 'default': u'Direct', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Direct', u'Indirect'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def roomair_modeling_type(self):
        """Get roomair_modeling_type

        Returns:
            str: the value of `roomair_modeling_type` or None if not set
        """
        return self["Room-Air Modeling Type"]

    @roomair_modeling_type.setter
    def roomair_modeling_type(self, value="Mixing"):
        """  Corresponds to IDD Field `Room-Air Modeling Type`
        Complete mixing air model
        UserDefined Room Air Temperature Patterns
        needs RoomAir:TemperaturePattern:UserDefined object referencing this Zone
        Mundt roomair model for displacement ventilation with single floor air node
        needs RoomAirSettings:OneNodeDisplacementVentilation object referencing this Zone
        (UCSD three-node displacement ventilation model)
        needs RoomAirSettings:ThreeNodeDisplacementVentilation object referencing this Zone
        (UCSD two-zone cross ventilation model)
        needs RoomAirSettings:CrossVentilation object referencing this Zone
        2-Node UFAD model for interior zones
        needs RoomAirSettings:UnderFloorAirDistributionInterior object referencing this Zone
        (2-Node UFAD model for exterior zones)
        needs RoomAirSettings:UnderFloorAirDistributionExterior object referencing this Zone

        Args:
            value (str): value for IDD Field `Room-Air Modeling Type`
                Default value: Mixing
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Room-Air Modeling Type"] = value

    @property
    def air_temperature_coupling_strategy(self):
        """Get air_temperature_coupling_strategy

        Returns:
            str: the value of `air_temperature_coupling_strategy` or None if not set
        """
        return self["Air Temperature Coupling Strategy"]

    @air_temperature_coupling_strategy.setter
    def air_temperature_coupling_strategy(self, value="Direct"):
        """  Corresponds to IDD Field `Air Temperature Coupling Strategy`

        Args:
            value (str): value for IDD Field `Air Temperature Coupling Strategy`
                Default value: Direct
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Temperature Coupling Strategy"] = value


class RoomAirTemperaturePatternUserDefined(DataObject):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:UserDefined`
        Used to explicitly define temperature patterns that are to be applied to the mean air
        temperature within a thermal zone.  Used with RoomAirModelType = UserDefined.
    """
    schema = {'min-fields': 0, 'name': u'RoomAir:TemperaturePattern:UserDefined', 'pyname': u'RoomAirTemperaturePatternUserDefined', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'availability schedule name', {'name': u'Availability Schedule Name', 'pyname': u'availability_schedule_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'pattern control schedule name', {'name': u'Pattern Control Schedule Name', 'pyname': u'pattern_control_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this model. Schedule value > 0 means the model is
        active. Schedule value = 0 means the model is inactive and the zone will be modeled
        as fully mixed (Mixing). If this field is blank, the model is always active.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Availability Schedule Name"] = value

    @property
    def pattern_control_schedule_name(self):
        """Get pattern_control_schedule_name

        Returns:
            str: the value of `pattern_control_schedule_name` or None if not set
        """
        return self["Pattern Control Schedule Name"]

    @pattern_control_schedule_name.setter
    def pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Pattern Control Schedule Name`
        The schedule should contain integer values that
        correspond to unique Control Integer fields in
        one of the RoomAir:TemperaturePattern:* objects.

        Args:
            value (str): value for IDD Field `Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Pattern Control Schedule Name"] = value


class RoomAirTemperaturePatternConstantGradient(DataObject):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:ConstantGradient`
        Used to model room air with a fixed temperature gradient in the vertical direction.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    """
    schema = {'min-fields': 0, 'name': u'RoomAir:TemperaturePattern:ConstantGradient', 'pyname': u'RoomAirTemperaturePatternConstantGradient', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'control integer for pattern control schedule name', {'name': u'Control Integer for Pattern Control Schedule Name', 'pyname': u'control_integer_for_pattern_control_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'thermostat offset', {'name': u'Thermostat Offset', 'pyname': u'thermostat_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'return air offset', {'name': u'Return Air Offset', 'pyname': u'return_air_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'exhaust air offset', {'name': u'Exhaust Air Offset', 'pyname': u'exhaust_air_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'temperature gradient', {'name': u'Temperature Gradient', 'pyname': u'temperature_gradient', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'K/m'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        reference this entry in Schedule Name

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `Thermostat Offset`
        = (Temp at thermostat- Mean Air Temp)

        Args:
            value (float): value for IDD Field `Thermostat Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `Return Air Offset`
        = (Tleaving - Mean Air Temp )

        Args:
            value (float): value for IDD Field `Return Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Offset`
        = (Texhaust - Mean Air Temp) deg C

        Args:
            value (float): value for IDD Field `Exhaust Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exhaust Air Offset"] = value

    @property
    def temperature_gradient(self):
        """Get temperature_gradient

        Returns:
            float: the value of `temperature_gradient` or None if not set
        """
        return self["Temperature Gradient"]

    @temperature_gradient.setter
    def temperature_gradient(self, value=None):
        """  Corresponds to IDD Field `Temperature Gradient`
        Slope of temperature change in vertical direction

        Args:
            value (float): value for IDD Field `Temperature Gradient`
                Units: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Gradient"] = value


class RoomAirTemperaturePatternTwoGradient(DataObject):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:TwoGradient`
        Used to model room air with two temperature gradients in the vertical direction.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    """
    schema = {'min-fields': 0, 'name': u'RoomAir:TemperaturePattern:TwoGradient', 'pyname': u'RoomAirTemperaturePatternTwoGradient', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'control integer for pattern control schedule name', {'name': u'Control Integer for Pattern Control Schedule Name', 'pyname': u'control_integer_for_pattern_control_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'thermostat height', {'name': u'Thermostat Height', 'pyname': u'thermostat_height', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'return air height', {'name': u'Return Air Height', 'pyname': u'return_air_height', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'exhaust air height', {'name': u'Exhaust Air Height', 'pyname': u'exhaust_air_height', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'temperature gradient lower bound', {'name': u'Temperature Gradient Lower Bound', 'pyname': u'temperature_gradient_lower_bound', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'K/m'}), (u'temperature gradient upper  bound', {'name': u'Temperature Gradient Upper  Bound', 'pyname': u'temperature_gradient_upper_bound', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'K/m'}), (u'gradient interpolation mode', {'name': u'Gradient Interpolation Mode', 'pyname': u'gradient_interpolation_mode', 'required-field': False, 'autosizable': False, 'accepted-values': [u'OutdoorDryBulbTemperature', u'ZoneDryBulbTemperature', u'ZoneAndOutdoorTemperatureDifference', u'SensibleCoolingLoad', u'SensibleHeatingLoad'], 'autocalculatable': False, 'type': 'alpha'}), (u'upper temperature bound', {'name': u'Upper Temperature Bound', 'pyname': u'upper_temperature_bound', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'lower temperature bound', {'name': u'Lower Temperature Bound', 'pyname': u'lower_temperature_bound', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'upper heat rate bound', {'name': u'Upper Heat Rate Bound', 'pyname': u'upper_heat_rate_bound', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'W'}), (u'lower heat rate bound', {'name': u'Lower Heat Rate Bound', 'pyname': u'lower_heat_rate_bound', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'W'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        reference this entry in Schedule Name

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=None):
        """  Corresponds to IDD Field `Thermostat Height`
        = Distance from floor of zone

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Height"] = value

    @property
    def return_air_height(self):
        """Get return_air_height

        Returns:
            float: the value of `return_air_height` or None if not set
        """
        return self["Return Air Height"]

    @return_air_height.setter
    def return_air_height(self, value=None):
        """  Corresponds to IDD Field `Return Air Height`
        = Distance from floor of zone

        Args:
            value (float): value for IDD Field `Return Air Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Return Air Height"] = value

    @property
    def exhaust_air_height(self):
        """Get exhaust_air_height

        Returns:
            float: the value of `exhaust_air_height` or None if not set
        """
        return self["Exhaust Air Height"]

    @exhaust_air_height.setter
    def exhaust_air_height(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Height`
        = Distance from floor of zone

        Args:
            value (float): value for IDD Field `Exhaust Air Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exhaust Air Height"] = value

    @property
    def temperature_gradient_lower_bound(self):
        """Get temperature_gradient_lower_bound

        Returns:
            float: the value of `temperature_gradient_lower_bound` or None if not set
        """
        return self["Temperature Gradient Lower Bound"]

    @temperature_gradient_lower_bound.setter
    def temperature_gradient_lower_bound(self, value=None):
        """  Corresponds to IDD Field `Temperature Gradient Lower Bound`
        Slope of temperature change in vertical direction

        Args:
            value (float): value for IDD Field `Temperature Gradient Lower Bound`
                Units: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Gradient Lower Bound"] = value

    @property
    def temperature_gradient_upper_bound(self):
        """Get temperature_gradient_upper_bound

        Returns:
            float: the value of `temperature_gradient_upper_bound` or None if not set
        """
        return self["Temperature Gradient Upper  Bound"]

    @temperature_gradient_upper_bound.setter
    def temperature_gradient_upper_bound(self, value=None):
        """  Corresponds to IDD Field `Temperature Gradient Upper  Bound`
        Slope of temperature change in vertical direction

        Args:
            value (float): value for IDD Field `Temperature Gradient Upper  Bound`
                Units: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Gradient Upper  Bound"] = value

    @property
    def gradient_interpolation_mode(self):
        """Get gradient_interpolation_mode

        Returns:
            str: the value of `gradient_interpolation_mode` or None if not set
        """
        return self["Gradient Interpolation Mode"]

    @gradient_interpolation_mode.setter
    def gradient_interpolation_mode(self, value=None):
        """  Corresponds to IDD Field `Gradient Interpolation Mode`

        Args:
            value (str): value for IDD Field `Gradient Interpolation Mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Gradient Interpolation Mode"] = value

    @property
    def upper_temperature_bound(self):
        """Get upper_temperature_bound

        Returns:
            float: the value of `upper_temperature_bound` or None if not set
        """
        return self["Upper Temperature Bound"]

    @upper_temperature_bound.setter
    def upper_temperature_bound(self, value=None):
        """  Corresponds to IDD Field `Upper Temperature Bound`

        Args:
            value (float): value for IDD Field `Upper Temperature Bound`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Upper Temperature Bound"] = value

    @property
    def lower_temperature_bound(self):
        """Get lower_temperature_bound

        Returns:
            float: the value of `lower_temperature_bound` or None if not set
        """
        return self["Lower Temperature Bound"]

    @lower_temperature_bound.setter
    def lower_temperature_bound(self, value=None):
        """  Corresponds to IDD Field `Lower Temperature Bound`

        Args:
            value (float): value for IDD Field `Lower Temperature Bound`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Lower Temperature Bound"] = value

    @property
    def upper_heat_rate_bound(self):
        """Get upper_heat_rate_bound

        Returns:
            float: the value of `upper_heat_rate_bound` or None if not set
        """
        return self["Upper Heat Rate Bound"]

    @upper_heat_rate_bound.setter
    def upper_heat_rate_bound(self, value=None):
        """  Corresponds to IDD Field `Upper Heat Rate Bound`

        Args:
            value (float): value for IDD Field `Upper Heat Rate Bound`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Upper Heat Rate Bound"] = value

    @property
    def lower_heat_rate_bound(self):
        """Get lower_heat_rate_bound

        Returns:
            float: the value of `lower_heat_rate_bound` or None if not set
        """
        return self["Lower Heat Rate Bound"]

    @lower_heat_rate_bound.setter
    def lower_heat_rate_bound(self, value=None):
        """  Corresponds to IDD Field `Lower Heat Rate Bound`

        Args:
            value (float): value for IDD Field `Lower Heat Rate Bound`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Lower Heat Rate Bound"] = value


class RoomAirTemperaturePatternNondimensionalHeight(DataObject):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:NondimensionalHeight`
        Defines a distribution pattern for air temperatures relative to the current mean air
        temperature as a function of height. The height, referred to as Zeta, is non-dimensional
        by normalizing with the zone ceiling height.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    """
    schema = {'min-fields': 0, 'name': u'RoomAir:TemperaturePattern:NondimensionalHeight', 'pyname': u'RoomAirTemperaturePatternNondimensionalHeight', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'control integer for pattern control schedule name', {'name': u'Control Integer for Pattern Control Schedule Name', 'pyname': u'control_integer_for_pattern_control_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'thermostat offset', {'name': u'Thermostat Offset', 'pyname': u'thermostat_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'return air offset', {'name': u'Return Air Offset', 'pyname': u'return_air_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'exhaust air offset', {'name': u'Exhaust Air Offset', 'pyname': u'exhaust_air_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'})]), 'extensible-fields': OrderedDict([(u'pair 1 zeta nondimensional height', {'name': u'Pair 1 Zeta Nondimensional Height', 'pyname': u'pair_1_zeta_nondimensional_height', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'pair 1 delta adjacent air temperature', {'name': u'Pair 1 Delta Adjacent Air Temperature', 'pyname': u'pair_1_delta_adjacent_air_temperature', 'maximum': 20.0, 'required-field': True, 'autosizable': False, 'minimum': -10.0, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'})]), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        this value should appear in as a schedule value

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `Thermostat Offset`
        = (Temp at thermostat- Mean Air Temp)

        Args:
            value (float): value for IDD Field `Thermostat Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `Return Air Offset`
        = (Temp leaving - Mean Air Temp ) deg C

        Args:
            value (float): value for IDD Field `Return Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Offset`
        = (Temp exhaust - Mean Air Temp) deg C
        the remaining fields have pairs that describe the relative
        temperature pattern in the vertical direction of a zone
        Zeta is the nondimensional height (in z-direction). on [0..1]
        DeltaTai =  (Tai - MAT) in units of deg. C
        relative deg C on [-10.0 .. 20.0 ]

        Args:
            value (float): value for IDD Field `Exhaust Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exhaust Air Offset"] = value

    def add_extensible(self,
                       pair_1_zeta_nondimensional_height=None,
                       pair_1_delta_adjacent_air_temperature=None,
                       ):
        """ Add values for extensible fields

        Args:

            pair_1_zeta_nondimensional_height (float): value for IDD Field `Pair 1 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            pair_1_delta_adjacent_air_temperature (float): value for IDD Field `Pair 1 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        pair_1_zeta_nondimensional_height = self.check_value("Pair 1 Zeta Nondimensional Height", pair_1_zeta_nondimensional_height)
        vals.append(pair_1_zeta_nondimensional_height)
        pair_1_delta_adjacent_air_temperature = self.check_value("Pair 1 Delta Adjacent Air Temperature", pair_1_delta_adjacent_air_temperature)
        vals.append(pair_1_delta_adjacent_air_temperature)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._extdata


class RoomAirTemperaturePatternSurfaceMapping(DataObject):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:SurfaceMapping`
        Defines a distribution pattern for the air temperatures adjacent to individual surfaces.
        This allows controlling the adjacent air temperature on a surface-by-surface basis
        rather than by height. This allows modeling different adjacent air temperatures on
        the opposite sides of the zone. Used in combination with
        RoomAir:TemperaturePattern:UserDefined.
    """
    schema = {'min-fields': 0, 'name': u'RoomAir:TemperaturePattern:SurfaceMapping', 'pyname': u'RoomAirTemperaturePatternSurfaceMapping', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'control integer for pattern control schedule name', {'name': u'Control Integer for Pattern Control Schedule Name', 'pyname': u'control_integer_for_pattern_control_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'integer'}), (u'thermostat offset', {'name': u'Thermostat Offset', 'pyname': u'thermostat_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real', 'unit': u'deltaC'}), (u'return air offset', {'name': u'Return Air Offset', 'pyname': u'return_air_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real', 'unit': u'deltaC'}), (u'exhaust air offset', {'name': u'Exhaust Air Offset', 'pyname': u'exhaust_air_offset', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': 'real', 'unit': u'deltaC'})]), 'extensible-fields': OrderedDict([(u'surface name pair 1', {'name': u'Surface Name Pair 1', 'pyname': u'surface_name_pair_1', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'delta adjacent air temperature pair 1', {'name': u'Delta Adjacent Air Temperature Pair 1', 'pyname': u'delta_adjacent_air_temperature_pair_1', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'})]), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        reference this entry in schedule

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `Thermostat Offset`
        = (Temp at thermostat- Mean Air Temp)

        Args:
            value (float): value for IDD Field `Thermostat Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `Return Air Offset`
        = (Tleaving - Mean Air Temp ) deg C

        Args:
            value (float): value for IDD Field `Return Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Offset`
        = (Texhaust - Mean Air Temp) deg C

        Args:
            value (float): value for IDD Field `Exhaust Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Exhaust Air Offset"] = value

    def add_extensible(self,
                       surface_name_pair_1=None,
                       delta_adjacent_air_temperature_pair_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_name_pair_1 (str): value for IDD Field `Surface Name Pair 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            delta_adjacent_air_temperature_pair_1 (float): value for IDD Field `Delta Adjacent Air Temperature Pair 1`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        surface_name_pair_1 = self.check_value("Surface Name Pair 1", surface_name_pair_1)
        vals.append(surface_name_pair_1)
        delta_adjacent_air_temperature_pair_1 = self.check_value("Delta Adjacent Air Temperature Pair 1", delta_adjacent_air_temperature_pair_1)
        vals.append(delta_adjacent_air_temperature_pair_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._extdata


class RoomAirNode(DataObject):
    """ Corresponds to IDD object `RoomAir:Node`
        Define an air node for some types of nodal room air models
    """
    schema = {'min-fields': 0, 'name': u'RoomAir:Node', 'pyname': u'RoomAirNode', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'Alpha'}), (u'node type', {'name': u'Node Type', 'pyname': u'node_type', 'required-field': True, 'autosizable': False, 'accepted-values': [u'Inlet', u'Floor', u'Control', u'Ceiling', u'MundtRoom', u'Return'], 'autocalculatable': False, 'type': 'alpha'}), (u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'height of nodal control volume center', {'name': u'Height of Nodal Control Volume Center', 'pyname': u'height_of_nodal_control_volume_center', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'surface 1 name', {'name': u'Surface 1 Name', 'pyname': u'surface_1_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 2 name', {'name': u'Surface 2 Name', 'pyname': u'surface_2_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 3 name', {'name': u'Surface 3 Name', 'pyname': u'surface_3_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 4 name', {'name': u'Surface 4 Name', 'pyname': u'surface_4_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 5 name', {'name': u'Surface 5 Name', 'pyname': u'surface_5_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 6 name', {'name': u'Surface 6 Name', 'pyname': u'surface_6_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 7 name', {'name': u'Surface 7 Name', 'pyname': u'surface_7_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 8 name', {'name': u'Surface 8 Name', 'pyname': u'surface_8_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 9 name', {'name': u'Surface 9 Name', 'pyname': u'surface_9_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 10 name', {'name': u'Surface 10 Name', 'pyname': u'surface_10_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 11 name', {'name': u'Surface 11 Name', 'pyname': u'surface_11_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 12 name', {'name': u'Surface 12 Name', 'pyname': u'surface_12_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 13 name', {'name': u'Surface 13 Name', 'pyname': u'surface_13_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 14 name', {'name': u'Surface 14 Name', 'pyname': u'surface_14_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 15 name', {'name': u'Surface 15 Name', 'pyname': u'surface_15_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 16 name', {'name': u'Surface 16 Name', 'pyname': u'surface_16_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 17 name', {'name': u'Surface 17 Name', 'pyname': u'surface_17_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 18 name', {'name': u'Surface 18 Name', 'pyname': u'surface_18_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 19 name', {'name': u'Surface 19 Name', 'pyname': u'surface_19_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 20 name', {'name': u'Surface 20 Name', 'pyname': u'surface_20_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'surface 21 name', {'name': u'Surface 21 Name', 'pyname': u'surface_21_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

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
    def node_type(self):
        """Get node_type

        Returns:
            str: the value of `node_type` or None if not set
        """
        return self["Node Type"]

    @node_type.setter
    def node_type(self, value=None):
        """  Corresponds to IDD Field `Node Type`

        Args:
            value (str): value for IDD Field `Node Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Node Type"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def height_of_nodal_control_volume_center(self):
        """Get height_of_nodal_control_volume_center

        Returns:
            float: the value of `height_of_nodal_control_volume_center` or None if not set
        """
        return self["Height of Nodal Control Volume Center"]

    @height_of_nodal_control_volume_center.setter
    def height_of_nodal_control_volume_center(self, value=None):
        """  Corresponds to IDD Field `Height of Nodal Control Volume Center`

        Args:
            value (float): value for IDD Field `Height of Nodal Control Volume Center`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Height of Nodal Control Volume Center"] = value

    @property
    def surface_1_name(self):
        """Get surface_1_name

        Returns:
            str: the value of `surface_1_name` or None if not set
        """
        return self["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """  Corresponds to IDD Field `Surface 1 Name`

        Args:
            value (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 1 Name"] = value

    @property
    def surface_2_name(self):
        """Get surface_2_name

        Returns:
            str: the value of `surface_2_name` or None if not set
        """
        return self["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """  Corresponds to IDD Field `Surface 2 Name`

        Args:
            value (str): value for IDD Field `Surface 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 2 Name"] = value

    @property
    def surface_3_name(self):
        """Get surface_3_name

        Returns:
            str: the value of `surface_3_name` or None if not set
        """
        return self["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """  Corresponds to IDD Field `Surface 3 Name`

        Args:
            value (str): value for IDD Field `Surface 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 3 Name"] = value

    @property
    def surface_4_name(self):
        """Get surface_4_name

        Returns:
            str: the value of `surface_4_name` or None if not set
        """
        return self["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """  Corresponds to IDD Field `Surface 4 Name`

        Args:
            value (str): value for IDD Field `Surface 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 4 Name"] = value

    @property
    def surface_5_name(self):
        """Get surface_5_name

        Returns:
            str: the value of `surface_5_name` or None if not set
        """
        return self["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """  Corresponds to IDD Field `Surface 5 Name`

        Args:
            value (str): value for IDD Field `Surface 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 5 Name"] = value

    @property
    def surface_6_name(self):
        """Get surface_6_name

        Returns:
            str: the value of `surface_6_name` or None if not set
        """
        return self["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """  Corresponds to IDD Field `Surface 6 Name`

        Args:
            value (str): value for IDD Field `Surface 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 6 Name"] = value

    @property
    def surface_7_name(self):
        """Get surface_7_name

        Returns:
            str: the value of `surface_7_name` or None if not set
        """
        return self["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """  Corresponds to IDD Field `Surface 7 Name`

        Args:
            value (str): value for IDD Field `Surface 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 7 Name"] = value

    @property
    def surface_8_name(self):
        """Get surface_8_name

        Returns:
            str: the value of `surface_8_name` or None if not set
        """
        return self["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """  Corresponds to IDD Field `Surface 8 Name`

        Args:
            value (str): value for IDD Field `Surface 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 8 Name"] = value

    @property
    def surface_9_name(self):
        """Get surface_9_name

        Returns:
            str: the value of `surface_9_name` or None if not set
        """
        return self["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """  Corresponds to IDD Field `Surface 9 Name`

        Args:
            value (str): value for IDD Field `Surface 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 9 Name"] = value

    @property
    def surface_10_name(self):
        """Get surface_10_name

        Returns:
            str: the value of `surface_10_name` or None if not set
        """
        return self["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """  Corresponds to IDD Field `Surface 10 Name`

        Args:
            value (str): value for IDD Field `Surface 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 10 Name"] = value

    @property
    def surface_11_name(self):
        """Get surface_11_name

        Returns:
            str: the value of `surface_11_name` or None if not set
        """
        return self["Surface 11 Name"]

    @surface_11_name.setter
    def surface_11_name(self, value=None):
        """  Corresponds to IDD Field `Surface 11 Name`

        Args:
            value (str): value for IDD Field `Surface 11 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 11 Name"] = value

    @property
    def surface_12_name(self):
        """Get surface_12_name

        Returns:
            str: the value of `surface_12_name` or None if not set
        """
        return self["Surface 12 Name"]

    @surface_12_name.setter
    def surface_12_name(self, value=None):
        """  Corresponds to IDD Field `Surface 12 Name`

        Args:
            value (str): value for IDD Field `Surface 12 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 12 Name"] = value

    @property
    def surface_13_name(self):
        """Get surface_13_name

        Returns:
            str: the value of `surface_13_name` or None if not set
        """
        return self["Surface 13 Name"]

    @surface_13_name.setter
    def surface_13_name(self, value=None):
        """  Corresponds to IDD Field `Surface 13 Name`

        Args:
            value (str): value for IDD Field `Surface 13 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 13 Name"] = value

    @property
    def surface_14_name(self):
        """Get surface_14_name

        Returns:
            str: the value of `surface_14_name` or None if not set
        """
        return self["Surface 14 Name"]

    @surface_14_name.setter
    def surface_14_name(self, value=None):
        """  Corresponds to IDD Field `Surface 14 Name`

        Args:
            value (str): value for IDD Field `Surface 14 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 14 Name"] = value

    @property
    def surface_15_name(self):
        """Get surface_15_name

        Returns:
            str: the value of `surface_15_name` or None if not set
        """
        return self["Surface 15 Name"]

    @surface_15_name.setter
    def surface_15_name(self, value=None):
        """  Corresponds to IDD Field `Surface 15 Name`

        Args:
            value (str): value for IDD Field `Surface 15 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 15 Name"] = value

    @property
    def surface_16_name(self):
        """Get surface_16_name

        Returns:
            str: the value of `surface_16_name` or None if not set
        """
        return self["Surface 16 Name"]

    @surface_16_name.setter
    def surface_16_name(self, value=None):
        """  Corresponds to IDD Field `Surface 16 Name`

        Args:
            value (str): value for IDD Field `Surface 16 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 16 Name"] = value

    @property
    def surface_17_name(self):
        """Get surface_17_name

        Returns:
            str: the value of `surface_17_name` or None if not set
        """
        return self["Surface 17 Name"]

    @surface_17_name.setter
    def surface_17_name(self, value=None):
        """  Corresponds to IDD Field `Surface 17 Name`

        Args:
            value (str): value for IDD Field `Surface 17 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 17 Name"] = value

    @property
    def surface_18_name(self):
        """Get surface_18_name

        Returns:
            str: the value of `surface_18_name` or None if not set
        """
        return self["Surface 18 Name"]

    @surface_18_name.setter
    def surface_18_name(self, value=None):
        """  Corresponds to IDD Field `Surface 18 Name`

        Args:
            value (str): value for IDD Field `Surface 18 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 18 Name"] = value

    @property
    def surface_19_name(self):
        """Get surface_19_name

        Returns:
            str: the value of `surface_19_name` or None if not set
        """
        return self["Surface 19 Name"]

    @surface_19_name.setter
    def surface_19_name(self, value=None):
        """  Corresponds to IDD Field `Surface 19 Name`

        Args:
            value (str): value for IDD Field `Surface 19 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 19 Name"] = value

    @property
    def surface_20_name(self):
        """Get surface_20_name

        Returns:
            str: the value of `surface_20_name` or None if not set
        """
        return self["Surface 20 Name"]

    @surface_20_name.setter
    def surface_20_name(self, value=None):
        """  Corresponds to IDD Field `Surface 20 Name`

        Args:
            value (str): value for IDD Field `Surface 20 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 20 Name"] = value

    @property
    def surface_21_name(self):
        """Get surface_21_name

        Returns:
            str: the value of `surface_21_name` or None if not set
        """
        return self["Surface 21 Name"]

    @surface_21_name.setter
    def surface_21_name(self, value=None):
        """  Corresponds to IDD Field `Surface 21 Name`

        Args:
            value (str): value for IDD Field `Surface 21 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Surface 21 Name"] = value


class RoomAirSettingsOneNodeDisplacementVentilation(DataObject):
    """ Corresponds to IDD object `RoomAirSettings:OneNodeDisplacementVentilation`
        The Mundt model for displacement ventilation
    """
    schema = {'min-fields': 0, 'name': u'RoomAirSettings:OneNodeDisplacementVentilation', 'pyname': u'RoomAirSettingsOneNodeDisplacementVentilation', 'format': None, 'fields': OrderedDict([(u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fraction of convective internal loads added to floor air', {'name': u'Fraction of Convective Internal Loads Added to Floor Air', 'pyname': u'fraction_of_convective_internal_loads_added_to_floor_air', 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'}), (u'fraction of infiltration internal loads added to floor air', {'name': u'Fraction of Infiltration Internal Loads Added to Floor Air', 'pyname': u'fraction_of_infiltration_internal_loads_added_to_floor_air', 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def fraction_of_convective_internal_loads_added_to_floor_air(self):
        """Get fraction_of_convective_internal_loads_added_to_floor_air

        Returns:
            float: the value of `fraction_of_convective_internal_loads_added_to_floor_air` or None if not set
        """
        return self["Fraction of Convective Internal Loads Added to Floor Air"]

    @fraction_of_convective_internal_loads_added_to_floor_air.setter
    def fraction_of_convective_internal_loads_added_to_floor_air(self, value=None):
        """  Corresponds to IDD Field `Fraction of Convective Internal Loads Added to Floor Air`

        Args:
            value (float): value for IDD Field `Fraction of Convective Internal Loads Added to Floor Air`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fraction of Convective Internal Loads Added to Floor Air"] = value

    @property
    def fraction_of_infiltration_internal_loads_added_to_floor_air(self):
        """Get fraction_of_infiltration_internal_loads_added_to_floor_air

        Returns:
            float: the value of `fraction_of_infiltration_internal_loads_added_to_floor_air` or None if not set
        """
        return self["Fraction of Infiltration Internal Loads Added to Floor Air"]

    @fraction_of_infiltration_internal_loads_added_to_floor_air.setter
    def fraction_of_infiltration_internal_loads_added_to_floor_air(self, value=None):
        """  Corresponds to IDD Field `Fraction of Infiltration Internal Loads Added to Floor Air`

        Args:
            value (float): value for IDD Field `Fraction of Infiltration Internal Loads Added to Floor Air`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fraction of Infiltration Internal Loads Added to Floor Air"] = value


class RoomAirSettingsThreeNodeDisplacementVentilation(DataObject):
    """ Corresponds to IDD object `RoomAirSettings:ThreeNodeDisplacementVentilation`
        The UCSD model for Displacement Ventilation
    """
    schema = {'min-fields': 0, 'name': u'RoomAirSettings:ThreeNodeDisplacementVentilation', 'pyname': u'RoomAirSettingsThreeNodeDisplacementVentilation', 'format': None, 'fields': OrderedDict([(u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'gain distribution schedule name', {'name': u'Gain Distribution Schedule Name', 'pyname': u'gain_distribution_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'number of plumes per occupant', {'name': u'Number of Plumes per Occupant', 'pyname': u'number_of_plumes_per_occupant', 'default': 1.0, 'minimum>': 0.0, 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'thermostat height', {'name': u'Thermostat Height', 'pyname': u'thermostat_height', 'default': 1.1, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'comfort height', {'name': u'Comfort Height', 'pyname': u'comfort_height', 'default': 1.1, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'temperature difference threshold for reporting', {'name': u'Temperature Difference Threshold for Reporting', 'pyname': u'temperature_difference_threshold_for_reporting', 'default': 0.4, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone being described. Any existing zone name

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def gain_distribution_schedule_name(self):
        """Get gain_distribution_schedule_name

        Returns:
            str: the value of `gain_distribution_schedule_name` or None if not set
        """
        return self["Gain Distribution Schedule Name"]

    @gain_distribution_schedule_name.setter
    def gain_distribution_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Gain Distribution Schedule Name`
        Distribution of the convective heat gains between the occupied and mixed zones.
        0<= Accepted Value <= 1.
        In the DV model 1 means all convective gains in the lower layer.

        Args:
            value (str): value for IDD Field `Gain Distribution Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Gain Distribution Schedule Name"] = value

    @property
    def number_of_plumes_per_occupant(self):
        """Get number_of_plumes_per_occupant

        Returns:
            float: the value of `number_of_plumes_per_occupant` or None if not set
        """
        return self["Number of Plumes per Occupant"]

    @number_of_plumes_per_occupant.setter
    def number_of_plumes_per_occupant(self, value=1.0):
        """  Corresponds to IDD Field `Number of Plumes per Occupant`
        Used only in the UCSD displacement ventilation model.
        Effective number of separate plumes per occupant in the occupied zone.
        Plumes that merge together in the occupied zone count as one.

        Args:
            value (float): value for IDD Field `Number of Plumes per Occupant`
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Plumes per Occupant"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.1):
        """  Corresponds to IDD Field `Thermostat Height`
        Height of thermostat/temperature control sensor above floor

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                Default value: 1.1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1):
        """  Corresponds to IDD Field `Comfort Height`
        Height at which air temperature is calculated for comfort purposes

        Args:
            value (float): value for IDD Field `Comfort Height`
                Units: m
                Default value: 1.1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4):
        """  Corresponds to IDD Field `Temperature Difference Threshold for Reporting`
        Minimum temperature difference between predicted upper and lower layer
        temperatures above which DV auxilliary outputs are calculated.
        These outputs are 'DV Transition Height', 'DV Fraction Min Recommended Flow Rate'
        'DV Average Temp Gradient' and 'DV Maximum Temp Gradient'.  They
        are set to negative values when the temperature difference is less than the
        threshold and the output 'DV Zone Is Mixed' is set to 1

        Args:
            value (float): value for IDD Field `Temperature Difference Threshold for Reporting`
                Units: deltaC
                Default value: 0.4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Difference Threshold for Reporting"] = value


class RoomAirSettingsCrossVentilation(DataObject):
    """ Corresponds to IDD object `RoomAirSettings:CrossVentilation`
        This UCSD Cross Ventilation Room Air Model provides a simple model for heat transfer
        and vertical temperature profile prediction in cross ventilated rooms. The model
        distinguishes two regions in the room, the main jet region and the recirculations,
        and predicts characteristic airflow velocities and average air temperatures.
        Used with RoomAirModelType = CrossVentilation.
    """
    schema = {'min-fields': 0, 'name': u'RoomAirSettings:CrossVentilation', 'pyname': u'RoomAirSettingsCrossVentilation', 'format': None, 'fields': OrderedDict([(u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'gain distribution schedule name', {'name': u'Gain Distribution Schedule Name', 'pyname': u'gain_distribution_schedule_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'airflow region used for thermal comfort evaluation', {'name': u'Airflow Region Used for Thermal Comfort Evaluation', 'pyname': u'airflow_region_used_for_thermal_comfort_evaluation', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Jet', u'Recirculation'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone being described. Any existing zone name

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def gain_distribution_schedule_name(self):
        """Get gain_distribution_schedule_name

        Returns:
            str: the value of `gain_distribution_schedule_name` or None if not set
        """
        return self["Gain Distribution Schedule Name"]

    @gain_distribution_schedule_name.setter
    def gain_distribution_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Gain Distribution Schedule Name`
        Distribution of the convective heat gains between the jet and recirculation zones.
        0<= Accepted Value <= 1.
        In the CV model 1 means all convective gains in the jet region.

        Args:
            value (str): value for IDD Field `Gain Distribution Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Gain Distribution Schedule Name"] = value

    @property
    def airflow_region_used_for_thermal_comfort_evaluation(self):
        """Get airflow_region_used_for_thermal_comfort_evaluation

        Returns:
            str: the value of `airflow_region_used_for_thermal_comfort_evaluation` or None if not set
        """
        return self["Airflow Region Used for Thermal Comfort Evaluation"]

    @airflow_region_used_for_thermal_comfort_evaluation.setter
    def airflow_region_used_for_thermal_comfort_evaluation(self, value=None):
        """  Corresponds to IDD Field `Airflow Region Used for Thermal Comfort Evaluation`
        Required field whenever thermal comfort is predicted
        defines Air temperature and Airflow velocity that will be used in the Fanger model
        conditions must refer to one of the two regions: jet or recirculation

        Args:
            value (str): value for IDD Field `Airflow Region Used for Thermal Comfort Evaluation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Airflow Region Used for Thermal Comfort Evaluation"] = value


class RoomAirSettingsUnderFloorAirDistributionInterior(DataObject):
    """ Corresponds to IDD object `RoomAirSettings:UnderFloorAirDistributionInterior`
        This Room Air Model is applicable to interior spaces that are served by an underfloor
        air distribution system. The dominant sources of heat gain should be from people,
        equipment, and other localized sources located in the occupied part of the room.
        The model should be used with caution in zones which have large heat gains or losses
        through exterior walls or windows or which have considerable direct solar gain.
        Used with RoomAirModelType = UnderFloorAirDistributionInterior.
    """
    schema = {'min-fields': 15, 'name': u'RoomAirSettings:UnderFloorAirDistributionInterior', 'pyname': u'RoomAirSettingsUnderFloorAirDistributionInterior', 'format': None, 'fields': OrderedDict([(u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'number of diffusers', {'name': u'Number of Diffusers', 'pyname': u'number_of_diffusers', 'default': 'autocalculate', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'power per plume', {'name': u'Power per Plume', 'pyname': u'power_per_plume', 'default': 'autocalculate', 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': True, 'type': u'real', 'unit': u'W'}), (u'design effective area of diffuser', {'name': u'Design Effective Area of Diffuser', 'pyname': u'design_effective_area_of_diffuser', 'default': 'Autocalculate', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real', 'unit': u'm2'}), (u'diffuser slot angle from vertical', {'name': u'Diffuser Slot Angle from Vertical', 'pyname': u'diffuser_slot_angle_from_vertical', 'default': 'Autocalculate', 'maximum': 90.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': True, 'type': u'real', 'unit': u'deg'}), (u'thermostat height', {'name': u'Thermostat Height', 'pyname': u'thermostat_height', 'default': 1.2, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'comfort height', {'name': u'Comfort Height', 'pyname': u'comfort_height', 'default': 1.1, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'temperature difference threshold for reporting', {'name': u'Temperature Difference Threshold for Reporting', 'pyname': u'temperature_difference_threshold_for_reporting', 'default': 0.4, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'floor diffuser type', {'name': u'Floor Diffuser Type', 'pyname': u'floor_diffuser_type', 'default': u'Swirl', 'required-field': True, 'autosizable': False, 'accepted-values': [u'Custom', u'Swirl', u'VariableArea', u'HorizontalSwirl', u'LinearBarGrille'], 'autocalculatable': False, 'type': 'alpha'}), (u'transition height', {'name': u'Transition Height', 'pyname': u'transition_height', 'default': 1.7, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real', 'unit': u'm'}), (u'coefficient a', {'name': u'Coefficient A', 'pyname': u'coefficient_a', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient b', {'name': u'Coefficient B', 'pyname': u'coefficient_b', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient c', {'name': u'Coefficient C', 'pyname': u'coefficient_c', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient d', {'name': u'Coefficient D', 'pyname': u'coefficient_d', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient e', {'name': u'Coefficient E', 'pyname': u'coefficient_e', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone with underfloor air distribution

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def number_of_diffusers(self):
        """Get number_of_diffusers

        Returns:
            float: the value of `number_of_diffusers` or None if not set
        """
        return self["Number of Diffusers"]

    @number_of_diffusers.setter
    def number_of_diffusers(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Diffusers`
        Total number of diffusers in this zone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Diffusers`
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Diffusers"] = value

    @property
    def power_per_plume(self):
        """Get power_per_plume

        Returns:
            float: the value of `power_per_plume` or None if not set
        """
        return self["Power per Plume"]

    @power_per_plume.setter
    def power_per_plume(self, value="autocalculate"):
        """  Corresponds to IDD Field `Power per Plume`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Power per Plume`
                Units: W
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Power per Plume"] = value

    @property
    def design_effective_area_of_diffuser(self):
        """Get design_effective_area_of_diffuser

        Returns:
            float: the value of `design_effective_area_of_diffuser` or None if not set
        """
        return self["Design Effective Area of Diffuser"]

    @design_effective_area_of_diffuser.setter
    def design_effective_area_of_diffuser(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Design Effective Area of Diffuser`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Effective Area of Diffuser`
                Units: m2
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Design Effective Area of Diffuser"] = value

    @property
    def diffuser_slot_angle_from_vertical(self):
        """Get diffuser_slot_angle_from_vertical

        Returns:
            float: the value of `diffuser_slot_angle_from_vertical` or None if not set
        """
        return self["Diffuser Slot Angle from Vertical"]

    @diffuser_slot_angle_from_vertical.setter
    def diffuser_slot_angle_from_vertical(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Diffuser Slot Angle from Vertical`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Diffuser Slot Angle from Vertical`
                Units: deg
                Default value: "Autocalculate"
                value <= 90.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Diffuser Slot Angle from Vertical"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.2):
        """  Corresponds to IDD Field `Thermostat Height`
        Height of thermostat/temperature control sensor above floor

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                Default value: 1.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1):
        """  Corresponds to IDD Field `Comfort Height`
        Height at which air temperature is calculated for comfort purposes

        Args:
            value (float): value for IDD Field `Comfort Height`
                Units: m
                Default value: 1.1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4):
        """  Corresponds to IDD Field `Temperature Difference Threshold for Reporting`
        Minimum temperature difference between predicted upper and lower layer
        temperatures above which UFAD auxilliary outputs are calculated.
        These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They
        are set to zero values when the temperature difference is less than the
        threshold and the output 'UF Zone Is Mixed' is set to 1

        Args:
            value (float): value for IDD Field `Temperature Difference Threshold for Reporting`
                Units: deltaC
                Default value: 0.4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Difference Threshold for Reporting"] = value

    @property
    def floor_diffuser_type(self):
        """Get floor_diffuser_type

        Returns:
            str: the value of `floor_diffuser_type` or None if not set
        """
        return self["Floor Diffuser Type"]

    @floor_diffuser_type.setter
    def floor_diffuser_type(self, value="Swirl"):
        """  Corresponds to IDD Field `Floor Diffuser Type`

        Args:
            value (str): value for IDD Field `Floor Diffuser Type`
                Default value: Swirl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Floor Diffuser Type"] = value

    @property
    def transition_height(self):
        """Get transition_height

        Returns:
            float: the value of `transition_height` or None if not set
        """
        return self["Transition Height"]

    @transition_height.setter
    def transition_height(self, value=1.7):
        """  Corresponds to IDD Field `Transition Height`
        user-specified height above floor of boundary between occupied and upper subzones

        Args:
            value (float or "Autocalculate"): value for IDD Field `Transition Height`
                Units: m
                Default value: 1.7
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Transition Height"] = value

    @property
    def coefficient_a(self):
        """Get coefficient_a

        Returns:
            float: the value of `coefficient_a` or None if not set
        """
        return self["Coefficient A"]

    @coefficient_a.setter
    def coefficient_a(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient A`
        Coefficient A in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient A`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient A"] = value

    @property
    def coefficient_b(self):
        """Get coefficient_b

        Returns:
            float: the value of `coefficient_b` or None if not set
        """
        return self["Coefficient B"]

    @coefficient_b.setter
    def coefficient_b(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient B`
        Coefficient B in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient B`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient B"] = value

    @property
    def coefficient_c(self):
        """Get coefficient_c

        Returns:
            float: the value of `coefficient_c` or None if not set
        """
        return self["Coefficient C"]

    @coefficient_c.setter
    def coefficient_c(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient C`
        Coefficient C in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient C`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient C"] = value

    @property
    def coefficient_d(self):
        """Get coefficient_d

        Returns:
            float: the value of `coefficient_d` or None if not set
        """
        return self["Coefficient D"]

    @coefficient_d.setter
    def coefficient_d(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient D`
        Coefficient D in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient D`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient D"] = value

    @property
    def coefficient_e(self):
        """Get coefficient_e

        Returns:
            float: the value of `coefficient_e` or None if not set
        """
        return self["Coefficient E"]

    @coefficient_e.setter
    def coefficient_e(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient E`
        Coefficient E in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient E`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient E"] = value


class RoomAirSettingsUnderFloorAirDistributionExterior(DataObject):
    """ Corresponds to IDD object `RoomAirSettings:UnderFloorAirDistributionExterior`
        Applicable to exterior spaces that are served by an underfloor air distribution system.
        The dominant sources of heat gain should be from people, equipment, and other
        localized sources located in the occupied part of the room, as well as convective gain
        coming from a warm window. Used with RoomAirModelType = CrossVentilation.
    """
    schema = {'min-fields': 15, 'name': u'RoomAirSettings:UnderFloorAirDistributionExterior', 'pyname': u'RoomAirSettingsUnderFloorAirDistributionExterior', 'format': None, 'fields': OrderedDict([(u'zone name', {'name': u'Zone Name', 'pyname': u'zone_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'number of diffusers per zone', {'name': u'Number of Diffusers per Zone', 'pyname': u'number_of_diffusers_per_zone', 'default': 'Autocalculate', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'power per plume', {'name': u'Power per Plume', 'pyname': u'power_per_plume', 'default': 'autocalculate', 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': True, 'type': u'real', 'unit': u'W'}), (u'design effective area of diffuser', {'name': u'Design Effective Area of Diffuser', 'pyname': u'design_effective_area_of_diffuser', 'default': 'Autocalculate', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real', 'unit': u'm2'}), (u'diffuser slot angle from vertical', {'name': u'Diffuser Slot Angle from Vertical', 'pyname': u'diffuser_slot_angle_from_vertical', 'default': 'autocalculate', 'maximum': 90.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': True, 'type': u'real', 'unit': u'deg'}), (u'thermostat height', {'name': u'Thermostat Height', 'pyname': u'thermostat_height', 'default': 1.2, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'comfort height', {'name': u'Comfort Height', 'pyname': u'comfort_height', 'default': 1.1, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'm'}), (u'temperature difference threshold for reporting', {'name': u'Temperature Difference Threshold for Reporting', 'pyname': u'temperature_difference_threshold_for_reporting', 'default': 0.4, 'required-field': True, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'deltaC'}), (u'floor diffuser type', {'name': u'Floor Diffuser Type', 'pyname': u'floor_diffuser_type', 'default': u'Swirl', 'required-field': True, 'autosizable': False, 'accepted-values': [u'Custom', u'Swirl', u'VariableArea', u'HorizontalSwirl', u'LinearBarGrille'], 'autocalculatable': False, 'type': 'alpha'}), (u'transition height', {'name': u'Transition Height', 'pyname': u'transition_height', 'default': 1.7, 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real', 'unit': u'm'}), (u'coefficient a in formula kc = a*gamma**b + c + d*gamma + e*gamma**2', {'name': u'Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', 'pyname': u'coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient b in formula kc = a*gamma**b + c + d*gamma + e*gamma**2', {'name': u'Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', 'pyname': u'coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient c in formula kc = a*gamma**b + c + d*gamma + e*gamma**2', {'name': u'Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', 'pyname': u'coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient d in formula kc = a*gamma**b + c + d*gamma + e*gamma**2', {'name': u'Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', 'pyname': u'coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'}), (u'coefficient e in formula kc = a*gamma**b + c + d*gamma + e*gamma**2', {'name': u'Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', 'pyname': u'coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2', 'default': 'Autocalculate', 'required-field': False, 'autosizable': False, 'autocalculatable': True, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False, 'group': u' Room Air Models'}

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone being described. Any existing zone name

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Zone Name"] = value

    @property
    def number_of_diffusers_per_zone(self):
        """Get number_of_diffusers_per_zone

        Returns:
            float: the value of `number_of_diffusers_per_zone` or None if not set
        """
        return self["Number of Diffusers per Zone"]

    @number_of_diffusers_per_zone.setter
    def number_of_diffusers_per_zone(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Number of Diffusers per Zone`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Diffusers per Zone`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Number of Diffusers per Zone"] = value

    @property
    def power_per_plume(self):
        """Get power_per_plume

        Returns:
            float: the value of `power_per_plume` or None if not set
        """
        return self["Power per Plume"]

    @power_per_plume.setter
    def power_per_plume(self, value="autocalculate"):
        """  Corresponds to IDD Field `Power per Plume`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Power per Plume`
                Units: W
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Power per Plume"] = value

    @property
    def design_effective_area_of_diffuser(self):
        """Get design_effective_area_of_diffuser

        Returns:
            float: the value of `design_effective_area_of_diffuser` or None if not set
        """
        return self["Design Effective Area of Diffuser"]

    @design_effective_area_of_diffuser.setter
    def design_effective_area_of_diffuser(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Design Effective Area of Diffuser`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Effective Area of Diffuser`
                Units: m2
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Design Effective Area of Diffuser"] = value

    @property
    def diffuser_slot_angle_from_vertical(self):
        """Get diffuser_slot_angle_from_vertical

        Returns:
            float: the value of `diffuser_slot_angle_from_vertical` or None if not set
        """
        return self["Diffuser Slot Angle from Vertical"]

    @diffuser_slot_angle_from_vertical.setter
    def diffuser_slot_angle_from_vertical(self, value="autocalculate"):
        """  Corresponds to IDD Field `Diffuser Slot Angle from Vertical`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Diffuser Slot Angle from Vertical`
                Units: deg
                Default value: "autocalculate"
                value <= 90.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Diffuser Slot Angle from Vertical"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.2):
        """  Corresponds to IDD Field `Thermostat Height`
        Height of thermostat/temperature control sensor above floor

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                Default value: 1.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1):
        """  Corresponds to IDD Field `Comfort Height`
        Height at which Air temperature is calculated for comfort purposes

        Args:
            value (float): value for IDD Field `Comfort Height`
                Units: m
                Default value: 1.1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4):
        """  Corresponds to IDD Field `Temperature Difference Threshold for Reporting`
        Minimum temperature difference between upper and lower layer
        temperatures above which UFAD auxilliary outputs are calculated.
        These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They
        are set to zero values when the temperature difference is less than the
        threshold and the output 'UF Zone Is Mixed' is set to 1

        Args:
            value (float): value for IDD Field `Temperature Difference Threshold for Reporting`
                Units: deltaC
                Default value: 0.4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Difference Threshold for Reporting"] = value

    @property
    def floor_diffuser_type(self):
        """Get floor_diffuser_type

        Returns:
            str: the value of `floor_diffuser_type` or None if not set
        """
        return self["Floor Diffuser Type"]

    @floor_diffuser_type.setter
    def floor_diffuser_type(self, value="Swirl"):
        """  Corresponds to IDD Field `Floor Diffuser Type`

        Args:
            value (str): value for IDD Field `Floor Diffuser Type`
                Default value: Swirl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Floor Diffuser Type"] = value

    @property
    def transition_height(self):
        """Get transition_height

        Returns:
            float: the value of `transition_height` or None if not set
        """
        return self["Transition Height"]

    @transition_height.setter
    def transition_height(self, value=1.7):
        """  Corresponds to IDD Field `Transition Height`
        User-specified height above floor of boundary between occupied and upper subzones

        Args:
            value (float or "Autocalculate"): value for IDD Field `Transition Height`
                Units: m
                Default value: 1.7
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Transition Height"] = value

    @property
    def coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value