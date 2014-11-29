from collections import OrderedDict

class RoomAirTemperaturePatternUserDefined(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:UserDefined`
        Used to explicitly define temperature patterns that are to be applied to the mean air
        temperature within a thermal zone.  Used with RoomAirModelType = UserDefined.
    """
    internal_name = "RoomAir:TemperaturePattern:UserDefined"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAir:TemperaturePattern:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Pattern Control Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pattern_control_schedule_name = None
        else:
            self.pattern_control_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this model. Schedule value > 0 means the model is
        active. Schedule value = 0 means the model is inactive and the zone will be modeled
        as fully mixed (Mixing). If this field is blank, the model is always active.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def pattern_control_schedule_name(self):
        """Get pattern_control_schedule_name

        Returns:
            str: the value of `pattern_control_schedule_name` or None if not set
        """
        return self._data["Pattern Control Schedule Name"]

    @pattern_control_schedule_name.setter
    def pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pattern_control_schedule_name`
        The schedule should contain integer values that
        correspond to unique Control Integer fields in
        one of the RoomAir:TemperaturePattern:* objects.

        Args:
            value (str): value for IDD Field `pattern_control_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pattern_control_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pattern_control_schedule_name`')

        self._data["Pattern Control Schedule Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.pattern_control_schedule_name))
        return ",".join(out)

class RoomAirTemperaturePatternConstantGradient(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:ConstantGradient`
        Used to model room air with a fixed temperature gradient in the vertical direction.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    """
    internal_name = "RoomAir:TemperaturePattern:ConstantGradient"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAir:TemperaturePattern:ConstantGradient`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Offset"] = None
        self._data["Return Air Offset"] = None
        self._data["Exhaust Air Offset"] = None
        self._data["Temperature Gradient"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_offset = None
        else:
            self.thermostat_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_offset = None
        else:
            self.return_air_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_offset = None
        else:
            self.exhaust_air_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_gradient = None
        else:
            self.temperature_gradient = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_integer_for_pattern_control_schedule_name`
        reference this entry in Schedule Name

        Args:
            value (int): value for IDD Field `control_integer_for_pattern_control_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))

        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self._data["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `thermostat_offset`
        = (Temp at thermostat- Mean Air Temp)

        Args:
            value (float): value for IDD Field `thermostat_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_offset`'.format(value))

        self._data["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self._data["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `return_air_offset`
        = (Tleaving - Mean Air Temp )

        Args:
            value (float): value for IDD Field `return_air_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_offset`'.format(value))

        self._data["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self._data["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_offset`
        = (Texhaust - Mean Air Temp) deg C

        Args:
            value (float): value for IDD Field `exhaust_air_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_offset`'.format(value))

        self._data["Exhaust Air Offset"] = value

    @property
    def temperature_gradient(self):
        """Get temperature_gradient

        Returns:
            float: the value of `temperature_gradient` or None if not set
        """
        return self._data["Temperature Gradient"]

    @temperature_gradient.setter
    def temperature_gradient(self, value=None):
        """  Corresponds to IDD Field `temperature_gradient`
        Slope of temperature change in vertical direction

        Args:
            value (float): value for IDD Field `temperature_gradient`
                Unit: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_gradient`'.format(value))

        self._data["Temperature Gradient"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.control_integer_for_pattern_control_schedule_name))
        out.append(self._to_str(self.thermostat_offset))
        out.append(self._to_str(self.return_air_offset))
        out.append(self._to_str(self.exhaust_air_offset))
        out.append(self._to_str(self.temperature_gradient))
        return ",".join(out)

class RoomAirTemperaturePatternTwoGradient(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:TwoGradient`
        Used to model room air with two temperature gradients in the vertical direction.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    """
    internal_name = "RoomAir:TemperaturePattern:TwoGradient"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAir:TemperaturePattern:TwoGradient`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Height"] = None
        self._data["Return Air Height"] = None
        self._data["Exhaust Air Height"] = None
        self._data["Temperature Gradient Lower Bound"] = None
        self._data["Temperature Gradient Upper  Bound"] = None
        self._data["Gradient Interpolation Mode"] = None
        self._data["Upper Temperature Bound"] = None
        self._data["Lower Temperature Bound"] = None
        self._data["Upper Heat Rate Bound"] = None
        self._data["Lower Heat Rate Bound"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_height = None
        else:
            self.return_air_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_height = None
        else:
            self.exhaust_air_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_gradient_lower_bound = None
        else:
            self.temperature_gradient_lower_bound = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_gradient_upper_bound = None
        else:
            self.temperature_gradient_upper_bound = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gradient_interpolation_mode = None
        else:
            self.gradient_interpolation_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.upper_temperature_bound = None
        else:
            self.upper_temperature_bound = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lower_temperature_bound = None
        else:
            self.lower_temperature_bound = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.upper_heat_rate_bound = None
        else:
            self.upper_heat_rate_bound = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lower_heat_rate_bound = None
        else:
            self.lower_heat_rate_bound = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_integer_for_pattern_control_schedule_name`
        reference this entry in Schedule Name

        Args:
            value (int): value for IDD Field `control_integer_for_pattern_control_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))

        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=None):
        """  Corresponds to IDD Field `thermostat_height`
        = Distance from floor of zone

        Args:
            value (float): value for IDD Field `thermostat_height`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_height`'.format(value))

        self._data["Thermostat Height"] = value

    @property
    def return_air_height(self):
        """Get return_air_height

        Returns:
            float: the value of `return_air_height` or None if not set
        """
        return self._data["Return Air Height"]

    @return_air_height.setter
    def return_air_height(self, value=None):
        """  Corresponds to IDD Field `return_air_height`
        = Distance from floor of zone

        Args:
            value (float): value for IDD Field `return_air_height`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_height`'.format(value))

        self._data["Return Air Height"] = value

    @property
    def exhaust_air_height(self):
        """Get exhaust_air_height

        Returns:
            float: the value of `exhaust_air_height` or None if not set
        """
        return self._data["Exhaust Air Height"]

    @exhaust_air_height.setter
    def exhaust_air_height(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_height`
        = Distance from floor of zone

        Args:
            value (float): value for IDD Field `exhaust_air_height`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_height`'.format(value))

        self._data["Exhaust Air Height"] = value

    @property
    def temperature_gradient_lower_bound(self):
        """Get temperature_gradient_lower_bound

        Returns:
            float: the value of `temperature_gradient_lower_bound` or None if not set
        """
        return self._data["Temperature Gradient Lower Bound"]

    @temperature_gradient_lower_bound.setter
    def temperature_gradient_lower_bound(self, value=None):
        """  Corresponds to IDD Field `temperature_gradient_lower_bound`
        Slope of temperature change in vertical direction

        Args:
            value (float): value for IDD Field `temperature_gradient_lower_bound`
                Unit: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_gradient_lower_bound`'.format(value))

        self._data["Temperature Gradient Lower Bound"] = value

    @property
    def temperature_gradient_upper_bound(self):
        """Get temperature_gradient_upper_bound

        Returns:
            float: the value of `temperature_gradient_upper_bound` or None if not set
        """
        return self._data["Temperature Gradient Upper  Bound"]

    @temperature_gradient_upper_bound.setter
    def temperature_gradient_upper_bound(self, value=None):
        """  Corresponds to IDD Field `temperature_gradient_upper_bound`
        Slope of temperature change in vertical direction

        Args:
            value (float): value for IDD Field `temperature_gradient_upper_bound`
                Unit: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_gradient_upper_bound`'.format(value))

        self._data["Temperature Gradient Upper  Bound"] = value

    @property
    def gradient_interpolation_mode(self):
        """Get gradient_interpolation_mode

        Returns:
            str: the value of `gradient_interpolation_mode` or None if not set
        """
        return self._data["Gradient Interpolation Mode"]

    @gradient_interpolation_mode.setter
    def gradient_interpolation_mode(self, value=None):
        """  Corresponds to IDD Field `gradient_interpolation_mode`

        Args:
            value (str): value for IDD Field `gradient_interpolation_mode`
                Accepted values are:
                      - OutdoorDryBulbTemperature
                      - ZoneDryBulbTemperature
                      - ZoneAndOutdoorTemperatureDifference
                      - SensibleCoolingLoad
                      - SensibleHeatingLoad
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `gradient_interpolation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gradient_interpolation_mode`')
            vals = set()
            vals.add("OutdoorDryBulbTemperature")
            vals.add("ZoneDryBulbTemperature")
            vals.add("ZoneAndOutdoorTemperatureDifference")
            vals.add("SensibleCoolingLoad")
            vals.add("SensibleHeatingLoad")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gradient_interpolation_mode`'.format(value))

        self._data["Gradient Interpolation Mode"] = value

    @property
    def upper_temperature_bound(self):
        """Get upper_temperature_bound

        Returns:
            float: the value of `upper_temperature_bound` or None if not set
        """
        return self._data["Upper Temperature Bound"]

    @upper_temperature_bound.setter
    def upper_temperature_bound(self, value=None):
        """  Corresponds to IDD Field `upper_temperature_bound`

        Args:
            value (float): value for IDD Field `upper_temperature_bound`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `upper_temperature_bound`'.format(value))

        self._data["Upper Temperature Bound"] = value

    @property
    def lower_temperature_bound(self):
        """Get lower_temperature_bound

        Returns:
            float: the value of `lower_temperature_bound` or None if not set
        """
        return self._data["Lower Temperature Bound"]

    @lower_temperature_bound.setter
    def lower_temperature_bound(self, value=None):
        """  Corresponds to IDD Field `lower_temperature_bound`

        Args:
            value (float): value for IDD Field `lower_temperature_bound`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `lower_temperature_bound`'.format(value))

        self._data["Lower Temperature Bound"] = value

    @property
    def upper_heat_rate_bound(self):
        """Get upper_heat_rate_bound

        Returns:
            float: the value of `upper_heat_rate_bound` or None if not set
        """
        return self._data["Upper Heat Rate Bound"]

    @upper_heat_rate_bound.setter
    def upper_heat_rate_bound(self, value=None):
        """  Corresponds to IDD Field `upper_heat_rate_bound`

        Args:
            value (float): value for IDD Field `upper_heat_rate_bound`
                Unit: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `upper_heat_rate_bound`'.format(value))

        self._data["Upper Heat Rate Bound"] = value

    @property
    def lower_heat_rate_bound(self):
        """Get lower_heat_rate_bound

        Returns:
            float: the value of `lower_heat_rate_bound` or None if not set
        """
        return self._data["Lower Heat Rate Bound"]

    @lower_heat_rate_bound.setter
    def lower_heat_rate_bound(self, value=None):
        """  Corresponds to IDD Field `lower_heat_rate_bound`

        Args:
            value (float): value for IDD Field `lower_heat_rate_bound`
                Unit: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `lower_heat_rate_bound`'.format(value))

        self._data["Lower Heat Rate Bound"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.control_integer_for_pattern_control_schedule_name))
        out.append(self._to_str(self.thermostat_height))
        out.append(self._to_str(self.return_air_height))
        out.append(self._to_str(self.exhaust_air_height))
        out.append(self._to_str(self.temperature_gradient_lower_bound))
        out.append(self._to_str(self.temperature_gradient_upper_bound))
        out.append(self._to_str(self.gradient_interpolation_mode))
        out.append(self._to_str(self.upper_temperature_bound))
        out.append(self._to_str(self.lower_temperature_bound))
        out.append(self._to_str(self.upper_heat_rate_bound))
        out.append(self._to_str(self.lower_heat_rate_bound))
        return ",".join(out)

class RoomAirTemperaturePatternNondimensionalHeight(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:NondimensionalHeight`
        Defines a distribution pattern for air temperatures relative to the current mean air
        temperature as a function of height. The height, referred to as Zeta, is non-dimensional
        by normalizing with the zone ceiling height.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    """
    internal_name = "RoomAir:TemperaturePattern:NondimensionalHeight"
    field_count = 43

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAir:TemperaturePattern:NondimensionalHeight`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Offset"] = None
        self._data["Return Air Offset"] = None
        self._data["Exhaust Air Offset"] = None
        self._data["Pair 1 Zeta Nondimensional Height"] = None
        self._data["Pair 1 Delta Adjacent Air Temperature"] = None
        self._data["Pair 2 Zeta Nondimensional Height"] = None
        self._data["Pair 2 Delta Adjacent Air Temperature"] = None
        self._data["Pair 3 Zeta Nondimensional Height"] = None
        self._data["Pair 3 Delta Adjacent Air Temperature"] = None
        self._data["Pair 4 Zeta Nondimensional Height"] = None
        self._data["Pair 4 Delta Adjacent Air Temperature"] = None
        self._data["Pair 5 Zeta Nondimensional Height"] = None
        self._data["Pair 5 Delta Adjacent Air Temperature"] = None
        self._data["Pair 6 Zeta Nondimensional Height"] = None
        self._data["Pair 6 Delta Adjacent Air Temperature"] = None
        self._data["Pair 7 Zeta Nondimensional Height"] = None
        self._data["Pair 7 Delta Adjacent Air Temperature"] = None
        self._data["Pair 8 Zeta Nondimensional Height"] = None
        self._data["Pair 8 Delta Adjacent Air Temperature"] = None
        self._data["Pair 9 Zeta Nondimensional Height"] = None
        self._data["Pair 9 Delta Adjacent Air Temperature"] = None
        self._data["Pair 10 Zeta Nondimensional Height"] = None
        self._data["Pair 10 Delta Adjacent Air Temperature"] = None
        self._data["Pair 11 Zeta Nondimensional Height"] = None
        self._data["Pair 11 Delta Adjacent Air Temperature"] = None
        self._data["Pair 12 Zeta Nondimensional Height"] = None
        self._data["Pair 12 Delta Adjacent Air Temperature"] = None
        self._data["Pair 13 Zeta Nondimensional Height"] = None
        self._data["Pair 13 Delta Adjacent Air Temperature"] = None
        self._data["Pair 14 Zeta Nondimensional Height"] = None
        self._data["Pair 14 Delta Adjacent Air Temperature"] = None
        self._data["Pair 15 Zeta Nondimensional Height"] = None
        self._data["Pair 15 Delta Adjacent Air Temperature"] = None
        self._data["Pair 16 Zeta Nondimensional Height"] = None
        self._data["Pair 16 Delta Adjacent Air Temperature"] = None
        self._data["Pair 17 Zeta Nondimensional Height"] = None
        self._data["Pair 17 Delta Adjacent Air Temperature"] = None
        self._data["Pair 18 Zeta Nondimensional Height"] = None
        self._data["Pair 18 Delta Adjacent Air Temperature"] = None
        self._data["Pair 19 Zeta Nondimensional Height"] = None
        self._data["Pair 19 Delta Adjacent Air Temperature"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_offset = None
        else:
            self.thermostat_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_offset = None
        else:
            self.return_air_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_offset = None
        else:
            self.exhaust_air_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_1_zeta_nondimensional_height = None
        else:
            self.pair_1_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_1_delta_adjacent_air_temperature = None
        else:
            self.pair_1_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_2_zeta_nondimensional_height = None
        else:
            self.pair_2_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_2_delta_adjacent_air_temperature = None
        else:
            self.pair_2_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_3_zeta_nondimensional_height = None
        else:
            self.pair_3_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_3_delta_adjacent_air_temperature = None
        else:
            self.pair_3_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_4_zeta_nondimensional_height = None
        else:
            self.pair_4_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_4_delta_adjacent_air_temperature = None
        else:
            self.pair_4_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_5_zeta_nondimensional_height = None
        else:
            self.pair_5_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_5_delta_adjacent_air_temperature = None
        else:
            self.pair_5_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_6_zeta_nondimensional_height = None
        else:
            self.pair_6_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_6_delta_adjacent_air_temperature = None
        else:
            self.pair_6_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_7_zeta_nondimensional_height = None
        else:
            self.pair_7_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_7_delta_adjacent_air_temperature = None
        else:
            self.pair_7_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_8_zeta_nondimensional_height = None
        else:
            self.pair_8_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_8_delta_adjacent_air_temperature = None
        else:
            self.pair_8_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_9_zeta_nondimensional_height = None
        else:
            self.pair_9_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_9_delta_adjacent_air_temperature = None
        else:
            self.pair_9_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_10_zeta_nondimensional_height = None
        else:
            self.pair_10_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_10_delta_adjacent_air_temperature = None
        else:
            self.pair_10_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_11_zeta_nondimensional_height = None
        else:
            self.pair_11_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_11_delta_adjacent_air_temperature = None
        else:
            self.pair_11_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_12_zeta_nondimensional_height = None
        else:
            self.pair_12_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_12_delta_adjacent_air_temperature = None
        else:
            self.pair_12_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_13_zeta_nondimensional_height = None
        else:
            self.pair_13_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_13_delta_adjacent_air_temperature = None
        else:
            self.pair_13_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_14_zeta_nondimensional_height = None
        else:
            self.pair_14_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_14_delta_adjacent_air_temperature = None
        else:
            self.pair_14_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_15_zeta_nondimensional_height = None
        else:
            self.pair_15_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_15_delta_adjacent_air_temperature = None
        else:
            self.pair_15_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_16_zeta_nondimensional_height = None
        else:
            self.pair_16_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_16_delta_adjacent_air_temperature = None
        else:
            self.pair_16_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_17_zeta_nondimensional_height = None
        else:
            self.pair_17_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_17_delta_adjacent_air_temperature = None
        else:
            self.pair_17_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_18_zeta_nondimensional_height = None
        else:
            self.pair_18_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_18_delta_adjacent_air_temperature = None
        else:
            self.pair_18_delta_adjacent_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_19_zeta_nondimensional_height = None
        else:
            self.pair_19_zeta_nondimensional_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pair_19_delta_adjacent_air_temperature = None
        else:
            self.pair_19_delta_adjacent_air_temperature = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_integer_for_pattern_control_schedule_name`
        this value should appear in as a schedule value

        Args:
            value (int): value for IDD Field `control_integer_for_pattern_control_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))

        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self._data["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `thermostat_offset`
        = (Temp at thermostat- Mean Air Temp)

        Args:
            value (float): value for IDD Field `thermostat_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_offset`'.format(value))

        self._data["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self._data["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `return_air_offset`
        = (Temp leaving - Mean Air Temp ) deg C

        Args:
            value (float): value for IDD Field `return_air_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_offset`'.format(value))

        self._data["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self._data["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_offset`
        = (Temp exhaust - Mean Air Temp) deg C
        the remaining fields have pairs that describe the relative
        temperature pattern in the vertical direction of a zone
        Zeta is the nondimensional height (in z-direction). on [0..1]
        DeltaTai =  (Tai - MAT) in units of deg. C
        relative deg C on [-10.0 .. 20.0 ]

        Args:
            value (float): value for IDD Field `exhaust_air_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_offset`'.format(value))

        self._data["Exhaust Air Offset"] = value

    @property
    def pair_1_zeta_nondimensional_height(self):
        """Get pair_1_zeta_nondimensional_height

        Returns:
            float: the value of `pair_1_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 1 Zeta Nondimensional Height"]

    @pair_1_zeta_nondimensional_height.setter
    def pair_1_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_1_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_1_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_1_zeta_nondimensional_height`'.format(value))

        self._data["Pair 1 Zeta Nondimensional Height"] = value

    @property
    def pair_1_delta_adjacent_air_temperature(self):
        """Get pair_1_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_1_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 1 Delta Adjacent Air Temperature"]

    @pair_1_delta_adjacent_air_temperature.setter
    def pair_1_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_1_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_1_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_1_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_1_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_1_delta_adjacent_air_temperature`')

        self._data["Pair 1 Delta Adjacent Air Temperature"] = value

    @property
    def pair_2_zeta_nondimensional_height(self):
        """Get pair_2_zeta_nondimensional_height

        Returns:
            float: the value of `pair_2_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 2 Zeta Nondimensional Height"]

    @pair_2_zeta_nondimensional_height.setter
    def pair_2_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_2_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_2_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_2_zeta_nondimensional_height`'.format(value))

        self._data["Pair 2 Zeta Nondimensional Height"] = value

    @property
    def pair_2_delta_adjacent_air_temperature(self):
        """Get pair_2_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_2_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 2 Delta Adjacent Air Temperature"]

    @pair_2_delta_adjacent_air_temperature.setter
    def pair_2_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_2_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_2_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_2_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_2_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_2_delta_adjacent_air_temperature`')

        self._data["Pair 2 Delta Adjacent Air Temperature"] = value

    @property
    def pair_3_zeta_nondimensional_height(self):
        """Get pair_3_zeta_nondimensional_height

        Returns:
            float: the value of `pair_3_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 3 Zeta Nondimensional Height"]

    @pair_3_zeta_nondimensional_height.setter
    def pair_3_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_3_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_3_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_3_zeta_nondimensional_height`'.format(value))

        self._data["Pair 3 Zeta Nondimensional Height"] = value

    @property
    def pair_3_delta_adjacent_air_temperature(self):
        """Get pair_3_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_3_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 3 Delta Adjacent Air Temperature"]

    @pair_3_delta_adjacent_air_temperature.setter
    def pair_3_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_3_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_3_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_3_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_3_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_3_delta_adjacent_air_temperature`')

        self._data["Pair 3 Delta Adjacent Air Temperature"] = value

    @property
    def pair_4_zeta_nondimensional_height(self):
        """Get pair_4_zeta_nondimensional_height

        Returns:
            float: the value of `pair_4_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 4 Zeta Nondimensional Height"]

    @pair_4_zeta_nondimensional_height.setter
    def pair_4_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_4_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_4_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_4_zeta_nondimensional_height`'.format(value))

        self._data["Pair 4 Zeta Nondimensional Height"] = value

    @property
    def pair_4_delta_adjacent_air_temperature(self):
        """Get pair_4_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_4_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 4 Delta Adjacent Air Temperature"]

    @pair_4_delta_adjacent_air_temperature.setter
    def pair_4_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_4_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_4_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_4_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_4_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_4_delta_adjacent_air_temperature`')

        self._data["Pair 4 Delta Adjacent Air Temperature"] = value

    @property
    def pair_5_zeta_nondimensional_height(self):
        """Get pair_5_zeta_nondimensional_height

        Returns:
            float: the value of `pair_5_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 5 Zeta Nondimensional Height"]

    @pair_5_zeta_nondimensional_height.setter
    def pair_5_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_5_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_5_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_5_zeta_nondimensional_height`'.format(value))

        self._data["Pair 5 Zeta Nondimensional Height"] = value

    @property
    def pair_5_delta_adjacent_air_temperature(self):
        """Get pair_5_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_5_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 5 Delta Adjacent Air Temperature"]

    @pair_5_delta_adjacent_air_temperature.setter
    def pair_5_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_5_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_5_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_5_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_5_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_5_delta_adjacent_air_temperature`')

        self._data["Pair 5 Delta Adjacent Air Temperature"] = value

    @property
    def pair_6_zeta_nondimensional_height(self):
        """Get pair_6_zeta_nondimensional_height

        Returns:
            float: the value of `pair_6_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 6 Zeta Nondimensional Height"]

    @pair_6_zeta_nondimensional_height.setter
    def pair_6_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_6_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_6_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_6_zeta_nondimensional_height`'.format(value))

        self._data["Pair 6 Zeta Nondimensional Height"] = value

    @property
    def pair_6_delta_adjacent_air_temperature(self):
        """Get pair_6_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_6_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 6 Delta Adjacent Air Temperature"]

    @pair_6_delta_adjacent_air_temperature.setter
    def pair_6_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_6_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_6_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_6_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_6_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_6_delta_adjacent_air_temperature`')

        self._data["Pair 6 Delta Adjacent Air Temperature"] = value

    @property
    def pair_7_zeta_nondimensional_height(self):
        """Get pair_7_zeta_nondimensional_height

        Returns:
            float: the value of `pair_7_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 7 Zeta Nondimensional Height"]

    @pair_7_zeta_nondimensional_height.setter
    def pair_7_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_7_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_7_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_7_zeta_nondimensional_height`'.format(value))

        self._data["Pair 7 Zeta Nondimensional Height"] = value

    @property
    def pair_7_delta_adjacent_air_temperature(self):
        """Get pair_7_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_7_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 7 Delta Adjacent Air Temperature"]

    @pair_7_delta_adjacent_air_temperature.setter
    def pair_7_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_7_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_7_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_7_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_7_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_7_delta_adjacent_air_temperature`')

        self._data["Pair 7 Delta Adjacent Air Temperature"] = value

    @property
    def pair_8_zeta_nondimensional_height(self):
        """Get pair_8_zeta_nondimensional_height

        Returns:
            float: the value of `pair_8_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 8 Zeta Nondimensional Height"]

    @pair_8_zeta_nondimensional_height.setter
    def pair_8_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_8_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_8_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_8_zeta_nondimensional_height`'.format(value))

        self._data["Pair 8 Zeta Nondimensional Height"] = value

    @property
    def pair_8_delta_adjacent_air_temperature(self):
        """Get pair_8_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_8_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 8 Delta Adjacent Air Temperature"]

    @pair_8_delta_adjacent_air_temperature.setter
    def pair_8_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_8_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_8_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_8_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_8_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_8_delta_adjacent_air_temperature`')

        self._data["Pair 8 Delta Adjacent Air Temperature"] = value

    @property
    def pair_9_zeta_nondimensional_height(self):
        """Get pair_9_zeta_nondimensional_height

        Returns:
            float: the value of `pair_9_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 9 Zeta Nondimensional Height"]

    @pair_9_zeta_nondimensional_height.setter
    def pair_9_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_9_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_9_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_9_zeta_nondimensional_height`'.format(value))

        self._data["Pair 9 Zeta Nondimensional Height"] = value

    @property
    def pair_9_delta_adjacent_air_temperature(self):
        """Get pair_9_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_9_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 9 Delta Adjacent Air Temperature"]

    @pair_9_delta_adjacent_air_temperature.setter
    def pair_9_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_9_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_9_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_9_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_9_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_9_delta_adjacent_air_temperature`')

        self._data["Pair 9 Delta Adjacent Air Temperature"] = value

    @property
    def pair_10_zeta_nondimensional_height(self):
        """Get pair_10_zeta_nondimensional_height

        Returns:
            float: the value of `pair_10_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 10 Zeta Nondimensional Height"]

    @pair_10_zeta_nondimensional_height.setter
    def pair_10_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_10_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_10_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_10_zeta_nondimensional_height`'.format(value))

        self._data["Pair 10 Zeta Nondimensional Height"] = value

    @property
    def pair_10_delta_adjacent_air_temperature(self):
        """Get pair_10_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_10_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 10 Delta Adjacent Air Temperature"]

    @pair_10_delta_adjacent_air_temperature.setter
    def pair_10_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_10_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_10_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_10_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_10_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_10_delta_adjacent_air_temperature`')

        self._data["Pair 10 Delta Adjacent Air Temperature"] = value

    @property
    def pair_11_zeta_nondimensional_height(self):
        """Get pair_11_zeta_nondimensional_height

        Returns:
            float: the value of `pair_11_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 11 Zeta Nondimensional Height"]

    @pair_11_zeta_nondimensional_height.setter
    def pair_11_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_11_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_11_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_11_zeta_nondimensional_height`'.format(value))

        self._data["Pair 11 Zeta Nondimensional Height"] = value

    @property
    def pair_11_delta_adjacent_air_temperature(self):
        """Get pair_11_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_11_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 11 Delta Adjacent Air Temperature"]

    @pair_11_delta_adjacent_air_temperature.setter
    def pair_11_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_11_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_11_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_11_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_11_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_11_delta_adjacent_air_temperature`')

        self._data["Pair 11 Delta Adjacent Air Temperature"] = value

    @property
    def pair_12_zeta_nondimensional_height(self):
        """Get pair_12_zeta_nondimensional_height

        Returns:
            float: the value of `pair_12_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 12 Zeta Nondimensional Height"]

    @pair_12_zeta_nondimensional_height.setter
    def pair_12_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_12_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_12_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_12_zeta_nondimensional_height`'.format(value))

        self._data["Pair 12 Zeta Nondimensional Height"] = value

    @property
    def pair_12_delta_adjacent_air_temperature(self):
        """Get pair_12_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_12_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 12 Delta Adjacent Air Temperature"]

    @pair_12_delta_adjacent_air_temperature.setter
    def pair_12_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_12_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_12_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_12_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_12_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_12_delta_adjacent_air_temperature`')

        self._data["Pair 12 Delta Adjacent Air Temperature"] = value

    @property
    def pair_13_zeta_nondimensional_height(self):
        """Get pair_13_zeta_nondimensional_height

        Returns:
            float: the value of `pair_13_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 13 Zeta Nondimensional Height"]

    @pair_13_zeta_nondimensional_height.setter
    def pair_13_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_13_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_13_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_13_zeta_nondimensional_height`'.format(value))

        self._data["Pair 13 Zeta Nondimensional Height"] = value

    @property
    def pair_13_delta_adjacent_air_temperature(self):
        """Get pair_13_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_13_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 13 Delta Adjacent Air Temperature"]

    @pair_13_delta_adjacent_air_temperature.setter
    def pair_13_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_13_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_13_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_13_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_13_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_13_delta_adjacent_air_temperature`')

        self._data["Pair 13 Delta Adjacent Air Temperature"] = value

    @property
    def pair_14_zeta_nondimensional_height(self):
        """Get pair_14_zeta_nondimensional_height

        Returns:
            float: the value of `pair_14_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 14 Zeta Nondimensional Height"]

    @pair_14_zeta_nondimensional_height.setter
    def pair_14_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_14_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_14_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_14_zeta_nondimensional_height`'.format(value))

        self._data["Pair 14 Zeta Nondimensional Height"] = value

    @property
    def pair_14_delta_adjacent_air_temperature(self):
        """Get pair_14_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_14_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 14 Delta Adjacent Air Temperature"]

    @pair_14_delta_adjacent_air_temperature.setter
    def pair_14_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_14_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_14_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_14_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_14_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_14_delta_adjacent_air_temperature`')

        self._data["Pair 14 Delta Adjacent Air Temperature"] = value

    @property
    def pair_15_zeta_nondimensional_height(self):
        """Get pair_15_zeta_nondimensional_height

        Returns:
            float: the value of `pair_15_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 15 Zeta Nondimensional Height"]

    @pair_15_zeta_nondimensional_height.setter
    def pair_15_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_15_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_15_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_15_zeta_nondimensional_height`'.format(value))

        self._data["Pair 15 Zeta Nondimensional Height"] = value

    @property
    def pair_15_delta_adjacent_air_temperature(self):
        """Get pair_15_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_15_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 15 Delta Adjacent Air Temperature"]

    @pair_15_delta_adjacent_air_temperature.setter
    def pair_15_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_15_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_15_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_15_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_15_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_15_delta_adjacent_air_temperature`')

        self._data["Pair 15 Delta Adjacent Air Temperature"] = value

    @property
    def pair_16_zeta_nondimensional_height(self):
        """Get pair_16_zeta_nondimensional_height

        Returns:
            float: the value of `pair_16_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 16 Zeta Nondimensional Height"]

    @pair_16_zeta_nondimensional_height.setter
    def pair_16_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_16_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_16_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_16_zeta_nondimensional_height`'.format(value))

        self._data["Pair 16 Zeta Nondimensional Height"] = value

    @property
    def pair_16_delta_adjacent_air_temperature(self):
        """Get pair_16_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_16_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 16 Delta Adjacent Air Temperature"]

    @pair_16_delta_adjacent_air_temperature.setter
    def pair_16_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_16_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_16_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_16_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_16_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_16_delta_adjacent_air_temperature`')

        self._data["Pair 16 Delta Adjacent Air Temperature"] = value

    @property
    def pair_17_zeta_nondimensional_height(self):
        """Get pair_17_zeta_nondimensional_height

        Returns:
            float: the value of `pair_17_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 17 Zeta Nondimensional Height"]

    @pair_17_zeta_nondimensional_height.setter
    def pair_17_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_17_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_17_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_17_zeta_nondimensional_height`'.format(value))

        self._data["Pair 17 Zeta Nondimensional Height"] = value

    @property
    def pair_17_delta_adjacent_air_temperature(self):
        """Get pair_17_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_17_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 17 Delta Adjacent Air Temperature"]

    @pair_17_delta_adjacent_air_temperature.setter
    def pair_17_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_17_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_17_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_17_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_17_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_17_delta_adjacent_air_temperature`')

        self._data["Pair 17 Delta Adjacent Air Temperature"] = value

    @property
    def pair_18_zeta_nondimensional_height(self):
        """Get pair_18_zeta_nondimensional_height

        Returns:
            float: the value of `pair_18_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 18 Zeta Nondimensional Height"]

    @pair_18_zeta_nondimensional_height.setter
    def pair_18_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_18_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_18_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_18_zeta_nondimensional_height`'.format(value))

        self._data["Pair 18 Zeta Nondimensional Height"] = value

    @property
    def pair_18_delta_adjacent_air_temperature(self):
        """Get pair_18_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_18_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 18 Delta Adjacent Air Temperature"]

    @pair_18_delta_adjacent_air_temperature.setter
    def pair_18_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_18_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_18_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_18_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_18_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_18_delta_adjacent_air_temperature`')

        self._data["Pair 18 Delta Adjacent Air Temperature"] = value

    @property
    def pair_19_zeta_nondimensional_height(self):
        """Get pair_19_zeta_nondimensional_height

        Returns:
            float: the value of `pair_19_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 19 Zeta Nondimensional Height"]

    @pair_19_zeta_nondimensional_height.setter
    def pair_19_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `pair_19_zeta_nondimensional_height`

        Args:
            value (float): value for IDD Field `pair_19_zeta_nondimensional_height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_19_zeta_nondimensional_height`'.format(value))

        self._data["Pair 19 Zeta Nondimensional Height"] = value

    @property
    def pair_19_delta_adjacent_air_temperature(self):
        """Get pair_19_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_19_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 19 Delta Adjacent Air Temperature"]

    @pair_19_delta_adjacent_air_temperature.setter
    def pair_19_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `pair_19_delta_adjacent_air_temperature`

        Args:
            value (float): value for IDD Field `pair_19_delta_adjacent_air_temperature`
                Unit: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_19_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_19_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_19_delta_adjacent_air_temperature`')

        self._data["Pair 19 Delta Adjacent Air Temperature"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.control_integer_for_pattern_control_schedule_name))
        out.append(self._to_str(self.thermostat_offset))
        out.append(self._to_str(self.return_air_offset))
        out.append(self._to_str(self.exhaust_air_offset))
        out.append(self._to_str(self.pair_1_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_1_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_2_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_2_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_3_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_3_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_4_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_4_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_5_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_5_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_6_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_6_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_7_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_7_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_8_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_8_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_9_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_9_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_10_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_10_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_11_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_11_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_12_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_12_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_13_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_13_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_14_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_14_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_15_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_15_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_16_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_16_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_17_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_17_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_18_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_18_delta_adjacent_air_temperature))
        out.append(self._to_str(self.pair_19_zeta_nondimensional_height))
        out.append(self._to_str(self.pair_19_delta_adjacent_air_temperature))
        return ",".join(out)

class RoomAirTemperaturePatternSurfaceMapping(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:SurfaceMapping`
        Defines a distribution pattern for the air temperatures adjacent to individual surfaces.
        This allows controlling the adjacent air temperature on a surface-by-surface basis
        rather than by height. This allows modeling different adjacent air temperatures on
        the opposite sides of the zone. Used in combination with
        RoomAir:TemperaturePattern:UserDefined.
    """
    internal_name = "RoomAir:TemperaturePattern:SurfaceMapping"
    field_count = 47

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAir:TemperaturePattern:SurfaceMapping`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Offset"] = None
        self._data["Return Air Offset"] = None
        self._data["Exhaust Air Offset"] = None
        self._data["Surface Name Pair 1"] = None
        self._data["Delta Adjacent Air Temperature Pair 1"] = None
        self._data["Surface Name Pair 2"] = None
        self._data["Delta Adjacent Air Temperature Pair 2"] = None
        self._data["Surface Name Pair 3"] = None
        self._data["Delta Adjacent Air Temperature Pair 3"] = None
        self._data["Surface Name Pair 4"] = None
        self._data["Delta Adjacent Air Temperature Pair 4"] = None
        self._data["Surface Name Pair 5"] = None
        self._data["Delta Adjacent Air Temperature Pair 5"] = None
        self._data["Surface Name Pair 6"] = None
        self._data["Delta Adjacent Air Temperature Pair 6"] = None
        self._data["Surface Name Pair 7"] = None
        self._data["Delta Adjacent Air Temperature Pair 7"] = None
        self._data["Surface Name Pair 8"] = None
        self._data["Delta Adjacent Air Temperature Pair 8"] = None
        self._data["Surface Name Pair 9"] = None
        self._data["Delta Adjacent Air Temperature Pair 9"] = None
        self._data["Surface Name Pair 10"] = None
        self._data["Delta Adjacent Air Temperature Pair 10"] = None
        self._data["Surface Name Pair 11"] = None
        self._data["Delta Adjacent Air Temperature Pair 11"] = None
        self._data["Surface Name Pair 12"] = None
        self._data["Delta Adjacent Air Temperature Pair 12"] = None
        self._data["Surface Name Pair 13"] = None
        self._data["Delta Adjacent Air Temperature Pair 13"] = None
        self._data["Surface Name Pair 14"] = None
        self._data["Delta Adjacent Air Temperature Pair 14"] = None
        self._data["Surface Name Pair 15"] = None
        self._data["Delta Adjacent Air Temperature Pair 15"] = None
        self._data["Surface Name Pair 16"] = None
        self._data["Delta Adjacent Air Temperature Pair 16"] = None
        self._data["Surface Name Pair 17"] = None
        self._data["Delta Adjacent Air Temperature Pair 17"] = None
        self._data["Surface Name Pair 18"] = None
        self._data["Delta Adjacent Air Temperature Pair 18"] = None
        self._data["Surface Name Pair 19"] = None
        self._data["Delta Adjacent Air Temperature Pair 19"] = None
        self._data["Surface Name Pair 20"] = None
        self._data["Delta Adjacent Air Temperature Pair 20"] = None
        self._data["Surface Name Pair 21"] = None
        self._data["Delta Adjacent Air Temperature Pair 21"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_offset = None
        else:
            self.thermostat_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_offset = None
        else:
            self.return_air_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_offset = None
        else:
            self.exhaust_air_offset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_1 = None
        else:
            self.surface_name_pair_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_1 = None
        else:
            self.delta_adjacent_air_temperature_pair_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_2 = None
        else:
            self.surface_name_pair_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_2 = None
        else:
            self.delta_adjacent_air_temperature_pair_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_3 = None
        else:
            self.surface_name_pair_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_3 = None
        else:
            self.delta_adjacent_air_temperature_pair_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_4 = None
        else:
            self.surface_name_pair_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_4 = None
        else:
            self.delta_adjacent_air_temperature_pair_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_5 = None
        else:
            self.surface_name_pair_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_5 = None
        else:
            self.delta_adjacent_air_temperature_pair_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_6 = None
        else:
            self.surface_name_pair_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_6 = None
        else:
            self.delta_adjacent_air_temperature_pair_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_7 = None
        else:
            self.surface_name_pair_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_7 = None
        else:
            self.delta_adjacent_air_temperature_pair_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_8 = None
        else:
            self.surface_name_pair_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_8 = None
        else:
            self.delta_adjacent_air_temperature_pair_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_9 = None
        else:
            self.surface_name_pair_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_9 = None
        else:
            self.delta_adjacent_air_temperature_pair_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_10 = None
        else:
            self.surface_name_pair_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_10 = None
        else:
            self.delta_adjacent_air_temperature_pair_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_11 = None
        else:
            self.surface_name_pair_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_11 = None
        else:
            self.delta_adjacent_air_temperature_pair_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_12 = None
        else:
            self.surface_name_pair_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_12 = None
        else:
            self.delta_adjacent_air_temperature_pair_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_13 = None
        else:
            self.surface_name_pair_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_13 = None
        else:
            self.delta_adjacent_air_temperature_pair_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_14 = None
        else:
            self.surface_name_pair_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_14 = None
        else:
            self.delta_adjacent_air_temperature_pair_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_15 = None
        else:
            self.surface_name_pair_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_15 = None
        else:
            self.delta_adjacent_air_temperature_pair_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_16 = None
        else:
            self.surface_name_pair_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_16 = None
        else:
            self.delta_adjacent_air_temperature_pair_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_17 = None
        else:
            self.surface_name_pair_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_17 = None
        else:
            self.delta_adjacent_air_temperature_pair_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_18 = None
        else:
            self.surface_name_pair_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_18 = None
        else:
            self.delta_adjacent_air_temperature_pair_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_19 = None
        else:
            self.surface_name_pair_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_19 = None
        else:
            self.delta_adjacent_air_temperature_pair_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_20 = None
        else:
            self.surface_name_pair_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_20 = None
        else:
            self.delta_adjacent_air_temperature_pair_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_pair_21 = None
        else:
            self.surface_name_pair_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_21 = None
        else:
            self.delta_adjacent_air_temperature_pair_21 = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_integer_for_pattern_control_schedule_name`
        reference this entry in schedule

        Args:
            value (int): value for IDD Field `control_integer_for_pattern_control_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))

        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self._data["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `thermostat_offset`
        = (Temp at thermostat- Mean Air Temp)

        Args:
            value (float): value for IDD Field `thermostat_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_offset`'.format(value))

        self._data["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self._data["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `return_air_offset`
        = (Tleaving - Mean Air Temp ) deg C

        Args:
            value (float): value for IDD Field `return_air_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_offset`'.format(value))

        self._data["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self._data["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_offset`
        = (Texhaust - Mean Air Temp) deg C

        Args:
            value (float): value for IDD Field `exhaust_air_offset`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_offset`'.format(value))

        self._data["Exhaust Air Offset"] = value

    @property
    def surface_name_pair_1(self):
        """Get surface_name_pair_1

        Returns:
            str: the value of `surface_name_pair_1` or None if not set
        """
        return self._data["Surface Name Pair 1"]

    @surface_name_pair_1.setter
    def surface_name_pair_1(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_1`

        Args:
            value (str): value for IDD Field `surface_name_pair_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_1`')

        self._data["Surface Name Pair 1"] = value

    @property
    def delta_adjacent_air_temperature_pair_1(self):
        """Get delta_adjacent_air_temperature_pair_1

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_1` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 1"]

    @delta_adjacent_air_temperature_pair_1.setter
    def delta_adjacent_air_temperature_pair_1(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_1`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_1`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_1`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 1"] = value

    @property
    def surface_name_pair_2(self):
        """Get surface_name_pair_2

        Returns:
            str: the value of `surface_name_pair_2` or None if not set
        """
        return self._data["Surface Name Pair 2"]

    @surface_name_pair_2.setter
    def surface_name_pair_2(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_2`

        Args:
            value (str): value for IDD Field `surface_name_pair_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_2`')

        self._data["Surface Name Pair 2"] = value

    @property
    def delta_adjacent_air_temperature_pair_2(self):
        """Get delta_adjacent_air_temperature_pair_2

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_2` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 2"]

    @delta_adjacent_air_temperature_pair_2.setter
    def delta_adjacent_air_temperature_pair_2(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_2`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_2`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_2`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 2"] = value

    @property
    def surface_name_pair_3(self):
        """Get surface_name_pair_3

        Returns:
            str: the value of `surface_name_pair_3` or None if not set
        """
        return self._data["Surface Name Pair 3"]

    @surface_name_pair_3.setter
    def surface_name_pair_3(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_3`

        Args:
            value (str): value for IDD Field `surface_name_pair_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_3`')

        self._data["Surface Name Pair 3"] = value

    @property
    def delta_adjacent_air_temperature_pair_3(self):
        """Get delta_adjacent_air_temperature_pair_3

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_3` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 3"]

    @delta_adjacent_air_temperature_pair_3.setter
    def delta_adjacent_air_temperature_pair_3(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_3`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_3`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_3`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 3"] = value

    @property
    def surface_name_pair_4(self):
        """Get surface_name_pair_4

        Returns:
            str: the value of `surface_name_pair_4` or None if not set
        """
        return self._data["Surface Name Pair 4"]

    @surface_name_pair_4.setter
    def surface_name_pair_4(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_4`

        Args:
            value (str): value for IDD Field `surface_name_pair_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_4`')

        self._data["Surface Name Pair 4"] = value

    @property
    def delta_adjacent_air_temperature_pair_4(self):
        """Get delta_adjacent_air_temperature_pair_4

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_4` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 4"]

    @delta_adjacent_air_temperature_pair_4.setter
    def delta_adjacent_air_temperature_pair_4(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_4`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_4`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_4`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 4"] = value

    @property
    def surface_name_pair_5(self):
        """Get surface_name_pair_5

        Returns:
            str: the value of `surface_name_pair_5` or None if not set
        """
        return self._data["Surface Name Pair 5"]

    @surface_name_pair_5.setter
    def surface_name_pair_5(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_5`

        Args:
            value (str): value for IDD Field `surface_name_pair_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_5`')

        self._data["Surface Name Pair 5"] = value

    @property
    def delta_adjacent_air_temperature_pair_5(self):
        """Get delta_adjacent_air_temperature_pair_5

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_5` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 5"]

    @delta_adjacent_air_temperature_pair_5.setter
    def delta_adjacent_air_temperature_pair_5(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_5`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_5`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_5`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 5"] = value

    @property
    def surface_name_pair_6(self):
        """Get surface_name_pair_6

        Returns:
            str: the value of `surface_name_pair_6` or None if not set
        """
        return self._data["Surface Name Pair 6"]

    @surface_name_pair_6.setter
    def surface_name_pair_6(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_6`

        Args:
            value (str): value for IDD Field `surface_name_pair_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_6`')

        self._data["Surface Name Pair 6"] = value

    @property
    def delta_adjacent_air_temperature_pair_6(self):
        """Get delta_adjacent_air_temperature_pair_6

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_6` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 6"]

    @delta_adjacent_air_temperature_pair_6.setter
    def delta_adjacent_air_temperature_pair_6(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_6`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_6`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_6`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 6"] = value

    @property
    def surface_name_pair_7(self):
        """Get surface_name_pair_7

        Returns:
            str: the value of `surface_name_pair_7` or None if not set
        """
        return self._data["Surface Name Pair 7"]

    @surface_name_pair_7.setter
    def surface_name_pair_7(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_7`

        Args:
            value (str): value for IDD Field `surface_name_pair_7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_7`')

        self._data["Surface Name Pair 7"] = value

    @property
    def delta_adjacent_air_temperature_pair_7(self):
        """Get delta_adjacent_air_temperature_pair_7

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_7` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 7"]

    @delta_adjacent_air_temperature_pair_7.setter
    def delta_adjacent_air_temperature_pair_7(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_7`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_7`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_7`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 7"] = value

    @property
    def surface_name_pair_8(self):
        """Get surface_name_pair_8

        Returns:
            str: the value of `surface_name_pair_8` or None if not set
        """
        return self._data["Surface Name Pair 8"]

    @surface_name_pair_8.setter
    def surface_name_pair_8(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_8`

        Args:
            value (str): value for IDD Field `surface_name_pair_8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_8`')

        self._data["Surface Name Pair 8"] = value

    @property
    def delta_adjacent_air_temperature_pair_8(self):
        """Get delta_adjacent_air_temperature_pair_8

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_8` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 8"]

    @delta_adjacent_air_temperature_pair_8.setter
    def delta_adjacent_air_temperature_pair_8(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_8`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_8`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_8`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 8"] = value

    @property
    def surface_name_pair_9(self):
        """Get surface_name_pair_9

        Returns:
            str: the value of `surface_name_pair_9` or None if not set
        """
        return self._data["Surface Name Pair 9"]

    @surface_name_pair_9.setter
    def surface_name_pair_9(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_9`

        Args:
            value (str): value for IDD Field `surface_name_pair_9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_9`')

        self._data["Surface Name Pair 9"] = value

    @property
    def delta_adjacent_air_temperature_pair_9(self):
        """Get delta_adjacent_air_temperature_pair_9

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_9` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 9"]

    @delta_adjacent_air_temperature_pair_9.setter
    def delta_adjacent_air_temperature_pair_9(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_9`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_9`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_9`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 9"] = value

    @property
    def surface_name_pair_10(self):
        """Get surface_name_pair_10

        Returns:
            str: the value of `surface_name_pair_10` or None if not set
        """
        return self._data["Surface Name Pair 10"]

    @surface_name_pair_10.setter
    def surface_name_pair_10(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_10`

        Args:
            value (str): value for IDD Field `surface_name_pair_10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_10`')

        self._data["Surface Name Pair 10"] = value

    @property
    def delta_adjacent_air_temperature_pair_10(self):
        """Get delta_adjacent_air_temperature_pair_10

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_10` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 10"]

    @delta_adjacent_air_temperature_pair_10.setter
    def delta_adjacent_air_temperature_pair_10(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_10`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_10`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_10`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 10"] = value

    @property
    def surface_name_pair_11(self):
        """Get surface_name_pair_11

        Returns:
            str: the value of `surface_name_pair_11` or None if not set
        """
        return self._data["Surface Name Pair 11"]

    @surface_name_pair_11.setter
    def surface_name_pair_11(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_11`

        Args:
            value (str): value for IDD Field `surface_name_pair_11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_11`')

        self._data["Surface Name Pair 11"] = value

    @property
    def delta_adjacent_air_temperature_pair_11(self):
        """Get delta_adjacent_air_temperature_pair_11

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_11` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 11"]

    @delta_adjacent_air_temperature_pair_11.setter
    def delta_adjacent_air_temperature_pair_11(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_11`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_11`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_11`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 11"] = value

    @property
    def surface_name_pair_12(self):
        """Get surface_name_pair_12

        Returns:
            str: the value of `surface_name_pair_12` or None if not set
        """
        return self._data["Surface Name Pair 12"]

    @surface_name_pair_12.setter
    def surface_name_pair_12(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_12`

        Args:
            value (str): value for IDD Field `surface_name_pair_12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_12`')

        self._data["Surface Name Pair 12"] = value

    @property
    def delta_adjacent_air_temperature_pair_12(self):
        """Get delta_adjacent_air_temperature_pair_12

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_12` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 12"]

    @delta_adjacent_air_temperature_pair_12.setter
    def delta_adjacent_air_temperature_pair_12(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_12`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_12`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_12`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 12"] = value

    @property
    def surface_name_pair_13(self):
        """Get surface_name_pair_13

        Returns:
            str: the value of `surface_name_pair_13` or None if not set
        """
        return self._data["Surface Name Pair 13"]

    @surface_name_pair_13.setter
    def surface_name_pair_13(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_13`

        Args:
            value (str): value for IDD Field `surface_name_pair_13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_13`')

        self._data["Surface Name Pair 13"] = value

    @property
    def delta_adjacent_air_temperature_pair_13(self):
        """Get delta_adjacent_air_temperature_pair_13

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_13` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 13"]

    @delta_adjacent_air_temperature_pair_13.setter
    def delta_adjacent_air_temperature_pair_13(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_13`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_13`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_13`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 13"] = value

    @property
    def surface_name_pair_14(self):
        """Get surface_name_pair_14

        Returns:
            str: the value of `surface_name_pair_14` or None if not set
        """
        return self._data["Surface Name Pair 14"]

    @surface_name_pair_14.setter
    def surface_name_pair_14(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_14`

        Args:
            value (str): value for IDD Field `surface_name_pair_14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_14`')

        self._data["Surface Name Pair 14"] = value

    @property
    def delta_adjacent_air_temperature_pair_14(self):
        """Get delta_adjacent_air_temperature_pair_14

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_14` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 14"]

    @delta_adjacent_air_temperature_pair_14.setter
    def delta_adjacent_air_temperature_pair_14(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_14`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_14`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_14`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 14"] = value

    @property
    def surface_name_pair_15(self):
        """Get surface_name_pair_15

        Returns:
            str: the value of `surface_name_pair_15` or None if not set
        """
        return self._data["Surface Name Pair 15"]

    @surface_name_pair_15.setter
    def surface_name_pair_15(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_15`

        Args:
            value (str): value for IDD Field `surface_name_pair_15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_15`')

        self._data["Surface Name Pair 15"] = value

    @property
    def delta_adjacent_air_temperature_pair_15(self):
        """Get delta_adjacent_air_temperature_pair_15

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_15` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 15"]

    @delta_adjacent_air_temperature_pair_15.setter
    def delta_adjacent_air_temperature_pair_15(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_15`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_15`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_15`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 15"] = value

    @property
    def surface_name_pair_16(self):
        """Get surface_name_pair_16

        Returns:
            str: the value of `surface_name_pair_16` or None if not set
        """
        return self._data["Surface Name Pair 16"]

    @surface_name_pair_16.setter
    def surface_name_pair_16(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_16`

        Args:
            value (str): value for IDD Field `surface_name_pair_16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_16`')

        self._data["Surface Name Pair 16"] = value

    @property
    def delta_adjacent_air_temperature_pair_16(self):
        """Get delta_adjacent_air_temperature_pair_16

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_16` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 16"]

    @delta_adjacent_air_temperature_pair_16.setter
    def delta_adjacent_air_temperature_pair_16(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_16`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_16`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_16`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 16"] = value

    @property
    def surface_name_pair_17(self):
        """Get surface_name_pair_17

        Returns:
            str: the value of `surface_name_pair_17` or None if not set
        """
        return self._data["Surface Name Pair 17"]

    @surface_name_pair_17.setter
    def surface_name_pair_17(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_17`

        Args:
            value (str): value for IDD Field `surface_name_pair_17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_17`')

        self._data["Surface Name Pair 17"] = value

    @property
    def delta_adjacent_air_temperature_pair_17(self):
        """Get delta_adjacent_air_temperature_pair_17

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_17` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 17"]

    @delta_adjacent_air_temperature_pair_17.setter
    def delta_adjacent_air_temperature_pair_17(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_17`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_17`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_17`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 17"] = value

    @property
    def surface_name_pair_18(self):
        """Get surface_name_pair_18

        Returns:
            str: the value of `surface_name_pair_18` or None if not set
        """
        return self._data["Surface Name Pair 18"]

    @surface_name_pair_18.setter
    def surface_name_pair_18(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_18`

        Args:
            value (str): value for IDD Field `surface_name_pair_18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_18`')

        self._data["Surface Name Pair 18"] = value

    @property
    def delta_adjacent_air_temperature_pair_18(self):
        """Get delta_adjacent_air_temperature_pair_18

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_18` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 18"]

    @delta_adjacent_air_temperature_pair_18.setter
    def delta_adjacent_air_temperature_pair_18(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_18`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_18`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_18`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 18"] = value

    @property
    def surface_name_pair_19(self):
        """Get surface_name_pair_19

        Returns:
            str: the value of `surface_name_pair_19` or None if not set
        """
        return self._data["Surface Name Pair 19"]

    @surface_name_pair_19.setter
    def surface_name_pair_19(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_19`

        Args:
            value (str): value for IDD Field `surface_name_pair_19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_19`')

        self._data["Surface Name Pair 19"] = value

    @property
    def delta_adjacent_air_temperature_pair_19(self):
        """Get delta_adjacent_air_temperature_pair_19

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_19` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 19"]

    @delta_adjacent_air_temperature_pair_19.setter
    def delta_adjacent_air_temperature_pair_19(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_19`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_19`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_19`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 19"] = value

    @property
    def surface_name_pair_20(self):
        """Get surface_name_pair_20

        Returns:
            str: the value of `surface_name_pair_20` or None if not set
        """
        return self._data["Surface Name Pair 20"]

    @surface_name_pair_20.setter
    def surface_name_pair_20(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_20`

        Args:
            value (str): value for IDD Field `surface_name_pair_20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_20`')

        self._data["Surface Name Pair 20"] = value

    @property
    def delta_adjacent_air_temperature_pair_20(self):
        """Get delta_adjacent_air_temperature_pair_20

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_20` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 20"]

    @delta_adjacent_air_temperature_pair_20.setter
    def delta_adjacent_air_temperature_pair_20(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_20`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_20`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_20`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 20"] = value

    @property
    def surface_name_pair_21(self):
        """Get surface_name_pair_21

        Returns:
            str: the value of `surface_name_pair_21` or None if not set
        """
        return self._data["Surface Name Pair 21"]

    @surface_name_pair_21.setter
    def surface_name_pair_21(self, value=None):
        """  Corresponds to IDD Field `surface_name_pair_21`

        Args:
            value (str): value for IDD Field `surface_name_pair_21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_21`')

        self._data["Surface Name Pair 21"] = value

    @property
    def delta_adjacent_air_temperature_pair_21(self):
        """Get delta_adjacent_air_temperature_pair_21

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_21` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 21"]

    @delta_adjacent_air_temperature_pair_21.setter
    def delta_adjacent_air_temperature_pair_21(self, value=None):
        """  Corresponds to IDD Field `delta_adjacent_air_temperature_pair_21`

        Args:
            value (float): value for IDD Field `delta_adjacent_air_temperature_pair_21`
                Unit: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_21`'.format(value))

        self._data["Delta Adjacent Air Temperature Pair 21"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.control_integer_for_pattern_control_schedule_name))
        out.append(self._to_str(self.thermostat_offset))
        out.append(self._to_str(self.return_air_offset))
        out.append(self._to_str(self.exhaust_air_offset))
        out.append(self._to_str(self.surface_name_pair_1))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_1))
        out.append(self._to_str(self.surface_name_pair_2))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_2))
        out.append(self._to_str(self.surface_name_pair_3))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_3))
        out.append(self._to_str(self.surface_name_pair_4))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_4))
        out.append(self._to_str(self.surface_name_pair_5))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_5))
        out.append(self._to_str(self.surface_name_pair_6))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_6))
        out.append(self._to_str(self.surface_name_pair_7))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_7))
        out.append(self._to_str(self.surface_name_pair_8))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_8))
        out.append(self._to_str(self.surface_name_pair_9))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_9))
        out.append(self._to_str(self.surface_name_pair_10))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_10))
        out.append(self._to_str(self.surface_name_pair_11))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_11))
        out.append(self._to_str(self.surface_name_pair_12))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_12))
        out.append(self._to_str(self.surface_name_pair_13))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_13))
        out.append(self._to_str(self.surface_name_pair_14))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_14))
        out.append(self._to_str(self.surface_name_pair_15))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_15))
        out.append(self._to_str(self.surface_name_pair_16))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_16))
        out.append(self._to_str(self.surface_name_pair_17))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_17))
        out.append(self._to_str(self.surface_name_pair_18))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_18))
        out.append(self._to_str(self.surface_name_pair_19))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_19))
        out.append(self._to_str(self.surface_name_pair_20))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_20))
        out.append(self._to_str(self.surface_name_pair_21))
        out.append(self._to_str(self.delta_adjacent_air_temperature_pair_21))
        return ",".join(out)

class RoomAirNode(object):
    """ Corresponds to IDD object `RoomAir:Node`
        Define an air node for some types of nodal room air models
    """
    internal_name = "RoomAir:Node"
    field_count = 25

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAir:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Node Type"] = None
        self._data["Zone Name"] = None
        self._data["Height of Nodal Control Volume Center"] = None
        self._data["Surface 1 Name"] = None
        self._data["Surface 2 Name"] = None
        self._data["Surface 3 Name"] = None
        self._data["Surface 4 Name"] = None
        self._data["Surface 5 Name"] = None
        self._data["Surface 6 Name"] = None
        self._data["Surface 7 Name"] = None
        self._data["Surface 8 Name"] = None
        self._data["Surface 9 Name"] = None
        self._data["Surface 10 Name"] = None
        self._data["Surface 11 Name"] = None
        self._data["Surface 12 Name"] = None
        self._data["Surface 13 Name"] = None
        self._data["Surface 14 Name"] = None
        self._data["Surface 15 Name"] = None
        self._data["Surface 16 Name"] = None
        self._data["Surface 17 Name"] = None
        self._data["Surface 18 Name"] = None
        self._data["Surface 19 Name"] = None
        self._data["Surface 20 Name"] = None
        self._data["Surface 21 Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_type = None
        else:
            self.node_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_of_nodal_control_volume_center = None
        else:
            self.height_of_nodal_control_volume_center = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_1_name = None
        else:
            self.surface_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_2_name = None
        else:
            self.surface_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_3_name = None
        else:
            self.surface_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_4_name = None
        else:
            self.surface_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_5_name = None
        else:
            self.surface_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_6_name = None
        else:
            self.surface_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_7_name = None
        else:
            self.surface_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_8_name = None
        else:
            self.surface_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_9_name = None
        else:
            self.surface_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_10_name = None
        else:
            self.surface_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_11_name = None
        else:
            self.surface_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_12_name = None
        else:
            self.surface_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_13_name = None
        else:
            self.surface_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_14_name = None
        else:
            self.surface_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_15_name = None
        else:
            self.surface_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_16_name = None
        else:
            self.surface_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_17_name = None
        else:
            self.surface_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_18_name = None
        else:
            self.surface_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_19_name = None
        else:
            self.surface_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_20_name = None
        else:
            self.surface_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_21_name = None
        else:
            self.surface_21_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def node_type(self):
        """Get node_type

        Returns:
            str: the value of `node_type` or None if not set
        """
        return self._data["Node Type"]

    @node_type.setter
    def node_type(self, value=None):
        """  Corresponds to IDD Field `node_type`

        Args:
            value (str): value for IDD Field `node_type`
                Accepted values are:
                      - Inlet
                      - Floor
                      - Control
                      - Ceiling
                      - MundtRoom
                      - Return
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `node_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_type`')
            vals = set()
            vals.add("Inlet")
            vals.add("Floor")
            vals.add("Control")
            vals.add("Ceiling")
            vals.add("MundtRoom")
            vals.add("Return")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `node_type`'.format(value))

        self._data["Node Type"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def height_of_nodal_control_volume_center(self):
        """Get height_of_nodal_control_volume_center

        Returns:
            float: the value of `height_of_nodal_control_volume_center` or None if not set
        """
        return self._data["Height of Nodal Control Volume Center"]

    @height_of_nodal_control_volume_center.setter
    def height_of_nodal_control_volume_center(self, value=None):
        """  Corresponds to IDD Field `height_of_nodal_control_volume_center`

        Args:
            value (float): value for IDD Field `height_of_nodal_control_volume_center`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_of_nodal_control_volume_center`'.format(value))

        self._data["Height of Nodal Control Volume Center"] = value

    @property
    def surface_1_name(self):
        """Get surface_1_name

        Returns:
            str: the value of `surface_1_name` or None if not set
        """
        return self._data["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """  Corresponds to IDD Field `surface_1_name`

        Args:
            value (str): value for IDD Field `surface_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_1_name`')

        self._data["Surface 1 Name"] = value

    @property
    def surface_2_name(self):
        """Get surface_2_name

        Returns:
            str: the value of `surface_2_name` or None if not set
        """
        return self._data["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """  Corresponds to IDD Field `surface_2_name`

        Args:
            value (str): value for IDD Field `surface_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_2_name`')

        self._data["Surface 2 Name"] = value

    @property
    def surface_3_name(self):
        """Get surface_3_name

        Returns:
            str: the value of `surface_3_name` or None if not set
        """
        return self._data["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """  Corresponds to IDD Field `surface_3_name`

        Args:
            value (str): value for IDD Field `surface_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_3_name`')

        self._data["Surface 3 Name"] = value

    @property
    def surface_4_name(self):
        """Get surface_4_name

        Returns:
            str: the value of `surface_4_name` or None if not set
        """
        return self._data["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """  Corresponds to IDD Field `surface_4_name`

        Args:
            value (str): value for IDD Field `surface_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_4_name`')

        self._data["Surface 4 Name"] = value

    @property
    def surface_5_name(self):
        """Get surface_5_name

        Returns:
            str: the value of `surface_5_name` or None if not set
        """
        return self._data["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """  Corresponds to IDD Field `surface_5_name`

        Args:
            value (str): value for IDD Field `surface_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_5_name`')

        self._data["Surface 5 Name"] = value

    @property
    def surface_6_name(self):
        """Get surface_6_name

        Returns:
            str: the value of `surface_6_name` or None if not set
        """
        return self._data["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """  Corresponds to IDD Field `surface_6_name`

        Args:
            value (str): value for IDD Field `surface_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_6_name`')

        self._data["Surface 6 Name"] = value

    @property
    def surface_7_name(self):
        """Get surface_7_name

        Returns:
            str: the value of `surface_7_name` or None if not set
        """
        return self._data["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """  Corresponds to IDD Field `surface_7_name`

        Args:
            value (str): value for IDD Field `surface_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_7_name`')

        self._data["Surface 7 Name"] = value

    @property
    def surface_8_name(self):
        """Get surface_8_name

        Returns:
            str: the value of `surface_8_name` or None if not set
        """
        return self._data["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """  Corresponds to IDD Field `surface_8_name`

        Args:
            value (str): value for IDD Field `surface_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_8_name`')

        self._data["Surface 8 Name"] = value

    @property
    def surface_9_name(self):
        """Get surface_9_name

        Returns:
            str: the value of `surface_9_name` or None if not set
        """
        return self._data["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """  Corresponds to IDD Field `surface_9_name`

        Args:
            value (str): value for IDD Field `surface_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_9_name`')

        self._data["Surface 9 Name"] = value

    @property
    def surface_10_name(self):
        """Get surface_10_name

        Returns:
            str: the value of `surface_10_name` or None if not set
        """
        return self._data["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """  Corresponds to IDD Field `surface_10_name`

        Args:
            value (str): value for IDD Field `surface_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_10_name`')

        self._data["Surface 10 Name"] = value

    @property
    def surface_11_name(self):
        """Get surface_11_name

        Returns:
            str: the value of `surface_11_name` or None if not set
        """
        return self._data["Surface 11 Name"]

    @surface_11_name.setter
    def surface_11_name(self, value=None):
        """  Corresponds to IDD Field `surface_11_name`

        Args:
            value (str): value for IDD Field `surface_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_11_name`')

        self._data["Surface 11 Name"] = value

    @property
    def surface_12_name(self):
        """Get surface_12_name

        Returns:
            str: the value of `surface_12_name` or None if not set
        """
        return self._data["Surface 12 Name"]

    @surface_12_name.setter
    def surface_12_name(self, value=None):
        """  Corresponds to IDD Field `surface_12_name`

        Args:
            value (str): value for IDD Field `surface_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_12_name`')

        self._data["Surface 12 Name"] = value

    @property
    def surface_13_name(self):
        """Get surface_13_name

        Returns:
            str: the value of `surface_13_name` or None if not set
        """
        return self._data["Surface 13 Name"]

    @surface_13_name.setter
    def surface_13_name(self, value=None):
        """  Corresponds to IDD Field `surface_13_name`

        Args:
            value (str): value for IDD Field `surface_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_13_name`')

        self._data["Surface 13 Name"] = value

    @property
    def surface_14_name(self):
        """Get surface_14_name

        Returns:
            str: the value of `surface_14_name` or None if not set
        """
        return self._data["Surface 14 Name"]

    @surface_14_name.setter
    def surface_14_name(self, value=None):
        """  Corresponds to IDD Field `surface_14_name`

        Args:
            value (str): value for IDD Field `surface_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_14_name`')

        self._data["Surface 14 Name"] = value

    @property
    def surface_15_name(self):
        """Get surface_15_name

        Returns:
            str: the value of `surface_15_name` or None if not set
        """
        return self._data["Surface 15 Name"]

    @surface_15_name.setter
    def surface_15_name(self, value=None):
        """  Corresponds to IDD Field `surface_15_name`

        Args:
            value (str): value for IDD Field `surface_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_15_name`')

        self._data["Surface 15 Name"] = value

    @property
    def surface_16_name(self):
        """Get surface_16_name

        Returns:
            str: the value of `surface_16_name` or None if not set
        """
        return self._data["Surface 16 Name"]

    @surface_16_name.setter
    def surface_16_name(self, value=None):
        """  Corresponds to IDD Field `surface_16_name`

        Args:
            value (str): value for IDD Field `surface_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_16_name`')

        self._data["Surface 16 Name"] = value

    @property
    def surface_17_name(self):
        """Get surface_17_name

        Returns:
            str: the value of `surface_17_name` or None if not set
        """
        return self._data["Surface 17 Name"]

    @surface_17_name.setter
    def surface_17_name(self, value=None):
        """  Corresponds to IDD Field `surface_17_name`

        Args:
            value (str): value for IDD Field `surface_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_17_name`')

        self._data["Surface 17 Name"] = value

    @property
    def surface_18_name(self):
        """Get surface_18_name

        Returns:
            str: the value of `surface_18_name` or None if not set
        """
        return self._data["Surface 18 Name"]

    @surface_18_name.setter
    def surface_18_name(self, value=None):
        """  Corresponds to IDD Field `surface_18_name`

        Args:
            value (str): value for IDD Field `surface_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_18_name`')

        self._data["Surface 18 Name"] = value

    @property
    def surface_19_name(self):
        """Get surface_19_name

        Returns:
            str: the value of `surface_19_name` or None if not set
        """
        return self._data["Surface 19 Name"]

    @surface_19_name.setter
    def surface_19_name(self, value=None):
        """  Corresponds to IDD Field `surface_19_name`

        Args:
            value (str): value for IDD Field `surface_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_19_name`')

        self._data["Surface 19 Name"] = value

    @property
    def surface_20_name(self):
        """Get surface_20_name

        Returns:
            str: the value of `surface_20_name` or None if not set
        """
        return self._data["Surface 20 Name"]

    @surface_20_name.setter
    def surface_20_name(self, value=None):
        """  Corresponds to IDD Field `surface_20_name`

        Args:
            value (str): value for IDD Field `surface_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_20_name`')

        self._data["Surface 20 Name"] = value

    @property
    def surface_21_name(self):
        """Get surface_21_name

        Returns:
            str: the value of `surface_21_name` or None if not set
        """
        return self._data["Surface 21 Name"]

    @surface_21_name.setter
    def surface_21_name(self, value=None):
        """  Corresponds to IDD Field `surface_21_name`

        Args:
            value (str): value for IDD Field `surface_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_21_name`')

        self._data["Surface 21 Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.node_type))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.height_of_nodal_control_volume_center))
        out.append(self._to_str(self.surface_1_name))
        out.append(self._to_str(self.surface_2_name))
        out.append(self._to_str(self.surface_3_name))
        out.append(self._to_str(self.surface_4_name))
        out.append(self._to_str(self.surface_5_name))
        out.append(self._to_str(self.surface_6_name))
        out.append(self._to_str(self.surface_7_name))
        out.append(self._to_str(self.surface_8_name))
        out.append(self._to_str(self.surface_9_name))
        out.append(self._to_str(self.surface_10_name))
        out.append(self._to_str(self.surface_11_name))
        out.append(self._to_str(self.surface_12_name))
        out.append(self._to_str(self.surface_13_name))
        out.append(self._to_str(self.surface_14_name))
        out.append(self._to_str(self.surface_15_name))
        out.append(self._to_str(self.surface_16_name))
        out.append(self._to_str(self.surface_17_name))
        out.append(self._to_str(self.surface_18_name))
        out.append(self._to_str(self.surface_19_name))
        out.append(self._to_str(self.surface_20_name))
        out.append(self._to_str(self.surface_21_name))
        return ",".join(out)