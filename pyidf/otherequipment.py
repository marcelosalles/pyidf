from collections import OrderedDict

class OtherEquipment(object):
    """ Corresponds to IDD object `OtherEquipment`
        Sets internal gains or losses for "other" equipment in the zone.
    """
    internal_name = "OtherEquipment"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OtherEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Design Level"] = None
        self._data["Power per Zone Floor Area"] = None
        self._data["Power per Person"] = None
        self._data["Fraction Latent"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Lost"] = None

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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_zone_floor_area = None
        else:
            self.power_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_person = None
        else:
            self.power_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_latent = None
        else:
            self.fraction_latent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_lost = None
        else:
            self.fraction_lost = vals[i]
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
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
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
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of other equipment.
        to set a loss, use a negative value in the following fields.
        for this set of attributes
        Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - EquipmentLevel
                      - Watts/Area
                      - Watts/Person
                      - Power/Area
                      - Power/Person
                Default value: EquipmentLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("EquipmentLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            vals.add("Power/Area")
            vals.add("Power/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `design_level`

        Args:
            value (float): value for IDD Field `design_level`
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
                                 'for field `design_level`'.format(value))

        self._data["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """Get power_per_zone_floor_area

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set
        """
        return self._data["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `power_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `power_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `power_per_zone_floor_area`'.format(value))

        self._data["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """Get power_per_person

        Returns:
            float: the value of `power_per_person` or None if not set
        """
        return self._data["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """  Corresponds to IDD Field `power_per_person`

        Args:
            value (float): value for IDD Field `power_per_person`
                Unit: W/Person
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
                                 'for field `power_per_person`'.format(value))

        self._data["Power per Person"] = value

    @property
    def fraction_latent(self):
        """Get fraction_latent

        Returns:
            float: the value of `fraction_latent` or None if not set
        """
        return self._data["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_latent`

        Args:
            value (float): value for IDD Field `fraction_latent`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `fraction_latent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_latent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_latent`')

        self._data["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """Get fraction_lost

        Returns:
            float: the value of `fraction_lost` or None if not set
        """
        return self._data["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_lost`

        Args:
            value (float): value for IDD Field `fraction_lost`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `fraction_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_lost`')

        self._data["Fraction Lost"] = value

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
        out.append(self._to_str(self.zone_or_zonelist_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.design_level))
        out.append(self._to_str(self.power_per_zone_floor_area))
        out.append(self._to_str(self.power_per_person))
        out.append(self._to_str(self.fraction_latent))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_lost))
        return ",".join(out)