from collections import OrderedDict

class MeterCustom(object):
    """ Corresponds to IDD object `Meter:Custom`
        Used to allow users to combine specific variables and/or meters into
        "custom" meter configurations. To access these meters by name, one must
        first run a simulation to generate the RDD/MDD files and names.
    """
    internal_name = "Meter:Custom"
    field_count = 46

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Meter:Custom`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fuel Type"] = None
        self._data["Key Name 1"] = None
        self._data["Output Variable or Meter Name 1"] = None
        self._data["Key Name 2"] = None
        self._data["Output Variable or Meter Name 2"] = None
        self._data["Key Name 3"] = None
        self._data["Output Variable or Meter Name 3"] = None
        self._data["Key Name 4"] = None
        self._data["Output Variable or Meter Name 4"] = None
        self._data["Key Name 5"] = None
        self._data["Output Variable or Meter Name 5"] = None
        self._data["Key Name 6"] = None
        self._data["Output Variable or Meter Name 6"] = None
        self._data["Key Name 7"] = None
        self._data["Output Variable or Meter Name 7"] = None
        self._data["Key Name 8"] = None
        self._data["Output Variable or Meter Name 8"] = None
        self._data["Key Name 9"] = None
        self._data["Output Variable or Meter Name 9"] = None
        self._data["Key Name 10"] = None
        self._data["Output Variable or Meter Name 10"] = None
        self._data["Key Name 11"] = None
        self._data["Output Variable or Meter Name 11"] = None
        self._data["Key Name 12"] = None
        self._data["Output Variable or Meter Name 12"] = None
        self._data["Key Name 13"] = None
        self._data["Output Variable or Meter Name 13"] = None
        self._data["Key Name 14"] = None
        self._data["Output Variable or Meter Name 14"] = None
        self._data["Key Name 15"] = None
        self._data["Output Variable or Meter Name 15"] = None
        self._data["Key Name 16"] = None
        self._data["Output Variable or Meter Name 16"] = None
        self._data["Key Name 17"] = None
        self._data["Output Variable or Meter Name 17"] = None
        self._data["Key Name 18"] = None
        self._data["Output Variable or Meter Name 18"] = None
        self._data["Key Name 19"] = None
        self._data["Output Variable or Meter Name 19"] = None
        self._data["Key Name 20"] = None
        self._data["Output Variable or Meter Name 20"] = None
        self._data["Key Name 21"] = None
        self._data["Output Variable or Meter Name 21"] = None
        self._data["Key Name 22"] = None
        self._data["Output Variable or Meter Name 22"] = None

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
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_1 = None
        else:
            self.key_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_1 = None
        else:
            self.output_variable_or_meter_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_2 = None
        else:
            self.key_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_2 = None
        else:
            self.output_variable_or_meter_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_3 = None
        else:
            self.key_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_3 = None
        else:
            self.output_variable_or_meter_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_4 = None
        else:
            self.key_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_4 = None
        else:
            self.output_variable_or_meter_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_5 = None
        else:
            self.key_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_5 = None
        else:
            self.output_variable_or_meter_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_6 = None
        else:
            self.key_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_6 = None
        else:
            self.output_variable_or_meter_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_7 = None
        else:
            self.key_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_7 = None
        else:
            self.output_variable_or_meter_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_8 = None
        else:
            self.key_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_8 = None
        else:
            self.output_variable_or_meter_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_9 = None
        else:
            self.key_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_9 = None
        else:
            self.output_variable_or_meter_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_10 = None
        else:
            self.key_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_10 = None
        else:
            self.output_variable_or_meter_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_11 = None
        else:
            self.key_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_11 = None
        else:
            self.output_variable_or_meter_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_12 = None
        else:
            self.key_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_12 = None
        else:
            self.output_variable_or_meter_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_13 = None
        else:
            self.key_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_13 = None
        else:
            self.output_variable_or_meter_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_14 = None
        else:
            self.key_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_14 = None
        else:
            self.output_variable_or_meter_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_15 = None
        else:
            self.key_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_15 = None
        else:
            self.output_variable_or_meter_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_16 = None
        else:
            self.key_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_16 = None
        else:
            self.output_variable_or_meter_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_17 = None
        else:
            self.key_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_17 = None
        else:
            self.output_variable_or_meter_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_18 = None
        else:
            self.key_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_18 = None
        else:
            self.output_variable_or_meter_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_19 = None
        else:
            self.key_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_19 = None
        else:
            self.output_variable_or_meter_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_20 = None
        else:
            self.key_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_20 = None
        else:
            self.output_variable_or_meter_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_21 = None
        else:
            self.key_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_21 = None
        else:
            self.output_variable_or_meter_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_22 = None
        else:
            self.key_name_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_22 = None
        else:
            self.output_variable_or_meter_name_22 = vals[i]
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
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """  Corresponds to IDD Field `fuel_type`

        Args:
            value (str): value for IDD Field `fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - Water
                      - Generic
                      - OtherFuel1
                      - OtherFuel2
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
                                 'for field `fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_type`')
            vals = set()
            vals.add("Electricity")
            vals.add("NaturalGas")
            vals.add("PropaneGas")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("Coal")
            vals.add("Diesel")
            vals.add("Gasoline")
            vals.add("Water")
            vals.add("Generic")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fuel_type`'.format(value))

        self._data["Fuel Type"] = value

    @property
    def key_name_1(self):
        """Get key_name_1

        Returns:
            str: the value of `key_name_1` or None if not set
        """
        return self._data["Key Name 1"]

    @key_name_1.setter
    def key_name_1(self, value=None):
        """  Corresponds to IDD Field `key_name_1`

        Args:
            value (str): value for IDD Field `key_name_1`
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
                                 'for field `key_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_1`')

        self._data["Key Name 1"] = value

    @property
    def output_variable_or_meter_name_1(self):
        """Get output_variable_or_meter_name_1

        Returns:
            str: the value of `output_variable_or_meter_name_1` or None if not set
        """
        return self._data["Output Variable or Meter Name 1"]

    @output_variable_or_meter_name_1.setter
    def output_variable_or_meter_name_1(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_1`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_1`
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
                                 'for field `output_variable_or_meter_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_1`')

        self._data["Output Variable or Meter Name 1"] = value

    @property
    def key_name_2(self):
        """Get key_name_2

        Returns:
            str: the value of `key_name_2` or None if not set
        """
        return self._data["Key Name 2"]

    @key_name_2.setter
    def key_name_2(self, value=None):
        """  Corresponds to IDD Field `key_name_2`

        Args:
            value (str): value for IDD Field `key_name_2`
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
                                 'for field `key_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_2`')

        self._data["Key Name 2"] = value

    @property
    def output_variable_or_meter_name_2(self):
        """Get output_variable_or_meter_name_2

        Returns:
            str: the value of `output_variable_or_meter_name_2` or None if not set
        """
        return self._data["Output Variable or Meter Name 2"]

    @output_variable_or_meter_name_2.setter
    def output_variable_or_meter_name_2(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_2`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_2`
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
                                 'for field `output_variable_or_meter_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_2`')

        self._data["Output Variable or Meter Name 2"] = value

    @property
    def key_name_3(self):
        """Get key_name_3

        Returns:
            str: the value of `key_name_3` or None if not set
        """
        return self._data["Key Name 3"]

    @key_name_3.setter
    def key_name_3(self, value=None):
        """  Corresponds to IDD Field `key_name_3`

        Args:
            value (str): value for IDD Field `key_name_3`
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
                                 'for field `key_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_3`')

        self._data["Key Name 3"] = value

    @property
    def output_variable_or_meter_name_3(self):
        """Get output_variable_or_meter_name_3

        Returns:
            str: the value of `output_variable_or_meter_name_3` or None if not set
        """
        return self._data["Output Variable or Meter Name 3"]

    @output_variable_or_meter_name_3.setter
    def output_variable_or_meter_name_3(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_3`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_3`
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
                                 'for field `output_variable_or_meter_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_3`')

        self._data["Output Variable or Meter Name 3"] = value

    @property
    def key_name_4(self):
        """Get key_name_4

        Returns:
            str: the value of `key_name_4` or None if not set
        """
        return self._data["Key Name 4"]

    @key_name_4.setter
    def key_name_4(self, value=None):
        """  Corresponds to IDD Field `key_name_4`

        Args:
            value (str): value for IDD Field `key_name_4`
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
                                 'for field `key_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_4`')

        self._data["Key Name 4"] = value

    @property
    def output_variable_or_meter_name_4(self):
        """Get output_variable_or_meter_name_4

        Returns:
            str: the value of `output_variable_or_meter_name_4` or None if not set
        """
        return self._data["Output Variable or Meter Name 4"]

    @output_variable_or_meter_name_4.setter
    def output_variable_or_meter_name_4(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_4`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_4`
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
                                 'for field `output_variable_or_meter_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_4`')

        self._data["Output Variable or Meter Name 4"] = value

    @property
    def key_name_5(self):
        """Get key_name_5

        Returns:
            str: the value of `key_name_5` or None if not set
        """
        return self._data["Key Name 5"]

    @key_name_5.setter
    def key_name_5(self, value=None):
        """  Corresponds to IDD Field `key_name_5`

        Args:
            value (str): value for IDD Field `key_name_5`
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
                                 'for field `key_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_5`')

        self._data["Key Name 5"] = value

    @property
    def output_variable_or_meter_name_5(self):
        """Get output_variable_or_meter_name_5

        Returns:
            str: the value of `output_variable_or_meter_name_5` or None if not set
        """
        return self._data["Output Variable or Meter Name 5"]

    @output_variable_or_meter_name_5.setter
    def output_variable_or_meter_name_5(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_5`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_5`
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
                                 'for field `output_variable_or_meter_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_5`')

        self._data["Output Variable or Meter Name 5"] = value

    @property
    def key_name_6(self):
        """Get key_name_6

        Returns:
            str: the value of `key_name_6` or None if not set
        """
        return self._data["Key Name 6"]

    @key_name_6.setter
    def key_name_6(self, value=None):
        """  Corresponds to IDD Field `key_name_6`

        Args:
            value (str): value for IDD Field `key_name_6`
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
                                 'for field `key_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_6`')

        self._data["Key Name 6"] = value

    @property
    def output_variable_or_meter_name_6(self):
        """Get output_variable_or_meter_name_6

        Returns:
            str: the value of `output_variable_or_meter_name_6` or None if not set
        """
        return self._data["Output Variable or Meter Name 6"]

    @output_variable_or_meter_name_6.setter
    def output_variable_or_meter_name_6(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_6`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_6`
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
                                 'for field `output_variable_or_meter_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_6`')

        self._data["Output Variable or Meter Name 6"] = value

    @property
    def key_name_7(self):
        """Get key_name_7

        Returns:
            str: the value of `key_name_7` or None if not set
        """
        return self._data["Key Name 7"]

    @key_name_7.setter
    def key_name_7(self, value=None):
        """  Corresponds to IDD Field `key_name_7`

        Args:
            value (str): value for IDD Field `key_name_7`
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
                                 'for field `key_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_7`')

        self._data["Key Name 7"] = value

    @property
    def output_variable_or_meter_name_7(self):
        """Get output_variable_or_meter_name_7

        Returns:
            str: the value of `output_variable_or_meter_name_7` or None if not set
        """
        return self._data["Output Variable or Meter Name 7"]

    @output_variable_or_meter_name_7.setter
    def output_variable_or_meter_name_7(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_7`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_7`
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
                                 'for field `output_variable_or_meter_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_7`')

        self._data["Output Variable or Meter Name 7"] = value

    @property
    def key_name_8(self):
        """Get key_name_8

        Returns:
            str: the value of `key_name_8` or None if not set
        """
        return self._data["Key Name 8"]

    @key_name_8.setter
    def key_name_8(self, value=None):
        """  Corresponds to IDD Field `key_name_8`

        Args:
            value (str): value for IDD Field `key_name_8`
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
                                 'for field `key_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_8`')

        self._data["Key Name 8"] = value

    @property
    def output_variable_or_meter_name_8(self):
        """Get output_variable_or_meter_name_8

        Returns:
            str: the value of `output_variable_or_meter_name_8` or None if not set
        """
        return self._data["Output Variable or Meter Name 8"]

    @output_variable_or_meter_name_8.setter
    def output_variable_or_meter_name_8(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_8`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_8`
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
                                 'for field `output_variable_or_meter_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_8`')

        self._data["Output Variable or Meter Name 8"] = value

    @property
    def key_name_9(self):
        """Get key_name_9

        Returns:
            str: the value of `key_name_9` or None if not set
        """
        return self._data["Key Name 9"]

    @key_name_9.setter
    def key_name_9(self, value=None):
        """  Corresponds to IDD Field `key_name_9`

        Args:
            value (str): value for IDD Field `key_name_9`
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
                                 'for field `key_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_9`')

        self._data["Key Name 9"] = value

    @property
    def output_variable_or_meter_name_9(self):
        """Get output_variable_or_meter_name_9

        Returns:
            str: the value of `output_variable_or_meter_name_9` or None if not set
        """
        return self._data["Output Variable or Meter Name 9"]

    @output_variable_or_meter_name_9.setter
    def output_variable_or_meter_name_9(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_9`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_9`
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
                                 'for field `output_variable_or_meter_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_9`')

        self._data["Output Variable or Meter Name 9"] = value

    @property
    def key_name_10(self):
        """Get key_name_10

        Returns:
            str: the value of `key_name_10` or None if not set
        """
        return self._data["Key Name 10"]

    @key_name_10.setter
    def key_name_10(self, value=None):
        """  Corresponds to IDD Field `key_name_10`

        Args:
            value (str): value for IDD Field `key_name_10`
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
                                 'for field `key_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_10`')

        self._data["Key Name 10"] = value

    @property
    def output_variable_or_meter_name_10(self):
        """Get output_variable_or_meter_name_10

        Returns:
            str: the value of `output_variable_or_meter_name_10` or None if not set
        """
        return self._data["Output Variable or Meter Name 10"]

    @output_variable_or_meter_name_10.setter
    def output_variable_or_meter_name_10(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_10`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_10`
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
                                 'for field `output_variable_or_meter_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_10`')

        self._data["Output Variable or Meter Name 10"] = value

    @property
    def key_name_11(self):
        """Get key_name_11

        Returns:
            str: the value of `key_name_11` or None if not set
        """
        return self._data["Key Name 11"]

    @key_name_11.setter
    def key_name_11(self, value=None):
        """  Corresponds to IDD Field `key_name_11`

        Args:
            value (str): value for IDD Field `key_name_11`
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
                                 'for field `key_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_11`')

        self._data["Key Name 11"] = value

    @property
    def output_variable_or_meter_name_11(self):
        """Get output_variable_or_meter_name_11

        Returns:
            str: the value of `output_variable_or_meter_name_11` or None if not set
        """
        return self._data["Output Variable or Meter Name 11"]

    @output_variable_or_meter_name_11.setter
    def output_variable_or_meter_name_11(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_11`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_11`
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
                                 'for field `output_variable_or_meter_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_11`')

        self._data["Output Variable or Meter Name 11"] = value

    @property
    def key_name_12(self):
        """Get key_name_12

        Returns:
            str: the value of `key_name_12` or None if not set
        """
        return self._data["Key Name 12"]

    @key_name_12.setter
    def key_name_12(self, value=None):
        """  Corresponds to IDD Field `key_name_12`

        Args:
            value (str): value for IDD Field `key_name_12`
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
                                 'for field `key_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_12`')

        self._data["Key Name 12"] = value

    @property
    def output_variable_or_meter_name_12(self):
        """Get output_variable_or_meter_name_12

        Returns:
            str: the value of `output_variable_or_meter_name_12` or None if not set
        """
        return self._data["Output Variable or Meter Name 12"]

    @output_variable_or_meter_name_12.setter
    def output_variable_or_meter_name_12(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_12`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_12`
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
                                 'for field `output_variable_or_meter_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_12`')

        self._data["Output Variable or Meter Name 12"] = value

    @property
    def key_name_13(self):
        """Get key_name_13

        Returns:
            str: the value of `key_name_13` or None if not set
        """
        return self._data["Key Name 13"]

    @key_name_13.setter
    def key_name_13(self, value=None):
        """  Corresponds to IDD Field `key_name_13`

        Args:
            value (str): value for IDD Field `key_name_13`
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
                                 'for field `key_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_13`')

        self._data["Key Name 13"] = value

    @property
    def output_variable_or_meter_name_13(self):
        """Get output_variable_or_meter_name_13

        Returns:
            str: the value of `output_variable_or_meter_name_13` or None if not set
        """
        return self._data["Output Variable or Meter Name 13"]

    @output_variable_or_meter_name_13.setter
    def output_variable_or_meter_name_13(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_13`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_13`
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
                                 'for field `output_variable_or_meter_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_13`')

        self._data["Output Variable or Meter Name 13"] = value

    @property
    def key_name_14(self):
        """Get key_name_14

        Returns:
            str: the value of `key_name_14` or None if not set
        """
        return self._data["Key Name 14"]

    @key_name_14.setter
    def key_name_14(self, value=None):
        """  Corresponds to IDD Field `key_name_14`

        Args:
            value (str): value for IDD Field `key_name_14`
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
                                 'for field `key_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_14`')

        self._data["Key Name 14"] = value

    @property
    def output_variable_or_meter_name_14(self):
        """Get output_variable_or_meter_name_14

        Returns:
            str: the value of `output_variable_or_meter_name_14` or None if not set
        """
        return self._data["Output Variable or Meter Name 14"]

    @output_variable_or_meter_name_14.setter
    def output_variable_or_meter_name_14(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_14`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_14`
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
                                 'for field `output_variable_or_meter_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_14`')

        self._data["Output Variable or Meter Name 14"] = value

    @property
    def key_name_15(self):
        """Get key_name_15

        Returns:
            str: the value of `key_name_15` or None if not set
        """
        return self._data["Key Name 15"]

    @key_name_15.setter
    def key_name_15(self, value=None):
        """  Corresponds to IDD Field `key_name_15`

        Args:
            value (str): value for IDD Field `key_name_15`
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
                                 'for field `key_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_15`')

        self._data["Key Name 15"] = value

    @property
    def output_variable_or_meter_name_15(self):
        """Get output_variable_or_meter_name_15

        Returns:
            str: the value of `output_variable_or_meter_name_15` or None if not set
        """
        return self._data["Output Variable or Meter Name 15"]

    @output_variable_or_meter_name_15.setter
    def output_variable_or_meter_name_15(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_15`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_15`
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
                                 'for field `output_variable_or_meter_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_15`')

        self._data["Output Variable or Meter Name 15"] = value

    @property
    def key_name_16(self):
        """Get key_name_16

        Returns:
            str: the value of `key_name_16` or None if not set
        """
        return self._data["Key Name 16"]

    @key_name_16.setter
    def key_name_16(self, value=None):
        """  Corresponds to IDD Field `key_name_16`

        Args:
            value (str): value for IDD Field `key_name_16`
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
                                 'for field `key_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_16`')

        self._data["Key Name 16"] = value

    @property
    def output_variable_or_meter_name_16(self):
        """Get output_variable_or_meter_name_16

        Returns:
            str: the value of `output_variable_or_meter_name_16` or None if not set
        """
        return self._data["Output Variable or Meter Name 16"]

    @output_variable_or_meter_name_16.setter
    def output_variable_or_meter_name_16(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_16`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_16`
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
                                 'for field `output_variable_or_meter_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_16`')

        self._data["Output Variable or Meter Name 16"] = value

    @property
    def key_name_17(self):
        """Get key_name_17

        Returns:
            str: the value of `key_name_17` or None if not set
        """
        return self._data["Key Name 17"]

    @key_name_17.setter
    def key_name_17(self, value=None):
        """  Corresponds to IDD Field `key_name_17`

        Args:
            value (str): value for IDD Field `key_name_17`
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
                                 'for field `key_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_17`')

        self._data["Key Name 17"] = value

    @property
    def output_variable_or_meter_name_17(self):
        """Get output_variable_or_meter_name_17

        Returns:
            str: the value of `output_variable_or_meter_name_17` or None if not set
        """
        return self._data["Output Variable or Meter Name 17"]

    @output_variable_or_meter_name_17.setter
    def output_variable_or_meter_name_17(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_17`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_17`
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
                                 'for field `output_variable_or_meter_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_17`')

        self._data["Output Variable or Meter Name 17"] = value

    @property
    def key_name_18(self):
        """Get key_name_18

        Returns:
            str: the value of `key_name_18` or None if not set
        """
        return self._data["Key Name 18"]

    @key_name_18.setter
    def key_name_18(self, value=None):
        """  Corresponds to IDD Field `key_name_18`

        Args:
            value (str): value for IDD Field `key_name_18`
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
                                 'for field `key_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_18`')

        self._data["Key Name 18"] = value

    @property
    def output_variable_or_meter_name_18(self):
        """Get output_variable_or_meter_name_18

        Returns:
            str: the value of `output_variable_or_meter_name_18` or None if not set
        """
        return self._data["Output Variable or Meter Name 18"]

    @output_variable_or_meter_name_18.setter
    def output_variable_or_meter_name_18(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_18`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_18`
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
                                 'for field `output_variable_or_meter_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_18`')

        self._data["Output Variable or Meter Name 18"] = value

    @property
    def key_name_19(self):
        """Get key_name_19

        Returns:
            str: the value of `key_name_19` or None if not set
        """
        return self._data["Key Name 19"]

    @key_name_19.setter
    def key_name_19(self, value=None):
        """  Corresponds to IDD Field `key_name_19`

        Args:
            value (str): value for IDD Field `key_name_19`
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
                                 'for field `key_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_19`')

        self._data["Key Name 19"] = value

    @property
    def output_variable_or_meter_name_19(self):
        """Get output_variable_or_meter_name_19

        Returns:
            str: the value of `output_variable_or_meter_name_19` or None if not set
        """
        return self._data["Output Variable or Meter Name 19"]

    @output_variable_or_meter_name_19.setter
    def output_variable_or_meter_name_19(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_19`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_19`
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
                                 'for field `output_variable_or_meter_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_19`')

        self._data["Output Variable or Meter Name 19"] = value

    @property
    def key_name_20(self):
        """Get key_name_20

        Returns:
            str: the value of `key_name_20` or None if not set
        """
        return self._data["Key Name 20"]

    @key_name_20.setter
    def key_name_20(self, value=None):
        """  Corresponds to IDD Field `key_name_20`

        Args:
            value (str): value for IDD Field `key_name_20`
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
                                 'for field `key_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_20`')

        self._data["Key Name 20"] = value

    @property
    def output_variable_or_meter_name_20(self):
        """Get output_variable_or_meter_name_20

        Returns:
            str: the value of `output_variable_or_meter_name_20` or None if not set
        """
        return self._data["Output Variable or Meter Name 20"]

    @output_variable_or_meter_name_20.setter
    def output_variable_or_meter_name_20(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_20`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_20`
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
                                 'for field `output_variable_or_meter_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_20`')

        self._data["Output Variable or Meter Name 20"] = value

    @property
    def key_name_21(self):
        """Get key_name_21

        Returns:
            str: the value of `key_name_21` or None if not set
        """
        return self._data["Key Name 21"]

    @key_name_21.setter
    def key_name_21(self, value=None):
        """  Corresponds to IDD Field `key_name_21`

        Args:
            value (str): value for IDD Field `key_name_21`
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
                                 'for field `key_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_21`')

        self._data["Key Name 21"] = value

    @property
    def output_variable_or_meter_name_21(self):
        """Get output_variable_or_meter_name_21

        Returns:
            str: the value of `output_variable_or_meter_name_21` or None if not set
        """
        return self._data["Output Variable or Meter Name 21"]

    @output_variable_or_meter_name_21.setter
    def output_variable_or_meter_name_21(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_21`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_21`
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
                                 'for field `output_variable_or_meter_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_21`')

        self._data["Output Variable or Meter Name 21"] = value

    @property
    def key_name_22(self):
        """Get key_name_22

        Returns:
            str: the value of `key_name_22` or None if not set
        """
        return self._data["Key Name 22"]

    @key_name_22.setter
    def key_name_22(self, value=None):
        """  Corresponds to IDD Field `key_name_22`

        Args:
            value (str): value for IDD Field `key_name_22`
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
                                 'for field `key_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_22`')

        self._data["Key Name 22"] = value

    @property
    def output_variable_or_meter_name_22(self):
        """Get output_variable_or_meter_name_22

        Returns:
            str: the value of `output_variable_or_meter_name_22` or None if not set
        """
        return self._data["Output Variable or Meter Name 22"]

    @output_variable_or_meter_name_22.setter
    def output_variable_or_meter_name_22(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_22`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_22`
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
                                 'for field `output_variable_or_meter_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_22`')

        self._data["Output Variable or Meter Name 22"] = value

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
        out.append(self._to_str(self.fuel_type))
        out.append(self._to_str(self.key_name_1))
        out.append(self._to_str(self.output_variable_or_meter_name_1))
        out.append(self._to_str(self.key_name_2))
        out.append(self._to_str(self.output_variable_or_meter_name_2))
        out.append(self._to_str(self.key_name_3))
        out.append(self._to_str(self.output_variable_or_meter_name_3))
        out.append(self._to_str(self.key_name_4))
        out.append(self._to_str(self.output_variable_or_meter_name_4))
        out.append(self._to_str(self.key_name_5))
        out.append(self._to_str(self.output_variable_or_meter_name_5))
        out.append(self._to_str(self.key_name_6))
        out.append(self._to_str(self.output_variable_or_meter_name_6))
        out.append(self._to_str(self.key_name_7))
        out.append(self._to_str(self.output_variable_or_meter_name_7))
        out.append(self._to_str(self.key_name_8))
        out.append(self._to_str(self.output_variable_or_meter_name_8))
        out.append(self._to_str(self.key_name_9))
        out.append(self._to_str(self.output_variable_or_meter_name_9))
        out.append(self._to_str(self.key_name_10))
        out.append(self._to_str(self.output_variable_or_meter_name_10))
        out.append(self._to_str(self.key_name_11))
        out.append(self._to_str(self.output_variable_or_meter_name_11))
        out.append(self._to_str(self.key_name_12))
        out.append(self._to_str(self.output_variable_or_meter_name_12))
        out.append(self._to_str(self.key_name_13))
        out.append(self._to_str(self.output_variable_or_meter_name_13))
        out.append(self._to_str(self.key_name_14))
        out.append(self._to_str(self.output_variable_or_meter_name_14))
        out.append(self._to_str(self.key_name_15))
        out.append(self._to_str(self.output_variable_or_meter_name_15))
        out.append(self._to_str(self.key_name_16))
        out.append(self._to_str(self.output_variable_or_meter_name_16))
        out.append(self._to_str(self.key_name_17))
        out.append(self._to_str(self.output_variable_or_meter_name_17))
        out.append(self._to_str(self.key_name_18))
        out.append(self._to_str(self.output_variable_or_meter_name_18))
        out.append(self._to_str(self.key_name_19))
        out.append(self._to_str(self.output_variable_or_meter_name_19))
        out.append(self._to_str(self.key_name_20))
        out.append(self._to_str(self.output_variable_or_meter_name_20))
        out.append(self._to_str(self.key_name_21))
        out.append(self._to_str(self.output_variable_or_meter_name_21))
        out.append(self._to_str(self.key_name_22))
        out.append(self._to_str(self.output_variable_or_meter_name_22))
        return ",".join(out)

class MeterCustomDecrement(object):
    """ Corresponds to IDD object `Meter:CustomDecrement`
        Used to allow users to combine specific variables and/or meters into
        "custom" meter configurations. To access these meters by name, one must
        first run a simulation to generate the RDD/MDD files and names.
    """
    internal_name = "Meter:CustomDecrement"
    field_count = 47

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Meter:CustomDecrement`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fuel Type"] = None
        self._data["Source Meter Name"] = None
        self._data["Key Name 1"] = None
        self._data["Output Variable or Meter Name 1"] = None
        self._data["Key Name 2"] = None
        self._data["Output Variable or Meter Name 2"] = None
        self._data["Key Name 3"] = None
        self._data["Output Variable or Meter Name 3"] = None
        self._data["Key Name 4"] = None
        self._data["Output Variable or Meter Name 4"] = None
        self._data["Key Name 5"] = None
        self._data["Output Variable or Meter Name 5"] = None
        self._data["Key Name 6"] = None
        self._data["Output Variable or Meter Name 6"] = None
        self._data["Key Name 7"] = None
        self._data["Output Variable or Meter Name 7"] = None
        self._data["Key Name 8"] = None
        self._data["Output Variable or Meter Name 8"] = None
        self._data["Key Name 9"] = None
        self._data["Output Variable or Meter Name 9"] = None
        self._data["Key Name 10"] = None
        self._data["Output Variable or Meter Name 10"] = None
        self._data["Key Name 11"] = None
        self._data["Output Variable or Meter Name 11"] = None
        self._data["Key Name 12"] = None
        self._data["Output Variable or Meter Name 12"] = None
        self._data["Key Name 13"] = None
        self._data["Output Variable or Meter Name 13"] = None
        self._data["Key Name 14"] = None
        self._data["Output Variable or Meter Name 14"] = None
        self._data["Key Name 15"] = None
        self._data["Output Variable or Meter Name 15"] = None
        self._data["Key Name 16"] = None
        self._data["Output Variable or Meter Name 16"] = None
        self._data["Key Name 17"] = None
        self._data["Output Variable or Meter Name 17"] = None
        self._data["Key Name 18"] = None
        self._data["Output Variable or Meter Name 18"] = None
        self._data["Key Name 19"] = None
        self._data["Output Variable or Meter Name 19"] = None
        self._data["Key Name 20"] = None
        self._data["Output Variable or Meter Name 20"] = None
        self._data["Key Name 21"] = None
        self._data["Output Variable or Meter Name 21"] = None
        self._data["Key Name 22"] = None
        self._data["Output Variable or Meter Name 22"] = None

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
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_meter_name = None
        else:
            self.source_meter_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_1 = None
        else:
            self.key_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_1 = None
        else:
            self.output_variable_or_meter_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_2 = None
        else:
            self.key_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_2 = None
        else:
            self.output_variable_or_meter_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_3 = None
        else:
            self.key_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_3 = None
        else:
            self.output_variable_or_meter_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_4 = None
        else:
            self.key_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_4 = None
        else:
            self.output_variable_or_meter_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_5 = None
        else:
            self.key_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_5 = None
        else:
            self.output_variable_or_meter_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_6 = None
        else:
            self.key_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_6 = None
        else:
            self.output_variable_or_meter_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_7 = None
        else:
            self.key_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_7 = None
        else:
            self.output_variable_or_meter_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_8 = None
        else:
            self.key_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_8 = None
        else:
            self.output_variable_or_meter_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_9 = None
        else:
            self.key_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_9 = None
        else:
            self.output_variable_or_meter_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_10 = None
        else:
            self.key_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_10 = None
        else:
            self.output_variable_or_meter_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_11 = None
        else:
            self.key_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_11 = None
        else:
            self.output_variable_or_meter_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_12 = None
        else:
            self.key_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_12 = None
        else:
            self.output_variable_or_meter_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_13 = None
        else:
            self.key_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_13 = None
        else:
            self.output_variable_or_meter_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_14 = None
        else:
            self.key_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_14 = None
        else:
            self.output_variable_or_meter_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_15 = None
        else:
            self.key_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_15 = None
        else:
            self.output_variable_or_meter_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_16 = None
        else:
            self.key_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_16 = None
        else:
            self.output_variable_or_meter_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_17 = None
        else:
            self.key_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_17 = None
        else:
            self.output_variable_or_meter_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_18 = None
        else:
            self.key_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_18 = None
        else:
            self.output_variable_or_meter_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_19 = None
        else:
            self.key_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_19 = None
        else:
            self.output_variable_or_meter_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_20 = None
        else:
            self.key_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_20 = None
        else:
            self.output_variable_or_meter_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_21 = None
        else:
            self.key_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_21 = None
        else:
            self.output_variable_or_meter_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.key_name_22 = None
        else:
            self.key_name_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_variable_or_meter_name_22 = None
        else:
            self.output_variable_or_meter_name_22 = vals[i]
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
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """  Corresponds to IDD Field `fuel_type`

        Args:
            value (str): value for IDD Field `fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - Water
                      - Generic
                      - OtherFuel1
                      - OtherFuel2
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
                                 'for field `fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_type`')
            vals = set()
            vals.add("Electricity")
            vals.add("NaturalGas")
            vals.add("PropaneGas")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("Coal")
            vals.add("Diesel")
            vals.add("Gasoline")
            vals.add("Water")
            vals.add("Generic")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fuel_type`'.format(value))

        self._data["Fuel Type"] = value

    @property
    def source_meter_name(self):
        """Get source_meter_name

        Returns:
            str: the value of `source_meter_name` or None if not set
        """
        return self._data["Source Meter Name"]

    @source_meter_name.setter
    def source_meter_name(self, value=None):
        """  Corresponds to IDD Field `source_meter_name`

        Args:
            value (str): value for IDD Field `source_meter_name`
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
                                 'for field `source_meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_meter_name`')

        self._data["Source Meter Name"] = value

    @property
    def key_name_1(self):
        """Get key_name_1

        Returns:
            str: the value of `key_name_1` or None if not set
        """
        return self._data["Key Name 1"]

    @key_name_1.setter
    def key_name_1(self, value=None):
        """  Corresponds to IDD Field `key_name_1`

        Args:
            value (str): value for IDD Field `key_name_1`
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
                                 'for field `key_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_1`')

        self._data["Key Name 1"] = value

    @property
    def output_variable_or_meter_name_1(self):
        """Get output_variable_or_meter_name_1

        Returns:
            str: the value of `output_variable_or_meter_name_1` or None if not set
        """
        return self._data["Output Variable or Meter Name 1"]

    @output_variable_or_meter_name_1.setter
    def output_variable_or_meter_name_1(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_1`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_1`
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
                                 'for field `output_variable_or_meter_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_1`')

        self._data["Output Variable or Meter Name 1"] = value

    @property
    def key_name_2(self):
        """Get key_name_2

        Returns:
            str: the value of `key_name_2` or None if not set
        """
        return self._data["Key Name 2"]

    @key_name_2.setter
    def key_name_2(self, value=None):
        """  Corresponds to IDD Field `key_name_2`

        Args:
            value (str): value for IDD Field `key_name_2`
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
                                 'for field `key_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_2`')

        self._data["Key Name 2"] = value

    @property
    def output_variable_or_meter_name_2(self):
        """Get output_variable_or_meter_name_2

        Returns:
            str: the value of `output_variable_or_meter_name_2` or None if not set
        """
        return self._data["Output Variable or Meter Name 2"]

    @output_variable_or_meter_name_2.setter
    def output_variable_or_meter_name_2(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_2`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_2`
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
                                 'for field `output_variable_or_meter_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_2`')

        self._data["Output Variable or Meter Name 2"] = value

    @property
    def key_name_3(self):
        """Get key_name_3

        Returns:
            str: the value of `key_name_3` or None if not set
        """
        return self._data["Key Name 3"]

    @key_name_3.setter
    def key_name_3(self, value=None):
        """  Corresponds to IDD Field `key_name_3`

        Args:
            value (str): value for IDD Field `key_name_3`
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
                                 'for field `key_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_3`')

        self._data["Key Name 3"] = value

    @property
    def output_variable_or_meter_name_3(self):
        """Get output_variable_or_meter_name_3

        Returns:
            str: the value of `output_variable_or_meter_name_3` or None if not set
        """
        return self._data["Output Variable or Meter Name 3"]

    @output_variable_or_meter_name_3.setter
    def output_variable_or_meter_name_3(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_3`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_3`
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
                                 'for field `output_variable_or_meter_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_3`')

        self._data["Output Variable or Meter Name 3"] = value

    @property
    def key_name_4(self):
        """Get key_name_4

        Returns:
            str: the value of `key_name_4` or None if not set
        """
        return self._data["Key Name 4"]

    @key_name_4.setter
    def key_name_4(self, value=None):
        """  Corresponds to IDD Field `key_name_4`

        Args:
            value (str): value for IDD Field `key_name_4`
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
                                 'for field `key_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_4`')

        self._data["Key Name 4"] = value

    @property
    def output_variable_or_meter_name_4(self):
        """Get output_variable_or_meter_name_4

        Returns:
            str: the value of `output_variable_or_meter_name_4` or None if not set
        """
        return self._data["Output Variable or Meter Name 4"]

    @output_variable_or_meter_name_4.setter
    def output_variable_or_meter_name_4(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_4`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_4`
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
                                 'for field `output_variable_or_meter_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_4`')

        self._data["Output Variable or Meter Name 4"] = value

    @property
    def key_name_5(self):
        """Get key_name_5

        Returns:
            str: the value of `key_name_5` or None if not set
        """
        return self._data["Key Name 5"]

    @key_name_5.setter
    def key_name_5(self, value=None):
        """  Corresponds to IDD Field `key_name_5`

        Args:
            value (str): value for IDD Field `key_name_5`
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
                                 'for field `key_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_5`')

        self._data["Key Name 5"] = value

    @property
    def output_variable_or_meter_name_5(self):
        """Get output_variable_or_meter_name_5

        Returns:
            str: the value of `output_variable_or_meter_name_5` or None if not set
        """
        return self._data["Output Variable or Meter Name 5"]

    @output_variable_or_meter_name_5.setter
    def output_variable_or_meter_name_5(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_5`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_5`
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
                                 'for field `output_variable_or_meter_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_5`')

        self._data["Output Variable or Meter Name 5"] = value

    @property
    def key_name_6(self):
        """Get key_name_6

        Returns:
            str: the value of `key_name_6` or None if not set
        """
        return self._data["Key Name 6"]

    @key_name_6.setter
    def key_name_6(self, value=None):
        """  Corresponds to IDD Field `key_name_6`

        Args:
            value (str): value for IDD Field `key_name_6`
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
                                 'for field `key_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_6`')

        self._data["Key Name 6"] = value

    @property
    def output_variable_or_meter_name_6(self):
        """Get output_variable_or_meter_name_6

        Returns:
            str: the value of `output_variable_or_meter_name_6` or None if not set
        """
        return self._data["Output Variable or Meter Name 6"]

    @output_variable_or_meter_name_6.setter
    def output_variable_or_meter_name_6(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_6`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_6`
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
                                 'for field `output_variable_or_meter_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_6`')

        self._data["Output Variable or Meter Name 6"] = value

    @property
    def key_name_7(self):
        """Get key_name_7

        Returns:
            str: the value of `key_name_7` or None if not set
        """
        return self._data["Key Name 7"]

    @key_name_7.setter
    def key_name_7(self, value=None):
        """  Corresponds to IDD Field `key_name_7`

        Args:
            value (str): value for IDD Field `key_name_7`
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
                                 'for field `key_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_7`')

        self._data["Key Name 7"] = value

    @property
    def output_variable_or_meter_name_7(self):
        """Get output_variable_or_meter_name_7

        Returns:
            str: the value of `output_variable_or_meter_name_7` or None if not set
        """
        return self._data["Output Variable or Meter Name 7"]

    @output_variable_or_meter_name_7.setter
    def output_variable_or_meter_name_7(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_7`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_7`
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
                                 'for field `output_variable_or_meter_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_7`')

        self._data["Output Variable or Meter Name 7"] = value

    @property
    def key_name_8(self):
        """Get key_name_8

        Returns:
            str: the value of `key_name_8` or None if not set
        """
        return self._data["Key Name 8"]

    @key_name_8.setter
    def key_name_8(self, value=None):
        """  Corresponds to IDD Field `key_name_8`

        Args:
            value (str): value for IDD Field `key_name_8`
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
                                 'for field `key_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_8`')

        self._data["Key Name 8"] = value

    @property
    def output_variable_or_meter_name_8(self):
        """Get output_variable_or_meter_name_8

        Returns:
            str: the value of `output_variable_or_meter_name_8` or None if not set
        """
        return self._data["Output Variable or Meter Name 8"]

    @output_variable_or_meter_name_8.setter
    def output_variable_or_meter_name_8(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_8`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_8`
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
                                 'for field `output_variable_or_meter_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_8`')

        self._data["Output Variable or Meter Name 8"] = value

    @property
    def key_name_9(self):
        """Get key_name_9

        Returns:
            str: the value of `key_name_9` or None if not set
        """
        return self._data["Key Name 9"]

    @key_name_9.setter
    def key_name_9(self, value=None):
        """  Corresponds to IDD Field `key_name_9`

        Args:
            value (str): value for IDD Field `key_name_9`
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
                                 'for field `key_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_9`')

        self._data["Key Name 9"] = value

    @property
    def output_variable_or_meter_name_9(self):
        """Get output_variable_or_meter_name_9

        Returns:
            str: the value of `output_variable_or_meter_name_9` or None if not set
        """
        return self._data["Output Variable or Meter Name 9"]

    @output_variable_or_meter_name_9.setter
    def output_variable_or_meter_name_9(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_9`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_9`
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
                                 'for field `output_variable_or_meter_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_9`')

        self._data["Output Variable or Meter Name 9"] = value

    @property
    def key_name_10(self):
        """Get key_name_10

        Returns:
            str: the value of `key_name_10` or None if not set
        """
        return self._data["Key Name 10"]

    @key_name_10.setter
    def key_name_10(self, value=None):
        """  Corresponds to IDD Field `key_name_10`

        Args:
            value (str): value for IDD Field `key_name_10`
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
                                 'for field `key_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_10`')

        self._data["Key Name 10"] = value

    @property
    def output_variable_or_meter_name_10(self):
        """Get output_variable_or_meter_name_10

        Returns:
            str: the value of `output_variable_or_meter_name_10` or None if not set
        """
        return self._data["Output Variable or Meter Name 10"]

    @output_variable_or_meter_name_10.setter
    def output_variable_or_meter_name_10(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_10`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_10`
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
                                 'for field `output_variable_or_meter_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_10`')

        self._data["Output Variable or Meter Name 10"] = value

    @property
    def key_name_11(self):
        """Get key_name_11

        Returns:
            str: the value of `key_name_11` or None if not set
        """
        return self._data["Key Name 11"]

    @key_name_11.setter
    def key_name_11(self, value=None):
        """  Corresponds to IDD Field `key_name_11`

        Args:
            value (str): value for IDD Field `key_name_11`
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
                                 'for field `key_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_11`')

        self._data["Key Name 11"] = value

    @property
    def output_variable_or_meter_name_11(self):
        """Get output_variable_or_meter_name_11

        Returns:
            str: the value of `output_variable_or_meter_name_11` or None if not set
        """
        return self._data["Output Variable or Meter Name 11"]

    @output_variable_or_meter_name_11.setter
    def output_variable_or_meter_name_11(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_11`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_11`
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
                                 'for field `output_variable_or_meter_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_11`')

        self._data["Output Variable or Meter Name 11"] = value

    @property
    def key_name_12(self):
        """Get key_name_12

        Returns:
            str: the value of `key_name_12` or None if not set
        """
        return self._data["Key Name 12"]

    @key_name_12.setter
    def key_name_12(self, value=None):
        """  Corresponds to IDD Field `key_name_12`

        Args:
            value (str): value for IDD Field `key_name_12`
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
                                 'for field `key_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_12`')

        self._data["Key Name 12"] = value

    @property
    def output_variable_or_meter_name_12(self):
        """Get output_variable_or_meter_name_12

        Returns:
            str: the value of `output_variable_or_meter_name_12` or None if not set
        """
        return self._data["Output Variable or Meter Name 12"]

    @output_variable_or_meter_name_12.setter
    def output_variable_or_meter_name_12(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_12`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_12`
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
                                 'for field `output_variable_or_meter_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_12`')

        self._data["Output Variable or Meter Name 12"] = value

    @property
    def key_name_13(self):
        """Get key_name_13

        Returns:
            str: the value of `key_name_13` or None if not set
        """
        return self._data["Key Name 13"]

    @key_name_13.setter
    def key_name_13(self, value=None):
        """  Corresponds to IDD Field `key_name_13`

        Args:
            value (str): value for IDD Field `key_name_13`
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
                                 'for field `key_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_13`')

        self._data["Key Name 13"] = value

    @property
    def output_variable_or_meter_name_13(self):
        """Get output_variable_or_meter_name_13

        Returns:
            str: the value of `output_variable_or_meter_name_13` or None if not set
        """
        return self._data["Output Variable or Meter Name 13"]

    @output_variable_or_meter_name_13.setter
    def output_variable_or_meter_name_13(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_13`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_13`
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
                                 'for field `output_variable_or_meter_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_13`')

        self._data["Output Variable or Meter Name 13"] = value

    @property
    def key_name_14(self):
        """Get key_name_14

        Returns:
            str: the value of `key_name_14` or None if not set
        """
        return self._data["Key Name 14"]

    @key_name_14.setter
    def key_name_14(self, value=None):
        """  Corresponds to IDD Field `key_name_14`

        Args:
            value (str): value for IDD Field `key_name_14`
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
                                 'for field `key_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_14`')

        self._data["Key Name 14"] = value

    @property
    def output_variable_or_meter_name_14(self):
        """Get output_variable_or_meter_name_14

        Returns:
            str: the value of `output_variable_or_meter_name_14` or None if not set
        """
        return self._data["Output Variable or Meter Name 14"]

    @output_variable_or_meter_name_14.setter
    def output_variable_or_meter_name_14(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_14`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_14`
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
                                 'for field `output_variable_or_meter_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_14`')

        self._data["Output Variable or Meter Name 14"] = value

    @property
    def key_name_15(self):
        """Get key_name_15

        Returns:
            str: the value of `key_name_15` or None if not set
        """
        return self._data["Key Name 15"]

    @key_name_15.setter
    def key_name_15(self, value=None):
        """  Corresponds to IDD Field `key_name_15`

        Args:
            value (str): value for IDD Field `key_name_15`
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
                                 'for field `key_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_15`')

        self._data["Key Name 15"] = value

    @property
    def output_variable_or_meter_name_15(self):
        """Get output_variable_or_meter_name_15

        Returns:
            str: the value of `output_variable_or_meter_name_15` or None if not set
        """
        return self._data["Output Variable or Meter Name 15"]

    @output_variable_or_meter_name_15.setter
    def output_variable_or_meter_name_15(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_15`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_15`
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
                                 'for field `output_variable_or_meter_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_15`')

        self._data["Output Variable or Meter Name 15"] = value

    @property
    def key_name_16(self):
        """Get key_name_16

        Returns:
            str: the value of `key_name_16` or None if not set
        """
        return self._data["Key Name 16"]

    @key_name_16.setter
    def key_name_16(self, value=None):
        """  Corresponds to IDD Field `key_name_16`

        Args:
            value (str): value for IDD Field `key_name_16`
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
                                 'for field `key_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_16`')

        self._data["Key Name 16"] = value

    @property
    def output_variable_or_meter_name_16(self):
        """Get output_variable_or_meter_name_16

        Returns:
            str: the value of `output_variable_or_meter_name_16` or None if not set
        """
        return self._data["Output Variable or Meter Name 16"]

    @output_variable_or_meter_name_16.setter
    def output_variable_or_meter_name_16(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_16`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_16`
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
                                 'for field `output_variable_or_meter_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_16`')

        self._data["Output Variable or Meter Name 16"] = value

    @property
    def key_name_17(self):
        """Get key_name_17

        Returns:
            str: the value of `key_name_17` or None if not set
        """
        return self._data["Key Name 17"]

    @key_name_17.setter
    def key_name_17(self, value=None):
        """  Corresponds to IDD Field `key_name_17`

        Args:
            value (str): value for IDD Field `key_name_17`
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
                                 'for field `key_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_17`')

        self._data["Key Name 17"] = value

    @property
    def output_variable_or_meter_name_17(self):
        """Get output_variable_or_meter_name_17

        Returns:
            str: the value of `output_variable_or_meter_name_17` or None if not set
        """
        return self._data["Output Variable or Meter Name 17"]

    @output_variable_or_meter_name_17.setter
    def output_variable_or_meter_name_17(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_17`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_17`
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
                                 'for field `output_variable_or_meter_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_17`')

        self._data["Output Variable or Meter Name 17"] = value

    @property
    def key_name_18(self):
        """Get key_name_18

        Returns:
            str: the value of `key_name_18` or None if not set
        """
        return self._data["Key Name 18"]

    @key_name_18.setter
    def key_name_18(self, value=None):
        """  Corresponds to IDD Field `key_name_18`

        Args:
            value (str): value for IDD Field `key_name_18`
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
                                 'for field `key_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_18`')

        self._data["Key Name 18"] = value

    @property
    def output_variable_or_meter_name_18(self):
        """Get output_variable_or_meter_name_18

        Returns:
            str: the value of `output_variable_or_meter_name_18` or None if not set
        """
        return self._data["Output Variable or Meter Name 18"]

    @output_variable_or_meter_name_18.setter
    def output_variable_or_meter_name_18(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_18`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_18`
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
                                 'for field `output_variable_or_meter_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_18`')

        self._data["Output Variable or Meter Name 18"] = value

    @property
    def key_name_19(self):
        """Get key_name_19

        Returns:
            str: the value of `key_name_19` or None if not set
        """
        return self._data["Key Name 19"]

    @key_name_19.setter
    def key_name_19(self, value=None):
        """  Corresponds to IDD Field `key_name_19`

        Args:
            value (str): value for IDD Field `key_name_19`
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
                                 'for field `key_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_19`')

        self._data["Key Name 19"] = value

    @property
    def output_variable_or_meter_name_19(self):
        """Get output_variable_or_meter_name_19

        Returns:
            str: the value of `output_variable_or_meter_name_19` or None if not set
        """
        return self._data["Output Variable or Meter Name 19"]

    @output_variable_or_meter_name_19.setter
    def output_variable_or_meter_name_19(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_19`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_19`
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
                                 'for field `output_variable_or_meter_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_19`')

        self._data["Output Variable or Meter Name 19"] = value

    @property
    def key_name_20(self):
        """Get key_name_20

        Returns:
            str: the value of `key_name_20` or None if not set
        """
        return self._data["Key Name 20"]

    @key_name_20.setter
    def key_name_20(self, value=None):
        """  Corresponds to IDD Field `key_name_20`

        Args:
            value (str): value for IDD Field `key_name_20`
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
                                 'for field `key_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_20`')

        self._data["Key Name 20"] = value

    @property
    def output_variable_or_meter_name_20(self):
        """Get output_variable_or_meter_name_20

        Returns:
            str: the value of `output_variable_or_meter_name_20` or None if not set
        """
        return self._data["Output Variable or Meter Name 20"]

    @output_variable_or_meter_name_20.setter
    def output_variable_or_meter_name_20(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_20`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_20`
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
                                 'for field `output_variable_or_meter_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_20`')

        self._data["Output Variable or Meter Name 20"] = value

    @property
    def key_name_21(self):
        """Get key_name_21

        Returns:
            str: the value of `key_name_21` or None if not set
        """
        return self._data["Key Name 21"]

    @key_name_21.setter
    def key_name_21(self, value=None):
        """  Corresponds to IDD Field `key_name_21`

        Args:
            value (str): value for IDD Field `key_name_21`
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
                                 'for field `key_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_21`')

        self._data["Key Name 21"] = value

    @property
    def output_variable_or_meter_name_21(self):
        """Get output_variable_or_meter_name_21

        Returns:
            str: the value of `output_variable_or_meter_name_21` or None if not set
        """
        return self._data["Output Variable or Meter Name 21"]

    @output_variable_or_meter_name_21.setter
    def output_variable_or_meter_name_21(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_21`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_21`
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
                                 'for field `output_variable_or_meter_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_21`')

        self._data["Output Variable or Meter Name 21"] = value

    @property
    def key_name_22(self):
        """Get key_name_22

        Returns:
            str: the value of `key_name_22` or None if not set
        """
        return self._data["Key Name 22"]

    @key_name_22.setter
    def key_name_22(self, value=None):
        """  Corresponds to IDD Field `key_name_22`

        Args:
            value (str): value for IDD Field `key_name_22`
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
                                 'for field `key_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `key_name_22`')

        self._data["Key Name 22"] = value

    @property
    def output_variable_or_meter_name_22(self):
        """Get output_variable_or_meter_name_22

        Returns:
            str: the value of `output_variable_or_meter_name_22` or None if not set
        """
        return self._data["Output Variable or Meter Name 22"]

    @output_variable_or_meter_name_22.setter
    def output_variable_or_meter_name_22(self, value=None):
        """  Corresponds to IDD Field `output_variable_or_meter_name_22`

        Args:
            value (str): value for IDD Field `output_variable_or_meter_name_22`
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
                                 'for field `output_variable_or_meter_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_variable_or_meter_name_22`')

        self._data["Output Variable or Meter Name 22"] = value

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
        out.append(self._to_str(self.fuel_type))
        out.append(self._to_str(self.source_meter_name))
        out.append(self._to_str(self.key_name_1))
        out.append(self._to_str(self.output_variable_or_meter_name_1))
        out.append(self._to_str(self.key_name_2))
        out.append(self._to_str(self.output_variable_or_meter_name_2))
        out.append(self._to_str(self.key_name_3))
        out.append(self._to_str(self.output_variable_or_meter_name_3))
        out.append(self._to_str(self.key_name_4))
        out.append(self._to_str(self.output_variable_or_meter_name_4))
        out.append(self._to_str(self.key_name_5))
        out.append(self._to_str(self.output_variable_or_meter_name_5))
        out.append(self._to_str(self.key_name_6))
        out.append(self._to_str(self.output_variable_or_meter_name_6))
        out.append(self._to_str(self.key_name_7))
        out.append(self._to_str(self.output_variable_or_meter_name_7))
        out.append(self._to_str(self.key_name_8))
        out.append(self._to_str(self.output_variable_or_meter_name_8))
        out.append(self._to_str(self.key_name_9))
        out.append(self._to_str(self.output_variable_or_meter_name_9))
        out.append(self._to_str(self.key_name_10))
        out.append(self._to_str(self.output_variable_or_meter_name_10))
        out.append(self._to_str(self.key_name_11))
        out.append(self._to_str(self.output_variable_or_meter_name_11))
        out.append(self._to_str(self.key_name_12))
        out.append(self._to_str(self.output_variable_or_meter_name_12))
        out.append(self._to_str(self.key_name_13))
        out.append(self._to_str(self.output_variable_or_meter_name_13))
        out.append(self._to_str(self.key_name_14))
        out.append(self._to_str(self.output_variable_or_meter_name_14))
        out.append(self._to_str(self.key_name_15))
        out.append(self._to_str(self.output_variable_or_meter_name_15))
        out.append(self._to_str(self.key_name_16))
        out.append(self._to_str(self.output_variable_or_meter_name_16))
        out.append(self._to_str(self.key_name_17))
        out.append(self._to_str(self.output_variable_or_meter_name_17))
        out.append(self._to_str(self.key_name_18))
        out.append(self._to_str(self.output_variable_or_meter_name_18))
        out.append(self._to_str(self.key_name_19))
        out.append(self._to_str(self.output_variable_or_meter_name_19))
        out.append(self._to_str(self.key_name_20))
        out.append(self._to_str(self.output_variable_or_meter_name_20))
        out.append(self._to_str(self.key_name_21))
        out.append(self._to_str(self.output_variable_or_meter_name_21))
        out.append(self._to_str(self.key_name_22))
        out.append(self._to_str(self.output_variable_or_meter_name_22))
        return ",".join(out)