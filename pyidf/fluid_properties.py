import six
from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())



class FluidPropertiesName(DataObject):
    """ Corresponds to IDD object `FluidProperties:Name`
        potential fluid name/type in the input file
        repeat this object for each fluid
    """
    schema = {'min-fields': 0, 'name': u'FluidProperties:Name', 'pyname': u'FluidPropertiesName', 'format': None, 'fields': OrderedDict([(u'fluid name', {'name': u'Fluid Name', 'pyname': u'fluid_name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'fluid type', {'name': u'Fluid Type', 'pyname': u'fluid_type', 'required-field': True, 'autosizable': False, 'accepted-values': [u'Refrigerant', u'Glycol'], 'autocalculatable': False, 'type': 'alpha'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def fluid_name(self):
        """Get fluid_name

        Returns:
            str: the value of `fluid_name` or None if not set
        """
        return self["Fluid Name"]

    @fluid_name.setter
    def fluid_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Name`

        Args:
            value (str): value for IDD Field `Fluid Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Name"] = value

    @property
    def fluid_type(self):
        """Get fluid_type

        Returns:
            str: the value of `fluid_type` or None if not set
        """
        return self["Fluid Type"]

    @fluid_type.setter
    def fluid_type(self, value=None):
        """  Corresponds to IDD Field `Fluid Type`

        Args:
            value (str): value for IDD Field `Fluid Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Type"] = value


class FluidPropertiesGlycolConcentration(DataObject):
    """ Corresponds to IDD object `FluidProperties:GlycolConcentration`
        glycol and what concentration it is
    """
    schema = {'min-fields': 0, 'name': u'FluidProperties:GlycolConcentration', 'pyname': u'FluidPropertiesGlycolConcentration', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': True, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'glycol type', {'name': u'Glycol Type', 'pyname': u'glycol_type', 'required-field': True, 'autosizable': False, 'accepted-values': [u'EthyleneGlycol', u'PropyleneGlycol', u'UserDefinedGlycolType'], 'autocalculatable': False, 'type': 'alpha'}), (u'user defined glycol name', {'name': u'User Defined Glycol Name', 'pyname': u'user_defined_glycol_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'glycol concentration', {'name': u'Glycol Concentration', 'pyname': u'glycol_concentration', 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

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
    def glycol_type(self):
        """Get glycol_type

        Returns:
            str: the value of `glycol_type` or None if not set
        """
        return self["Glycol Type"]

    @glycol_type.setter
    def glycol_type(self, value=None):
        """  Corresponds to IDD Field `Glycol Type`
        or UserDefined Fluid (must show up as a glycol in FluidProperties:Name object)

        Args:
            value (str): value for IDD Field `Glycol Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Glycol Type"] = value

    @property
    def user_defined_glycol_name(self):
        """Get user_defined_glycol_name

        Returns:
            str: the value of `user_defined_glycol_name` or None if not set
        """
        return self["User Defined Glycol Name"]

    @user_defined_glycol_name.setter
    def user_defined_glycol_name(self, value=None):
        """  Corresponds to IDD Field `User Defined Glycol Name`

        Args:
            value (str): value for IDD Field `User Defined Glycol Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["User Defined Glycol Name"] = value

    @property
    def glycol_concentration(self):
        """Get glycol_concentration

        Returns:
            float: the value of `glycol_concentration` or None if not set
        """
        return self["Glycol Concentration"]

    @glycol_concentration.setter
    def glycol_concentration(self, value=None):
        """  Corresponds to IDD Field `Glycol Concentration`

        Args:
            value (float): value for IDD Field `Glycol Concentration`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Glycol Concentration"] = value


class FluidPropertiesTemperatures(DataObject):
    """ Corresponds to IDD object `FluidProperties:Temperatures`
        property values for fluid properties
        list of up to 250 temperatures, note that number of property values must match the number of properties
        in other words, there must be a one-to-one correspondence between the property values in this list and
        the actual properties list in other syntax
        degrees C (for all temperature inputs)
    """
    schema = {'min-fields': 0, 'name': u'FluidProperties:Temperatures', 'pyname': u'FluidPropertiesTemperatures', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'alpha'}), (u'temperature 1', {'name': u'Temperature 1', 'pyname': u'temperature_1', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 2', {'name': u'Temperature 2', 'pyname': u'temperature_2', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 3', {'name': u'Temperature 3', 'pyname': u'temperature_3', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 4', {'name': u'Temperature 4', 'pyname': u'temperature_4', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 5', {'name': u'Temperature 5', 'pyname': u'temperature_5', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 6', {'name': u'Temperature 6', 'pyname': u'temperature_6', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 7', {'name': u'Temperature 7', 'pyname': u'temperature_7', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 8', {'name': u'Temperature 8', 'pyname': u'temperature_8', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 9', {'name': u'Temperature 9', 'pyname': u'temperature_9', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 10', {'name': u'Temperature 10', 'pyname': u'temperature_10', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 11', {'name': u'Temperature 11', 'pyname': u'temperature_11', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 12', {'name': u'Temperature 12', 'pyname': u'temperature_12', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 13', {'name': u'Temperature 13', 'pyname': u'temperature_13', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 14', {'name': u'Temperature 14', 'pyname': u'temperature_14', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 15', {'name': u'Temperature 15', 'pyname': u'temperature_15', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 16', {'name': u'Temperature 16', 'pyname': u'temperature_16', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 17', {'name': u'Temperature 17', 'pyname': u'temperature_17', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 18', {'name': u'Temperature 18', 'pyname': u'temperature_18', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 19', {'name': u'Temperature 19', 'pyname': u'temperature_19', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 20', {'name': u'Temperature 20', 'pyname': u'temperature_20', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 21', {'name': u'Temperature 21', 'pyname': u'temperature_21', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 22', {'name': u'Temperature 22', 'pyname': u'temperature_22', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 23', {'name': u'Temperature 23', 'pyname': u'temperature_23', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 24', {'name': u'Temperature 24', 'pyname': u'temperature_24', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 25', {'name': u'Temperature 25', 'pyname': u'temperature_25', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 26', {'name': u'Temperature 26', 'pyname': u'temperature_26', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 27', {'name': u'Temperature 27', 'pyname': u'temperature_27', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 28', {'name': u'Temperature 28', 'pyname': u'temperature_28', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 29', {'name': u'Temperature 29', 'pyname': u'temperature_29', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 30', {'name': u'Temperature 30', 'pyname': u'temperature_30', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 31', {'name': u'Temperature 31', 'pyname': u'temperature_31', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 32', {'name': u'Temperature 32', 'pyname': u'temperature_32', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 33', {'name': u'Temperature 33', 'pyname': u'temperature_33', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 34', {'name': u'Temperature 34', 'pyname': u'temperature_34', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 35', {'name': u'Temperature 35', 'pyname': u'temperature_35', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 36', {'name': u'Temperature 36', 'pyname': u'temperature_36', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 37', {'name': u'Temperature 37', 'pyname': u'temperature_37', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 38', {'name': u'Temperature 38', 'pyname': u'temperature_38', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 39', {'name': u'Temperature 39', 'pyname': u'temperature_39', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 40', {'name': u'Temperature 40', 'pyname': u'temperature_40', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 41', {'name': u'Temperature 41', 'pyname': u'temperature_41', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 42', {'name': u'Temperature 42', 'pyname': u'temperature_42', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 43', {'name': u'Temperature 43', 'pyname': u'temperature_43', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 44', {'name': u'Temperature 44', 'pyname': u'temperature_44', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 45', {'name': u'Temperature 45', 'pyname': u'temperature_45', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 46', {'name': u'Temperature 46', 'pyname': u'temperature_46', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 47', {'name': u'Temperature 47', 'pyname': u'temperature_47', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 48', {'name': u'Temperature 48', 'pyname': u'temperature_48', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 49', {'name': u'Temperature 49', 'pyname': u'temperature_49', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 50', {'name': u'Temperature 50', 'pyname': u'temperature_50', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 51', {'name': u'Temperature 51', 'pyname': u'temperature_51', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 52', {'name': u'Temperature 52', 'pyname': u'temperature_52', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 53', {'name': u'Temperature 53', 'pyname': u'temperature_53', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 54', {'name': u'Temperature 54', 'pyname': u'temperature_54', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 55', {'name': u'Temperature 55', 'pyname': u'temperature_55', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 56', {'name': u'Temperature 56', 'pyname': u'temperature_56', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 57', {'name': u'Temperature 57', 'pyname': u'temperature_57', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 58', {'name': u'Temperature 58', 'pyname': u'temperature_58', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 59', {'name': u'Temperature 59', 'pyname': u'temperature_59', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 60', {'name': u'Temperature 60', 'pyname': u'temperature_60', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 61', {'name': u'Temperature 61', 'pyname': u'temperature_61', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 62', {'name': u'Temperature 62', 'pyname': u'temperature_62', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 63', {'name': u'Temperature 63', 'pyname': u'temperature_63', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 64', {'name': u'Temperature 64', 'pyname': u'temperature_64', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 65', {'name': u'Temperature 65', 'pyname': u'temperature_65', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 66', {'name': u'Temperature 66', 'pyname': u'temperature_66', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 67', {'name': u'Temperature 67', 'pyname': u'temperature_67', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 68', {'name': u'Temperature 68', 'pyname': u'temperature_68', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 69', {'name': u'Temperature 69', 'pyname': u'temperature_69', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 70', {'name': u'Temperature 70', 'pyname': u'temperature_70', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 71', {'name': u'Temperature 71', 'pyname': u'temperature_71', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 72', {'name': u'Temperature 72', 'pyname': u'temperature_72', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 73', {'name': u'Temperature 73', 'pyname': u'temperature_73', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 74', {'name': u'Temperature 74', 'pyname': u'temperature_74', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 75', {'name': u'Temperature 75', 'pyname': u'temperature_75', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 76', {'name': u'Temperature 76', 'pyname': u'temperature_76', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 77', {'name': u'Temperature 77', 'pyname': u'temperature_77', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 78', {'name': u'Temperature 78', 'pyname': u'temperature_78', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 79', {'name': u'Temperature 79', 'pyname': u'temperature_79', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 80', {'name': u'Temperature 80', 'pyname': u'temperature_80', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 81', {'name': u'Temperature 81', 'pyname': u'temperature_81', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 82', {'name': u'Temperature 82', 'pyname': u'temperature_82', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 83', {'name': u'Temperature 83', 'pyname': u'temperature_83', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 84', {'name': u'Temperature 84', 'pyname': u'temperature_84', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 85', {'name': u'Temperature 85', 'pyname': u'temperature_85', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 86', {'name': u'Temperature 86', 'pyname': u'temperature_86', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 87', {'name': u'Temperature 87', 'pyname': u'temperature_87', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 88', {'name': u'Temperature 88', 'pyname': u'temperature_88', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 89', {'name': u'Temperature 89', 'pyname': u'temperature_89', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 90', {'name': u'Temperature 90', 'pyname': u'temperature_90', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 91', {'name': u'Temperature 91', 'pyname': u'temperature_91', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 92', {'name': u'Temperature 92', 'pyname': u'temperature_92', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 93', {'name': u'Temperature 93', 'pyname': u'temperature_93', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 94', {'name': u'Temperature 94', 'pyname': u'temperature_94', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 95', {'name': u'Temperature 95', 'pyname': u'temperature_95', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 96', {'name': u'Temperature 96', 'pyname': u'temperature_96', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 97', {'name': u'Temperature 97', 'pyname': u'temperature_97', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 98', {'name': u'Temperature 98', 'pyname': u'temperature_98', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 99', {'name': u'Temperature 99', 'pyname': u'temperature_99', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 100', {'name': u'Temperature 100', 'pyname': u'temperature_100', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 101', {'name': u'Temperature 101', 'pyname': u'temperature_101', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 102', {'name': u'Temperature 102', 'pyname': u'temperature_102', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 103', {'name': u'Temperature 103', 'pyname': u'temperature_103', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 104', {'name': u'Temperature 104', 'pyname': u'temperature_104', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 105', {'name': u'Temperature 105', 'pyname': u'temperature_105', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 106', {'name': u'Temperature 106', 'pyname': u'temperature_106', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 107', {'name': u'Temperature 107', 'pyname': u'temperature_107', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 108', {'name': u'Temperature 108', 'pyname': u'temperature_108', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 109', {'name': u'Temperature 109', 'pyname': u'temperature_109', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 110', {'name': u'Temperature 110', 'pyname': u'temperature_110', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 111', {'name': u'Temperature 111', 'pyname': u'temperature_111', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 112', {'name': u'Temperature 112', 'pyname': u'temperature_112', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 113', {'name': u'Temperature 113', 'pyname': u'temperature_113', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 114', {'name': u'Temperature 114', 'pyname': u'temperature_114', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 115', {'name': u'Temperature 115', 'pyname': u'temperature_115', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 116', {'name': u'Temperature 116', 'pyname': u'temperature_116', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 117', {'name': u'Temperature 117', 'pyname': u'temperature_117', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 118', {'name': u'Temperature 118', 'pyname': u'temperature_118', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 119', {'name': u'Temperature 119', 'pyname': u'temperature_119', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 120', {'name': u'Temperature 120', 'pyname': u'temperature_120', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 121', {'name': u'Temperature 121', 'pyname': u'temperature_121', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 122', {'name': u'Temperature 122', 'pyname': u'temperature_122', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 123', {'name': u'Temperature 123', 'pyname': u'temperature_123', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 124', {'name': u'Temperature 124', 'pyname': u'temperature_124', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 125', {'name': u'Temperature 125', 'pyname': u'temperature_125', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 126', {'name': u'Temperature 126', 'pyname': u'temperature_126', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 127', {'name': u'Temperature 127', 'pyname': u'temperature_127', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 128', {'name': u'Temperature 128', 'pyname': u'temperature_128', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 129', {'name': u'Temperature 129', 'pyname': u'temperature_129', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 130', {'name': u'Temperature 130', 'pyname': u'temperature_130', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 131', {'name': u'Temperature 131', 'pyname': u'temperature_131', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 132', {'name': u'Temperature 132', 'pyname': u'temperature_132', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 133', {'name': u'Temperature 133', 'pyname': u'temperature_133', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 134', {'name': u'Temperature 134', 'pyname': u'temperature_134', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 135', {'name': u'Temperature 135', 'pyname': u'temperature_135', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 136', {'name': u'Temperature 136', 'pyname': u'temperature_136', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 137', {'name': u'Temperature 137', 'pyname': u'temperature_137', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 138', {'name': u'Temperature 138', 'pyname': u'temperature_138', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 139', {'name': u'Temperature 139', 'pyname': u'temperature_139', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 140', {'name': u'Temperature 140', 'pyname': u'temperature_140', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 141', {'name': u'Temperature 141', 'pyname': u'temperature_141', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 142', {'name': u'Temperature 142', 'pyname': u'temperature_142', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 143', {'name': u'Temperature 143', 'pyname': u'temperature_143', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 144', {'name': u'Temperature 144', 'pyname': u'temperature_144', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 145', {'name': u'Temperature 145', 'pyname': u'temperature_145', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 146', {'name': u'Temperature 146', 'pyname': u'temperature_146', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 147', {'name': u'Temperature 147', 'pyname': u'temperature_147', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 148', {'name': u'Temperature 148', 'pyname': u'temperature_148', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 149', {'name': u'Temperature 149', 'pyname': u'temperature_149', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 150', {'name': u'Temperature 150', 'pyname': u'temperature_150', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 151', {'name': u'Temperature 151', 'pyname': u'temperature_151', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 152', {'name': u'Temperature 152', 'pyname': u'temperature_152', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 153', {'name': u'Temperature 153', 'pyname': u'temperature_153', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 154', {'name': u'Temperature 154', 'pyname': u'temperature_154', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 155', {'name': u'Temperature 155', 'pyname': u'temperature_155', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 156', {'name': u'Temperature 156', 'pyname': u'temperature_156', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 157', {'name': u'Temperature 157', 'pyname': u'temperature_157', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 158', {'name': u'Temperature 158', 'pyname': u'temperature_158', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 159', {'name': u'Temperature 159', 'pyname': u'temperature_159', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 160', {'name': u'Temperature 160', 'pyname': u'temperature_160', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 161', {'name': u'Temperature 161', 'pyname': u'temperature_161', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 162', {'name': u'Temperature 162', 'pyname': u'temperature_162', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 163', {'name': u'Temperature 163', 'pyname': u'temperature_163', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 164', {'name': u'Temperature 164', 'pyname': u'temperature_164', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 165', {'name': u'Temperature 165', 'pyname': u'temperature_165', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 166', {'name': u'Temperature 166', 'pyname': u'temperature_166', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 167', {'name': u'Temperature 167', 'pyname': u'temperature_167', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 168', {'name': u'Temperature 168', 'pyname': u'temperature_168', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 169', {'name': u'Temperature 169', 'pyname': u'temperature_169', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 170', {'name': u'Temperature 170', 'pyname': u'temperature_170', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 171', {'name': u'Temperature 171', 'pyname': u'temperature_171', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 172', {'name': u'Temperature 172', 'pyname': u'temperature_172', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 173', {'name': u'Temperature 173', 'pyname': u'temperature_173', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 174', {'name': u'Temperature 174', 'pyname': u'temperature_174', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 175', {'name': u'Temperature 175', 'pyname': u'temperature_175', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 176', {'name': u'Temperature 176', 'pyname': u'temperature_176', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 177', {'name': u'Temperature 177', 'pyname': u'temperature_177', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 178', {'name': u'Temperature 178', 'pyname': u'temperature_178', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 179', {'name': u'Temperature 179', 'pyname': u'temperature_179', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 180', {'name': u'Temperature 180', 'pyname': u'temperature_180', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 181', {'name': u'Temperature 181', 'pyname': u'temperature_181', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 182', {'name': u'Temperature 182', 'pyname': u'temperature_182', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 183', {'name': u'Temperature 183', 'pyname': u'temperature_183', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 184', {'name': u'Temperature 184', 'pyname': u'temperature_184', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 185', {'name': u'Temperature 185', 'pyname': u'temperature_185', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 186', {'name': u'Temperature 186', 'pyname': u'temperature_186', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 187', {'name': u'Temperature 187', 'pyname': u'temperature_187', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 188', {'name': u'Temperature 188', 'pyname': u'temperature_188', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 189', {'name': u'Temperature 189', 'pyname': u'temperature_189', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 190', {'name': u'Temperature 190', 'pyname': u'temperature_190', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 191', {'name': u'Temperature 191', 'pyname': u'temperature_191', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 192', {'name': u'Temperature 192', 'pyname': u'temperature_192', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 193', {'name': u'Temperature 193', 'pyname': u'temperature_193', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 194', {'name': u'Temperature 194', 'pyname': u'temperature_194', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 195', {'name': u'Temperature 195', 'pyname': u'temperature_195', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 196', {'name': u'Temperature 196', 'pyname': u'temperature_196', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 197', {'name': u'Temperature 197', 'pyname': u'temperature_197', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 198', {'name': u'Temperature 198', 'pyname': u'temperature_198', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 199', {'name': u'Temperature 199', 'pyname': u'temperature_199', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 200', {'name': u'Temperature 200', 'pyname': u'temperature_200', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 201', {'name': u'Temperature 201', 'pyname': u'temperature_201', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 202', {'name': u'Temperature 202', 'pyname': u'temperature_202', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 203', {'name': u'Temperature 203', 'pyname': u'temperature_203', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 204', {'name': u'Temperature 204', 'pyname': u'temperature_204', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 205', {'name': u'Temperature 205', 'pyname': u'temperature_205', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 206', {'name': u'Temperature 206', 'pyname': u'temperature_206', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 207', {'name': u'Temperature 207', 'pyname': u'temperature_207', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 208', {'name': u'Temperature 208', 'pyname': u'temperature_208', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 209', {'name': u'Temperature 209', 'pyname': u'temperature_209', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 210', {'name': u'Temperature 210', 'pyname': u'temperature_210', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 211', {'name': u'Temperature 211', 'pyname': u'temperature_211', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 212', {'name': u'Temperature 212', 'pyname': u'temperature_212', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 213', {'name': u'Temperature 213', 'pyname': u'temperature_213', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 214', {'name': u'Temperature 214', 'pyname': u'temperature_214', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 215', {'name': u'Temperature 215', 'pyname': u'temperature_215', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 216', {'name': u'Temperature 216', 'pyname': u'temperature_216', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 217', {'name': u'Temperature 217', 'pyname': u'temperature_217', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 218', {'name': u'Temperature 218', 'pyname': u'temperature_218', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 219', {'name': u'Temperature 219', 'pyname': u'temperature_219', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 220', {'name': u'Temperature 220', 'pyname': u'temperature_220', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 221', {'name': u'Temperature 221', 'pyname': u'temperature_221', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 222', {'name': u'Temperature 222', 'pyname': u'temperature_222', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 223', {'name': u'Temperature 223', 'pyname': u'temperature_223', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 224', {'name': u'Temperature 224', 'pyname': u'temperature_224', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 225', {'name': u'Temperature 225', 'pyname': u'temperature_225', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 226', {'name': u'Temperature 226', 'pyname': u'temperature_226', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 227', {'name': u'Temperature 227', 'pyname': u'temperature_227', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 228', {'name': u'Temperature 228', 'pyname': u'temperature_228', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 229', {'name': u'Temperature 229', 'pyname': u'temperature_229', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 230', {'name': u'Temperature 230', 'pyname': u'temperature_230', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 231', {'name': u'Temperature 231', 'pyname': u'temperature_231', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 232', {'name': u'Temperature 232', 'pyname': u'temperature_232', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 233', {'name': u'Temperature 233', 'pyname': u'temperature_233', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 234', {'name': u'Temperature 234', 'pyname': u'temperature_234', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 235', {'name': u'Temperature 235', 'pyname': u'temperature_235', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 236', {'name': u'Temperature 236', 'pyname': u'temperature_236', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 237', {'name': u'Temperature 237', 'pyname': u'temperature_237', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 238', {'name': u'Temperature 238', 'pyname': u'temperature_238', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 239', {'name': u'Temperature 239', 'pyname': u'temperature_239', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 240', {'name': u'Temperature 240', 'pyname': u'temperature_240', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 241', {'name': u'Temperature 241', 'pyname': u'temperature_241', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 242', {'name': u'Temperature 242', 'pyname': u'temperature_242', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 243', {'name': u'Temperature 243', 'pyname': u'temperature_243', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 244', {'name': u'Temperature 244', 'pyname': u'temperature_244', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 245', {'name': u'Temperature 245', 'pyname': u'temperature_245', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 246', {'name': u'Temperature 246', 'pyname': u'temperature_246', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 247', {'name': u'Temperature 247', 'pyname': u'temperature_247', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 248', {'name': u'Temperature 248', 'pyname': u'temperature_248', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 249', {'name': u'Temperature 249', 'pyname': u'temperature_249', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'}), (u'temperature 250', {'name': u'Temperature 250', 'pyname': u'temperature_250', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'C'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

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
    def temperature_1(self):
        """Get temperature_1

        Returns:
            float: the value of `temperature_1` or None if not set
        """
        return self["Temperature 1"]

    @temperature_1.setter
    def temperature_1(self, value=None):
        """  Corresponds to IDD Field `Temperature 1`

        Args:
            value (float): value for IDD Field `Temperature 1`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 1"] = value

    @property
    def temperature_2(self):
        """Get temperature_2

        Returns:
            float: the value of `temperature_2` or None if not set
        """
        return self["Temperature 2"]

    @temperature_2.setter
    def temperature_2(self, value=None):
        """  Corresponds to IDD Field `Temperature 2`

        Args:
            value (float): value for IDD Field `Temperature 2`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 2"] = value

    @property
    def temperature_3(self):
        """Get temperature_3

        Returns:
            float: the value of `temperature_3` or None if not set
        """
        return self["Temperature 3"]

    @temperature_3.setter
    def temperature_3(self, value=None):
        """  Corresponds to IDD Field `Temperature 3`

        Args:
            value (float): value for IDD Field `Temperature 3`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 3"] = value

    @property
    def temperature_4(self):
        """Get temperature_4

        Returns:
            float: the value of `temperature_4` or None if not set
        """
        return self["Temperature 4"]

    @temperature_4.setter
    def temperature_4(self, value=None):
        """  Corresponds to IDD Field `Temperature 4`

        Args:
            value (float): value for IDD Field `Temperature 4`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 4"] = value

    @property
    def temperature_5(self):
        """Get temperature_5

        Returns:
            float: the value of `temperature_5` or None if not set
        """
        return self["Temperature 5"]

    @temperature_5.setter
    def temperature_5(self, value=None):
        """  Corresponds to IDD Field `Temperature 5`

        Args:
            value (float): value for IDD Field `Temperature 5`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 5"] = value

    @property
    def temperature_6(self):
        """Get temperature_6

        Returns:
            float: the value of `temperature_6` or None if not set
        """
        return self["Temperature 6"]

    @temperature_6.setter
    def temperature_6(self, value=None):
        """  Corresponds to IDD Field `Temperature 6`

        Args:
            value (float): value for IDD Field `Temperature 6`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 6"] = value

    @property
    def temperature_7(self):
        """Get temperature_7

        Returns:
            float: the value of `temperature_7` or None if not set
        """
        return self["Temperature 7"]

    @temperature_7.setter
    def temperature_7(self, value=None):
        """  Corresponds to IDD Field `Temperature 7`

        Args:
            value (float): value for IDD Field `Temperature 7`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 7"] = value

    @property
    def temperature_8(self):
        """Get temperature_8

        Returns:
            float: the value of `temperature_8` or None if not set
        """
        return self["Temperature 8"]

    @temperature_8.setter
    def temperature_8(self, value=None):
        """  Corresponds to IDD Field `Temperature 8`

        Args:
            value (float): value for IDD Field `Temperature 8`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 8"] = value

    @property
    def temperature_9(self):
        """Get temperature_9

        Returns:
            float: the value of `temperature_9` or None if not set
        """
        return self["Temperature 9"]

    @temperature_9.setter
    def temperature_9(self, value=None):
        """  Corresponds to IDD Field `Temperature 9`

        Args:
            value (float): value for IDD Field `Temperature 9`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 9"] = value

    @property
    def temperature_10(self):
        """Get temperature_10

        Returns:
            float: the value of `temperature_10` or None if not set
        """
        return self["Temperature 10"]

    @temperature_10.setter
    def temperature_10(self, value=None):
        """  Corresponds to IDD Field `Temperature 10`

        Args:
            value (float): value for IDD Field `Temperature 10`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 10"] = value

    @property
    def temperature_11(self):
        """Get temperature_11

        Returns:
            float: the value of `temperature_11` or None if not set
        """
        return self["Temperature 11"]

    @temperature_11.setter
    def temperature_11(self, value=None):
        """  Corresponds to IDD Field `Temperature 11`

        Args:
            value (float): value for IDD Field `Temperature 11`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 11"] = value

    @property
    def temperature_12(self):
        """Get temperature_12

        Returns:
            float: the value of `temperature_12` or None if not set
        """
        return self["Temperature 12"]

    @temperature_12.setter
    def temperature_12(self, value=None):
        """  Corresponds to IDD Field `Temperature 12`

        Args:
            value (float): value for IDD Field `Temperature 12`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 12"] = value

    @property
    def temperature_13(self):
        """Get temperature_13

        Returns:
            float: the value of `temperature_13` or None if not set
        """
        return self["Temperature 13"]

    @temperature_13.setter
    def temperature_13(self, value=None):
        """  Corresponds to IDD Field `Temperature 13`

        Args:
            value (float): value for IDD Field `Temperature 13`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 13"] = value

    @property
    def temperature_14(self):
        """Get temperature_14

        Returns:
            float: the value of `temperature_14` or None if not set
        """
        return self["Temperature 14"]

    @temperature_14.setter
    def temperature_14(self, value=None):
        """  Corresponds to IDD Field `Temperature 14`

        Args:
            value (float): value for IDD Field `Temperature 14`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 14"] = value

    @property
    def temperature_15(self):
        """Get temperature_15

        Returns:
            float: the value of `temperature_15` or None if not set
        """
        return self["Temperature 15"]

    @temperature_15.setter
    def temperature_15(self, value=None):
        """  Corresponds to IDD Field `Temperature 15`

        Args:
            value (float): value for IDD Field `Temperature 15`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 15"] = value

    @property
    def temperature_16(self):
        """Get temperature_16

        Returns:
            float: the value of `temperature_16` or None if not set
        """
        return self["Temperature 16"]

    @temperature_16.setter
    def temperature_16(self, value=None):
        """  Corresponds to IDD Field `Temperature 16`

        Args:
            value (float): value for IDD Field `Temperature 16`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 16"] = value

    @property
    def temperature_17(self):
        """Get temperature_17

        Returns:
            float: the value of `temperature_17` or None if not set
        """
        return self["Temperature 17"]

    @temperature_17.setter
    def temperature_17(self, value=None):
        """  Corresponds to IDD Field `Temperature 17`

        Args:
            value (float): value for IDD Field `Temperature 17`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 17"] = value

    @property
    def temperature_18(self):
        """Get temperature_18

        Returns:
            float: the value of `temperature_18` or None if not set
        """
        return self["Temperature 18"]

    @temperature_18.setter
    def temperature_18(self, value=None):
        """  Corresponds to IDD Field `Temperature 18`

        Args:
            value (float): value for IDD Field `Temperature 18`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 18"] = value

    @property
    def temperature_19(self):
        """Get temperature_19

        Returns:
            float: the value of `temperature_19` or None if not set
        """
        return self["Temperature 19"]

    @temperature_19.setter
    def temperature_19(self, value=None):
        """  Corresponds to IDD Field `Temperature 19`

        Args:
            value (float): value for IDD Field `Temperature 19`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 19"] = value

    @property
    def temperature_20(self):
        """Get temperature_20

        Returns:
            float: the value of `temperature_20` or None if not set
        """
        return self["Temperature 20"]

    @temperature_20.setter
    def temperature_20(self, value=None):
        """  Corresponds to IDD Field `Temperature 20`

        Args:
            value (float): value for IDD Field `Temperature 20`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 20"] = value

    @property
    def temperature_21(self):
        """Get temperature_21

        Returns:
            float: the value of `temperature_21` or None if not set
        """
        return self["Temperature 21"]

    @temperature_21.setter
    def temperature_21(self, value=None):
        """  Corresponds to IDD Field `Temperature 21`

        Args:
            value (float): value for IDD Field `Temperature 21`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 21"] = value

    @property
    def temperature_22(self):
        """Get temperature_22

        Returns:
            float: the value of `temperature_22` or None if not set
        """
        return self["Temperature 22"]

    @temperature_22.setter
    def temperature_22(self, value=None):
        """  Corresponds to IDD Field `Temperature 22`

        Args:
            value (float): value for IDD Field `Temperature 22`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 22"] = value

    @property
    def temperature_23(self):
        """Get temperature_23

        Returns:
            float: the value of `temperature_23` or None if not set
        """
        return self["Temperature 23"]

    @temperature_23.setter
    def temperature_23(self, value=None):
        """  Corresponds to IDD Field `Temperature 23`

        Args:
            value (float): value for IDD Field `Temperature 23`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 23"] = value

    @property
    def temperature_24(self):
        """Get temperature_24

        Returns:
            float: the value of `temperature_24` or None if not set
        """
        return self["Temperature 24"]

    @temperature_24.setter
    def temperature_24(self, value=None):
        """  Corresponds to IDD Field `Temperature 24`

        Args:
            value (float): value for IDD Field `Temperature 24`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 24"] = value

    @property
    def temperature_25(self):
        """Get temperature_25

        Returns:
            float: the value of `temperature_25` or None if not set
        """
        return self["Temperature 25"]

    @temperature_25.setter
    def temperature_25(self, value=None):
        """  Corresponds to IDD Field `Temperature 25`

        Args:
            value (float): value for IDD Field `Temperature 25`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 25"] = value

    @property
    def temperature_26(self):
        """Get temperature_26

        Returns:
            float: the value of `temperature_26` or None if not set
        """
        return self["Temperature 26"]

    @temperature_26.setter
    def temperature_26(self, value=None):
        """  Corresponds to IDD Field `Temperature 26`

        Args:
            value (float): value for IDD Field `Temperature 26`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 26"] = value

    @property
    def temperature_27(self):
        """Get temperature_27

        Returns:
            float: the value of `temperature_27` or None if not set
        """
        return self["Temperature 27"]

    @temperature_27.setter
    def temperature_27(self, value=None):
        """  Corresponds to IDD Field `Temperature 27`

        Args:
            value (float): value for IDD Field `Temperature 27`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 27"] = value

    @property
    def temperature_28(self):
        """Get temperature_28

        Returns:
            float: the value of `temperature_28` or None if not set
        """
        return self["Temperature 28"]

    @temperature_28.setter
    def temperature_28(self, value=None):
        """  Corresponds to IDD Field `Temperature 28`

        Args:
            value (float): value for IDD Field `Temperature 28`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 28"] = value

    @property
    def temperature_29(self):
        """Get temperature_29

        Returns:
            float: the value of `temperature_29` or None if not set
        """
        return self["Temperature 29"]

    @temperature_29.setter
    def temperature_29(self, value=None):
        """  Corresponds to IDD Field `Temperature 29`

        Args:
            value (float): value for IDD Field `Temperature 29`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 29"] = value

    @property
    def temperature_30(self):
        """Get temperature_30

        Returns:
            float: the value of `temperature_30` or None if not set
        """
        return self["Temperature 30"]

    @temperature_30.setter
    def temperature_30(self, value=None):
        """  Corresponds to IDD Field `Temperature 30`

        Args:
            value (float): value for IDD Field `Temperature 30`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 30"] = value

    @property
    def temperature_31(self):
        """Get temperature_31

        Returns:
            float: the value of `temperature_31` or None if not set
        """
        return self["Temperature 31"]

    @temperature_31.setter
    def temperature_31(self, value=None):
        """  Corresponds to IDD Field `Temperature 31`

        Args:
            value (float): value for IDD Field `Temperature 31`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 31"] = value

    @property
    def temperature_32(self):
        """Get temperature_32

        Returns:
            float: the value of `temperature_32` or None if not set
        """
        return self["Temperature 32"]

    @temperature_32.setter
    def temperature_32(self, value=None):
        """  Corresponds to IDD Field `Temperature 32`

        Args:
            value (float): value for IDD Field `Temperature 32`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 32"] = value

    @property
    def temperature_33(self):
        """Get temperature_33

        Returns:
            float: the value of `temperature_33` or None if not set
        """
        return self["Temperature 33"]

    @temperature_33.setter
    def temperature_33(self, value=None):
        """  Corresponds to IDD Field `Temperature 33`

        Args:
            value (float): value for IDD Field `Temperature 33`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 33"] = value

    @property
    def temperature_34(self):
        """Get temperature_34

        Returns:
            float: the value of `temperature_34` or None if not set
        """
        return self["Temperature 34"]

    @temperature_34.setter
    def temperature_34(self, value=None):
        """  Corresponds to IDD Field `Temperature 34`

        Args:
            value (float): value for IDD Field `Temperature 34`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 34"] = value

    @property
    def temperature_35(self):
        """Get temperature_35

        Returns:
            float: the value of `temperature_35` or None if not set
        """
        return self["Temperature 35"]

    @temperature_35.setter
    def temperature_35(self, value=None):
        """  Corresponds to IDD Field `Temperature 35`

        Args:
            value (float): value for IDD Field `Temperature 35`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 35"] = value

    @property
    def temperature_36(self):
        """Get temperature_36

        Returns:
            float: the value of `temperature_36` or None if not set
        """
        return self["Temperature 36"]

    @temperature_36.setter
    def temperature_36(self, value=None):
        """  Corresponds to IDD Field `Temperature 36`

        Args:
            value (float): value for IDD Field `Temperature 36`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 36"] = value

    @property
    def temperature_37(self):
        """Get temperature_37

        Returns:
            float: the value of `temperature_37` or None if not set
        """
        return self["Temperature 37"]

    @temperature_37.setter
    def temperature_37(self, value=None):
        """  Corresponds to IDD Field `Temperature 37`

        Args:
            value (float): value for IDD Field `Temperature 37`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 37"] = value

    @property
    def temperature_38(self):
        """Get temperature_38

        Returns:
            float: the value of `temperature_38` or None if not set
        """
        return self["Temperature 38"]

    @temperature_38.setter
    def temperature_38(self, value=None):
        """  Corresponds to IDD Field `Temperature 38`

        Args:
            value (float): value for IDD Field `Temperature 38`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 38"] = value

    @property
    def temperature_39(self):
        """Get temperature_39

        Returns:
            float: the value of `temperature_39` or None if not set
        """
        return self["Temperature 39"]

    @temperature_39.setter
    def temperature_39(self, value=None):
        """  Corresponds to IDD Field `Temperature 39`

        Args:
            value (float): value for IDD Field `Temperature 39`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 39"] = value

    @property
    def temperature_40(self):
        """Get temperature_40

        Returns:
            float: the value of `temperature_40` or None if not set
        """
        return self["Temperature 40"]

    @temperature_40.setter
    def temperature_40(self, value=None):
        """  Corresponds to IDD Field `Temperature 40`

        Args:
            value (float): value for IDD Field `Temperature 40`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 40"] = value

    @property
    def temperature_41(self):
        """Get temperature_41

        Returns:
            float: the value of `temperature_41` or None if not set
        """
        return self["Temperature 41"]

    @temperature_41.setter
    def temperature_41(self, value=None):
        """  Corresponds to IDD Field `Temperature 41`

        Args:
            value (float): value for IDD Field `Temperature 41`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 41"] = value

    @property
    def temperature_42(self):
        """Get temperature_42

        Returns:
            float: the value of `temperature_42` or None if not set
        """
        return self["Temperature 42"]

    @temperature_42.setter
    def temperature_42(self, value=None):
        """  Corresponds to IDD Field `Temperature 42`

        Args:
            value (float): value for IDD Field `Temperature 42`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 42"] = value

    @property
    def temperature_43(self):
        """Get temperature_43

        Returns:
            float: the value of `temperature_43` or None if not set
        """
        return self["Temperature 43"]

    @temperature_43.setter
    def temperature_43(self, value=None):
        """  Corresponds to IDD Field `Temperature 43`

        Args:
            value (float): value for IDD Field `Temperature 43`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 43"] = value

    @property
    def temperature_44(self):
        """Get temperature_44

        Returns:
            float: the value of `temperature_44` or None if not set
        """
        return self["Temperature 44"]

    @temperature_44.setter
    def temperature_44(self, value=None):
        """  Corresponds to IDD Field `Temperature 44`

        Args:
            value (float): value for IDD Field `Temperature 44`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 44"] = value

    @property
    def temperature_45(self):
        """Get temperature_45

        Returns:
            float: the value of `temperature_45` or None if not set
        """
        return self["Temperature 45"]

    @temperature_45.setter
    def temperature_45(self, value=None):
        """  Corresponds to IDD Field `Temperature 45`

        Args:
            value (float): value for IDD Field `Temperature 45`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 45"] = value

    @property
    def temperature_46(self):
        """Get temperature_46

        Returns:
            float: the value of `temperature_46` or None if not set
        """
        return self["Temperature 46"]

    @temperature_46.setter
    def temperature_46(self, value=None):
        """  Corresponds to IDD Field `Temperature 46`

        Args:
            value (float): value for IDD Field `Temperature 46`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 46"] = value

    @property
    def temperature_47(self):
        """Get temperature_47

        Returns:
            float: the value of `temperature_47` or None if not set
        """
        return self["Temperature 47"]

    @temperature_47.setter
    def temperature_47(self, value=None):
        """  Corresponds to IDD Field `Temperature 47`

        Args:
            value (float): value for IDD Field `Temperature 47`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 47"] = value

    @property
    def temperature_48(self):
        """Get temperature_48

        Returns:
            float: the value of `temperature_48` or None if not set
        """
        return self["Temperature 48"]

    @temperature_48.setter
    def temperature_48(self, value=None):
        """  Corresponds to IDD Field `Temperature 48`

        Args:
            value (float): value for IDD Field `Temperature 48`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 48"] = value

    @property
    def temperature_49(self):
        """Get temperature_49

        Returns:
            float: the value of `temperature_49` or None if not set
        """
        return self["Temperature 49"]

    @temperature_49.setter
    def temperature_49(self, value=None):
        """  Corresponds to IDD Field `Temperature 49`

        Args:
            value (float): value for IDD Field `Temperature 49`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 49"] = value

    @property
    def temperature_50(self):
        """Get temperature_50

        Returns:
            float: the value of `temperature_50` or None if not set
        """
        return self["Temperature 50"]

    @temperature_50.setter
    def temperature_50(self, value=None):
        """  Corresponds to IDD Field `Temperature 50`

        Args:
            value (float): value for IDD Field `Temperature 50`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 50"] = value

    @property
    def temperature_51(self):
        """Get temperature_51

        Returns:
            float: the value of `temperature_51` or None if not set
        """
        return self["Temperature 51"]

    @temperature_51.setter
    def temperature_51(self, value=None):
        """  Corresponds to IDD Field `Temperature 51`

        Args:
            value (float): value for IDD Field `Temperature 51`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 51"] = value

    @property
    def temperature_52(self):
        """Get temperature_52

        Returns:
            float: the value of `temperature_52` or None if not set
        """
        return self["Temperature 52"]

    @temperature_52.setter
    def temperature_52(self, value=None):
        """  Corresponds to IDD Field `Temperature 52`

        Args:
            value (float): value for IDD Field `Temperature 52`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 52"] = value

    @property
    def temperature_53(self):
        """Get temperature_53

        Returns:
            float: the value of `temperature_53` or None if not set
        """
        return self["Temperature 53"]

    @temperature_53.setter
    def temperature_53(self, value=None):
        """  Corresponds to IDD Field `Temperature 53`

        Args:
            value (float): value for IDD Field `Temperature 53`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 53"] = value

    @property
    def temperature_54(self):
        """Get temperature_54

        Returns:
            float: the value of `temperature_54` or None if not set
        """
        return self["Temperature 54"]

    @temperature_54.setter
    def temperature_54(self, value=None):
        """  Corresponds to IDD Field `Temperature 54`

        Args:
            value (float): value for IDD Field `Temperature 54`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 54"] = value

    @property
    def temperature_55(self):
        """Get temperature_55

        Returns:
            float: the value of `temperature_55` or None if not set
        """
        return self["Temperature 55"]

    @temperature_55.setter
    def temperature_55(self, value=None):
        """  Corresponds to IDD Field `Temperature 55`

        Args:
            value (float): value for IDD Field `Temperature 55`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 55"] = value

    @property
    def temperature_56(self):
        """Get temperature_56

        Returns:
            float: the value of `temperature_56` or None if not set
        """
        return self["Temperature 56"]

    @temperature_56.setter
    def temperature_56(self, value=None):
        """  Corresponds to IDD Field `Temperature 56`

        Args:
            value (float): value for IDD Field `Temperature 56`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 56"] = value

    @property
    def temperature_57(self):
        """Get temperature_57

        Returns:
            float: the value of `temperature_57` or None if not set
        """
        return self["Temperature 57"]

    @temperature_57.setter
    def temperature_57(self, value=None):
        """  Corresponds to IDD Field `Temperature 57`

        Args:
            value (float): value for IDD Field `Temperature 57`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 57"] = value

    @property
    def temperature_58(self):
        """Get temperature_58

        Returns:
            float: the value of `temperature_58` or None if not set
        """
        return self["Temperature 58"]

    @temperature_58.setter
    def temperature_58(self, value=None):
        """  Corresponds to IDD Field `Temperature 58`

        Args:
            value (float): value for IDD Field `Temperature 58`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 58"] = value

    @property
    def temperature_59(self):
        """Get temperature_59

        Returns:
            float: the value of `temperature_59` or None if not set
        """
        return self["Temperature 59"]

    @temperature_59.setter
    def temperature_59(self, value=None):
        """  Corresponds to IDD Field `Temperature 59`

        Args:
            value (float): value for IDD Field `Temperature 59`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 59"] = value

    @property
    def temperature_60(self):
        """Get temperature_60

        Returns:
            float: the value of `temperature_60` or None if not set
        """
        return self["Temperature 60"]

    @temperature_60.setter
    def temperature_60(self, value=None):
        """  Corresponds to IDD Field `Temperature 60`

        Args:
            value (float): value for IDD Field `Temperature 60`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 60"] = value

    @property
    def temperature_61(self):
        """Get temperature_61

        Returns:
            float: the value of `temperature_61` or None if not set
        """
        return self["Temperature 61"]

    @temperature_61.setter
    def temperature_61(self, value=None):
        """  Corresponds to IDD Field `Temperature 61`

        Args:
            value (float): value for IDD Field `Temperature 61`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 61"] = value

    @property
    def temperature_62(self):
        """Get temperature_62

        Returns:
            float: the value of `temperature_62` or None if not set
        """
        return self["Temperature 62"]

    @temperature_62.setter
    def temperature_62(self, value=None):
        """  Corresponds to IDD Field `Temperature 62`

        Args:
            value (float): value for IDD Field `Temperature 62`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 62"] = value

    @property
    def temperature_63(self):
        """Get temperature_63

        Returns:
            float: the value of `temperature_63` or None if not set
        """
        return self["Temperature 63"]

    @temperature_63.setter
    def temperature_63(self, value=None):
        """  Corresponds to IDD Field `Temperature 63`

        Args:
            value (float): value for IDD Field `Temperature 63`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 63"] = value

    @property
    def temperature_64(self):
        """Get temperature_64

        Returns:
            float: the value of `temperature_64` or None if not set
        """
        return self["Temperature 64"]

    @temperature_64.setter
    def temperature_64(self, value=None):
        """  Corresponds to IDD Field `Temperature 64`

        Args:
            value (float): value for IDD Field `Temperature 64`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 64"] = value

    @property
    def temperature_65(self):
        """Get temperature_65

        Returns:
            float: the value of `temperature_65` or None if not set
        """
        return self["Temperature 65"]

    @temperature_65.setter
    def temperature_65(self, value=None):
        """  Corresponds to IDD Field `Temperature 65`

        Args:
            value (float): value for IDD Field `Temperature 65`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 65"] = value

    @property
    def temperature_66(self):
        """Get temperature_66

        Returns:
            float: the value of `temperature_66` or None if not set
        """
        return self["Temperature 66"]

    @temperature_66.setter
    def temperature_66(self, value=None):
        """  Corresponds to IDD Field `Temperature 66`

        Args:
            value (float): value for IDD Field `Temperature 66`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 66"] = value

    @property
    def temperature_67(self):
        """Get temperature_67

        Returns:
            float: the value of `temperature_67` or None if not set
        """
        return self["Temperature 67"]

    @temperature_67.setter
    def temperature_67(self, value=None):
        """  Corresponds to IDD Field `Temperature 67`

        Args:
            value (float): value for IDD Field `Temperature 67`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 67"] = value

    @property
    def temperature_68(self):
        """Get temperature_68

        Returns:
            float: the value of `temperature_68` or None if not set
        """
        return self["Temperature 68"]

    @temperature_68.setter
    def temperature_68(self, value=None):
        """  Corresponds to IDD Field `Temperature 68`

        Args:
            value (float): value for IDD Field `Temperature 68`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 68"] = value

    @property
    def temperature_69(self):
        """Get temperature_69

        Returns:
            float: the value of `temperature_69` or None if not set
        """
        return self["Temperature 69"]

    @temperature_69.setter
    def temperature_69(self, value=None):
        """  Corresponds to IDD Field `Temperature 69`

        Args:
            value (float): value for IDD Field `Temperature 69`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 69"] = value

    @property
    def temperature_70(self):
        """Get temperature_70

        Returns:
            float: the value of `temperature_70` or None if not set
        """
        return self["Temperature 70"]

    @temperature_70.setter
    def temperature_70(self, value=None):
        """  Corresponds to IDD Field `Temperature 70`

        Args:
            value (float): value for IDD Field `Temperature 70`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 70"] = value

    @property
    def temperature_71(self):
        """Get temperature_71

        Returns:
            float: the value of `temperature_71` or None if not set
        """
        return self["Temperature 71"]

    @temperature_71.setter
    def temperature_71(self, value=None):
        """  Corresponds to IDD Field `Temperature 71`

        Args:
            value (float): value for IDD Field `Temperature 71`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 71"] = value

    @property
    def temperature_72(self):
        """Get temperature_72

        Returns:
            float: the value of `temperature_72` or None if not set
        """
        return self["Temperature 72"]

    @temperature_72.setter
    def temperature_72(self, value=None):
        """  Corresponds to IDD Field `Temperature 72`

        Args:
            value (float): value for IDD Field `Temperature 72`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 72"] = value

    @property
    def temperature_73(self):
        """Get temperature_73

        Returns:
            float: the value of `temperature_73` or None if not set
        """
        return self["Temperature 73"]

    @temperature_73.setter
    def temperature_73(self, value=None):
        """  Corresponds to IDD Field `Temperature 73`

        Args:
            value (float): value for IDD Field `Temperature 73`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 73"] = value

    @property
    def temperature_74(self):
        """Get temperature_74

        Returns:
            float: the value of `temperature_74` or None if not set
        """
        return self["Temperature 74"]

    @temperature_74.setter
    def temperature_74(self, value=None):
        """  Corresponds to IDD Field `Temperature 74`

        Args:
            value (float): value for IDD Field `Temperature 74`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 74"] = value

    @property
    def temperature_75(self):
        """Get temperature_75

        Returns:
            float: the value of `temperature_75` or None if not set
        """
        return self["Temperature 75"]

    @temperature_75.setter
    def temperature_75(self, value=None):
        """  Corresponds to IDD Field `Temperature 75`

        Args:
            value (float): value for IDD Field `Temperature 75`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 75"] = value

    @property
    def temperature_76(self):
        """Get temperature_76

        Returns:
            float: the value of `temperature_76` or None if not set
        """
        return self["Temperature 76"]

    @temperature_76.setter
    def temperature_76(self, value=None):
        """  Corresponds to IDD Field `Temperature 76`

        Args:
            value (float): value for IDD Field `Temperature 76`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 76"] = value

    @property
    def temperature_77(self):
        """Get temperature_77

        Returns:
            float: the value of `temperature_77` or None if not set
        """
        return self["Temperature 77"]

    @temperature_77.setter
    def temperature_77(self, value=None):
        """  Corresponds to IDD Field `Temperature 77`

        Args:
            value (float): value for IDD Field `Temperature 77`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 77"] = value

    @property
    def temperature_78(self):
        """Get temperature_78

        Returns:
            float: the value of `temperature_78` or None if not set
        """
        return self["Temperature 78"]

    @temperature_78.setter
    def temperature_78(self, value=None):
        """  Corresponds to IDD Field `Temperature 78`

        Args:
            value (float): value for IDD Field `Temperature 78`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 78"] = value

    @property
    def temperature_79(self):
        """Get temperature_79

        Returns:
            float: the value of `temperature_79` or None if not set
        """
        return self["Temperature 79"]

    @temperature_79.setter
    def temperature_79(self, value=None):
        """  Corresponds to IDD Field `Temperature 79`

        Args:
            value (float): value for IDD Field `Temperature 79`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 79"] = value

    @property
    def temperature_80(self):
        """Get temperature_80

        Returns:
            float: the value of `temperature_80` or None if not set
        """
        return self["Temperature 80"]

    @temperature_80.setter
    def temperature_80(self, value=None):
        """  Corresponds to IDD Field `Temperature 80`

        Args:
            value (float): value for IDD Field `Temperature 80`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 80"] = value

    @property
    def temperature_81(self):
        """Get temperature_81

        Returns:
            float: the value of `temperature_81` or None if not set
        """
        return self["Temperature 81"]

    @temperature_81.setter
    def temperature_81(self, value=None):
        """  Corresponds to IDD Field `Temperature 81`

        Args:
            value (float): value for IDD Field `Temperature 81`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 81"] = value

    @property
    def temperature_82(self):
        """Get temperature_82

        Returns:
            float: the value of `temperature_82` or None if not set
        """
        return self["Temperature 82"]

    @temperature_82.setter
    def temperature_82(self, value=None):
        """  Corresponds to IDD Field `Temperature 82`

        Args:
            value (float): value for IDD Field `Temperature 82`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 82"] = value

    @property
    def temperature_83(self):
        """Get temperature_83

        Returns:
            float: the value of `temperature_83` or None if not set
        """
        return self["Temperature 83"]

    @temperature_83.setter
    def temperature_83(self, value=None):
        """  Corresponds to IDD Field `Temperature 83`

        Args:
            value (float): value for IDD Field `Temperature 83`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 83"] = value

    @property
    def temperature_84(self):
        """Get temperature_84

        Returns:
            float: the value of `temperature_84` or None if not set
        """
        return self["Temperature 84"]

    @temperature_84.setter
    def temperature_84(self, value=None):
        """  Corresponds to IDD Field `Temperature 84`

        Args:
            value (float): value for IDD Field `Temperature 84`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 84"] = value

    @property
    def temperature_85(self):
        """Get temperature_85

        Returns:
            float: the value of `temperature_85` or None if not set
        """
        return self["Temperature 85"]

    @temperature_85.setter
    def temperature_85(self, value=None):
        """  Corresponds to IDD Field `Temperature 85`

        Args:
            value (float): value for IDD Field `Temperature 85`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 85"] = value

    @property
    def temperature_86(self):
        """Get temperature_86

        Returns:
            float: the value of `temperature_86` or None if not set
        """
        return self["Temperature 86"]

    @temperature_86.setter
    def temperature_86(self, value=None):
        """  Corresponds to IDD Field `Temperature 86`

        Args:
            value (float): value for IDD Field `Temperature 86`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 86"] = value

    @property
    def temperature_87(self):
        """Get temperature_87

        Returns:
            float: the value of `temperature_87` or None if not set
        """
        return self["Temperature 87"]

    @temperature_87.setter
    def temperature_87(self, value=None):
        """  Corresponds to IDD Field `Temperature 87`

        Args:
            value (float): value for IDD Field `Temperature 87`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 87"] = value

    @property
    def temperature_88(self):
        """Get temperature_88

        Returns:
            float: the value of `temperature_88` or None if not set
        """
        return self["Temperature 88"]

    @temperature_88.setter
    def temperature_88(self, value=None):
        """  Corresponds to IDD Field `Temperature 88`

        Args:
            value (float): value for IDD Field `Temperature 88`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 88"] = value

    @property
    def temperature_89(self):
        """Get temperature_89

        Returns:
            float: the value of `temperature_89` or None if not set
        """
        return self["Temperature 89"]

    @temperature_89.setter
    def temperature_89(self, value=None):
        """  Corresponds to IDD Field `Temperature 89`

        Args:
            value (float): value for IDD Field `Temperature 89`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 89"] = value

    @property
    def temperature_90(self):
        """Get temperature_90

        Returns:
            float: the value of `temperature_90` or None if not set
        """
        return self["Temperature 90"]

    @temperature_90.setter
    def temperature_90(self, value=None):
        """  Corresponds to IDD Field `Temperature 90`

        Args:
            value (float): value for IDD Field `Temperature 90`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 90"] = value

    @property
    def temperature_91(self):
        """Get temperature_91

        Returns:
            float: the value of `temperature_91` or None if not set
        """
        return self["Temperature 91"]

    @temperature_91.setter
    def temperature_91(self, value=None):
        """  Corresponds to IDD Field `Temperature 91`

        Args:
            value (float): value for IDD Field `Temperature 91`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 91"] = value

    @property
    def temperature_92(self):
        """Get temperature_92

        Returns:
            float: the value of `temperature_92` or None if not set
        """
        return self["Temperature 92"]

    @temperature_92.setter
    def temperature_92(self, value=None):
        """  Corresponds to IDD Field `Temperature 92`

        Args:
            value (float): value for IDD Field `Temperature 92`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 92"] = value

    @property
    def temperature_93(self):
        """Get temperature_93

        Returns:
            float: the value of `temperature_93` or None if not set
        """
        return self["Temperature 93"]

    @temperature_93.setter
    def temperature_93(self, value=None):
        """  Corresponds to IDD Field `Temperature 93`

        Args:
            value (float): value for IDD Field `Temperature 93`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 93"] = value

    @property
    def temperature_94(self):
        """Get temperature_94

        Returns:
            float: the value of `temperature_94` or None if not set
        """
        return self["Temperature 94"]

    @temperature_94.setter
    def temperature_94(self, value=None):
        """  Corresponds to IDD Field `Temperature 94`

        Args:
            value (float): value for IDD Field `Temperature 94`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 94"] = value

    @property
    def temperature_95(self):
        """Get temperature_95

        Returns:
            float: the value of `temperature_95` or None if not set
        """
        return self["Temperature 95"]

    @temperature_95.setter
    def temperature_95(self, value=None):
        """  Corresponds to IDD Field `Temperature 95`

        Args:
            value (float): value for IDD Field `Temperature 95`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 95"] = value

    @property
    def temperature_96(self):
        """Get temperature_96

        Returns:
            float: the value of `temperature_96` or None if not set
        """
        return self["Temperature 96"]

    @temperature_96.setter
    def temperature_96(self, value=None):
        """  Corresponds to IDD Field `Temperature 96`

        Args:
            value (float): value for IDD Field `Temperature 96`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 96"] = value

    @property
    def temperature_97(self):
        """Get temperature_97

        Returns:
            float: the value of `temperature_97` or None if not set
        """
        return self["Temperature 97"]

    @temperature_97.setter
    def temperature_97(self, value=None):
        """  Corresponds to IDD Field `Temperature 97`

        Args:
            value (float): value for IDD Field `Temperature 97`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 97"] = value

    @property
    def temperature_98(self):
        """Get temperature_98

        Returns:
            float: the value of `temperature_98` or None if not set
        """
        return self["Temperature 98"]

    @temperature_98.setter
    def temperature_98(self, value=None):
        """  Corresponds to IDD Field `Temperature 98`

        Args:
            value (float): value for IDD Field `Temperature 98`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 98"] = value

    @property
    def temperature_99(self):
        """Get temperature_99

        Returns:
            float: the value of `temperature_99` or None if not set
        """
        return self["Temperature 99"]

    @temperature_99.setter
    def temperature_99(self, value=None):
        """  Corresponds to IDD Field `Temperature 99`

        Args:
            value (float): value for IDD Field `Temperature 99`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 99"] = value

    @property
    def temperature_100(self):
        """Get temperature_100

        Returns:
            float: the value of `temperature_100` or None if not set
        """
        return self["Temperature 100"]

    @temperature_100.setter
    def temperature_100(self, value=None):
        """  Corresponds to IDD Field `Temperature 100`

        Args:
            value (float): value for IDD Field `Temperature 100`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 100"] = value

    @property
    def temperature_101(self):
        """Get temperature_101

        Returns:
            float: the value of `temperature_101` or None if not set
        """
        return self["Temperature 101"]

    @temperature_101.setter
    def temperature_101(self, value=None):
        """  Corresponds to IDD Field `Temperature 101`

        Args:
            value (float): value for IDD Field `Temperature 101`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 101"] = value

    @property
    def temperature_102(self):
        """Get temperature_102

        Returns:
            float: the value of `temperature_102` or None if not set
        """
        return self["Temperature 102"]

    @temperature_102.setter
    def temperature_102(self, value=None):
        """  Corresponds to IDD Field `Temperature 102`

        Args:
            value (float): value for IDD Field `Temperature 102`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 102"] = value

    @property
    def temperature_103(self):
        """Get temperature_103

        Returns:
            float: the value of `temperature_103` or None if not set
        """
        return self["Temperature 103"]

    @temperature_103.setter
    def temperature_103(self, value=None):
        """  Corresponds to IDD Field `Temperature 103`

        Args:
            value (float): value for IDD Field `Temperature 103`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 103"] = value

    @property
    def temperature_104(self):
        """Get temperature_104

        Returns:
            float: the value of `temperature_104` or None if not set
        """
        return self["Temperature 104"]

    @temperature_104.setter
    def temperature_104(self, value=None):
        """  Corresponds to IDD Field `Temperature 104`

        Args:
            value (float): value for IDD Field `Temperature 104`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 104"] = value

    @property
    def temperature_105(self):
        """Get temperature_105

        Returns:
            float: the value of `temperature_105` or None if not set
        """
        return self["Temperature 105"]

    @temperature_105.setter
    def temperature_105(self, value=None):
        """  Corresponds to IDD Field `Temperature 105`

        Args:
            value (float): value for IDD Field `Temperature 105`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 105"] = value

    @property
    def temperature_106(self):
        """Get temperature_106

        Returns:
            float: the value of `temperature_106` or None if not set
        """
        return self["Temperature 106"]

    @temperature_106.setter
    def temperature_106(self, value=None):
        """  Corresponds to IDD Field `Temperature 106`

        Args:
            value (float): value for IDD Field `Temperature 106`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 106"] = value

    @property
    def temperature_107(self):
        """Get temperature_107

        Returns:
            float: the value of `temperature_107` or None if not set
        """
        return self["Temperature 107"]

    @temperature_107.setter
    def temperature_107(self, value=None):
        """  Corresponds to IDD Field `Temperature 107`

        Args:
            value (float): value for IDD Field `Temperature 107`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 107"] = value

    @property
    def temperature_108(self):
        """Get temperature_108

        Returns:
            float: the value of `temperature_108` or None if not set
        """
        return self["Temperature 108"]

    @temperature_108.setter
    def temperature_108(self, value=None):
        """  Corresponds to IDD Field `Temperature 108`

        Args:
            value (float): value for IDD Field `Temperature 108`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 108"] = value

    @property
    def temperature_109(self):
        """Get temperature_109

        Returns:
            float: the value of `temperature_109` or None if not set
        """
        return self["Temperature 109"]

    @temperature_109.setter
    def temperature_109(self, value=None):
        """  Corresponds to IDD Field `Temperature 109`

        Args:
            value (float): value for IDD Field `Temperature 109`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 109"] = value

    @property
    def temperature_110(self):
        """Get temperature_110

        Returns:
            float: the value of `temperature_110` or None if not set
        """
        return self["Temperature 110"]

    @temperature_110.setter
    def temperature_110(self, value=None):
        """  Corresponds to IDD Field `Temperature 110`

        Args:
            value (float): value for IDD Field `Temperature 110`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 110"] = value

    @property
    def temperature_111(self):
        """Get temperature_111

        Returns:
            float: the value of `temperature_111` or None if not set
        """
        return self["Temperature 111"]

    @temperature_111.setter
    def temperature_111(self, value=None):
        """  Corresponds to IDD Field `Temperature 111`

        Args:
            value (float): value for IDD Field `Temperature 111`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 111"] = value

    @property
    def temperature_112(self):
        """Get temperature_112

        Returns:
            float: the value of `temperature_112` or None if not set
        """
        return self["Temperature 112"]

    @temperature_112.setter
    def temperature_112(self, value=None):
        """  Corresponds to IDD Field `Temperature 112`

        Args:
            value (float): value for IDD Field `Temperature 112`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 112"] = value

    @property
    def temperature_113(self):
        """Get temperature_113

        Returns:
            float: the value of `temperature_113` or None if not set
        """
        return self["Temperature 113"]

    @temperature_113.setter
    def temperature_113(self, value=None):
        """  Corresponds to IDD Field `Temperature 113`

        Args:
            value (float): value for IDD Field `Temperature 113`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 113"] = value

    @property
    def temperature_114(self):
        """Get temperature_114

        Returns:
            float: the value of `temperature_114` or None if not set
        """
        return self["Temperature 114"]

    @temperature_114.setter
    def temperature_114(self, value=None):
        """  Corresponds to IDD Field `Temperature 114`

        Args:
            value (float): value for IDD Field `Temperature 114`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 114"] = value

    @property
    def temperature_115(self):
        """Get temperature_115

        Returns:
            float: the value of `temperature_115` or None if not set
        """
        return self["Temperature 115"]

    @temperature_115.setter
    def temperature_115(self, value=None):
        """  Corresponds to IDD Field `Temperature 115`

        Args:
            value (float): value for IDD Field `Temperature 115`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 115"] = value

    @property
    def temperature_116(self):
        """Get temperature_116

        Returns:
            float: the value of `temperature_116` or None if not set
        """
        return self["Temperature 116"]

    @temperature_116.setter
    def temperature_116(self, value=None):
        """  Corresponds to IDD Field `Temperature 116`

        Args:
            value (float): value for IDD Field `Temperature 116`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 116"] = value

    @property
    def temperature_117(self):
        """Get temperature_117

        Returns:
            float: the value of `temperature_117` or None if not set
        """
        return self["Temperature 117"]

    @temperature_117.setter
    def temperature_117(self, value=None):
        """  Corresponds to IDD Field `Temperature 117`

        Args:
            value (float): value for IDD Field `Temperature 117`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 117"] = value

    @property
    def temperature_118(self):
        """Get temperature_118

        Returns:
            float: the value of `temperature_118` or None if not set
        """
        return self["Temperature 118"]

    @temperature_118.setter
    def temperature_118(self, value=None):
        """  Corresponds to IDD Field `Temperature 118`

        Args:
            value (float): value for IDD Field `Temperature 118`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 118"] = value

    @property
    def temperature_119(self):
        """Get temperature_119

        Returns:
            float: the value of `temperature_119` or None if not set
        """
        return self["Temperature 119"]

    @temperature_119.setter
    def temperature_119(self, value=None):
        """  Corresponds to IDD Field `Temperature 119`

        Args:
            value (float): value for IDD Field `Temperature 119`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 119"] = value

    @property
    def temperature_120(self):
        """Get temperature_120

        Returns:
            float: the value of `temperature_120` or None if not set
        """
        return self["Temperature 120"]

    @temperature_120.setter
    def temperature_120(self, value=None):
        """  Corresponds to IDD Field `Temperature 120`

        Args:
            value (float): value for IDD Field `Temperature 120`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 120"] = value

    @property
    def temperature_121(self):
        """Get temperature_121

        Returns:
            float: the value of `temperature_121` or None if not set
        """
        return self["Temperature 121"]

    @temperature_121.setter
    def temperature_121(self, value=None):
        """  Corresponds to IDD Field `Temperature 121`

        Args:
            value (float): value for IDD Field `Temperature 121`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 121"] = value

    @property
    def temperature_122(self):
        """Get temperature_122

        Returns:
            float: the value of `temperature_122` or None if not set
        """
        return self["Temperature 122"]

    @temperature_122.setter
    def temperature_122(self, value=None):
        """  Corresponds to IDD Field `Temperature 122`

        Args:
            value (float): value for IDD Field `Temperature 122`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 122"] = value

    @property
    def temperature_123(self):
        """Get temperature_123

        Returns:
            float: the value of `temperature_123` or None if not set
        """
        return self["Temperature 123"]

    @temperature_123.setter
    def temperature_123(self, value=None):
        """  Corresponds to IDD Field `Temperature 123`

        Args:
            value (float): value for IDD Field `Temperature 123`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 123"] = value

    @property
    def temperature_124(self):
        """Get temperature_124

        Returns:
            float: the value of `temperature_124` or None if not set
        """
        return self["Temperature 124"]

    @temperature_124.setter
    def temperature_124(self, value=None):
        """  Corresponds to IDD Field `Temperature 124`

        Args:
            value (float): value for IDD Field `Temperature 124`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 124"] = value

    @property
    def temperature_125(self):
        """Get temperature_125

        Returns:
            float: the value of `temperature_125` or None if not set
        """
        return self["Temperature 125"]

    @temperature_125.setter
    def temperature_125(self, value=None):
        """  Corresponds to IDD Field `Temperature 125`

        Args:
            value (float): value for IDD Field `Temperature 125`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 125"] = value

    @property
    def temperature_126(self):
        """Get temperature_126

        Returns:
            float: the value of `temperature_126` or None if not set
        """
        return self["Temperature 126"]

    @temperature_126.setter
    def temperature_126(self, value=None):
        """  Corresponds to IDD Field `Temperature 126`

        Args:
            value (float): value for IDD Field `Temperature 126`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 126"] = value

    @property
    def temperature_127(self):
        """Get temperature_127

        Returns:
            float: the value of `temperature_127` or None if not set
        """
        return self["Temperature 127"]

    @temperature_127.setter
    def temperature_127(self, value=None):
        """  Corresponds to IDD Field `Temperature 127`

        Args:
            value (float): value for IDD Field `Temperature 127`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 127"] = value

    @property
    def temperature_128(self):
        """Get temperature_128

        Returns:
            float: the value of `temperature_128` or None if not set
        """
        return self["Temperature 128"]

    @temperature_128.setter
    def temperature_128(self, value=None):
        """  Corresponds to IDD Field `Temperature 128`

        Args:
            value (float): value for IDD Field `Temperature 128`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 128"] = value

    @property
    def temperature_129(self):
        """Get temperature_129

        Returns:
            float: the value of `temperature_129` or None if not set
        """
        return self["Temperature 129"]

    @temperature_129.setter
    def temperature_129(self, value=None):
        """  Corresponds to IDD Field `Temperature 129`

        Args:
            value (float): value for IDD Field `Temperature 129`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 129"] = value

    @property
    def temperature_130(self):
        """Get temperature_130

        Returns:
            float: the value of `temperature_130` or None if not set
        """
        return self["Temperature 130"]

    @temperature_130.setter
    def temperature_130(self, value=None):
        """  Corresponds to IDD Field `Temperature 130`

        Args:
            value (float): value for IDD Field `Temperature 130`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 130"] = value

    @property
    def temperature_131(self):
        """Get temperature_131

        Returns:
            float: the value of `temperature_131` or None if not set
        """
        return self["Temperature 131"]

    @temperature_131.setter
    def temperature_131(self, value=None):
        """  Corresponds to IDD Field `Temperature 131`

        Args:
            value (float): value for IDD Field `Temperature 131`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 131"] = value

    @property
    def temperature_132(self):
        """Get temperature_132

        Returns:
            float: the value of `temperature_132` or None if not set
        """
        return self["Temperature 132"]

    @temperature_132.setter
    def temperature_132(self, value=None):
        """  Corresponds to IDD Field `Temperature 132`

        Args:
            value (float): value for IDD Field `Temperature 132`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 132"] = value

    @property
    def temperature_133(self):
        """Get temperature_133

        Returns:
            float: the value of `temperature_133` or None if not set
        """
        return self["Temperature 133"]

    @temperature_133.setter
    def temperature_133(self, value=None):
        """  Corresponds to IDD Field `Temperature 133`

        Args:
            value (float): value for IDD Field `Temperature 133`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 133"] = value

    @property
    def temperature_134(self):
        """Get temperature_134

        Returns:
            float: the value of `temperature_134` or None if not set
        """
        return self["Temperature 134"]

    @temperature_134.setter
    def temperature_134(self, value=None):
        """  Corresponds to IDD Field `Temperature 134`

        Args:
            value (float): value for IDD Field `Temperature 134`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 134"] = value

    @property
    def temperature_135(self):
        """Get temperature_135

        Returns:
            float: the value of `temperature_135` or None if not set
        """
        return self["Temperature 135"]

    @temperature_135.setter
    def temperature_135(self, value=None):
        """  Corresponds to IDD Field `Temperature 135`

        Args:
            value (float): value for IDD Field `Temperature 135`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 135"] = value

    @property
    def temperature_136(self):
        """Get temperature_136

        Returns:
            float: the value of `temperature_136` or None if not set
        """
        return self["Temperature 136"]

    @temperature_136.setter
    def temperature_136(self, value=None):
        """  Corresponds to IDD Field `Temperature 136`

        Args:
            value (float): value for IDD Field `Temperature 136`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 136"] = value

    @property
    def temperature_137(self):
        """Get temperature_137

        Returns:
            float: the value of `temperature_137` or None if not set
        """
        return self["Temperature 137"]

    @temperature_137.setter
    def temperature_137(self, value=None):
        """  Corresponds to IDD Field `Temperature 137`

        Args:
            value (float): value for IDD Field `Temperature 137`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 137"] = value

    @property
    def temperature_138(self):
        """Get temperature_138

        Returns:
            float: the value of `temperature_138` or None if not set
        """
        return self["Temperature 138"]

    @temperature_138.setter
    def temperature_138(self, value=None):
        """  Corresponds to IDD Field `Temperature 138`

        Args:
            value (float): value for IDD Field `Temperature 138`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 138"] = value

    @property
    def temperature_139(self):
        """Get temperature_139

        Returns:
            float: the value of `temperature_139` or None if not set
        """
        return self["Temperature 139"]

    @temperature_139.setter
    def temperature_139(self, value=None):
        """  Corresponds to IDD Field `Temperature 139`

        Args:
            value (float): value for IDD Field `Temperature 139`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 139"] = value

    @property
    def temperature_140(self):
        """Get temperature_140

        Returns:
            float: the value of `temperature_140` or None if not set
        """
        return self["Temperature 140"]

    @temperature_140.setter
    def temperature_140(self, value=None):
        """  Corresponds to IDD Field `Temperature 140`

        Args:
            value (float): value for IDD Field `Temperature 140`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 140"] = value

    @property
    def temperature_141(self):
        """Get temperature_141

        Returns:
            float: the value of `temperature_141` or None if not set
        """
        return self["Temperature 141"]

    @temperature_141.setter
    def temperature_141(self, value=None):
        """  Corresponds to IDD Field `Temperature 141`

        Args:
            value (float): value for IDD Field `Temperature 141`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 141"] = value

    @property
    def temperature_142(self):
        """Get temperature_142

        Returns:
            float: the value of `temperature_142` or None if not set
        """
        return self["Temperature 142"]

    @temperature_142.setter
    def temperature_142(self, value=None):
        """  Corresponds to IDD Field `Temperature 142`

        Args:
            value (float): value for IDD Field `Temperature 142`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 142"] = value

    @property
    def temperature_143(self):
        """Get temperature_143

        Returns:
            float: the value of `temperature_143` or None if not set
        """
        return self["Temperature 143"]

    @temperature_143.setter
    def temperature_143(self, value=None):
        """  Corresponds to IDD Field `Temperature 143`

        Args:
            value (float): value for IDD Field `Temperature 143`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 143"] = value

    @property
    def temperature_144(self):
        """Get temperature_144

        Returns:
            float: the value of `temperature_144` or None if not set
        """
        return self["Temperature 144"]

    @temperature_144.setter
    def temperature_144(self, value=None):
        """  Corresponds to IDD Field `Temperature 144`

        Args:
            value (float): value for IDD Field `Temperature 144`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 144"] = value

    @property
    def temperature_145(self):
        """Get temperature_145

        Returns:
            float: the value of `temperature_145` or None if not set
        """
        return self["Temperature 145"]

    @temperature_145.setter
    def temperature_145(self, value=None):
        """  Corresponds to IDD Field `Temperature 145`

        Args:
            value (float): value for IDD Field `Temperature 145`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 145"] = value

    @property
    def temperature_146(self):
        """Get temperature_146

        Returns:
            float: the value of `temperature_146` or None if not set
        """
        return self["Temperature 146"]

    @temperature_146.setter
    def temperature_146(self, value=None):
        """  Corresponds to IDD Field `Temperature 146`

        Args:
            value (float): value for IDD Field `Temperature 146`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 146"] = value

    @property
    def temperature_147(self):
        """Get temperature_147

        Returns:
            float: the value of `temperature_147` or None if not set
        """
        return self["Temperature 147"]

    @temperature_147.setter
    def temperature_147(self, value=None):
        """  Corresponds to IDD Field `Temperature 147`

        Args:
            value (float): value for IDD Field `Temperature 147`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 147"] = value

    @property
    def temperature_148(self):
        """Get temperature_148

        Returns:
            float: the value of `temperature_148` or None if not set
        """
        return self["Temperature 148"]

    @temperature_148.setter
    def temperature_148(self, value=None):
        """  Corresponds to IDD Field `Temperature 148`

        Args:
            value (float): value for IDD Field `Temperature 148`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 148"] = value

    @property
    def temperature_149(self):
        """Get temperature_149

        Returns:
            float: the value of `temperature_149` or None if not set
        """
        return self["Temperature 149"]

    @temperature_149.setter
    def temperature_149(self, value=None):
        """  Corresponds to IDD Field `Temperature 149`

        Args:
            value (float): value for IDD Field `Temperature 149`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 149"] = value

    @property
    def temperature_150(self):
        """Get temperature_150

        Returns:
            float: the value of `temperature_150` or None if not set
        """
        return self["Temperature 150"]

    @temperature_150.setter
    def temperature_150(self, value=None):
        """  Corresponds to IDD Field `Temperature 150`

        Args:
            value (float): value for IDD Field `Temperature 150`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 150"] = value

    @property
    def temperature_151(self):
        """Get temperature_151

        Returns:
            float: the value of `temperature_151` or None if not set
        """
        return self["Temperature 151"]

    @temperature_151.setter
    def temperature_151(self, value=None):
        """  Corresponds to IDD Field `Temperature 151`

        Args:
            value (float): value for IDD Field `Temperature 151`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 151"] = value

    @property
    def temperature_152(self):
        """Get temperature_152

        Returns:
            float: the value of `temperature_152` or None if not set
        """
        return self["Temperature 152"]

    @temperature_152.setter
    def temperature_152(self, value=None):
        """  Corresponds to IDD Field `Temperature 152`

        Args:
            value (float): value for IDD Field `Temperature 152`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 152"] = value

    @property
    def temperature_153(self):
        """Get temperature_153

        Returns:
            float: the value of `temperature_153` or None if not set
        """
        return self["Temperature 153"]

    @temperature_153.setter
    def temperature_153(self, value=None):
        """  Corresponds to IDD Field `Temperature 153`

        Args:
            value (float): value for IDD Field `Temperature 153`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 153"] = value

    @property
    def temperature_154(self):
        """Get temperature_154

        Returns:
            float: the value of `temperature_154` or None if not set
        """
        return self["Temperature 154"]

    @temperature_154.setter
    def temperature_154(self, value=None):
        """  Corresponds to IDD Field `Temperature 154`

        Args:
            value (float): value for IDD Field `Temperature 154`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 154"] = value

    @property
    def temperature_155(self):
        """Get temperature_155

        Returns:
            float: the value of `temperature_155` or None if not set
        """
        return self["Temperature 155"]

    @temperature_155.setter
    def temperature_155(self, value=None):
        """  Corresponds to IDD Field `Temperature 155`

        Args:
            value (float): value for IDD Field `Temperature 155`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 155"] = value

    @property
    def temperature_156(self):
        """Get temperature_156

        Returns:
            float: the value of `temperature_156` or None if not set
        """
        return self["Temperature 156"]

    @temperature_156.setter
    def temperature_156(self, value=None):
        """  Corresponds to IDD Field `Temperature 156`

        Args:
            value (float): value for IDD Field `Temperature 156`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 156"] = value

    @property
    def temperature_157(self):
        """Get temperature_157

        Returns:
            float: the value of `temperature_157` or None if not set
        """
        return self["Temperature 157"]

    @temperature_157.setter
    def temperature_157(self, value=None):
        """  Corresponds to IDD Field `Temperature 157`

        Args:
            value (float): value for IDD Field `Temperature 157`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 157"] = value

    @property
    def temperature_158(self):
        """Get temperature_158

        Returns:
            float: the value of `temperature_158` or None if not set
        """
        return self["Temperature 158"]

    @temperature_158.setter
    def temperature_158(self, value=None):
        """  Corresponds to IDD Field `Temperature 158`

        Args:
            value (float): value for IDD Field `Temperature 158`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 158"] = value

    @property
    def temperature_159(self):
        """Get temperature_159

        Returns:
            float: the value of `temperature_159` or None if not set
        """
        return self["Temperature 159"]

    @temperature_159.setter
    def temperature_159(self, value=None):
        """  Corresponds to IDD Field `Temperature 159`

        Args:
            value (float): value for IDD Field `Temperature 159`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 159"] = value

    @property
    def temperature_160(self):
        """Get temperature_160

        Returns:
            float: the value of `temperature_160` or None if not set
        """
        return self["Temperature 160"]

    @temperature_160.setter
    def temperature_160(self, value=None):
        """  Corresponds to IDD Field `Temperature 160`

        Args:
            value (float): value for IDD Field `Temperature 160`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 160"] = value

    @property
    def temperature_161(self):
        """Get temperature_161

        Returns:
            float: the value of `temperature_161` or None if not set
        """
        return self["Temperature 161"]

    @temperature_161.setter
    def temperature_161(self, value=None):
        """  Corresponds to IDD Field `Temperature 161`

        Args:
            value (float): value for IDD Field `Temperature 161`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 161"] = value

    @property
    def temperature_162(self):
        """Get temperature_162

        Returns:
            float: the value of `temperature_162` or None if not set
        """
        return self["Temperature 162"]

    @temperature_162.setter
    def temperature_162(self, value=None):
        """  Corresponds to IDD Field `Temperature 162`

        Args:
            value (float): value for IDD Field `Temperature 162`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 162"] = value

    @property
    def temperature_163(self):
        """Get temperature_163

        Returns:
            float: the value of `temperature_163` or None if not set
        """
        return self["Temperature 163"]

    @temperature_163.setter
    def temperature_163(self, value=None):
        """  Corresponds to IDD Field `Temperature 163`

        Args:
            value (float): value for IDD Field `Temperature 163`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 163"] = value

    @property
    def temperature_164(self):
        """Get temperature_164

        Returns:
            float: the value of `temperature_164` or None if not set
        """
        return self["Temperature 164"]

    @temperature_164.setter
    def temperature_164(self, value=None):
        """  Corresponds to IDD Field `Temperature 164`

        Args:
            value (float): value for IDD Field `Temperature 164`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 164"] = value

    @property
    def temperature_165(self):
        """Get temperature_165

        Returns:
            float: the value of `temperature_165` or None if not set
        """
        return self["Temperature 165"]

    @temperature_165.setter
    def temperature_165(self, value=None):
        """  Corresponds to IDD Field `Temperature 165`

        Args:
            value (float): value for IDD Field `Temperature 165`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 165"] = value

    @property
    def temperature_166(self):
        """Get temperature_166

        Returns:
            float: the value of `temperature_166` or None if not set
        """
        return self["Temperature 166"]

    @temperature_166.setter
    def temperature_166(self, value=None):
        """  Corresponds to IDD Field `Temperature 166`

        Args:
            value (float): value for IDD Field `Temperature 166`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 166"] = value

    @property
    def temperature_167(self):
        """Get temperature_167

        Returns:
            float: the value of `temperature_167` or None if not set
        """
        return self["Temperature 167"]

    @temperature_167.setter
    def temperature_167(self, value=None):
        """  Corresponds to IDD Field `Temperature 167`

        Args:
            value (float): value for IDD Field `Temperature 167`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 167"] = value

    @property
    def temperature_168(self):
        """Get temperature_168

        Returns:
            float: the value of `temperature_168` or None if not set
        """
        return self["Temperature 168"]

    @temperature_168.setter
    def temperature_168(self, value=None):
        """  Corresponds to IDD Field `Temperature 168`

        Args:
            value (float): value for IDD Field `Temperature 168`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 168"] = value

    @property
    def temperature_169(self):
        """Get temperature_169

        Returns:
            float: the value of `temperature_169` or None if not set
        """
        return self["Temperature 169"]

    @temperature_169.setter
    def temperature_169(self, value=None):
        """  Corresponds to IDD Field `Temperature 169`

        Args:
            value (float): value for IDD Field `Temperature 169`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 169"] = value

    @property
    def temperature_170(self):
        """Get temperature_170

        Returns:
            float: the value of `temperature_170` or None if not set
        """
        return self["Temperature 170"]

    @temperature_170.setter
    def temperature_170(self, value=None):
        """  Corresponds to IDD Field `Temperature 170`

        Args:
            value (float): value for IDD Field `Temperature 170`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 170"] = value

    @property
    def temperature_171(self):
        """Get temperature_171

        Returns:
            float: the value of `temperature_171` or None if not set
        """
        return self["Temperature 171"]

    @temperature_171.setter
    def temperature_171(self, value=None):
        """  Corresponds to IDD Field `Temperature 171`

        Args:
            value (float): value for IDD Field `Temperature 171`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 171"] = value

    @property
    def temperature_172(self):
        """Get temperature_172

        Returns:
            float: the value of `temperature_172` or None if not set
        """
        return self["Temperature 172"]

    @temperature_172.setter
    def temperature_172(self, value=None):
        """  Corresponds to IDD Field `Temperature 172`

        Args:
            value (float): value for IDD Field `Temperature 172`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 172"] = value

    @property
    def temperature_173(self):
        """Get temperature_173

        Returns:
            float: the value of `temperature_173` or None if not set
        """
        return self["Temperature 173"]

    @temperature_173.setter
    def temperature_173(self, value=None):
        """  Corresponds to IDD Field `Temperature 173`

        Args:
            value (float): value for IDD Field `Temperature 173`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 173"] = value

    @property
    def temperature_174(self):
        """Get temperature_174

        Returns:
            float: the value of `temperature_174` or None if not set
        """
        return self["Temperature 174"]

    @temperature_174.setter
    def temperature_174(self, value=None):
        """  Corresponds to IDD Field `Temperature 174`

        Args:
            value (float): value for IDD Field `Temperature 174`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 174"] = value

    @property
    def temperature_175(self):
        """Get temperature_175

        Returns:
            float: the value of `temperature_175` or None if not set
        """
        return self["Temperature 175"]

    @temperature_175.setter
    def temperature_175(self, value=None):
        """  Corresponds to IDD Field `Temperature 175`

        Args:
            value (float): value for IDD Field `Temperature 175`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 175"] = value

    @property
    def temperature_176(self):
        """Get temperature_176

        Returns:
            float: the value of `temperature_176` or None if not set
        """
        return self["Temperature 176"]

    @temperature_176.setter
    def temperature_176(self, value=None):
        """  Corresponds to IDD Field `Temperature 176`

        Args:
            value (float): value for IDD Field `Temperature 176`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 176"] = value

    @property
    def temperature_177(self):
        """Get temperature_177

        Returns:
            float: the value of `temperature_177` or None if not set
        """
        return self["Temperature 177"]

    @temperature_177.setter
    def temperature_177(self, value=None):
        """  Corresponds to IDD Field `Temperature 177`

        Args:
            value (float): value for IDD Field `Temperature 177`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 177"] = value

    @property
    def temperature_178(self):
        """Get temperature_178

        Returns:
            float: the value of `temperature_178` or None if not set
        """
        return self["Temperature 178"]

    @temperature_178.setter
    def temperature_178(self, value=None):
        """  Corresponds to IDD Field `Temperature 178`

        Args:
            value (float): value for IDD Field `Temperature 178`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 178"] = value

    @property
    def temperature_179(self):
        """Get temperature_179

        Returns:
            float: the value of `temperature_179` or None if not set
        """
        return self["Temperature 179"]

    @temperature_179.setter
    def temperature_179(self, value=None):
        """  Corresponds to IDD Field `Temperature 179`

        Args:
            value (float): value for IDD Field `Temperature 179`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 179"] = value

    @property
    def temperature_180(self):
        """Get temperature_180

        Returns:
            float: the value of `temperature_180` or None if not set
        """
        return self["Temperature 180"]

    @temperature_180.setter
    def temperature_180(self, value=None):
        """  Corresponds to IDD Field `Temperature 180`

        Args:
            value (float): value for IDD Field `Temperature 180`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 180"] = value

    @property
    def temperature_181(self):
        """Get temperature_181

        Returns:
            float: the value of `temperature_181` or None if not set
        """
        return self["Temperature 181"]

    @temperature_181.setter
    def temperature_181(self, value=None):
        """  Corresponds to IDD Field `Temperature 181`

        Args:
            value (float): value for IDD Field `Temperature 181`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 181"] = value

    @property
    def temperature_182(self):
        """Get temperature_182

        Returns:
            float: the value of `temperature_182` or None if not set
        """
        return self["Temperature 182"]

    @temperature_182.setter
    def temperature_182(self, value=None):
        """  Corresponds to IDD Field `Temperature 182`

        Args:
            value (float): value for IDD Field `Temperature 182`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 182"] = value

    @property
    def temperature_183(self):
        """Get temperature_183

        Returns:
            float: the value of `temperature_183` or None if not set
        """
        return self["Temperature 183"]

    @temperature_183.setter
    def temperature_183(self, value=None):
        """  Corresponds to IDD Field `Temperature 183`

        Args:
            value (float): value for IDD Field `Temperature 183`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 183"] = value

    @property
    def temperature_184(self):
        """Get temperature_184

        Returns:
            float: the value of `temperature_184` or None if not set
        """
        return self["Temperature 184"]

    @temperature_184.setter
    def temperature_184(self, value=None):
        """  Corresponds to IDD Field `Temperature 184`

        Args:
            value (float): value for IDD Field `Temperature 184`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 184"] = value

    @property
    def temperature_185(self):
        """Get temperature_185

        Returns:
            float: the value of `temperature_185` or None if not set
        """
        return self["Temperature 185"]

    @temperature_185.setter
    def temperature_185(self, value=None):
        """  Corresponds to IDD Field `Temperature 185`

        Args:
            value (float): value for IDD Field `Temperature 185`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 185"] = value

    @property
    def temperature_186(self):
        """Get temperature_186

        Returns:
            float: the value of `temperature_186` or None if not set
        """
        return self["Temperature 186"]

    @temperature_186.setter
    def temperature_186(self, value=None):
        """  Corresponds to IDD Field `Temperature 186`

        Args:
            value (float): value for IDD Field `Temperature 186`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 186"] = value

    @property
    def temperature_187(self):
        """Get temperature_187

        Returns:
            float: the value of `temperature_187` or None if not set
        """
        return self["Temperature 187"]

    @temperature_187.setter
    def temperature_187(self, value=None):
        """  Corresponds to IDD Field `Temperature 187`

        Args:
            value (float): value for IDD Field `Temperature 187`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 187"] = value

    @property
    def temperature_188(self):
        """Get temperature_188

        Returns:
            float: the value of `temperature_188` or None if not set
        """
        return self["Temperature 188"]

    @temperature_188.setter
    def temperature_188(self, value=None):
        """  Corresponds to IDD Field `Temperature 188`

        Args:
            value (float): value for IDD Field `Temperature 188`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 188"] = value

    @property
    def temperature_189(self):
        """Get temperature_189

        Returns:
            float: the value of `temperature_189` or None if not set
        """
        return self["Temperature 189"]

    @temperature_189.setter
    def temperature_189(self, value=None):
        """  Corresponds to IDD Field `Temperature 189`

        Args:
            value (float): value for IDD Field `Temperature 189`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 189"] = value

    @property
    def temperature_190(self):
        """Get temperature_190

        Returns:
            float: the value of `temperature_190` or None if not set
        """
        return self["Temperature 190"]

    @temperature_190.setter
    def temperature_190(self, value=None):
        """  Corresponds to IDD Field `Temperature 190`

        Args:
            value (float): value for IDD Field `Temperature 190`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 190"] = value

    @property
    def temperature_191(self):
        """Get temperature_191

        Returns:
            float: the value of `temperature_191` or None if not set
        """
        return self["Temperature 191"]

    @temperature_191.setter
    def temperature_191(self, value=None):
        """  Corresponds to IDD Field `Temperature 191`

        Args:
            value (float): value for IDD Field `Temperature 191`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 191"] = value

    @property
    def temperature_192(self):
        """Get temperature_192

        Returns:
            float: the value of `temperature_192` or None if not set
        """
        return self["Temperature 192"]

    @temperature_192.setter
    def temperature_192(self, value=None):
        """  Corresponds to IDD Field `Temperature 192`

        Args:
            value (float): value for IDD Field `Temperature 192`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 192"] = value

    @property
    def temperature_193(self):
        """Get temperature_193

        Returns:
            float: the value of `temperature_193` or None if not set
        """
        return self["Temperature 193"]

    @temperature_193.setter
    def temperature_193(self, value=None):
        """  Corresponds to IDD Field `Temperature 193`

        Args:
            value (float): value for IDD Field `Temperature 193`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 193"] = value

    @property
    def temperature_194(self):
        """Get temperature_194

        Returns:
            float: the value of `temperature_194` or None if not set
        """
        return self["Temperature 194"]

    @temperature_194.setter
    def temperature_194(self, value=None):
        """  Corresponds to IDD Field `Temperature 194`

        Args:
            value (float): value for IDD Field `Temperature 194`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 194"] = value

    @property
    def temperature_195(self):
        """Get temperature_195

        Returns:
            float: the value of `temperature_195` or None if not set
        """
        return self["Temperature 195"]

    @temperature_195.setter
    def temperature_195(self, value=None):
        """  Corresponds to IDD Field `Temperature 195`

        Args:
            value (float): value for IDD Field `Temperature 195`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 195"] = value

    @property
    def temperature_196(self):
        """Get temperature_196

        Returns:
            float: the value of `temperature_196` or None if not set
        """
        return self["Temperature 196"]

    @temperature_196.setter
    def temperature_196(self, value=None):
        """  Corresponds to IDD Field `Temperature 196`

        Args:
            value (float): value for IDD Field `Temperature 196`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 196"] = value

    @property
    def temperature_197(self):
        """Get temperature_197

        Returns:
            float: the value of `temperature_197` or None if not set
        """
        return self["Temperature 197"]

    @temperature_197.setter
    def temperature_197(self, value=None):
        """  Corresponds to IDD Field `Temperature 197`

        Args:
            value (float): value for IDD Field `Temperature 197`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 197"] = value

    @property
    def temperature_198(self):
        """Get temperature_198

        Returns:
            float: the value of `temperature_198` or None if not set
        """
        return self["Temperature 198"]

    @temperature_198.setter
    def temperature_198(self, value=None):
        """  Corresponds to IDD Field `Temperature 198`

        Args:
            value (float): value for IDD Field `Temperature 198`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 198"] = value

    @property
    def temperature_199(self):
        """Get temperature_199

        Returns:
            float: the value of `temperature_199` or None if not set
        """
        return self["Temperature 199"]

    @temperature_199.setter
    def temperature_199(self, value=None):
        """  Corresponds to IDD Field `Temperature 199`

        Args:
            value (float): value for IDD Field `Temperature 199`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 199"] = value

    @property
    def temperature_200(self):
        """Get temperature_200

        Returns:
            float: the value of `temperature_200` or None if not set
        """
        return self["Temperature 200"]

    @temperature_200.setter
    def temperature_200(self, value=None):
        """  Corresponds to IDD Field `Temperature 200`

        Args:
            value (float): value for IDD Field `Temperature 200`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 200"] = value

    @property
    def temperature_201(self):
        """Get temperature_201

        Returns:
            float: the value of `temperature_201` or None if not set
        """
        return self["Temperature 201"]

    @temperature_201.setter
    def temperature_201(self, value=None):
        """  Corresponds to IDD Field `Temperature 201`

        Args:
            value (float): value for IDD Field `Temperature 201`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 201"] = value

    @property
    def temperature_202(self):
        """Get temperature_202

        Returns:
            float: the value of `temperature_202` or None if not set
        """
        return self["Temperature 202"]

    @temperature_202.setter
    def temperature_202(self, value=None):
        """  Corresponds to IDD Field `Temperature 202`

        Args:
            value (float): value for IDD Field `Temperature 202`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 202"] = value

    @property
    def temperature_203(self):
        """Get temperature_203

        Returns:
            float: the value of `temperature_203` or None if not set
        """
        return self["Temperature 203"]

    @temperature_203.setter
    def temperature_203(self, value=None):
        """  Corresponds to IDD Field `Temperature 203`

        Args:
            value (float): value for IDD Field `Temperature 203`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 203"] = value

    @property
    def temperature_204(self):
        """Get temperature_204

        Returns:
            float: the value of `temperature_204` or None if not set
        """
        return self["Temperature 204"]

    @temperature_204.setter
    def temperature_204(self, value=None):
        """  Corresponds to IDD Field `Temperature 204`

        Args:
            value (float): value for IDD Field `Temperature 204`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 204"] = value

    @property
    def temperature_205(self):
        """Get temperature_205

        Returns:
            float: the value of `temperature_205` or None if not set
        """
        return self["Temperature 205"]

    @temperature_205.setter
    def temperature_205(self, value=None):
        """  Corresponds to IDD Field `Temperature 205`

        Args:
            value (float): value for IDD Field `Temperature 205`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 205"] = value

    @property
    def temperature_206(self):
        """Get temperature_206

        Returns:
            float: the value of `temperature_206` or None if not set
        """
        return self["Temperature 206"]

    @temperature_206.setter
    def temperature_206(self, value=None):
        """  Corresponds to IDD Field `Temperature 206`

        Args:
            value (float): value for IDD Field `Temperature 206`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 206"] = value

    @property
    def temperature_207(self):
        """Get temperature_207

        Returns:
            float: the value of `temperature_207` or None if not set
        """
        return self["Temperature 207"]

    @temperature_207.setter
    def temperature_207(self, value=None):
        """  Corresponds to IDD Field `Temperature 207`

        Args:
            value (float): value for IDD Field `Temperature 207`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 207"] = value

    @property
    def temperature_208(self):
        """Get temperature_208

        Returns:
            float: the value of `temperature_208` or None if not set
        """
        return self["Temperature 208"]

    @temperature_208.setter
    def temperature_208(self, value=None):
        """  Corresponds to IDD Field `Temperature 208`

        Args:
            value (float): value for IDD Field `Temperature 208`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 208"] = value

    @property
    def temperature_209(self):
        """Get temperature_209

        Returns:
            float: the value of `temperature_209` or None if not set
        """
        return self["Temperature 209"]

    @temperature_209.setter
    def temperature_209(self, value=None):
        """  Corresponds to IDD Field `Temperature 209`

        Args:
            value (float): value for IDD Field `Temperature 209`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 209"] = value

    @property
    def temperature_210(self):
        """Get temperature_210

        Returns:
            float: the value of `temperature_210` or None if not set
        """
        return self["Temperature 210"]

    @temperature_210.setter
    def temperature_210(self, value=None):
        """  Corresponds to IDD Field `Temperature 210`

        Args:
            value (float): value for IDD Field `Temperature 210`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 210"] = value

    @property
    def temperature_211(self):
        """Get temperature_211

        Returns:
            float: the value of `temperature_211` or None if not set
        """
        return self["Temperature 211"]

    @temperature_211.setter
    def temperature_211(self, value=None):
        """  Corresponds to IDD Field `Temperature 211`

        Args:
            value (float): value for IDD Field `Temperature 211`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 211"] = value

    @property
    def temperature_212(self):
        """Get temperature_212

        Returns:
            float: the value of `temperature_212` or None if not set
        """
        return self["Temperature 212"]

    @temperature_212.setter
    def temperature_212(self, value=None):
        """  Corresponds to IDD Field `Temperature 212`

        Args:
            value (float): value for IDD Field `Temperature 212`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 212"] = value

    @property
    def temperature_213(self):
        """Get temperature_213

        Returns:
            float: the value of `temperature_213` or None if not set
        """
        return self["Temperature 213"]

    @temperature_213.setter
    def temperature_213(self, value=None):
        """  Corresponds to IDD Field `Temperature 213`

        Args:
            value (float): value for IDD Field `Temperature 213`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 213"] = value

    @property
    def temperature_214(self):
        """Get temperature_214

        Returns:
            float: the value of `temperature_214` or None if not set
        """
        return self["Temperature 214"]

    @temperature_214.setter
    def temperature_214(self, value=None):
        """  Corresponds to IDD Field `Temperature 214`

        Args:
            value (float): value for IDD Field `Temperature 214`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 214"] = value

    @property
    def temperature_215(self):
        """Get temperature_215

        Returns:
            float: the value of `temperature_215` or None if not set
        """
        return self["Temperature 215"]

    @temperature_215.setter
    def temperature_215(self, value=None):
        """  Corresponds to IDD Field `Temperature 215`

        Args:
            value (float): value for IDD Field `Temperature 215`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 215"] = value

    @property
    def temperature_216(self):
        """Get temperature_216

        Returns:
            float: the value of `temperature_216` or None if not set
        """
        return self["Temperature 216"]

    @temperature_216.setter
    def temperature_216(self, value=None):
        """  Corresponds to IDD Field `Temperature 216`

        Args:
            value (float): value for IDD Field `Temperature 216`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 216"] = value

    @property
    def temperature_217(self):
        """Get temperature_217

        Returns:
            float: the value of `temperature_217` or None if not set
        """
        return self["Temperature 217"]

    @temperature_217.setter
    def temperature_217(self, value=None):
        """  Corresponds to IDD Field `Temperature 217`

        Args:
            value (float): value for IDD Field `Temperature 217`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 217"] = value

    @property
    def temperature_218(self):
        """Get temperature_218

        Returns:
            float: the value of `temperature_218` or None if not set
        """
        return self["Temperature 218"]

    @temperature_218.setter
    def temperature_218(self, value=None):
        """  Corresponds to IDD Field `Temperature 218`

        Args:
            value (float): value for IDD Field `Temperature 218`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 218"] = value

    @property
    def temperature_219(self):
        """Get temperature_219

        Returns:
            float: the value of `temperature_219` or None if not set
        """
        return self["Temperature 219"]

    @temperature_219.setter
    def temperature_219(self, value=None):
        """  Corresponds to IDD Field `Temperature 219`

        Args:
            value (float): value for IDD Field `Temperature 219`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 219"] = value

    @property
    def temperature_220(self):
        """Get temperature_220

        Returns:
            float: the value of `temperature_220` or None if not set
        """
        return self["Temperature 220"]

    @temperature_220.setter
    def temperature_220(self, value=None):
        """  Corresponds to IDD Field `Temperature 220`

        Args:
            value (float): value for IDD Field `Temperature 220`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 220"] = value

    @property
    def temperature_221(self):
        """Get temperature_221

        Returns:
            float: the value of `temperature_221` or None if not set
        """
        return self["Temperature 221"]

    @temperature_221.setter
    def temperature_221(self, value=None):
        """  Corresponds to IDD Field `Temperature 221`

        Args:
            value (float): value for IDD Field `Temperature 221`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 221"] = value

    @property
    def temperature_222(self):
        """Get temperature_222

        Returns:
            float: the value of `temperature_222` or None if not set
        """
        return self["Temperature 222"]

    @temperature_222.setter
    def temperature_222(self, value=None):
        """  Corresponds to IDD Field `Temperature 222`

        Args:
            value (float): value for IDD Field `Temperature 222`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 222"] = value

    @property
    def temperature_223(self):
        """Get temperature_223

        Returns:
            float: the value of `temperature_223` or None if not set
        """
        return self["Temperature 223"]

    @temperature_223.setter
    def temperature_223(self, value=None):
        """  Corresponds to IDD Field `Temperature 223`

        Args:
            value (float): value for IDD Field `Temperature 223`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 223"] = value

    @property
    def temperature_224(self):
        """Get temperature_224

        Returns:
            float: the value of `temperature_224` or None if not set
        """
        return self["Temperature 224"]

    @temperature_224.setter
    def temperature_224(self, value=None):
        """  Corresponds to IDD Field `Temperature 224`

        Args:
            value (float): value for IDD Field `Temperature 224`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 224"] = value

    @property
    def temperature_225(self):
        """Get temperature_225

        Returns:
            float: the value of `temperature_225` or None if not set
        """
        return self["Temperature 225"]

    @temperature_225.setter
    def temperature_225(self, value=None):
        """  Corresponds to IDD Field `Temperature 225`

        Args:
            value (float): value for IDD Field `Temperature 225`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 225"] = value

    @property
    def temperature_226(self):
        """Get temperature_226

        Returns:
            float: the value of `temperature_226` or None if not set
        """
        return self["Temperature 226"]

    @temperature_226.setter
    def temperature_226(self, value=None):
        """  Corresponds to IDD Field `Temperature 226`

        Args:
            value (float): value for IDD Field `Temperature 226`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 226"] = value

    @property
    def temperature_227(self):
        """Get temperature_227

        Returns:
            float: the value of `temperature_227` or None if not set
        """
        return self["Temperature 227"]

    @temperature_227.setter
    def temperature_227(self, value=None):
        """  Corresponds to IDD Field `Temperature 227`

        Args:
            value (float): value for IDD Field `Temperature 227`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 227"] = value

    @property
    def temperature_228(self):
        """Get temperature_228

        Returns:
            float: the value of `temperature_228` or None if not set
        """
        return self["Temperature 228"]

    @temperature_228.setter
    def temperature_228(self, value=None):
        """  Corresponds to IDD Field `Temperature 228`

        Args:
            value (float): value for IDD Field `Temperature 228`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 228"] = value

    @property
    def temperature_229(self):
        """Get temperature_229

        Returns:
            float: the value of `temperature_229` or None if not set
        """
        return self["Temperature 229"]

    @temperature_229.setter
    def temperature_229(self, value=None):
        """  Corresponds to IDD Field `Temperature 229`

        Args:
            value (float): value for IDD Field `Temperature 229`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 229"] = value

    @property
    def temperature_230(self):
        """Get temperature_230

        Returns:
            float: the value of `temperature_230` or None if not set
        """
        return self["Temperature 230"]

    @temperature_230.setter
    def temperature_230(self, value=None):
        """  Corresponds to IDD Field `Temperature 230`

        Args:
            value (float): value for IDD Field `Temperature 230`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 230"] = value

    @property
    def temperature_231(self):
        """Get temperature_231

        Returns:
            float: the value of `temperature_231` or None if not set
        """
        return self["Temperature 231"]

    @temperature_231.setter
    def temperature_231(self, value=None):
        """  Corresponds to IDD Field `Temperature 231`

        Args:
            value (float): value for IDD Field `Temperature 231`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 231"] = value

    @property
    def temperature_232(self):
        """Get temperature_232

        Returns:
            float: the value of `temperature_232` or None if not set
        """
        return self["Temperature 232"]

    @temperature_232.setter
    def temperature_232(self, value=None):
        """  Corresponds to IDD Field `Temperature 232`

        Args:
            value (float): value for IDD Field `Temperature 232`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 232"] = value

    @property
    def temperature_233(self):
        """Get temperature_233

        Returns:
            float: the value of `temperature_233` or None if not set
        """
        return self["Temperature 233"]

    @temperature_233.setter
    def temperature_233(self, value=None):
        """  Corresponds to IDD Field `Temperature 233`

        Args:
            value (float): value for IDD Field `Temperature 233`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 233"] = value

    @property
    def temperature_234(self):
        """Get temperature_234

        Returns:
            float: the value of `temperature_234` or None if not set
        """
        return self["Temperature 234"]

    @temperature_234.setter
    def temperature_234(self, value=None):
        """  Corresponds to IDD Field `Temperature 234`

        Args:
            value (float): value for IDD Field `Temperature 234`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 234"] = value

    @property
    def temperature_235(self):
        """Get temperature_235

        Returns:
            float: the value of `temperature_235` or None if not set
        """
        return self["Temperature 235"]

    @temperature_235.setter
    def temperature_235(self, value=None):
        """  Corresponds to IDD Field `Temperature 235`

        Args:
            value (float): value for IDD Field `Temperature 235`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 235"] = value

    @property
    def temperature_236(self):
        """Get temperature_236

        Returns:
            float: the value of `temperature_236` or None if not set
        """
        return self["Temperature 236"]

    @temperature_236.setter
    def temperature_236(self, value=None):
        """  Corresponds to IDD Field `Temperature 236`

        Args:
            value (float): value for IDD Field `Temperature 236`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 236"] = value

    @property
    def temperature_237(self):
        """Get temperature_237

        Returns:
            float: the value of `temperature_237` or None if not set
        """
        return self["Temperature 237"]

    @temperature_237.setter
    def temperature_237(self, value=None):
        """  Corresponds to IDD Field `Temperature 237`

        Args:
            value (float): value for IDD Field `Temperature 237`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 237"] = value

    @property
    def temperature_238(self):
        """Get temperature_238

        Returns:
            float: the value of `temperature_238` or None if not set
        """
        return self["Temperature 238"]

    @temperature_238.setter
    def temperature_238(self, value=None):
        """  Corresponds to IDD Field `Temperature 238`

        Args:
            value (float): value for IDD Field `Temperature 238`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 238"] = value

    @property
    def temperature_239(self):
        """Get temperature_239

        Returns:
            float: the value of `temperature_239` or None if not set
        """
        return self["Temperature 239"]

    @temperature_239.setter
    def temperature_239(self, value=None):
        """  Corresponds to IDD Field `Temperature 239`

        Args:
            value (float): value for IDD Field `Temperature 239`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 239"] = value

    @property
    def temperature_240(self):
        """Get temperature_240

        Returns:
            float: the value of `temperature_240` or None if not set
        """
        return self["Temperature 240"]

    @temperature_240.setter
    def temperature_240(self, value=None):
        """  Corresponds to IDD Field `Temperature 240`

        Args:
            value (float): value for IDD Field `Temperature 240`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 240"] = value

    @property
    def temperature_241(self):
        """Get temperature_241

        Returns:
            float: the value of `temperature_241` or None if not set
        """
        return self["Temperature 241"]

    @temperature_241.setter
    def temperature_241(self, value=None):
        """  Corresponds to IDD Field `Temperature 241`

        Args:
            value (float): value for IDD Field `Temperature 241`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 241"] = value

    @property
    def temperature_242(self):
        """Get temperature_242

        Returns:
            float: the value of `temperature_242` or None if not set
        """
        return self["Temperature 242"]

    @temperature_242.setter
    def temperature_242(self, value=None):
        """  Corresponds to IDD Field `Temperature 242`

        Args:
            value (float): value for IDD Field `Temperature 242`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 242"] = value

    @property
    def temperature_243(self):
        """Get temperature_243

        Returns:
            float: the value of `temperature_243` or None if not set
        """
        return self["Temperature 243"]

    @temperature_243.setter
    def temperature_243(self, value=None):
        """  Corresponds to IDD Field `Temperature 243`

        Args:
            value (float): value for IDD Field `Temperature 243`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 243"] = value

    @property
    def temperature_244(self):
        """Get temperature_244

        Returns:
            float: the value of `temperature_244` or None if not set
        """
        return self["Temperature 244"]

    @temperature_244.setter
    def temperature_244(self, value=None):
        """  Corresponds to IDD Field `Temperature 244`

        Args:
            value (float): value for IDD Field `Temperature 244`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 244"] = value

    @property
    def temperature_245(self):
        """Get temperature_245

        Returns:
            float: the value of `temperature_245` or None if not set
        """
        return self["Temperature 245"]

    @temperature_245.setter
    def temperature_245(self, value=None):
        """  Corresponds to IDD Field `Temperature 245`

        Args:
            value (float): value for IDD Field `Temperature 245`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 245"] = value

    @property
    def temperature_246(self):
        """Get temperature_246

        Returns:
            float: the value of `temperature_246` or None if not set
        """
        return self["Temperature 246"]

    @temperature_246.setter
    def temperature_246(self, value=None):
        """  Corresponds to IDD Field `Temperature 246`

        Args:
            value (float): value for IDD Field `Temperature 246`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 246"] = value

    @property
    def temperature_247(self):
        """Get temperature_247

        Returns:
            float: the value of `temperature_247` or None if not set
        """
        return self["Temperature 247"]

    @temperature_247.setter
    def temperature_247(self, value=None):
        """  Corresponds to IDD Field `Temperature 247`

        Args:
            value (float): value for IDD Field `Temperature 247`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 247"] = value

    @property
    def temperature_248(self):
        """Get temperature_248

        Returns:
            float: the value of `temperature_248` or None if not set
        """
        return self["Temperature 248"]

    @temperature_248.setter
    def temperature_248(self, value=None):
        """  Corresponds to IDD Field `Temperature 248`

        Args:
            value (float): value for IDD Field `Temperature 248`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 248"] = value

    @property
    def temperature_249(self):
        """Get temperature_249

        Returns:
            float: the value of `temperature_249` or None if not set
        """
        return self["Temperature 249"]

    @temperature_249.setter
    def temperature_249(self, value=None):
        """  Corresponds to IDD Field `Temperature 249`

        Args:
            value (float): value for IDD Field `Temperature 249`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 249"] = value

    @property
    def temperature_250(self):
        """Get temperature_250

        Returns:
            float: the value of `temperature_250` or None if not set
        """
        return self["Temperature 250"]

    @temperature_250.setter
    def temperature_250(self, value=None):
        """  Corresponds to IDD Field `Temperature 250`

        Args:
            value (float): value for IDD Field `Temperature 250`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature 250"] = value


class FluidPropertiesSaturated(DataObject):
    """ Corresponds to IDD object `FluidProperties:Saturated`
        fluid properties for the saturated region
    """
    schema = {'min-fields': 0, 'name': u'FluidProperties:Saturated', 'pyname': u'FluidPropertiesSaturated', 'format': None, 'fields': OrderedDict([(u'name', {'name': u'Name', 'pyname': u'name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fluid property type', {'name': u'Fluid Property Type', 'pyname': u'fluid_property_type', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Enthalpy', u'Density', u'SpecificHeat', u'Pressure'], 'autocalculatable': False, 'type': 'alpha'}), (u'fluid phase', {'name': u'Fluid Phase', 'pyname': u'fluid_phase', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Fluid', u'FluidGas'], 'autocalculatable': False, 'type': 'alpha'}), (u'temperature values name', {'name': u'Temperature Values Name', 'pyname': u'temperature_values_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'property value 1', {'name': u'Property Value 1', 'pyname': u'property_value_1', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 2', {'name': u'Property Value 2', 'pyname': u'property_value_2', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 3', {'name': u'Property Value 3', 'pyname': u'property_value_3', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 4', {'name': u'Property Value 4', 'pyname': u'property_value_4', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 5', {'name': u'Property Value 5', 'pyname': u'property_value_5', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 6', {'name': u'Property Value 6', 'pyname': u'property_value_6', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 7', {'name': u'Property Value 7', 'pyname': u'property_value_7', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 8', {'name': u'Property Value 8', 'pyname': u'property_value_8', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 9', {'name': u'Property Value 9', 'pyname': u'property_value_9', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 10', {'name': u'Property Value 10', 'pyname': u'property_value_10', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 11', {'name': u'Property Value 11', 'pyname': u'property_value_11', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 12', {'name': u'Property Value 12', 'pyname': u'property_value_12', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 13', {'name': u'Property Value 13', 'pyname': u'property_value_13', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 14', {'name': u'Property Value 14', 'pyname': u'property_value_14', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 15', {'name': u'Property Value 15', 'pyname': u'property_value_15', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 16', {'name': u'Property Value 16', 'pyname': u'property_value_16', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 17', {'name': u'Property Value 17', 'pyname': u'property_value_17', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 18', {'name': u'Property Value 18', 'pyname': u'property_value_18', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 19', {'name': u'Property Value 19', 'pyname': u'property_value_19', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 20', {'name': u'Property Value 20', 'pyname': u'property_value_20', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 21', {'name': u'Property Value 21', 'pyname': u'property_value_21', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 22', {'name': u'Property Value 22', 'pyname': u'property_value_22', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 23', {'name': u'Property Value 23', 'pyname': u'property_value_23', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 24', {'name': u'Property Value 24', 'pyname': u'property_value_24', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 25', {'name': u'Property Value 25', 'pyname': u'property_value_25', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 26', {'name': u'Property Value 26', 'pyname': u'property_value_26', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 27', {'name': u'Property Value 27', 'pyname': u'property_value_27', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 28', {'name': u'Property Value 28', 'pyname': u'property_value_28', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 29', {'name': u'Property Value 29', 'pyname': u'property_value_29', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 30', {'name': u'Property Value 30', 'pyname': u'property_value_30', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 31', {'name': u'Property Value 31', 'pyname': u'property_value_31', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 32', {'name': u'Property Value 32', 'pyname': u'property_value_32', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 33', {'name': u'Property Value 33', 'pyname': u'property_value_33', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 34', {'name': u'Property Value 34', 'pyname': u'property_value_34', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 35', {'name': u'Property Value 35', 'pyname': u'property_value_35', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 36', {'name': u'Property Value 36', 'pyname': u'property_value_36', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 37', {'name': u'Property Value 37', 'pyname': u'property_value_37', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 38', {'name': u'Property Value 38', 'pyname': u'property_value_38', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 39', {'name': u'Property Value 39', 'pyname': u'property_value_39', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 40', {'name': u'Property Value 40', 'pyname': u'property_value_40', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 41', {'name': u'Property Value 41', 'pyname': u'property_value_41', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 42', {'name': u'Property Value 42', 'pyname': u'property_value_42', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 43', {'name': u'Property Value 43', 'pyname': u'property_value_43', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 44', {'name': u'Property Value 44', 'pyname': u'property_value_44', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 45', {'name': u'Property Value 45', 'pyname': u'property_value_45', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 46', {'name': u'Property Value 46', 'pyname': u'property_value_46', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 47', {'name': u'Property Value 47', 'pyname': u'property_value_47', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 48', {'name': u'Property Value 48', 'pyname': u'property_value_48', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 49', {'name': u'Property Value 49', 'pyname': u'property_value_49', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 50', {'name': u'Property Value 50', 'pyname': u'property_value_50', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 51', {'name': u'Property Value 51', 'pyname': u'property_value_51', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 52', {'name': u'Property Value 52', 'pyname': u'property_value_52', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 53', {'name': u'Property Value 53', 'pyname': u'property_value_53', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 54', {'name': u'Property Value 54', 'pyname': u'property_value_54', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 55', {'name': u'Property Value 55', 'pyname': u'property_value_55', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 56', {'name': u'Property Value 56', 'pyname': u'property_value_56', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 57', {'name': u'Property Value 57', 'pyname': u'property_value_57', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 58', {'name': u'Property Value 58', 'pyname': u'property_value_58', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 59', {'name': u'Property Value 59', 'pyname': u'property_value_59', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 60', {'name': u'Property Value 60', 'pyname': u'property_value_60', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 61', {'name': u'Property Value 61', 'pyname': u'property_value_61', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 62', {'name': u'Property Value 62', 'pyname': u'property_value_62', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 63', {'name': u'Property Value 63', 'pyname': u'property_value_63', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 64', {'name': u'Property Value 64', 'pyname': u'property_value_64', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 65', {'name': u'Property Value 65', 'pyname': u'property_value_65', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 66', {'name': u'Property Value 66', 'pyname': u'property_value_66', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 67', {'name': u'Property Value 67', 'pyname': u'property_value_67', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 68', {'name': u'Property Value 68', 'pyname': u'property_value_68', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 69', {'name': u'Property Value 69', 'pyname': u'property_value_69', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 70', {'name': u'Property Value 70', 'pyname': u'property_value_70', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 71', {'name': u'Property Value 71', 'pyname': u'property_value_71', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 72', {'name': u'Property Value 72', 'pyname': u'property_value_72', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 73', {'name': u'Property Value 73', 'pyname': u'property_value_73', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 74', {'name': u'Property Value 74', 'pyname': u'property_value_74', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 75', {'name': u'Property Value 75', 'pyname': u'property_value_75', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 76', {'name': u'Property Value 76', 'pyname': u'property_value_76', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 77', {'name': u'Property Value 77', 'pyname': u'property_value_77', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 78', {'name': u'Property Value 78', 'pyname': u'property_value_78', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 79', {'name': u'Property Value 79', 'pyname': u'property_value_79', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 80', {'name': u'Property Value 80', 'pyname': u'property_value_80', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 81', {'name': u'Property Value 81', 'pyname': u'property_value_81', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 82', {'name': u'Property Value 82', 'pyname': u'property_value_82', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 83', {'name': u'Property Value 83', 'pyname': u'property_value_83', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 84', {'name': u'Property Value 84', 'pyname': u'property_value_84', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 85', {'name': u'Property Value 85', 'pyname': u'property_value_85', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 86', {'name': u'Property Value 86', 'pyname': u'property_value_86', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 87', {'name': u'Property Value 87', 'pyname': u'property_value_87', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 88', {'name': u'Property Value 88', 'pyname': u'property_value_88', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 89', {'name': u'Property Value 89', 'pyname': u'property_value_89', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 90', {'name': u'Property Value 90', 'pyname': u'property_value_90', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 91', {'name': u'Property Value 91', 'pyname': u'property_value_91', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 92', {'name': u'Property Value 92', 'pyname': u'property_value_92', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 93', {'name': u'Property Value 93', 'pyname': u'property_value_93', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 94', {'name': u'Property Value 94', 'pyname': u'property_value_94', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 95', {'name': u'Property Value 95', 'pyname': u'property_value_95', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 96', {'name': u'Property Value 96', 'pyname': u'property_value_96', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 97', {'name': u'Property Value 97', 'pyname': u'property_value_97', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 98', {'name': u'Property Value 98', 'pyname': u'property_value_98', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 99', {'name': u'Property Value 99', 'pyname': u'property_value_99', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 100', {'name': u'Property Value 100', 'pyname': u'property_value_100', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 101', {'name': u'Property Value 101', 'pyname': u'property_value_101', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 102', {'name': u'Property Value 102', 'pyname': u'property_value_102', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 103', {'name': u'Property Value 103', 'pyname': u'property_value_103', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 104', {'name': u'Property Value 104', 'pyname': u'property_value_104', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 105', {'name': u'Property Value 105', 'pyname': u'property_value_105', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 106', {'name': u'Property Value 106', 'pyname': u'property_value_106', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 107', {'name': u'Property Value 107', 'pyname': u'property_value_107', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 108', {'name': u'Property Value 108', 'pyname': u'property_value_108', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 109', {'name': u'Property Value 109', 'pyname': u'property_value_109', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 110', {'name': u'Property Value 110', 'pyname': u'property_value_110', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 111', {'name': u'Property Value 111', 'pyname': u'property_value_111', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 112', {'name': u'Property Value 112', 'pyname': u'property_value_112', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 113', {'name': u'Property Value 113', 'pyname': u'property_value_113', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 114', {'name': u'Property Value 114', 'pyname': u'property_value_114', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 115', {'name': u'Property Value 115', 'pyname': u'property_value_115', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 116', {'name': u'Property Value 116', 'pyname': u'property_value_116', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 117', {'name': u'Property Value 117', 'pyname': u'property_value_117', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 118', {'name': u'Property Value 118', 'pyname': u'property_value_118', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 119', {'name': u'Property Value 119', 'pyname': u'property_value_119', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 120', {'name': u'Property Value 120', 'pyname': u'property_value_120', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 121', {'name': u'Property Value 121', 'pyname': u'property_value_121', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 122', {'name': u'Property Value 122', 'pyname': u'property_value_122', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 123', {'name': u'Property Value 123', 'pyname': u'property_value_123', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 124', {'name': u'Property Value 124', 'pyname': u'property_value_124', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 125', {'name': u'Property Value 125', 'pyname': u'property_value_125', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 126', {'name': u'Property Value 126', 'pyname': u'property_value_126', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 127', {'name': u'Property Value 127', 'pyname': u'property_value_127', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 128', {'name': u'Property Value 128', 'pyname': u'property_value_128', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 129', {'name': u'Property Value 129', 'pyname': u'property_value_129', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 130', {'name': u'Property Value 130', 'pyname': u'property_value_130', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 131', {'name': u'Property Value 131', 'pyname': u'property_value_131', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 132', {'name': u'Property Value 132', 'pyname': u'property_value_132', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 133', {'name': u'Property Value 133', 'pyname': u'property_value_133', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 134', {'name': u'Property Value 134', 'pyname': u'property_value_134', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 135', {'name': u'Property Value 135', 'pyname': u'property_value_135', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 136', {'name': u'Property Value 136', 'pyname': u'property_value_136', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 137', {'name': u'Property Value 137', 'pyname': u'property_value_137', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 138', {'name': u'Property Value 138', 'pyname': u'property_value_138', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 139', {'name': u'Property Value 139', 'pyname': u'property_value_139', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 140', {'name': u'Property Value 140', 'pyname': u'property_value_140', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 141', {'name': u'Property Value 141', 'pyname': u'property_value_141', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 142', {'name': u'Property Value 142', 'pyname': u'property_value_142', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 143', {'name': u'Property Value 143', 'pyname': u'property_value_143', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 144', {'name': u'Property Value 144', 'pyname': u'property_value_144', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 145', {'name': u'Property Value 145', 'pyname': u'property_value_145', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 146', {'name': u'Property Value 146', 'pyname': u'property_value_146', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 147', {'name': u'Property Value 147', 'pyname': u'property_value_147', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 148', {'name': u'Property Value 148', 'pyname': u'property_value_148', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 149', {'name': u'Property Value 149', 'pyname': u'property_value_149', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 150', {'name': u'Property Value 150', 'pyname': u'property_value_150', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 151', {'name': u'Property Value 151', 'pyname': u'property_value_151', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 152', {'name': u'Property Value 152', 'pyname': u'property_value_152', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 153', {'name': u'Property Value 153', 'pyname': u'property_value_153', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 154', {'name': u'Property Value 154', 'pyname': u'property_value_154', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 155', {'name': u'Property Value 155', 'pyname': u'property_value_155', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 156', {'name': u'Property Value 156', 'pyname': u'property_value_156', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 157', {'name': u'Property Value 157', 'pyname': u'property_value_157', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 158', {'name': u'Property Value 158', 'pyname': u'property_value_158', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 159', {'name': u'Property Value 159', 'pyname': u'property_value_159', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 160', {'name': u'Property Value 160', 'pyname': u'property_value_160', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 161', {'name': u'Property Value 161', 'pyname': u'property_value_161', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 162', {'name': u'Property Value 162', 'pyname': u'property_value_162', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 163', {'name': u'Property Value 163', 'pyname': u'property_value_163', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 164', {'name': u'Property Value 164', 'pyname': u'property_value_164', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 165', {'name': u'Property Value 165', 'pyname': u'property_value_165', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 166', {'name': u'Property Value 166', 'pyname': u'property_value_166', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 167', {'name': u'Property Value 167', 'pyname': u'property_value_167', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 168', {'name': u'Property Value 168', 'pyname': u'property_value_168', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 169', {'name': u'Property Value 169', 'pyname': u'property_value_169', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 170', {'name': u'Property Value 170', 'pyname': u'property_value_170', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 171', {'name': u'Property Value 171', 'pyname': u'property_value_171', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 172', {'name': u'Property Value 172', 'pyname': u'property_value_172', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 173', {'name': u'Property Value 173', 'pyname': u'property_value_173', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 174', {'name': u'Property Value 174', 'pyname': u'property_value_174', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 175', {'name': u'Property Value 175', 'pyname': u'property_value_175', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 176', {'name': u'Property Value 176', 'pyname': u'property_value_176', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 177', {'name': u'Property Value 177', 'pyname': u'property_value_177', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 178', {'name': u'Property Value 178', 'pyname': u'property_value_178', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 179', {'name': u'Property Value 179', 'pyname': u'property_value_179', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 180', {'name': u'Property Value 180', 'pyname': u'property_value_180', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 181', {'name': u'Property Value 181', 'pyname': u'property_value_181', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 182', {'name': u'Property Value 182', 'pyname': u'property_value_182', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 183', {'name': u'Property Value 183', 'pyname': u'property_value_183', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 184', {'name': u'Property Value 184', 'pyname': u'property_value_184', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 185', {'name': u'Property Value 185', 'pyname': u'property_value_185', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 186', {'name': u'Property Value 186', 'pyname': u'property_value_186', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 187', {'name': u'Property Value 187', 'pyname': u'property_value_187', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 188', {'name': u'Property Value 188', 'pyname': u'property_value_188', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 189', {'name': u'Property Value 189', 'pyname': u'property_value_189', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 190', {'name': u'Property Value 190', 'pyname': u'property_value_190', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 191', {'name': u'Property Value 191', 'pyname': u'property_value_191', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 192', {'name': u'Property Value 192', 'pyname': u'property_value_192', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 193', {'name': u'Property Value 193', 'pyname': u'property_value_193', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 194', {'name': u'Property Value 194', 'pyname': u'property_value_194', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 195', {'name': u'Property Value 195', 'pyname': u'property_value_195', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 196', {'name': u'Property Value 196', 'pyname': u'property_value_196', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 197', {'name': u'Property Value 197', 'pyname': u'property_value_197', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 198', {'name': u'Property Value 198', 'pyname': u'property_value_198', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 199', {'name': u'Property Value 199', 'pyname': u'property_value_199', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 200', {'name': u'Property Value 200', 'pyname': u'property_value_200', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 201', {'name': u'Property Value 201', 'pyname': u'property_value_201', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 202', {'name': u'Property Value 202', 'pyname': u'property_value_202', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 203', {'name': u'Property Value 203', 'pyname': u'property_value_203', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 204', {'name': u'Property Value 204', 'pyname': u'property_value_204', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 205', {'name': u'Property Value 205', 'pyname': u'property_value_205', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 206', {'name': u'Property Value 206', 'pyname': u'property_value_206', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 207', {'name': u'Property Value 207', 'pyname': u'property_value_207', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 208', {'name': u'Property Value 208', 'pyname': u'property_value_208', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 209', {'name': u'Property Value 209', 'pyname': u'property_value_209', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 210', {'name': u'Property Value 210', 'pyname': u'property_value_210', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 211', {'name': u'Property Value 211', 'pyname': u'property_value_211', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 212', {'name': u'Property Value 212', 'pyname': u'property_value_212', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 213', {'name': u'Property Value 213', 'pyname': u'property_value_213', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 214', {'name': u'Property Value 214', 'pyname': u'property_value_214', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 215', {'name': u'Property Value 215', 'pyname': u'property_value_215', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 216', {'name': u'Property Value 216', 'pyname': u'property_value_216', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 217', {'name': u'Property Value 217', 'pyname': u'property_value_217', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 218', {'name': u'Property Value 218', 'pyname': u'property_value_218', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 219', {'name': u'Property Value 219', 'pyname': u'property_value_219', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 220', {'name': u'Property Value 220', 'pyname': u'property_value_220', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 221', {'name': u'Property Value 221', 'pyname': u'property_value_221', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 222', {'name': u'Property Value 222', 'pyname': u'property_value_222', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 223', {'name': u'Property Value 223', 'pyname': u'property_value_223', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 224', {'name': u'Property Value 224', 'pyname': u'property_value_224', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 225', {'name': u'Property Value 225', 'pyname': u'property_value_225', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 226', {'name': u'Property Value 226', 'pyname': u'property_value_226', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 227', {'name': u'Property Value 227', 'pyname': u'property_value_227', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 228', {'name': u'Property Value 228', 'pyname': u'property_value_228', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 229', {'name': u'Property Value 229', 'pyname': u'property_value_229', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 230', {'name': u'Property Value 230', 'pyname': u'property_value_230', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 231', {'name': u'Property Value 231', 'pyname': u'property_value_231', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 232', {'name': u'Property Value 232', 'pyname': u'property_value_232', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 233', {'name': u'Property Value 233', 'pyname': u'property_value_233', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 234', {'name': u'Property Value 234', 'pyname': u'property_value_234', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 235', {'name': u'Property Value 235', 'pyname': u'property_value_235', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 236', {'name': u'Property Value 236', 'pyname': u'property_value_236', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 237', {'name': u'Property Value 237', 'pyname': u'property_value_237', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 238', {'name': u'Property Value 238', 'pyname': u'property_value_238', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 239', {'name': u'Property Value 239', 'pyname': u'property_value_239', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 240', {'name': u'Property Value 240', 'pyname': u'property_value_240', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 241', {'name': u'Property Value 241', 'pyname': u'property_value_241', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 242', {'name': u'Property Value 242', 'pyname': u'property_value_242', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 243', {'name': u'Property Value 243', 'pyname': u'property_value_243', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 244', {'name': u'Property Value 244', 'pyname': u'property_value_244', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 245', {'name': u'Property Value 245', 'pyname': u'property_value_245', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 246', {'name': u'Property Value 246', 'pyname': u'property_value_246', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 247', {'name': u'Property Value 247', 'pyname': u'property_value_247', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 248', {'name': u'Property Value 248', 'pyname': u'property_value_248', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 249', {'name': u'Property Value 249', 'pyname': u'property_value_249', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 250', {'name': u'Property Value 250', 'pyname': u'property_value_250', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

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
    def fluid_property_type(self):
        """Get fluid_property_type

        Returns:
            str: the value of `fluid_property_type` or None if not set
        """
        return self["Fluid Property Type"]

    @fluid_property_type.setter
    def fluid_property_type(self, value=None):
        """  Corresponds to IDD Field `Fluid Property Type`
        Enthalpy Units are J/kg
        Density Units are kg/m3
        SpecificHeat Units are J/kg-K
        Pressure Units are Pa

        Args:
            value (str): value for IDD Field `Fluid Property Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Property Type"] = value

    @property
    def fluid_phase(self):
        """Get fluid_phase

        Returns:
            str: the value of `fluid_phase` or None if not set
        """
        return self["Fluid Phase"]

    @fluid_phase.setter
    def fluid_phase(self, value=None):
        """  Corresponds to IDD Field `Fluid Phase`
        Fluid=saturated fluid
        FluidGas=saturated vapor

        Args:
            value (str): value for IDD Field `Fluid Phase`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Phase"] = value

    @property
    def temperature_values_name(self):
        """Get temperature_values_name

        Returns:
            str: the value of `temperature_values_name` or None if not set
        """
        return self["Temperature Values Name"]

    @temperature_values_name.setter
    def temperature_values_name(self, value=None):
        """  Corresponds to IDD Field `Temperature Values Name`
        Enter the name of a FluidProperties:Temperatures object.

        Args:
            value (str): value for IDD Field `Temperature Values Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Values Name"] = value

    @property
    def property_value_1(self):
        """Get property_value_1

        Returns:
            float: the value of `property_value_1` or None if not set
        """
        return self["Property Value 1"]

    @property_value_1.setter
    def property_value_1(self, value=None):
        """  Corresponds to IDD Field `Property Value 1`

        Args:
            value (float): value for IDD Field `Property Value 1`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 1"] = value

    @property
    def property_value_2(self):
        """Get property_value_2

        Returns:
            float: the value of `property_value_2` or None if not set
        """
        return self["Property Value 2"]

    @property_value_2.setter
    def property_value_2(self, value=None):
        """  Corresponds to IDD Field `Property Value 2`

        Args:
            value (float): value for IDD Field `Property Value 2`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 2"] = value

    @property
    def property_value_3(self):
        """Get property_value_3

        Returns:
            float: the value of `property_value_3` or None if not set
        """
        return self["Property Value 3"]

    @property_value_3.setter
    def property_value_3(self, value=None):
        """  Corresponds to IDD Field `Property Value 3`

        Args:
            value (float): value for IDD Field `Property Value 3`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 3"] = value

    @property
    def property_value_4(self):
        """Get property_value_4

        Returns:
            float: the value of `property_value_4` or None if not set
        """
        return self["Property Value 4"]

    @property_value_4.setter
    def property_value_4(self, value=None):
        """  Corresponds to IDD Field `Property Value 4`

        Args:
            value (float): value for IDD Field `Property Value 4`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 4"] = value

    @property
    def property_value_5(self):
        """Get property_value_5

        Returns:
            float: the value of `property_value_5` or None if not set
        """
        return self["Property Value 5"]

    @property_value_5.setter
    def property_value_5(self, value=None):
        """  Corresponds to IDD Field `Property Value 5`

        Args:
            value (float): value for IDD Field `Property Value 5`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 5"] = value

    @property
    def property_value_6(self):
        """Get property_value_6

        Returns:
            float: the value of `property_value_6` or None if not set
        """
        return self["Property Value 6"]

    @property_value_6.setter
    def property_value_6(self, value=None):
        """  Corresponds to IDD Field `Property Value 6`

        Args:
            value (float): value for IDD Field `Property Value 6`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 6"] = value

    @property
    def property_value_7(self):
        """Get property_value_7

        Returns:
            float: the value of `property_value_7` or None if not set
        """
        return self["Property Value 7"]

    @property_value_7.setter
    def property_value_7(self, value=None):
        """  Corresponds to IDD Field `Property Value 7`

        Args:
            value (float): value for IDD Field `Property Value 7`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 7"] = value

    @property
    def property_value_8(self):
        """Get property_value_8

        Returns:
            float: the value of `property_value_8` or None if not set
        """
        return self["Property Value 8"]

    @property_value_8.setter
    def property_value_8(self, value=None):
        """  Corresponds to IDD Field `Property Value 8`

        Args:
            value (float): value for IDD Field `Property Value 8`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 8"] = value

    @property
    def property_value_9(self):
        """Get property_value_9

        Returns:
            float: the value of `property_value_9` or None if not set
        """
        return self["Property Value 9"]

    @property_value_9.setter
    def property_value_9(self, value=None):
        """  Corresponds to IDD Field `Property Value 9`

        Args:
            value (float): value for IDD Field `Property Value 9`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 9"] = value

    @property
    def property_value_10(self):
        """Get property_value_10

        Returns:
            float: the value of `property_value_10` or None if not set
        """
        return self["Property Value 10"]

    @property_value_10.setter
    def property_value_10(self, value=None):
        """  Corresponds to IDD Field `Property Value 10`

        Args:
            value (float): value for IDD Field `Property Value 10`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 10"] = value

    @property
    def property_value_11(self):
        """Get property_value_11

        Returns:
            float: the value of `property_value_11` or None if not set
        """
        return self["Property Value 11"]

    @property_value_11.setter
    def property_value_11(self, value=None):
        """  Corresponds to IDD Field `Property Value 11`

        Args:
            value (float): value for IDD Field `Property Value 11`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 11"] = value

    @property
    def property_value_12(self):
        """Get property_value_12

        Returns:
            float: the value of `property_value_12` or None if not set
        """
        return self["Property Value 12"]

    @property_value_12.setter
    def property_value_12(self, value=None):
        """  Corresponds to IDD Field `Property Value 12`

        Args:
            value (float): value for IDD Field `Property Value 12`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 12"] = value

    @property
    def property_value_13(self):
        """Get property_value_13

        Returns:
            float: the value of `property_value_13` or None if not set
        """
        return self["Property Value 13"]

    @property_value_13.setter
    def property_value_13(self, value=None):
        """  Corresponds to IDD Field `Property Value 13`

        Args:
            value (float): value for IDD Field `Property Value 13`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 13"] = value

    @property
    def property_value_14(self):
        """Get property_value_14

        Returns:
            float: the value of `property_value_14` or None if not set
        """
        return self["Property Value 14"]

    @property_value_14.setter
    def property_value_14(self, value=None):
        """  Corresponds to IDD Field `Property Value 14`

        Args:
            value (float): value for IDD Field `Property Value 14`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 14"] = value

    @property
    def property_value_15(self):
        """Get property_value_15

        Returns:
            float: the value of `property_value_15` or None if not set
        """
        return self["Property Value 15"]

    @property_value_15.setter
    def property_value_15(self, value=None):
        """  Corresponds to IDD Field `Property Value 15`

        Args:
            value (float): value for IDD Field `Property Value 15`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 15"] = value

    @property
    def property_value_16(self):
        """Get property_value_16

        Returns:
            float: the value of `property_value_16` or None if not set
        """
        return self["Property Value 16"]

    @property_value_16.setter
    def property_value_16(self, value=None):
        """  Corresponds to IDD Field `Property Value 16`

        Args:
            value (float): value for IDD Field `Property Value 16`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 16"] = value

    @property
    def property_value_17(self):
        """Get property_value_17

        Returns:
            float: the value of `property_value_17` or None if not set
        """
        return self["Property Value 17"]

    @property_value_17.setter
    def property_value_17(self, value=None):
        """  Corresponds to IDD Field `Property Value 17`

        Args:
            value (float): value for IDD Field `Property Value 17`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 17"] = value

    @property
    def property_value_18(self):
        """Get property_value_18

        Returns:
            float: the value of `property_value_18` or None if not set
        """
        return self["Property Value 18"]

    @property_value_18.setter
    def property_value_18(self, value=None):
        """  Corresponds to IDD Field `Property Value 18`

        Args:
            value (float): value for IDD Field `Property Value 18`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 18"] = value

    @property
    def property_value_19(self):
        """Get property_value_19

        Returns:
            float: the value of `property_value_19` or None if not set
        """
        return self["Property Value 19"]

    @property_value_19.setter
    def property_value_19(self, value=None):
        """  Corresponds to IDD Field `Property Value 19`

        Args:
            value (float): value for IDD Field `Property Value 19`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 19"] = value

    @property
    def property_value_20(self):
        """Get property_value_20

        Returns:
            float: the value of `property_value_20` or None if not set
        """
        return self["Property Value 20"]

    @property_value_20.setter
    def property_value_20(self, value=None):
        """  Corresponds to IDD Field `Property Value 20`

        Args:
            value (float): value for IDD Field `Property Value 20`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 20"] = value

    @property
    def property_value_21(self):
        """Get property_value_21

        Returns:
            float: the value of `property_value_21` or None if not set
        """
        return self["Property Value 21"]

    @property_value_21.setter
    def property_value_21(self, value=None):
        """  Corresponds to IDD Field `Property Value 21`

        Args:
            value (float): value for IDD Field `Property Value 21`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 21"] = value

    @property
    def property_value_22(self):
        """Get property_value_22

        Returns:
            float: the value of `property_value_22` or None if not set
        """
        return self["Property Value 22"]

    @property_value_22.setter
    def property_value_22(self, value=None):
        """  Corresponds to IDD Field `Property Value 22`

        Args:
            value (float): value for IDD Field `Property Value 22`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 22"] = value

    @property
    def property_value_23(self):
        """Get property_value_23

        Returns:
            float: the value of `property_value_23` or None if not set
        """
        return self["Property Value 23"]

    @property_value_23.setter
    def property_value_23(self, value=None):
        """  Corresponds to IDD Field `Property Value 23`

        Args:
            value (float): value for IDD Field `Property Value 23`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 23"] = value

    @property
    def property_value_24(self):
        """Get property_value_24

        Returns:
            float: the value of `property_value_24` or None if not set
        """
        return self["Property Value 24"]

    @property_value_24.setter
    def property_value_24(self, value=None):
        """  Corresponds to IDD Field `Property Value 24`

        Args:
            value (float): value for IDD Field `Property Value 24`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 24"] = value

    @property
    def property_value_25(self):
        """Get property_value_25

        Returns:
            float: the value of `property_value_25` or None if not set
        """
        return self["Property Value 25"]

    @property_value_25.setter
    def property_value_25(self, value=None):
        """  Corresponds to IDD Field `Property Value 25`

        Args:
            value (float): value for IDD Field `Property Value 25`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 25"] = value

    @property
    def property_value_26(self):
        """Get property_value_26

        Returns:
            float: the value of `property_value_26` or None if not set
        """
        return self["Property Value 26"]

    @property_value_26.setter
    def property_value_26(self, value=None):
        """  Corresponds to IDD Field `Property Value 26`

        Args:
            value (float): value for IDD Field `Property Value 26`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 26"] = value

    @property
    def property_value_27(self):
        """Get property_value_27

        Returns:
            float: the value of `property_value_27` or None if not set
        """
        return self["Property Value 27"]

    @property_value_27.setter
    def property_value_27(self, value=None):
        """  Corresponds to IDD Field `Property Value 27`

        Args:
            value (float): value for IDD Field `Property Value 27`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 27"] = value

    @property
    def property_value_28(self):
        """Get property_value_28

        Returns:
            float: the value of `property_value_28` or None if not set
        """
        return self["Property Value 28"]

    @property_value_28.setter
    def property_value_28(self, value=None):
        """  Corresponds to IDD Field `Property Value 28`

        Args:
            value (float): value for IDD Field `Property Value 28`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 28"] = value

    @property
    def property_value_29(self):
        """Get property_value_29

        Returns:
            float: the value of `property_value_29` or None if not set
        """
        return self["Property Value 29"]

    @property_value_29.setter
    def property_value_29(self, value=None):
        """  Corresponds to IDD Field `Property Value 29`

        Args:
            value (float): value for IDD Field `Property Value 29`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 29"] = value

    @property
    def property_value_30(self):
        """Get property_value_30

        Returns:
            float: the value of `property_value_30` or None if not set
        """
        return self["Property Value 30"]

    @property_value_30.setter
    def property_value_30(self, value=None):
        """  Corresponds to IDD Field `Property Value 30`

        Args:
            value (float): value for IDD Field `Property Value 30`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 30"] = value

    @property
    def property_value_31(self):
        """Get property_value_31

        Returns:
            float: the value of `property_value_31` or None if not set
        """
        return self["Property Value 31"]

    @property_value_31.setter
    def property_value_31(self, value=None):
        """  Corresponds to IDD Field `Property Value 31`

        Args:
            value (float): value for IDD Field `Property Value 31`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 31"] = value

    @property
    def property_value_32(self):
        """Get property_value_32

        Returns:
            float: the value of `property_value_32` or None if not set
        """
        return self["Property Value 32"]

    @property_value_32.setter
    def property_value_32(self, value=None):
        """  Corresponds to IDD Field `Property Value 32`

        Args:
            value (float): value for IDD Field `Property Value 32`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 32"] = value

    @property
    def property_value_33(self):
        """Get property_value_33

        Returns:
            float: the value of `property_value_33` or None if not set
        """
        return self["Property Value 33"]

    @property_value_33.setter
    def property_value_33(self, value=None):
        """  Corresponds to IDD Field `Property Value 33`

        Args:
            value (float): value for IDD Field `Property Value 33`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 33"] = value

    @property
    def property_value_34(self):
        """Get property_value_34

        Returns:
            float: the value of `property_value_34` or None if not set
        """
        return self["Property Value 34"]

    @property_value_34.setter
    def property_value_34(self, value=None):
        """  Corresponds to IDD Field `Property Value 34`

        Args:
            value (float): value for IDD Field `Property Value 34`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 34"] = value

    @property
    def property_value_35(self):
        """Get property_value_35

        Returns:
            float: the value of `property_value_35` or None if not set
        """
        return self["Property Value 35"]

    @property_value_35.setter
    def property_value_35(self, value=None):
        """  Corresponds to IDD Field `Property Value 35`

        Args:
            value (float): value for IDD Field `Property Value 35`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 35"] = value

    @property
    def property_value_36(self):
        """Get property_value_36

        Returns:
            float: the value of `property_value_36` or None if not set
        """
        return self["Property Value 36"]

    @property_value_36.setter
    def property_value_36(self, value=None):
        """  Corresponds to IDD Field `Property Value 36`

        Args:
            value (float): value for IDD Field `Property Value 36`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 36"] = value

    @property
    def property_value_37(self):
        """Get property_value_37

        Returns:
            float: the value of `property_value_37` or None if not set
        """
        return self["Property Value 37"]

    @property_value_37.setter
    def property_value_37(self, value=None):
        """  Corresponds to IDD Field `Property Value 37`

        Args:
            value (float): value for IDD Field `Property Value 37`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 37"] = value

    @property
    def property_value_38(self):
        """Get property_value_38

        Returns:
            float: the value of `property_value_38` or None if not set
        """
        return self["Property Value 38"]

    @property_value_38.setter
    def property_value_38(self, value=None):
        """  Corresponds to IDD Field `Property Value 38`

        Args:
            value (float): value for IDD Field `Property Value 38`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 38"] = value

    @property
    def property_value_39(self):
        """Get property_value_39

        Returns:
            float: the value of `property_value_39` or None if not set
        """
        return self["Property Value 39"]

    @property_value_39.setter
    def property_value_39(self, value=None):
        """  Corresponds to IDD Field `Property Value 39`

        Args:
            value (float): value for IDD Field `Property Value 39`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 39"] = value

    @property
    def property_value_40(self):
        """Get property_value_40

        Returns:
            float: the value of `property_value_40` or None if not set
        """
        return self["Property Value 40"]

    @property_value_40.setter
    def property_value_40(self, value=None):
        """  Corresponds to IDD Field `Property Value 40`

        Args:
            value (float): value for IDD Field `Property Value 40`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 40"] = value

    @property
    def property_value_41(self):
        """Get property_value_41

        Returns:
            float: the value of `property_value_41` or None if not set
        """
        return self["Property Value 41"]

    @property_value_41.setter
    def property_value_41(self, value=None):
        """  Corresponds to IDD Field `Property Value 41`

        Args:
            value (float): value for IDD Field `Property Value 41`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 41"] = value

    @property
    def property_value_42(self):
        """Get property_value_42

        Returns:
            float: the value of `property_value_42` or None if not set
        """
        return self["Property Value 42"]

    @property_value_42.setter
    def property_value_42(self, value=None):
        """  Corresponds to IDD Field `Property Value 42`

        Args:
            value (float): value for IDD Field `Property Value 42`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 42"] = value

    @property
    def property_value_43(self):
        """Get property_value_43

        Returns:
            float: the value of `property_value_43` or None if not set
        """
        return self["Property Value 43"]

    @property_value_43.setter
    def property_value_43(self, value=None):
        """  Corresponds to IDD Field `Property Value 43`

        Args:
            value (float): value for IDD Field `Property Value 43`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 43"] = value

    @property
    def property_value_44(self):
        """Get property_value_44

        Returns:
            float: the value of `property_value_44` or None if not set
        """
        return self["Property Value 44"]

    @property_value_44.setter
    def property_value_44(self, value=None):
        """  Corresponds to IDD Field `Property Value 44`

        Args:
            value (float): value for IDD Field `Property Value 44`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 44"] = value

    @property
    def property_value_45(self):
        """Get property_value_45

        Returns:
            float: the value of `property_value_45` or None if not set
        """
        return self["Property Value 45"]

    @property_value_45.setter
    def property_value_45(self, value=None):
        """  Corresponds to IDD Field `Property Value 45`

        Args:
            value (float): value for IDD Field `Property Value 45`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 45"] = value

    @property
    def property_value_46(self):
        """Get property_value_46

        Returns:
            float: the value of `property_value_46` or None if not set
        """
        return self["Property Value 46"]

    @property_value_46.setter
    def property_value_46(self, value=None):
        """  Corresponds to IDD Field `Property Value 46`

        Args:
            value (float): value for IDD Field `Property Value 46`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 46"] = value

    @property
    def property_value_47(self):
        """Get property_value_47

        Returns:
            float: the value of `property_value_47` or None if not set
        """
        return self["Property Value 47"]

    @property_value_47.setter
    def property_value_47(self, value=None):
        """  Corresponds to IDD Field `Property Value 47`

        Args:
            value (float): value for IDD Field `Property Value 47`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 47"] = value

    @property
    def property_value_48(self):
        """Get property_value_48

        Returns:
            float: the value of `property_value_48` or None if not set
        """
        return self["Property Value 48"]

    @property_value_48.setter
    def property_value_48(self, value=None):
        """  Corresponds to IDD Field `Property Value 48`

        Args:
            value (float): value for IDD Field `Property Value 48`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 48"] = value

    @property
    def property_value_49(self):
        """Get property_value_49

        Returns:
            float: the value of `property_value_49` or None if not set
        """
        return self["Property Value 49"]

    @property_value_49.setter
    def property_value_49(self, value=None):
        """  Corresponds to IDD Field `Property Value 49`

        Args:
            value (float): value for IDD Field `Property Value 49`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 49"] = value

    @property
    def property_value_50(self):
        """Get property_value_50

        Returns:
            float: the value of `property_value_50` or None if not set
        """
        return self["Property Value 50"]

    @property_value_50.setter
    def property_value_50(self, value=None):
        """  Corresponds to IDD Field `Property Value 50`

        Args:
            value (float): value for IDD Field `Property Value 50`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 50"] = value

    @property
    def property_value_51(self):
        """Get property_value_51

        Returns:
            float: the value of `property_value_51` or None if not set
        """
        return self["Property Value 51"]

    @property_value_51.setter
    def property_value_51(self, value=None):
        """  Corresponds to IDD Field `Property Value 51`

        Args:
            value (float): value for IDD Field `Property Value 51`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 51"] = value

    @property
    def property_value_52(self):
        """Get property_value_52

        Returns:
            float: the value of `property_value_52` or None if not set
        """
        return self["Property Value 52"]

    @property_value_52.setter
    def property_value_52(self, value=None):
        """  Corresponds to IDD Field `Property Value 52`

        Args:
            value (float): value for IDD Field `Property Value 52`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 52"] = value

    @property
    def property_value_53(self):
        """Get property_value_53

        Returns:
            float: the value of `property_value_53` or None if not set
        """
        return self["Property Value 53"]

    @property_value_53.setter
    def property_value_53(self, value=None):
        """  Corresponds to IDD Field `Property Value 53`

        Args:
            value (float): value for IDD Field `Property Value 53`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 53"] = value

    @property
    def property_value_54(self):
        """Get property_value_54

        Returns:
            float: the value of `property_value_54` or None if not set
        """
        return self["Property Value 54"]

    @property_value_54.setter
    def property_value_54(self, value=None):
        """  Corresponds to IDD Field `Property Value 54`

        Args:
            value (float): value for IDD Field `Property Value 54`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 54"] = value

    @property
    def property_value_55(self):
        """Get property_value_55

        Returns:
            float: the value of `property_value_55` or None if not set
        """
        return self["Property Value 55"]

    @property_value_55.setter
    def property_value_55(self, value=None):
        """  Corresponds to IDD Field `Property Value 55`

        Args:
            value (float): value for IDD Field `Property Value 55`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 55"] = value

    @property
    def property_value_56(self):
        """Get property_value_56

        Returns:
            float: the value of `property_value_56` or None if not set
        """
        return self["Property Value 56"]

    @property_value_56.setter
    def property_value_56(self, value=None):
        """  Corresponds to IDD Field `Property Value 56`

        Args:
            value (float): value for IDD Field `Property Value 56`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 56"] = value

    @property
    def property_value_57(self):
        """Get property_value_57

        Returns:
            float: the value of `property_value_57` or None if not set
        """
        return self["Property Value 57"]

    @property_value_57.setter
    def property_value_57(self, value=None):
        """  Corresponds to IDD Field `Property Value 57`

        Args:
            value (float): value for IDD Field `Property Value 57`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 57"] = value

    @property
    def property_value_58(self):
        """Get property_value_58

        Returns:
            float: the value of `property_value_58` or None if not set
        """
        return self["Property Value 58"]

    @property_value_58.setter
    def property_value_58(self, value=None):
        """  Corresponds to IDD Field `Property Value 58`

        Args:
            value (float): value for IDD Field `Property Value 58`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 58"] = value

    @property
    def property_value_59(self):
        """Get property_value_59

        Returns:
            float: the value of `property_value_59` or None if not set
        """
        return self["Property Value 59"]

    @property_value_59.setter
    def property_value_59(self, value=None):
        """  Corresponds to IDD Field `Property Value 59`

        Args:
            value (float): value for IDD Field `Property Value 59`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 59"] = value

    @property
    def property_value_60(self):
        """Get property_value_60

        Returns:
            float: the value of `property_value_60` or None if not set
        """
        return self["Property Value 60"]

    @property_value_60.setter
    def property_value_60(self, value=None):
        """  Corresponds to IDD Field `Property Value 60`

        Args:
            value (float): value for IDD Field `Property Value 60`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 60"] = value

    @property
    def property_value_61(self):
        """Get property_value_61

        Returns:
            float: the value of `property_value_61` or None if not set
        """
        return self["Property Value 61"]

    @property_value_61.setter
    def property_value_61(self, value=None):
        """  Corresponds to IDD Field `Property Value 61`

        Args:
            value (float): value for IDD Field `Property Value 61`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 61"] = value

    @property
    def property_value_62(self):
        """Get property_value_62

        Returns:
            float: the value of `property_value_62` or None if not set
        """
        return self["Property Value 62"]

    @property_value_62.setter
    def property_value_62(self, value=None):
        """  Corresponds to IDD Field `Property Value 62`

        Args:
            value (float): value for IDD Field `Property Value 62`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 62"] = value

    @property
    def property_value_63(self):
        """Get property_value_63

        Returns:
            float: the value of `property_value_63` or None if not set
        """
        return self["Property Value 63"]

    @property_value_63.setter
    def property_value_63(self, value=None):
        """  Corresponds to IDD Field `Property Value 63`

        Args:
            value (float): value for IDD Field `Property Value 63`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 63"] = value

    @property
    def property_value_64(self):
        """Get property_value_64

        Returns:
            float: the value of `property_value_64` or None if not set
        """
        return self["Property Value 64"]

    @property_value_64.setter
    def property_value_64(self, value=None):
        """  Corresponds to IDD Field `Property Value 64`

        Args:
            value (float): value for IDD Field `Property Value 64`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 64"] = value

    @property
    def property_value_65(self):
        """Get property_value_65

        Returns:
            float: the value of `property_value_65` or None if not set
        """
        return self["Property Value 65"]

    @property_value_65.setter
    def property_value_65(self, value=None):
        """  Corresponds to IDD Field `Property Value 65`

        Args:
            value (float): value for IDD Field `Property Value 65`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 65"] = value

    @property
    def property_value_66(self):
        """Get property_value_66

        Returns:
            float: the value of `property_value_66` or None if not set
        """
        return self["Property Value 66"]

    @property_value_66.setter
    def property_value_66(self, value=None):
        """  Corresponds to IDD Field `Property Value 66`

        Args:
            value (float): value for IDD Field `Property Value 66`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 66"] = value

    @property
    def property_value_67(self):
        """Get property_value_67

        Returns:
            float: the value of `property_value_67` or None if not set
        """
        return self["Property Value 67"]

    @property_value_67.setter
    def property_value_67(self, value=None):
        """  Corresponds to IDD Field `Property Value 67`

        Args:
            value (float): value for IDD Field `Property Value 67`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 67"] = value

    @property
    def property_value_68(self):
        """Get property_value_68

        Returns:
            float: the value of `property_value_68` or None if not set
        """
        return self["Property Value 68"]

    @property_value_68.setter
    def property_value_68(self, value=None):
        """  Corresponds to IDD Field `Property Value 68`

        Args:
            value (float): value for IDD Field `Property Value 68`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 68"] = value

    @property
    def property_value_69(self):
        """Get property_value_69

        Returns:
            float: the value of `property_value_69` or None if not set
        """
        return self["Property Value 69"]

    @property_value_69.setter
    def property_value_69(self, value=None):
        """  Corresponds to IDD Field `Property Value 69`

        Args:
            value (float): value for IDD Field `Property Value 69`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 69"] = value

    @property
    def property_value_70(self):
        """Get property_value_70

        Returns:
            float: the value of `property_value_70` or None if not set
        """
        return self["Property Value 70"]

    @property_value_70.setter
    def property_value_70(self, value=None):
        """  Corresponds to IDD Field `Property Value 70`

        Args:
            value (float): value for IDD Field `Property Value 70`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 70"] = value

    @property
    def property_value_71(self):
        """Get property_value_71

        Returns:
            float: the value of `property_value_71` or None if not set
        """
        return self["Property Value 71"]

    @property_value_71.setter
    def property_value_71(self, value=None):
        """  Corresponds to IDD Field `Property Value 71`

        Args:
            value (float): value for IDD Field `Property Value 71`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 71"] = value

    @property
    def property_value_72(self):
        """Get property_value_72

        Returns:
            float: the value of `property_value_72` or None if not set
        """
        return self["Property Value 72"]

    @property_value_72.setter
    def property_value_72(self, value=None):
        """  Corresponds to IDD Field `Property Value 72`

        Args:
            value (float): value for IDD Field `Property Value 72`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 72"] = value

    @property
    def property_value_73(self):
        """Get property_value_73

        Returns:
            float: the value of `property_value_73` or None if not set
        """
        return self["Property Value 73"]

    @property_value_73.setter
    def property_value_73(self, value=None):
        """  Corresponds to IDD Field `Property Value 73`

        Args:
            value (float): value for IDD Field `Property Value 73`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 73"] = value

    @property
    def property_value_74(self):
        """Get property_value_74

        Returns:
            float: the value of `property_value_74` or None if not set
        """
        return self["Property Value 74"]

    @property_value_74.setter
    def property_value_74(self, value=None):
        """  Corresponds to IDD Field `Property Value 74`

        Args:
            value (float): value for IDD Field `Property Value 74`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 74"] = value

    @property
    def property_value_75(self):
        """Get property_value_75

        Returns:
            float: the value of `property_value_75` or None if not set
        """
        return self["Property Value 75"]

    @property_value_75.setter
    def property_value_75(self, value=None):
        """  Corresponds to IDD Field `Property Value 75`

        Args:
            value (float): value for IDD Field `Property Value 75`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 75"] = value

    @property
    def property_value_76(self):
        """Get property_value_76

        Returns:
            float: the value of `property_value_76` or None if not set
        """
        return self["Property Value 76"]

    @property_value_76.setter
    def property_value_76(self, value=None):
        """  Corresponds to IDD Field `Property Value 76`

        Args:
            value (float): value for IDD Field `Property Value 76`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 76"] = value

    @property
    def property_value_77(self):
        """Get property_value_77

        Returns:
            float: the value of `property_value_77` or None if not set
        """
        return self["Property Value 77"]

    @property_value_77.setter
    def property_value_77(self, value=None):
        """  Corresponds to IDD Field `Property Value 77`

        Args:
            value (float): value for IDD Field `Property Value 77`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 77"] = value

    @property
    def property_value_78(self):
        """Get property_value_78

        Returns:
            float: the value of `property_value_78` or None if not set
        """
        return self["Property Value 78"]

    @property_value_78.setter
    def property_value_78(self, value=None):
        """  Corresponds to IDD Field `Property Value 78`

        Args:
            value (float): value for IDD Field `Property Value 78`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 78"] = value

    @property
    def property_value_79(self):
        """Get property_value_79

        Returns:
            float: the value of `property_value_79` or None if not set
        """
        return self["Property Value 79"]

    @property_value_79.setter
    def property_value_79(self, value=None):
        """  Corresponds to IDD Field `Property Value 79`

        Args:
            value (float): value for IDD Field `Property Value 79`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 79"] = value

    @property
    def property_value_80(self):
        """Get property_value_80

        Returns:
            float: the value of `property_value_80` or None if not set
        """
        return self["Property Value 80"]

    @property_value_80.setter
    def property_value_80(self, value=None):
        """  Corresponds to IDD Field `Property Value 80`

        Args:
            value (float): value for IDD Field `Property Value 80`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 80"] = value

    @property
    def property_value_81(self):
        """Get property_value_81

        Returns:
            float: the value of `property_value_81` or None if not set
        """
        return self["Property Value 81"]

    @property_value_81.setter
    def property_value_81(self, value=None):
        """  Corresponds to IDD Field `Property Value 81`

        Args:
            value (float): value for IDD Field `Property Value 81`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 81"] = value

    @property
    def property_value_82(self):
        """Get property_value_82

        Returns:
            float: the value of `property_value_82` or None if not set
        """
        return self["Property Value 82"]

    @property_value_82.setter
    def property_value_82(self, value=None):
        """  Corresponds to IDD Field `Property Value 82`

        Args:
            value (float): value for IDD Field `Property Value 82`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 82"] = value

    @property
    def property_value_83(self):
        """Get property_value_83

        Returns:
            float: the value of `property_value_83` or None if not set
        """
        return self["Property Value 83"]

    @property_value_83.setter
    def property_value_83(self, value=None):
        """  Corresponds to IDD Field `Property Value 83`

        Args:
            value (float): value for IDD Field `Property Value 83`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 83"] = value

    @property
    def property_value_84(self):
        """Get property_value_84

        Returns:
            float: the value of `property_value_84` or None if not set
        """
        return self["Property Value 84"]

    @property_value_84.setter
    def property_value_84(self, value=None):
        """  Corresponds to IDD Field `Property Value 84`

        Args:
            value (float): value for IDD Field `Property Value 84`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 84"] = value

    @property
    def property_value_85(self):
        """Get property_value_85

        Returns:
            float: the value of `property_value_85` or None if not set
        """
        return self["Property Value 85"]

    @property_value_85.setter
    def property_value_85(self, value=None):
        """  Corresponds to IDD Field `Property Value 85`

        Args:
            value (float): value for IDD Field `Property Value 85`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 85"] = value

    @property
    def property_value_86(self):
        """Get property_value_86

        Returns:
            float: the value of `property_value_86` or None if not set
        """
        return self["Property Value 86"]

    @property_value_86.setter
    def property_value_86(self, value=None):
        """  Corresponds to IDD Field `Property Value 86`

        Args:
            value (float): value for IDD Field `Property Value 86`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 86"] = value

    @property
    def property_value_87(self):
        """Get property_value_87

        Returns:
            float: the value of `property_value_87` or None if not set
        """
        return self["Property Value 87"]

    @property_value_87.setter
    def property_value_87(self, value=None):
        """  Corresponds to IDD Field `Property Value 87`

        Args:
            value (float): value for IDD Field `Property Value 87`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 87"] = value

    @property
    def property_value_88(self):
        """Get property_value_88

        Returns:
            float: the value of `property_value_88` or None if not set
        """
        return self["Property Value 88"]

    @property_value_88.setter
    def property_value_88(self, value=None):
        """  Corresponds to IDD Field `Property Value 88`

        Args:
            value (float): value for IDD Field `Property Value 88`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 88"] = value

    @property
    def property_value_89(self):
        """Get property_value_89

        Returns:
            float: the value of `property_value_89` or None if not set
        """
        return self["Property Value 89"]

    @property_value_89.setter
    def property_value_89(self, value=None):
        """  Corresponds to IDD Field `Property Value 89`

        Args:
            value (float): value for IDD Field `Property Value 89`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 89"] = value

    @property
    def property_value_90(self):
        """Get property_value_90

        Returns:
            float: the value of `property_value_90` or None if not set
        """
        return self["Property Value 90"]

    @property_value_90.setter
    def property_value_90(self, value=None):
        """  Corresponds to IDD Field `Property Value 90`

        Args:
            value (float): value for IDD Field `Property Value 90`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 90"] = value

    @property
    def property_value_91(self):
        """Get property_value_91

        Returns:
            float: the value of `property_value_91` or None if not set
        """
        return self["Property Value 91"]

    @property_value_91.setter
    def property_value_91(self, value=None):
        """  Corresponds to IDD Field `Property Value 91`

        Args:
            value (float): value for IDD Field `Property Value 91`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 91"] = value

    @property
    def property_value_92(self):
        """Get property_value_92

        Returns:
            float: the value of `property_value_92` or None if not set
        """
        return self["Property Value 92"]

    @property_value_92.setter
    def property_value_92(self, value=None):
        """  Corresponds to IDD Field `Property Value 92`

        Args:
            value (float): value for IDD Field `Property Value 92`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 92"] = value

    @property
    def property_value_93(self):
        """Get property_value_93

        Returns:
            float: the value of `property_value_93` or None if not set
        """
        return self["Property Value 93"]

    @property_value_93.setter
    def property_value_93(self, value=None):
        """  Corresponds to IDD Field `Property Value 93`

        Args:
            value (float): value for IDD Field `Property Value 93`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 93"] = value

    @property
    def property_value_94(self):
        """Get property_value_94

        Returns:
            float: the value of `property_value_94` or None if not set
        """
        return self["Property Value 94"]

    @property_value_94.setter
    def property_value_94(self, value=None):
        """  Corresponds to IDD Field `Property Value 94`

        Args:
            value (float): value for IDD Field `Property Value 94`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 94"] = value

    @property
    def property_value_95(self):
        """Get property_value_95

        Returns:
            float: the value of `property_value_95` or None if not set
        """
        return self["Property Value 95"]

    @property_value_95.setter
    def property_value_95(self, value=None):
        """  Corresponds to IDD Field `Property Value 95`

        Args:
            value (float): value for IDD Field `Property Value 95`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 95"] = value

    @property
    def property_value_96(self):
        """Get property_value_96

        Returns:
            float: the value of `property_value_96` or None if not set
        """
        return self["Property Value 96"]

    @property_value_96.setter
    def property_value_96(self, value=None):
        """  Corresponds to IDD Field `Property Value 96`

        Args:
            value (float): value for IDD Field `Property Value 96`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 96"] = value

    @property
    def property_value_97(self):
        """Get property_value_97

        Returns:
            float: the value of `property_value_97` or None if not set
        """
        return self["Property Value 97"]

    @property_value_97.setter
    def property_value_97(self, value=None):
        """  Corresponds to IDD Field `Property Value 97`

        Args:
            value (float): value for IDD Field `Property Value 97`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 97"] = value

    @property
    def property_value_98(self):
        """Get property_value_98

        Returns:
            float: the value of `property_value_98` or None if not set
        """
        return self["Property Value 98"]

    @property_value_98.setter
    def property_value_98(self, value=None):
        """  Corresponds to IDD Field `Property Value 98`

        Args:
            value (float): value for IDD Field `Property Value 98`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 98"] = value

    @property
    def property_value_99(self):
        """Get property_value_99

        Returns:
            float: the value of `property_value_99` or None if not set
        """
        return self["Property Value 99"]

    @property_value_99.setter
    def property_value_99(self, value=None):
        """  Corresponds to IDD Field `Property Value 99`

        Args:
            value (float): value for IDD Field `Property Value 99`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 99"] = value

    @property
    def property_value_100(self):
        """Get property_value_100

        Returns:
            float: the value of `property_value_100` or None if not set
        """
        return self["Property Value 100"]

    @property_value_100.setter
    def property_value_100(self, value=None):
        """  Corresponds to IDD Field `Property Value 100`

        Args:
            value (float): value for IDD Field `Property Value 100`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 100"] = value

    @property
    def property_value_101(self):
        """Get property_value_101

        Returns:
            float: the value of `property_value_101` or None if not set
        """
        return self["Property Value 101"]

    @property_value_101.setter
    def property_value_101(self, value=None):
        """  Corresponds to IDD Field `Property Value 101`

        Args:
            value (float): value for IDD Field `Property Value 101`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 101"] = value

    @property
    def property_value_102(self):
        """Get property_value_102

        Returns:
            float: the value of `property_value_102` or None if not set
        """
        return self["Property Value 102"]

    @property_value_102.setter
    def property_value_102(self, value=None):
        """  Corresponds to IDD Field `Property Value 102`

        Args:
            value (float): value for IDD Field `Property Value 102`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 102"] = value

    @property
    def property_value_103(self):
        """Get property_value_103

        Returns:
            float: the value of `property_value_103` or None if not set
        """
        return self["Property Value 103"]

    @property_value_103.setter
    def property_value_103(self, value=None):
        """  Corresponds to IDD Field `Property Value 103`

        Args:
            value (float): value for IDD Field `Property Value 103`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 103"] = value

    @property
    def property_value_104(self):
        """Get property_value_104

        Returns:
            float: the value of `property_value_104` or None if not set
        """
        return self["Property Value 104"]

    @property_value_104.setter
    def property_value_104(self, value=None):
        """  Corresponds to IDD Field `Property Value 104`

        Args:
            value (float): value for IDD Field `Property Value 104`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 104"] = value

    @property
    def property_value_105(self):
        """Get property_value_105

        Returns:
            float: the value of `property_value_105` or None if not set
        """
        return self["Property Value 105"]

    @property_value_105.setter
    def property_value_105(self, value=None):
        """  Corresponds to IDD Field `Property Value 105`

        Args:
            value (float): value for IDD Field `Property Value 105`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 105"] = value

    @property
    def property_value_106(self):
        """Get property_value_106

        Returns:
            float: the value of `property_value_106` or None if not set
        """
        return self["Property Value 106"]

    @property_value_106.setter
    def property_value_106(self, value=None):
        """  Corresponds to IDD Field `Property Value 106`

        Args:
            value (float): value for IDD Field `Property Value 106`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 106"] = value

    @property
    def property_value_107(self):
        """Get property_value_107

        Returns:
            float: the value of `property_value_107` or None if not set
        """
        return self["Property Value 107"]

    @property_value_107.setter
    def property_value_107(self, value=None):
        """  Corresponds to IDD Field `Property Value 107`

        Args:
            value (float): value for IDD Field `Property Value 107`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 107"] = value

    @property
    def property_value_108(self):
        """Get property_value_108

        Returns:
            float: the value of `property_value_108` or None if not set
        """
        return self["Property Value 108"]

    @property_value_108.setter
    def property_value_108(self, value=None):
        """  Corresponds to IDD Field `Property Value 108`

        Args:
            value (float): value for IDD Field `Property Value 108`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 108"] = value

    @property
    def property_value_109(self):
        """Get property_value_109

        Returns:
            float: the value of `property_value_109` or None if not set
        """
        return self["Property Value 109"]

    @property_value_109.setter
    def property_value_109(self, value=None):
        """  Corresponds to IDD Field `Property Value 109`

        Args:
            value (float): value for IDD Field `Property Value 109`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 109"] = value

    @property
    def property_value_110(self):
        """Get property_value_110

        Returns:
            float: the value of `property_value_110` or None if not set
        """
        return self["Property Value 110"]

    @property_value_110.setter
    def property_value_110(self, value=None):
        """  Corresponds to IDD Field `Property Value 110`

        Args:
            value (float): value for IDD Field `Property Value 110`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 110"] = value

    @property
    def property_value_111(self):
        """Get property_value_111

        Returns:
            float: the value of `property_value_111` or None if not set
        """
        return self["Property Value 111"]

    @property_value_111.setter
    def property_value_111(self, value=None):
        """  Corresponds to IDD Field `Property Value 111`

        Args:
            value (float): value for IDD Field `Property Value 111`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 111"] = value

    @property
    def property_value_112(self):
        """Get property_value_112

        Returns:
            float: the value of `property_value_112` or None if not set
        """
        return self["Property Value 112"]

    @property_value_112.setter
    def property_value_112(self, value=None):
        """  Corresponds to IDD Field `Property Value 112`

        Args:
            value (float): value for IDD Field `Property Value 112`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 112"] = value

    @property
    def property_value_113(self):
        """Get property_value_113

        Returns:
            float: the value of `property_value_113` or None if not set
        """
        return self["Property Value 113"]

    @property_value_113.setter
    def property_value_113(self, value=None):
        """  Corresponds to IDD Field `Property Value 113`

        Args:
            value (float): value for IDD Field `Property Value 113`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 113"] = value

    @property
    def property_value_114(self):
        """Get property_value_114

        Returns:
            float: the value of `property_value_114` or None if not set
        """
        return self["Property Value 114"]

    @property_value_114.setter
    def property_value_114(self, value=None):
        """  Corresponds to IDD Field `Property Value 114`

        Args:
            value (float): value for IDD Field `Property Value 114`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 114"] = value

    @property
    def property_value_115(self):
        """Get property_value_115

        Returns:
            float: the value of `property_value_115` or None if not set
        """
        return self["Property Value 115"]

    @property_value_115.setter
    def property_value_115(self, value=None):
        """  Corresponds to IDD Field `Property Value 115`

        Args:
            value (float): value for IDD Field `Property Value 115`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 115"] = value

    @property
    def property_value_116(self):
        """Get property_value_116

        Returns:
            float: the value of `property_value_116` or None if not set
        """
        return self["Property Value 116"]

    @property_value_116.setter
    def property_value_116(self, value=None):
        """  Corresponds to IDD Field `Property Value 116`

        Args:
            value (float): value for IDD Field `Property Value 116`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 116"] = value

    @property
    def property_value_117(self):
        """Get property_value_117

        Returns:
            float: the value of `property_value_117` or None if not set
        """
        return self["Property Value 117"]

    @property_value_117.setter
    def property_value_117(self, value=None):
        """  Corresponds to IDD Field `Property Value 117`

        Args:
            value (float): value for IDD Field `Property Value 117`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 117"] = value

    @property
    def property_value_118(self):
        """Get property_value_118

        Returns:
            float: the value of `property_value_118` or None if not set
        """
        return self["Property Value 118"]

    @property_value_118.setter
    def property_value_118(self, value=None):
        """  Corresponds to IDD Field `Property Value 118`

        Args:
            value (float): value for IDD Field `Property Value 118`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 118"] = value

    @property
    def property_value_119(self):
        """Get property_value_119

        Returns:
            float: the value of `property_value_119` or None if not set
        """
        return self["Property Value 119"]

    @property_value_119.setter
    def property_value_119(self, value=None):
        """  Corresponds to IDD Field `Property Value 119`

        Args:
            value (float): value for IDD Field `Property Value 119`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 119"] = value

    @property
    def property_value_120(self):
        """Get property_value_120

        Returns:
            float: the value of `property_value_120` or None if not set
        """
        return self["Property Value 120"]

    @property_value_120.setter
    def property_value_120(self, value=None):
        """  Corresponds to IDD Field `Property Value 120`

        Args:
            value (float): value for IDD Field `Property Value 120`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 120"] = value

    @property
    def property_value_121(self):
        """Get property_value_121

        Returns:
            float: the value of `property_value_121` or None if not set
        """
        return self["Property Value 121"]

    @property_value_121.setter
    def property_value_121(self, value=None):
        """  Corresponds to IDD Field `Property Value 121`

        Args:
            value (float): value for IDD Field `Property Value 121`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 121"] = value

    @property
    def property_value_122(self):
        """Get property_value_122

        Returns:
            float: the value of `property_value_122` or None if not set
        """
        return self["Property Value 122"]

    @property_value_122.setter
    def property_value_122(self, value=None):
        """  Corresponds to IDD Field `Property Value 122`

        Args:
            value (float): value for IDD Field `Property Value 122`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 122"] = value

    @property
    def property_value_123(self):
        """Get property_value_123

        Returns:
            float: the value of `property_value_123` or None if not set
        """
        return self["Property Value 123"]

    @property_value_123.setter
    def property_value_123(self, value=None):
        """  Corresponds to IDD Field `Property Value 123`

        Args:
            value (float): value for IDD Field `Property Value 123`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 123"] = value

    @property
    def property_value_124(self):
        """Get property_value_124

        Returns:
            float: the value of `property_value_124` or None if not set
        """
        return self["Property Value 124"]

    @property_value_124.setter
    def property_value_124(self, value=None):
        """  Corresponds to IDD Field `Property Value 124`

        Args:
            value (float): value for IDD Field `Property Value 124`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 124"] = value

    @property
    def property_value_125(self):
        """Get property_value_125

        Returns:
            float: the value of `property_value_125` or None if not set
        """
        return self["Property Value 125"]

    @property_value_125.setter
    def property_value_125(self, value=None):
        """  Corresponds to IDD Field `Property Value 125`

        Args:
            value (float): value for IDD Field `Property Value 125`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 125"] = value

    @property
    def property_value_126(self):
        """Get property_value_126

        Returns:
            float: the value of `property_value_126` or None if not set
        """
        return self["Property Value 126"]

    @property_value_126.setter
    def property_value_126(self, value=None):
        """  Corresponds to IDD Field `Property Value 126`

        Args:
            value (float): value for IDD Field `Property Value 126`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 126"] = value

    @property
    def property_value_127(self):
        """Get property_value_127

        Returns:
            float: the value of `property_value_127` or None if not set
        """
        return self["Property Value 127"]

    @property_value_127.setter
    def property_value_127(self, value=None):
        """  Corresponds to IDD Field `Property Value 127`

        Args:
            value (float): value for IDD Field `Property Value 127`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 127"] = value

    @property
    def property_value_128(self):
        """Get property_value_128

        Returns:
            float: the value of `property_value_128` or None if not set
        """
        return self["Property Value 128"]

    @property_value_128.setter
    def property_value_128(self, value=None):
        """  Corresponds to IDD Field `Property Value 128`

        Args:
            value (float): value for IDD Field `Property Value 128`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 128"] = value

    @property
    def property_value_129(self):
        """Get property_value_129

        Returns:
            float: the value of `property_value_129` or None if not set
        """
        return self["Property Value 129"]

    @property_value_129.setter
    def property_value_129(self, value=None):
        """  Corresponds to IDD Field `Property Value 129`

        Args:
            value (float): value for IDD Field `Property Value 129`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 129"] = value

    @property
    def property_value_130(self):
        """Get property_value_130

        Returns:
            float: the value of `property_value_130` or None if not set
        """
        return self["Property Value 130"]

    @property_value_130.setter
    def property_value_130(self, value=None):
        """  Corresponds to IDD Field `Property Value 130`

        Args:
            value (float): value for IDD Field `Property Value 130`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 130"] = value

    @property
    def property_value_131(self):
        """Get property_value_131

        Returns:
            float: the value of `property_value_131` or None if not set
        """
        return self["Property Value 131"]

    @property_value_131.setter
    def property_value_131(self, value=None):
        """  Corresponds to IDD Field `Property Value 131`

        Args:
            value (float): value for IDD Field `Property Value 131`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 131"] = value

    @property
    def property_value_132(self):
        """Get property_value_132

        Returns:
            float: the value of `property_value_132` or None if not set
        """
        return self["Property Value 132"]

    @property_value_132.setter
    def property_value_132(self, value=None):
        """  Corresponds to IDD Field `Property Value 132`

        Args:
            value (float): value for IDD Field `Property Value 132`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 132"] = value

    @property
    def property_value_133(self):
        """Get property_value_133

        Returns:
            float: the value of `property_value_133` or None if not set
        """
        return self["Property Value 133"]

    @property_value_133.setter
    def property_value_133(self, value=None):
        """  Corresponds to IDD Field `Property Value 133`

        Args:
            value (float): value for IDD Field `Property Value 133`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 133"] = value

    @property
    def property_value_134(self):
        """Get property_value_134

        Returns:
            float: the value of `property_value_134` or None if not set
        """
        return self["Property Value 134"]

    @property_value_134.setter
    def property_value_134(self, value=None):
        """  Corresponds to IDD Field `Property Value 134`

        Args:
            value (float): value for IDD Field `Property Value 134`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 134"] = value

    @property
    def property_value_135(self):
        """Get property_value_135

        Returns:
            float: the value of `property_value_135` or None if not set
        """
        return self["Property Value 135"]

    @property_value_135.setter
    def property_value_135(self, value=None):
        """  Corresponds to IDD Field `Property Value 135`

        Args:
            value (float): value for IDD Field `Property Value 135`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 135"] = value

    @property
    def property_value_136(self):
        """Get property_value_136

        Returns:
            float: the value of `property_value_136` or None if not set
        """
        return self["Property Value 136"]

    @property_value_136.setter
    def property_value_136(self, value=None):
        """  Corresponds to IDD Field `Property Value 136`

        Args:
            value (float): value for IDD Field `Property Value 136`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 136"] = value

    @property
    def property_value_137(self):
        """Get property_value_137

        Returns:
            float: the value of `property_value_137` or None if not set
        """
        return self["Property Value 137"]

    @property_value_137.setter
    def property_value_137(self, value=None):
        """  Corresponds to IDD Field `Property Value 137`

        Args:
            value (float): value for IDD Field `Property Value 137`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 137"] = value

    @property
    def property_value_138(self):
        """Get property_value_138

        Returns:
            float: the value of `property_value_138` or None if not set
        """
        return self["Property Value 138"]

    @property_value_138.setter
    def property_value_138(self, value=None):
        """  Corresponds to IDD Field `Property Value 138`

        Args:
            value (float): value for IDD Field `Property Value 138`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 138"] = value

    @property
    def property_value_139(self):
        """Get property_value_139

        Returns:
            float: the value of `property_value_139` or None if not set
        """
        return self["Property Value 139"]

    @property_value_139.setter
    def property_value_139(self, value=None):
        """  Corresponds to IDD Field `Property Value 139`

        Args:
            value (float): value for IDD Field `Property Value 139`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 139"] = value

    @property
    def property_value_140(self):
        """Get property_value_140

        Returns:
            float: the value of `property_value_140` or None if not set
        """
        return self["Property Value 140"]

    @property_value_140.setter
    def property_value_140(self, value=None):
        """  Corresponds to IDD Field `Property Value 140`

        Args:
            value (float): value for IDD Field `Property Value 140`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 140"] = value

    @property
    def property_value_141(self):
        """Get property_value_141

        Returns:
            float: the value of `property_value_141` or None if not set
        """
        return self["Property Value 141"]

    @property_value_141.setter
    def property_value_141(self, value=None):
        """  Corresponds to IDD Field `Property Value 141`

        Args:
            value (float): value for IDD Field `Property Value 141`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 141"] = value

    @property
    def property_value_142(self):
        """Get property_value_142

        Returns:
            float: the value of `property_value_142` or None if not set
        """
        return self["Property Value 142"]

    @property_value_142.setter
    def property_value_142(self, value=None):
        """  Corresponds to IDD Field `Property Value 142`

        Args:
            value (float): value for IDD Field `Property Value 142`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 142"] = value

    @property
    def property_value_143(self):
        """Get property_value_143

        Returns:
            float: the value of `property_value_143` or None if not set
        """
        return self["Property Value 143"]

    @property_value_143.setter
    def property_value_143(self, value=None):
        """  Corresponds to IDD Field `Property Value 143`

        Args:
            value (float): value for IDD Field `Property Value 143`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 143"] = value

    @property
    def property_value_144(self):
        """Get property_value_144

        Returns:
            float: the value of `property_value_144` or None if not set
        """
        return self["Property Value 144"]

    @property_value_144.setter
    def property_value_144(self, value=None):
        """  Corresponds to IDD Field `Property Value 144`

        Args:
            value (float): value for IDD Field `Property Value 144`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 144"] = value

    @property
    def property_value_145(self):
        """Get property_value_145

        Returns:
            float: the value of `property_value_145` or None if not set
        """
        return self["Property Value 145"]

    @property_value_145.setter
    def property_value_145(self, value=None):
        """  Corresponds to IDD Field `Property Value 145`

        Args:
            value (float): value for IDD Field `Property Value 145`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 145"] = value

    @property
    def property_value_146(self):
        """Get property_value_146

        Returns:
            float: the value of `property_value_146` or None if not set
        """
        return self["Property Value 146"]

    @property_value_146.setter
    def property_value_146(self, value=None):
        """  Corresponds to IDD Field `Property Value 146`

        Args:
            value (float): value for IDD Field `Property Value 146`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 146"] = value

    @property
    def property_value_147(self):
        """Get property_value_147

        Returns:
            float: the value of `property_value_147` or None if not set
        """
        return self["Property Value 147"]

    @property_value_147.setter
    def property_value_147(self, value=None):
        """  Corresponds to IDD Field `Property Value 147`

        Args:
            value (float): value for IDD Field `Property Value 147`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 147"] = value

    @property
    def property_value_148(self):
        """Get property_value_148

        Returns:
            float: the value of `property_value_148` or None if not set
        """
        return self["Property Value 148"]

    @property_value_148.setter
    def property_value_148(self, value=None):
        """  Corresponds to IDD Field `Property Value 148`

        Args:
            value (float): value for IDD Field `Property Value 148`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 148"] = value

    @property
    def property_value_149(self):
        """Get property_value_149

        Returns:
            float: the value of `property_value_149` or None if not set
        """
        return self["Property Value 149"]

    @property_value_149.setter
    def property_value_149(self, value=None):
        """  Corresponds to IDD Field `Property Value 149`

        Args:
            value (float): value for IDD Field `Property Value 149`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 149"] = value

    @property
    def property_value_150(self):
        """Get property_value_150

        Returns:
            float: the value of `property_value_150` or None if not set
        """
        return self["Property Value 150"]

    @property_value_150.setter
    def property_value_150(self, value=None):
        """  Corresponds to IDD Field `Property Value 150`

        Args:
            value (float): value for IDD Field `Property Value 150`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 150"] = value

    @property
    def property_value_151(self):
        """Get property_value_151

        Returns:
            float: the value of `property_value_151` or None if not set
        """
        return self["Property Value 151"]

    @property_value_151.setter
    def property_value_151(self, value=None):
        """  Corresponds to IDD Field `Property Value 151`

        Args:
            value (float): value for IDD Field `Property Value 151`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 151"] = value

    @property
    def property_value_152(self):
        """Get property_value_152

        Returns:
            float: the value of `property_value_152` or None if not set
        """
        return self["Property Value 152"]

    @property_value_152.setter
    def property_value_152(self, value=None):
        """  Corresponds to IDD Field `Property Value 152`

        Args:
            value (float): value for IDD Field `Property Value 152`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 152"] = value

    @property
    def property_value_153(self):
        """Get property_value_153

        Returns:
            float: the value of `property_value_153` or None if not set
        """
        return self["Property Value 153"]

    @property_value_153.setter
    def property_value_153(self, value=None):
        """  Corresponds to IDD Field `Property Value 153`

        Args:
            value (float): value for IDD Field `Property Value 153`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 153"] = value

    @property
    def property_value_154(self):
        """Get property_value_154

        Returns:
            float: the value of `property_value_154` or None if not set
        """
        return self["Property Value 154"]

    @property_value_154.setter
    def property_value_154(self, value=None):
        """  Corresponds to IDD Field `Property Value 154`

        Args:
            value (float): value for IDD Field `Property Value 154`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 154"] = value

    @property
    def property_value_155(self):
        """Get property_value_155

        Returns:
            float: the value of `property_value_155` or None if not set
        """
        return self["Property Value 155"]

    @property_value_155.setter
    def property_value_155(self, value=None):
        """  Corresponds to IDD Field `Property Value 155`

        Args:
            value (float): value for IDD Field `Property Value 155`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 155"] = value

    @property
    def property_value_156(self):
        """Get property_value_156

        Returns:
            float: the value of `property_value_156` or None if not set
        """
        return self["Property Value 156"]

    @property_value_156.setter
    def property_value_156(self, value=None):
        """  Corresponds to IDD Field `Property Value 156`

        Args:
            value (float): value for IDD Field `Property Value 156`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 156"] = value

    @property
    def property_value_157(self):
        """Get property_value_157

        Returns:
            float: the value of `property_value_157` or None if not set
        """
        return self["Property Value 157"]

    @property_value_157.setter
    def property_value_157(self, value=None):
        """  Corresponds to IDD Field `Property Value 157`

        Args:
            value (float): value for IDD Field `Property Value 157`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 157"] = value

    @property
    def property_value_158(self):
        """Get property_value_158

        Returns:
            float: the value of `property_value_158` or None if not set
        """
        return self["Property Value 158"]

    @property_value_158.setter
    def property_value_158(self, value=None):
        """  Corresponds to IDD Field `Property Value 158`

        Args:
            value (float): value for IDD Field `Property Value 158`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 158"] = value

    @property
    def property_value_159(self):
        """Get property_value_159

        Returns:
            float: the value of `property_value_159` or None if not set
        """
        return self["Property Value 159"]

    @property_value_159.setter
    def property_value_159(self, value=None):
        """  Corresponds to IDD Field `Property Value 159`

        Args:
            value (float): value for IDD Field `Property Value 159`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 159"] = value

    @property
    def property_value_160(self):
        """Get property_value_160

        Returns:
            float: the value of `property_value_160` or None if not set
        """
        return self["Property Value 160"]

    @property_value_160.setter
    def property_value_160(self, value=None):
        """  Corresponds to IDD Field `Property Value 160`

        Args:
            value (float): value for IDD Field `Property Value 160`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 160"] = value

    @property
    def property_value_161(self):
        """Get property_value_161

        Returns:
            float: the value of `property_value_161` or None if not set
        """
        return self["Property Value 161"]

    @property_value_161.setter
    def property_value_161(self, value=None):
        """  Corresponds to IDD Field `Property Value 161`

        Args:
            value (float): value for IDD Field `Property Value 161`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 161"] = value

    @property
    def property_value_162(self):
        """Get property_value_162

        Returns:
            float: the value of `property_value_162` or None if not set
        """
        return self["Property Value 162"]

    @property_value_162.setter
    def property_value_162(self, value=None):
        """  Corresponds to IDD Field `Property Value 162`

        Args:
            value (float): value for IDD Field `Property Value 162`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 162"] = value

    @property
    def property_value_163(self):
        """Get property_value_163

        Returns:
            float: the value of `property_value_163` or None if not set
        """
        return self["Property Value 163"]

    @property_value_163.setter
    def property_value_163(self, value=None):
        """  Corresponds to IDD Field `Property Value 163`

        Args:
            value (float): value for IDD Field `Property Value 163`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 163"] = value

    @property
    def property_value_164(self):
        """Get property_value_164

        Returns:
            float: the value of `property_value_164` or None if not set
        """
        return self["Property Value 164"]

    @property_value_164.setter
    def property_value_164(self, value=None):
        """  Corresponds to IDD Field `Property Value 164`

        Args:
            value (float): value for IDD Field `Property Value 164`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 164"] = value

    @property
    def property_value_165(self):
        """Get property_value_165

        Returns:
            float: the value of `property_value_165` or None if not set
        """
        return self["Property Value 165"]

    @property_value_165.setter
    def property_value_165(self, value=None):
        """  Corresponds to IDD Field `Property Value 165`

        Args:
            value (float): value for IDD Field `Property Value 165`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 165"] = value

    @property
    def property_value_166(self):
        """Get property_value_166

        Returns:
            float: the value of `property_value_166` or None if not set
        """
        return self["Property Value 166"]

    @property_value_166.setter
    def property_value_166(self, value=None):
        """  Corresponds to IDD Field `Property Value 166`

        Args:
            value (float): value for IDD Field `Property Value 166`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 166"] = value

    @property
    def property_value_167(self):
        """Get property_value_167

        Returns:
            float: the value of `property_value_167` or None if not set
        """
        return self["Property Value 167"]

    @property_value_167.setter
    def property_value_167(self, value=None):
        """  Corresponds to IDD Field `Property Value 167`

        Args:
            value (float): value for IDD Field `Property Value 167`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 167"] = value

    @property
    def property_value_168(self):
        """Get property_value_168

        Returns:
            float: the value of `property_value_168` or None if not set
        """
        return self["Property Value 168"]

    @property_value_168.setter
    def property_value_168(self, value=None):
        """  Corresponds to IDD Field `Property Value 168`

        Args:
            value (float): value for IDD Field `Property Value 168`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 168"] = value

    @property
    def property_value_169(self):
        """Get property_value_169

        Returns:
            float: the value of `property_value_169` or None if not set
        """
        return self["Property Value 169"]

    @property_value_169.setter
    def property_value_169(self, value=None):
        """  Corresponds to IDD Field `Property Value 169`

        Args:
            value (float): value for IDD Field `Property Value 169`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 169"] = value

    @property
    def property_value_170(self):
        """Get property_value_170

        Returns:
            float: the value of `property_value_170` or None if not set
        """
        return self["Property Value 170"]

    @property_value_170.setter
    def property_value_170(self, value=None):
        """  Corresponds to IDD Field `Property Value 170`

        Args:
            value (float): value for IDD Field `Property Value 170`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 170"] = value

    @property
    def property_value_171(self):
        """Get property_value_171

        Returns:
            float: the value of `property_value_171` or None if not set
        """
        return self["Property Value 171"]

    @property_value_171.setter
    def property_value_171(self, value=None):
        """  Corresponds to IDD Field `Property Value 171`

        Args:
            value (float): value for IDD Field `Property Value 171`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 171"] = value

    @property
    def property_value_172(self):
        """Get property_value_172

        Returns:
            float: the value of `property_value_172` or None if not set
        """
        return self["Property Value 172"]

    @property_value_172.setter
    def property_value_172(self, value=None):
        """  Corresponds to IDD Field `Property Value 172`

        Args:
            value (float): value for IDD Field `Property Value 172`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 172"] = value

    @property
    def property_value_173(self):
        """Get property_value_173

        Returns:
            float: the value of `property_value_173` or None if not set
        """
        return self["Property Value 173"]

    @property_value_173.setter
    def property_value_173(self, value=None):
        """  Corresponds to IDD Field `Property Value 173`

        Args:
            value (float): value for IDD Field `Property Value 173`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 173"] = value

    @property
    def property_value_174(self):
        """Get property_value_174

        Returns:
            float: the value of `property_value_174` or None if not set
        """
        return self["Property Value 174"]

    @property_value_174.setter
    def property_value_174(self, value=None):
        """  Corresponds to IDD Field `Property Value 174`

        Args:
            value (float): value for IDD Field `Property Value 174`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 174"] = value

    @property
    def property_value_175(self):
        """Get property_value_175

        Returns:
            float: the value of `property_value_175` or None if not set
        """
        return self["Property Value 175"]

    @property_value_175.setter
    def property_value_175(self, value=None):
        """  Corresponds to IDD Field `Property Value 175`

        Args:
            value (float): value for IDD Field `Property Value 175`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 175"] = value

    @property
    def property_value_176(self):
        """Get property_value_176

        Returns:
            float: the value of `property_value_176` or None if not set
        """
        return self["Property Value 176"]

    @property_value_176.setter
    def property_value_176(self, value=None):
        """  Corresponds to IDD Field `Property Value 176`

        Args:
            value (float): value for IDD Field `Property Value 176`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 176"] = value

    @property
    def property_value_177(self):
        """Get property_value_177

        Returns:
            float: the value of `property_value_177` or None if not set
        """
        return self["Property Value 177"]

    @property_value_177.setter
    def property_value_177(self, value=None):
        """  Corresponds to IDD Field `Property Value 177`

        Args:
            value (float): value for IDD Field `Property Value 177`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 177"] = value

    @property
    def property_value_178(self):
        """Get property_value_178

        Returns:
            float: the value of `property_value_178` or None if not set
        """
        return self["Property Value 178"]

    @property_value_178.setter
    def property_value_178(self, value=None):
        """  Corresponds to IDD Field `Property Value 178`

        Args:
            value (float): value for IDD Field `Property Value 178`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 178"] = value

    @property
    def property_value_179(self):
        """Get property_value_179

        Returns:
            float: the value of `property_value_179` or None if not set
        """
        return self["Property Value 179"]

    @property_value_179.setter
    def property_value_179(self, value=None):
        """  Corresponds to IDD Field `Property Value 179`

        Args:
            value (float): value for IDD Field `Property Value 179`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 179"] = value

    @property
    def property_value_180(self):
        """Get property_value_180

        Returns:
            float: the value of `property_value_180` or None if not set
        """
        return self["Property Value 180"]

    @property_value_180.setter
    def property_value_180(self, value=None):
        """  Corresponds to IDD Field `Property Value 180`

        Args:
            value (float): value for IDD Field `Property Value 180`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 180"] = value

    @property
    def property_value_181(self):
        """Get property_value_181

        Returns:
            float: the value of `property_value_181` or None if not set
        """
        return self["Property Value 181"]

    @property_value_181.setter
    def property_value_181(self, value=None):
        """  Corresponds to IDD Field `Property Value 181`

        Args:
            value (float): value for IDD Field `Property Value 181`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 181"] = value

    @property
    def property_value_182(self):
        """Get property_value_182

        Returns:
            float: the value of `property_value_182` or None if not set
        """
        return self["Property Value 182"]

    @property_value_182.setter
    def property_value_182(self, value=None):
        """  Corresponds to IDD Field `Property Value 182`

        Args:
            value (float): value for IDD Field `Property Value 182`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 182"] = value

    @property
    def property_value_183(self):
        """Get property_value_183

        Returns:
            float: the value of `property_value_183` or None if not set
        """
        return self["Property Value 183"]

    @property_value_183.setter
    def property_value_183(self, value=None):
        """  Corresponds to IDD Field `Property Value 183`

        Args:
            value (float): value for IDD Field `Property Value 183`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 183"] = value

    @property
    def property_value_184(self):
        """Get property_value_184

        Returns:
            float: the value of `property_value_184` or None if not set
        """
        return self["Property Value 184"]

    @property_value_184.setter
    def property_value_184(self, value=None):
        """  Corresponds to IDD Field `Property Value 184`

        Args:
            value (float): value for IDD Field `Property Value 184`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 184"] = value

    @property
    def property_value_185(self):
        """Get property_value_185

        Returns:
            float: the value of `property_value_185` or None if not set
        """
        return self["Property Value 185"]

    @property_value_185.setter
    def property_value_185(self, value=None):
        """  Corresponds to IDD Field `Property Value 185`

        Args:
            value (float): value for IDD Field `Property Value 185`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 185"] = value

    @property
    def property_value_186(self):
        """Get property_value_186

        Returns:
            float: the value of `property_value_186` or None if not set
        """
        return self["Property Value 186"]

    @property_value_186.setter
    def property_value_186(self, value=None):
        """  Corresponds to IDD Field `Property Value 186`

        Args:
            value (float): value for IDD Field `Property Value 186`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 186"] = value

    @property
    def property_value_187(self):
        """Get property_value_187

        Returns:
            float: the value of `property_value_187` or None if not set
        """
        return self["Property Value 187"]

    @property_value_187.setter
    def property_value_187(self, value=None):
        """  Corresponds to IDD Field `Property Value 187`

        Args:
            value (float): value for IDD Field `Property Value 187`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 187"] = value

    @property
    def property_value_188(self):
        """Get property_value_188

        Returns:
            float: the value of `property_value_188` or None if not set
        """
        return self["Property Value 188"]

    @property_value_188.setter
    def property_value_188(self, value=None):
        """  Corresponds to IDD Field `Property Value 188`

        Args:
            value (float): value for IDD Field `Property Value 188`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 188"] = value

    @property
    def property_value_189(self):
        """Get property_value_189

        Returns:
            float: the value of `property_value_189` or None if not set
        """
        return self["Property Value 189"]

    @property_value_189.setter
    def property_value_189(self, value=None):
        """  Corresponds to IDD Field `Property Value 189`

        Args:
            value (float): value for IDD Field `Property Value 189`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 189"] = value

    @property
    def property_value_190(self):
        """Get property_value_190

        Returns:
            float: the value of `property_value_190` or None if not set
        """
        return self["Property Value 190"]

    @property_value_190.setter
    def property_value_190(self, value=None):
        """  Corresponds to IDD Field `Property Value 190`

        Args:
            value (float): value for IDD Field `Property Value 190`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 190"] = value

    @property
    def property_value_191(self):
        """Get property_value_191

        Returns:
            float: the value of `property_value_191` or None if not set
        """
        return self["Property Value 191"]

    @property_value_191.setter
    def property_value_191(self, value=None):
        """  Corresponds to IDD Field `Property Value 191`

        Args:
            value (float): value for IDD Field `Property Value 191`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 191"] = value

    @property
    def property_value_192(self):
        """Get property_value_192

        Returns:
            float: the value of `property_value_192` or None if not set
        """
        return self["Property Value 192"]

    @property_value_192.setter
    def property_value_192(self, value=None):
        """  Corresponds to IDD Field `Property Value 192`

        Args:
            value (float): value for IDD Field `Property Value 192`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 192"] = value

    @property
    def property_value_193(self):
        """Get property_value_193

        Returns:
            float: the value of `property_value_193` or None if not set
        """
        return self["Property Value 193"]

    @property_value_193.setter
    def property_value_193(self, value=None):
        """  Corresponds to IDD Field `Property Value 193`

        Args:
            value (float): value for IDD Field `Property Value 193`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 193"] = value

    @property
    def property_value_194(self):
        """Get property_value_194

        Returns:
            float: the value of `property_value_194` or None if not set
        """
        return self["Property Value 194"]

    @property_value_194.setter
    def property_value_194(self, value=None):
        """  Corresponds to IDD Field `Property Value 194`

        Args:
            value (float): value for IDD Field `Property Value 194`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 194"] = value

    @property
    def property_value_195(self):
        """Get property_value_195

        Returns:
            float: the value of `property_value_195` or None if not set
        """
        return self["Property Value 195"]

    @property_value_195.setter
    def property_value_195(self, value=None):
        """  Corresponds to IDD Field `Property Value 195`

        Args:
            value (float): value for IDD Field `Property Value 195`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 195"] = value

    @property
    def property_value_196(self):
        """Get property_value_196

        Returns:
            float: the value of `property_value_196` or None if not set
        """
        return self["Property Value 196"]

    @property_value_196.setter
    def property_value_196(self, value=None):
        """  Corresponds to IDD Field `Property Value 196`

        Args:
            value (float): value for IDD Field `Property Value 196`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 196"] = value

    @property
    def property_value_197(self):
        """Get property_value_197

        Returns:
            float: the value of `property_value_197` or None if not set
        """
        return self["Property Value 197"]

    @property_value_197.setter
    def property_value_197(self, value=None):
        """  Corresponds to IDD Field `Property Value 197`

        Args:
            value (float): value for IDD Field `Property Value 197`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 197"] = value

    @property
    def property_value_198(self):
        """Get property_value_198

        Returns:
            float: the value of `property_value_198` or None if not set
        """
        return self["Property Value 198"]

    @property_value_198.setter
    def property_value_198(self, value=None):
        """  Corresponds to IDD Field `Property Value 198`

        Args:
            value (float): value for IDD Field `Property Value 198`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 198"] = value

    @property
    def property_value_199(self):
        """Get property_value_199

        Returns:
            float: the value of `property_value_199` or None if not set
        """
        return self["Property Value 199"]

    @property_value_199.setter
    def property_value_199(self, value=None):
        """  Corresponds to IDD Field `Property Value 199`

        Args:
            value (float): value for IDD Field `Property Value 199`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 199"] = value

    @property
    def property_value_200(self):
        """Get property_value_200

        Returns:
            float: the value of `property_value_200` or None if not set
        """
        return self["Property Value 200"]

    @property_value_200.setter
    def property_value_200(self, value=None):
        """  Corresponds to IDD Field `Property Value 200`

        Args:
            value (float): value for IDD Field `Property Value 200`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 200"] = value

    @property
    def property_value_201(self):
        """Get property_value_201

        Returns:
            float: the value of `property_value_201` or None if not set
        """
        return self["Property Value 201"]

    @property_value_201.setter
    def property_value_201(self, value=None):
        """  Corresponds to IDD Field `Property Value 201`

        Args:
            value (float): value for IDD Field `Property Value 201`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 201"] = value

    @property
    def property_value_202(self):
        """Get property_value_202

        Returns:
            float: the value of `property_value_202` or None if not set
        """
        return self["Property Value 202"]

    @property_value_202.setter
    def property_value_202(self, value=None):
        """  Corresponds to IDD Field `Property Value 202`

        Args:
            value (float): value for IDD Field `Property Value 202`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 202"] = value

    @property
    def property_value_203(self):
        """Get property_value_203

        Returns:
            float: the value of `property_value_203` or None if not set
        """
        return self["Property Value 203"]

    @property_value_203.setter
    def property_value_203(self, value=None):
        """  Corresponds to IDD Field `Property Value 203`

        Args:
            value (float): value for IDD Field `Property Value 203`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 203"] = value

    @property
    def property_value_204(self):
        """Get property_value_204

        Returns:
            float: the value of `property_value_204` or None if not set
        """
        return self["Property Value 204"]

    @property_value_204.setter
    def property_value_204(self, value=None):
        """  Corresponds to IDD Field `Property Value 204`

        Args:
            value (float): value for IDD Field `Property Value 204`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 204"] = value

    @property
    def property_value_205(self):
        """Get property_value_205

        Returns:
            float: the value of `property_value_205` or None if not set
        """
        return self["Property Value 205"]

    @property_value_205.setter
    def property_value_205(self, value=None):
        """  Corresponds to IDD Field `Property Value 205`

        Args:
            value (float): value for IDD Field `Property Value 205`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 205"] = value

    @property
    def property_value_206(self):
        """Get property_value_206

        Returns:
            float: the value of `property_value_206` or None if not set
        """
        return self["Property Value 206"]

    @property_value_206.setter
    def property_value_206(self, value=None):
        """  Corresponds to IDD Field `Property Value 206`

        Args:
            value (float): value for IDD Field `Property Value 206`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 206"] = value

    @property
    def property_value_207(self):
        """Get property_value_207

        Returns:
            float: the value of `property_value_207` or None if not set
        """
        return self["Property Value 207"]

    @property_value_207.setter
    def property_value_207(self, value=None):
        """  Corresponds to IDD Field `Property Value 207`

        Args:
            value (float): value for IDD Field `Property Value 207`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 207"] = value

    @property
    def property_value_208(self):
        """Get property_value_208

        Returns:
            float: the value of `property_value_208` or None if not set
        """
        return self["Property Value 208"]

    @property_value_208.setter
    def property_value_208(self, value=None):
        """  Corresponds to IDD Field `Property Value 208`

        Args:
            value (float): value for IDD Field `Property Value 208`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 208"] = value

    @property
    def property_value_209(self):
        """Get property_value_209

        Returns:
            float: the value of `property_value_209` or None if not set
        """
        return self["Property Value 209"]

    @property_value_209.setter
    def property_value_209(self, value=None):
        """  Corresponds to IDD Field `Property Value 209`

        Args:
            value (float): value for IDD Field `Property Value 209`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 209"] = value

    @property
    def property_value_210(self):
        """Get property_value_210

        Returns:
            float: the value of `property_value_210` or None if not set
        """
        return self["Property Value 210"]

    @property_value_210.setter
    def property_value_210(self, value=None):
        """  Corresponds to IDD Field `Property Value 210`

        Args:
            value (float): value for IDD Field `Property Value 210`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 210"] = value

    @property
    def property_value_211(self):
        """Get property_value_211

        Returns:
            float: the value of `property_value_211` or None if not set
        """
        return self["Property Value 211"]

    @property_value_211.setter
    def property_value_211(self, value=None):
        """  Corresponds to IDD Field `Property Value 211`

        Args:
            value (float): value for IDD Field `Property Value 211`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 211"] = value

    @property
    def property_value_212(self):
        """Get property_value_212

        Returns:
            float: the value of `property_value_212` or None if not set
        """
        return self["Property Value 212"]

    @property_value_212.setter
    def property_value_212(self, value=None):
        """  Corresponds to IDD Field `Property Value 212`

        Args:
            value (float): value for IDD Field `Property Value 212`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 212"] = value

    @property
    def property_value_213(self):
        """Get property_value_213

        Returns:
            float: the value of `property_value_213` or None if not set
        """
        return self["Property Value 213"]

    @property_value_213.setter
    def property_value_213(self, value=None):
        """  Corresponds to IDD Field `Property Value 213`

        Args:
            value (float): value for IDD Field `Property Value 213`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 213"] = value

    @property
    def property_value_214(self):
        """Get property_value_214

        Returns:
            float: the value of `property_value_214` or None if not set
        """
        return self["Property Value 214"]

    @property_value_214.setter
    def property_value_214(self, value=None):
        """  Corresponds to IDD Field `Property Value 214`

        Args:
            value (float): value for IDD Field `Property Value 214`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 214"] = value

    @property
    def property_value_215(self):
        """Get property_value_215

        Returns:
            float: the value of `property_value_215` or None if not set
        """
        return self["Property Value 215"]

    @property_value_215.setter
    def property_value_215(self, value=None):
        """  Corresponds to IDD Field `Property Value 215`

        Args:
            value (float): value for IDD Field `Property Value 215`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 215"] = value

    @property
    def property_value_216(self):
        """Get property_value_216

        Returns:
            float: the value of `property_value_216` or None if not set
        """
        return self["Property Value 216"]

    @property_value_216.setter
    def property_value_216(self, value=None):
        """  Corresponds to IDD Field `Property Value 216`

        Args:
            value (float): value for IDD Field `Property Value 216`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 216"] = value

    @property
    def property_value_217(self):
        """Get property_value_217

        Returns:
            float: the value of `property_value_217` or None if not set
        """
        return self["Property Value 217"]

    @property_value_217.setter
    def property_value_217(self, value=None):
        """  Corresponds to IDD Field `Property Value 217`

        Args:
            value (float): value for IDD Field `Property Value 217`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 217"] = value

    @property
    def property_value_218(self):
        """Get property_value_218

        Returns:
            float: the value of `property_value_218` or None if not set
        """
        return self["Property Value 218"]

    @property_value_218.setter
    def property_value_218(self, value=None):
        """  Corresponds to IDD Field `Property Value 218`

        Args:
            value (float): value for IDD Field `Property Value 218`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 218"] = value

    @property
    def property_value_219(self):
        """Get property_value_219

        Returns:
            float: the value of `property_value_219` or None if not set
        """
        return self["Property Value 219"]

    @property_value_219.setter
    def property_value_219(self, value=None):
        """  Corresponds to IDD Field `Property Value 219`

        Args:
            value (float): value for IDD Field `Property Value 219`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 219"] = value

    @property
    def property_value_220(self):
        """Get property_value_220

        Returns:
            float: the value of `property_value_220` or None if not set
        """
        return self["Property Value 220"]

    @property_value_220.setter
    def property_value_220(self, value=None):
        """  Corresponds to IDD Field `Property Value 220`

        Args:
            value (float): value for IDD Field `Property Value 220`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 220"] = value

    @property
    def property_value_221(self):
        """Get property_value_221

        Returns:
            float: the value of `property_value_221` or None if not set
        """
        return self["Property Value 221"]

    @property_value_221.setter
    def property_value_221(self, value=None):
        """  Corresponds to IDD Field `Property Value 221`

        Args:
            value (float): value for IDD Field `Property Value 221`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 221"] = value

    @property
    def property_value_222(self):
        """Get property_value_222

        Returns:
            float: the value of `property_value_222` or None if not set
        """
        return self["Property Value 222"]

    @property_value_222.setter
    def property_value_222(self, value=None):
        """  Corresponds to IDD Field `Property Value 222`

        Args:
            value (float): value for IDD Field `Property Value 222`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 222"] = value

    @property
    def property_value_223(self):
        """Get property_value_223

        Returns:
            float: the value of `property_value_223` or None if not set
        """
        return self["Property Value 223"]

    @property_value_223.setter
    def property_value_223(self, value=None):
        """  Corresponds to IDD Field `Property Value 223`

        Args:
            value (float): value for IDD Field `Property Value 223`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 223"] = value

    @property
    def property_value_224(self):
        """Get property_value_224

        Returns:
            float: the value of `property_value_224` or None if not set
        """
        return self["Property Value 224"]

    @property_value_224.setter
    def property_value_224(self, value=None):
        """  Corresponds to IDD Field `Property Value 224`

        Args:
            value (float): value for IDD Field `Property Value 224`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 224"] = value

    @property
    def property_value_225(self):
        """Get property_value_225

        Returns:
            float: the value of `property_value_225` or None if not set
        """
        return self["Property Value 225"]

    @property_value_225.setter
    def property_value_225(self, value=None):
        """  Corresponds to IDD Field `Property Value 225`

        Args:
            value (float): value for IDD Field `Property Value 225`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 225"] = value

    @property
    def property_value_226(self):
        """Get property_value_226

        Returns:
            float: the value of `property_value_226` or None if not set
        """
        return self["Property Value 226"]

    @property_value_226.setter
    def property_value_226(self, value=None):
        """  Corresponds to IDD Field `Property Value 226`

        Args:
            value (float): value for IDD Field `Property Value 226`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 226"] = value

    @property
    def property_value_227(self):
        """Get property_value_227

        Returns:
            float: the value of `property_value_227` or None if not set
        """
        return self["Property Value 227"]

    @property_value_227.setter
    def property_value_227(self, value=None):
        """  Corresponds to IDD Field `Property Value 227`

        Args:
            value (float): value for IDD Field `Property Value 227`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 227"] = value

    @property
    def property_value_228(self):
        """Get property_value_228

        Returns:
            float: the value of `property_value_228` or None if not set
        """
        return self["Property Value 228"]

    @property_value_228.setter
    def property_value_228(self, value=None):
        """  Corresponds to IDD Field `Property Value 228`

        Args:
            value (float): value for IDD Field `Property Value 228`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 228"] = value

    @property
    def property_value_229(self):
        """Get property_value_229

        Returns:
            float: the value of `property_value_229` or None if not set
        """
        return self["Property Value 229"]

    @property_value_229.setter
    def property_value_229(self, value=None):
        """  Corresponds to IDD Field `Property Value 229`

        Args:
            value (float): value for IDD Field `Property Value 229`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 229"] = value

    @property
    def property_value_230(self):
        """Get property_value_230

        Returns:
            float: the value of `property_value_230` or None if not set
        """
        return self["Property Value 230"]

    @property_value_230.setter
    def property_value_230(self, value=None):
        """  Corresponds to IDD Field `Property Value 230`

        Args:
            value (float): value for IDD Field `Property Value 230`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 230"] = value

    @property
    def property_value_231(self):
        """Get property_value_231

        Returns:
            float: the value of `property_value_231` or None if not set
        """
        return self["Property Value 231"]

    @property_value_231.setter
    def property_value_231(self, value=None):
        """  Corresponds to IDD Field `Property Value 231`

        Args:
            value (float): value for IDD Field `Property Value 231`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 231"] = value

    @property
    def property_value_232(self):
        """Get property_value_232

        Returns:
            float: the value of `property_value_232` or None if not set
        """
        return self["Property Value 232"]

    @property_value_232.setter
    def property_value_232(self, value=None):
        """  Corresponds to IDD Field `Property Value 232`

        Args:
            value (float): value for IDD Field `Property Value 232`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 232"] = value

    @property
    def property_value_233(self):
        """Get property_value_233

        Returns:
            float: the value of `property_value_233` or None if not set
        """
        return self["Property Value 233"]

    @property_value_233.setter
    def property_value_233(self, value=None):
        """  Corresponds to IDD Field `Property Value 233`

        Args:
            value (float): value for IDD Field `Property Value 233`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 233"] = value

    @property
    def property_value_234(self):
        """Get property_value_234

        Returns:
            float: the value of `property_value_234` or None if not set
        """
        return self["Property Value 234"]

    @property_value_234.setter
    def property_value_234(self, value=None):
        """  Corresponds to IDD Field `Property Value 234`

        Args:
            value (float): value for IDD Field `Property Value 234`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 234"] = value

    @property
    def property_value_235(self):
        """Get property_value_235

        Returns:
            float: the value of `property_value_235` or None if not set
        """
        return self["Property Value 235"]

    @property_value_235.setter
    def property_value_235(self, value=None):
        """  Corresponds to IDD Field `Property Value 235`

        Args:
            value (float): value for IDD Field `Property Value 235`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 235"] = value

    @property
    def property_value_236(self):
        """Get property_value_236

        Returns:
            float: the value of `property_value_236` or None if not set
        """
        return self["Property Value 236"]

    @property_value_236.setter
    def property_value_236(self, value=None):
        """  Corresponds to IDD Field `Property Value 236`

        Args:
            value (float): value for IDD Field `Property Value 236`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 236"] = value

    @property
    def property_value_237(self):
        """Get property_value_237

        Returns:
            float: the value of `property_value_237` or None if not set
        """
        return self["Property Value 237"]

    @property_value_237.setter
    def property_value_237(self, value=None):
        """  Corresponds to IDD Field `Property Value 237`

        Args:
            value (float): value for IDD Field `Property Value 237`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 237"] = value

    @property
    def property_value_238(self):
        """Get property_value_238

        Returns:
            float: the value of `property_value_238` or None if not set
        """
        return self["Property Value 238"]

    @property_value_238.setter
    def property_value_238(self, value=None):
        """  Corresponds to IDD Field `Property Value 238`

        Args:
            value (float): value for IDD Field `Property Value 238`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 238"] = value

    @property
    def property_value_239(self):
        """Get property_value_239

        Returns:
            float: the value of `property_value_239` or None if not set
        """
        return self["Property Value 239"]

    @property_value_239.setter
    def property_value_239(self, value=None):
        """  Corresponds to IDD Field `Property Value 239`

        Args:
            value (float): value for IDD Field `Property Value 239`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 239"] = value

    @property
    def property_value_240(self):
        """Get property_value_240

        Returns:
            float: the value of `property_value_240` or None if not set
        """
        return self["Property Value 240"]

    @property_value_240.setter
    def property_value_240(self, value=None):
        """  Corresponds to IDD Field `Property Value 240`

        Args:
            value (float): value for IDD Field `Property Value 240`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 240"] = value

    @property
    def property_value_241(self):
        """Get property_value_241

        Returns:
            float: the value of `property_value_241` or None if not set
        """
        return self["Property Value 241"]

    @property_value_241.setter
    def property_value_241(self, value=None):
        """  Corresponds to IDD Field `Property Value 241`

        Args:
            value (float): value for IDD Field `Property Value 241`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 241"] = value

    @property
    def property_value_242(self):
        """Get property_value_242

        Returns:
            float: the value of `property_value_242` or None if not set
        """
        return self["Property Value 242"]

    @property_value_242.setter
    def property_value_242(self, value=None):
        """  Corresponds to IDD Field `Property Value 242`

        Args:
            value (float): value for IDD Field `Property Value 242`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 242"] = value

    @property
    def property_value_243(self):
        """Get property_value_243

        Returns:
            float: the value of `property_value_243` or None if not set
        """
        return self["Property Value 243"]

    @property_value_243.setter
    def property_value_243(self, value=None):
        """  Corresponds to IDD Field `Property Value 243`

        Args:
            value (float): value for IDD Field `Property Value 243`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 243"] = value

    @property
    def property_value_244(self):
        """Get property_value_244

        Returns:
            float: the value of `property_value_244` or None if not set
        """
        return self["Property Value 244"]

    @property_value_244.setter
    def property_value_244(self, value=None):
        """  Corresponds to IDD Field `Property Value 244`

        Args:
            value (float): value for IDD Field `Property Value 244`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 244"] = value

    @property
    def property_value_245(self):
        """Get property_value_245

        Returns:
            float: the value of `property_value_245` or None if not set
        """
        return self["Property Value 245"]

    @property_value_245.setter
    def property_value_245(self, value=None):
        """  Corresponds to IDD Field `Property Value 245`

        Args:
            value (float): value for IDD Field `Property Value 245`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 245"] = value

    @property
    def property_value_246(self):
        """Get property_value_246

        Returns:
            float: the value of `property_value_246` or None if not set
        """
        return self["Property Value 246"]

    @property_value_246.setter
    def property_value_246(self, value=None):
        """  Corresponds to IDD Field `Property Value 246`

        Args:
            value (float): value for IDD Field `Property Value 246`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 246"] = value

    @property
    def property_value_247(self):
        """Get property_value_247

        Returns:
            float: the value of `property_value_247` or None if not set
        """
        return self["Property Value 247"]

    @property_value_247.setter
    def property_value_247(self, value=None):
        """  Corresponds to IDD Field `Property Value 247`

        Args:
            value (float): value for IDD Field `Property Value 247`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 247"] = value

    @property
    def property_value_248(self):
        """Get property_value_248

        Returns:
            float: the value of `property_value_248` or None if not set
        """
        return self["Property Value 248"]

    @property_value_248.setter
    def property_value_248(self, value=None):
        """  Corresponds to IDD Field `Property Value 248`

        Args:
            value (float): value for IDD Field `Property Value 248`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 248"] = value

    @property
    def property_value_249(self):
        """Get property_value_249

        Returns:
            float: the value of `property_value_249` or None if not set
        """
        return self["Property Value 249"]

    @property_value_249.setter
    def property_value_249(self, value=None):
        """  Corresponds to IDD Field `Property Value 249`

        Args:
            value (float): value for IDD Field `Property Value 249`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 249"] = value

    @property
    def property_value_250(self):
        """Get property_value_250

        Returns:
            float: the value of `property_value_250` or None if not set
        """
        return self["Property Value 250"]

    @property_value_250.setter
    def property_value_250(self, value=None):
        """  Corresponds to IDD Field `Property Value 250`

        Args:
            value (float): value for IDD Field `Property Value 250`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 250"] = value


class FluidPropertiesSuperheated(DataObject):
    """ Corresponds to IDD object `FluidProperties:Superheated`
        fluid properties for the superheated region
    """
    schema = {'min-fields': 0, 'name': u'FluidProperties:Superheated', 'pyname': u'FluidPropertiesSuperheated', 'format': None, 'fields': OrderedDict([(u'fluid name', {'name': u'Fluid Name', 'pyname': u'fluid_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fluid property type', {'name': u'Fluid Property Type', 'pyname': u'fluid_property_type', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Enthalpy', u'Density'], 'autocalculatable': False, 'type': 'alpha'}), (u'temperature values name', {'name': u'Temperature Values Name', 'pyname': u'temperature_values_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'pressure', {'name': u'Pressure', 'pyname': u'pressure', 'minimum>': 0.0, 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real', 'unit': u'Pa'}), (u'property value 1', {'name': u'Property Value 1', 'pyname': u'property_value_1', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 2', {'name': u'Property Value 2', 'pyname': u'property_value_2', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 3', {'name': u'Property Value 3', 'pyname': u'property_value_3', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 4', {'name': u'Property Value 4', 'pyname': u'property_value_4', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 5', {'name': u'Property Value 5', 'pyname': u'property_value_5', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 6', {'name': u'Property Value 6', 'pyname': u'property_value_6', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 7', {'name': u'Property Value 7', 'pyname': u'property_value_7', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 8', {'name': u'Property Value 8', 'pyname': u'property_value_8', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 9', {'name': u'Property Value 9', 'pyname': u'property_value_9', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 10', {'name': u'Property Value 10', 'pyname': u'property_value_10', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 11', {'name': u'Property Value 11', 'pyname': u'property_value_11', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 12', {'name': u'Property Value 12', 'pyname': u'property_value_12', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 13', {'name': u'Property Value 13', 'pyname': u'property_value_13', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 14', {'name': u'Property Value 14', 'pyname': u'property_value_14', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 15', {'name': u'Property Value 15', 'pyname': u'property_value_15', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 16', {'name': u'Property Value 16', 'pyname': u'property_value_16', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 17', {'name': u'Property Value 17', 'pyname': u'property_value_17', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 18', {'name': u'Property Value 18', 'pyname': u'property_value_18', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 19', {'name': u'Property Value 19', 'pyname': u'property_value_19', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 20', {'name': u'Property Value 20', 'pyname': u'property_value_20', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 21', {'name': u'Property Value 21', 'pyname': u'property_value_21', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 22', {'name': u'Property Value 22', 'pyname': u'property_value_22', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 23', {'name': u'Property Value 23', 'pyname': u'property_value_23', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 24', {'name': u'Property Value 24', 'pyname': u'property_value_24', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 25', {'name': u'Property Value 25', 'pyname': u'property_value_25', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 26', {'name': u'Property Value 26', 'pyname': u'property_value_26', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 27', {'name': u'Property Value 27', 'pyname': u'property_value_27', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 28', {'name': u'Property Value 28', 'pyname': u'property_value_28', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 29', {'name': u'Property Value 29', 'pyname': u'property_value_29', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 30', {'name': u'Property Value 30', 'pyname': u'property_value_30', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 31', {'name': u'Property Value 31', 'pyname': u'property_value_31', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 32', {'name': u'Property Value 32', 'pyname': u'property_value_32', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 33', {'name': u'Property Value 33', 'pyname': u'property_value_33', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 34', {'name': u'Property Value 34', 'pyname': u'property_value_34', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 35', {'name': u'Property Value 35', 'pyname': u'property_value_35', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 36', {'name': u'Property Value 36', 'pyname': u'property_value_36', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 37', {'name': u'Property Value 37', 'pyname': u'property_value_37', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 38', {'name': u'Property Value 38', 'pyname': u'property_value_38', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 39', {'name': u'Property Value 39', 'pyname': u'property_value_39', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 40', {'name': u'Property Value 40', 'pyname': u'property_value_40', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 41', {'name': u'Property Value 41', 'pyname': u'property_value_41', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 42', {'name': u'Property Value 42', 'pyname': u'property_value_42', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 43', {'name': u'Property Value 43', 'pyname': u'property_value_43', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 44', {'name': u'Property Value 44', 'pyname': u'property_value_44', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 45', {'name': u'Property Value 45', 'pyname': u'property_value_45', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 46', {'name': u'Property Value 46', 'pyname': u'property_value_46', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 47', {'name': u'Property Value 47', 'pyname': u'property_value_47', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 48', {'name': u'Property Value 48', 'pyname': u'property_value_48', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 49', {'name': u'Property Value 49', 'pyname': u'property_value_49', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 50', {'name': u'Property Value 50', 'pyname': u'property_value_50', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 51', {'name': u'Property Value 51', 'pyname': u'property_value_51', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 52', {'name': u'Property Value 52', 'pyname': u'property_value_52', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 53', {'name': u'Property Value 53', 'pyname': u'property_value_53', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 54', {'name': u'Property Value 54', 'pyname': u'property_value_54', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 55', {'name': u'Property Value 55', 'pyname': u'property_value_55', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 56', {'name': u'Property Value 56', 'pyname': u'property_value_56', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 57', {'name': u'Property Value 57', 'pyname': u'property_value_57', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 58', {'name': u'Property Value 58', 'pyname': u'property_value_58', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 59', {'name': u'Property Value 59', 'pyname': u'property_value_59', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 60', {'name': u'Property Value 60', 'pyname': u'property_value_60', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 61', {'name': u'Property Value 61', 'pyname': u'property_value_61', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 62', {'name': u'Property Value 62', 'pyname': u'property_value_62', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 63', {'name': u'Property Value 63', 'pyname': u'property_value_63', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 64', {'name': u'Property Value 64', 'pyname': u'property_value_64', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 65', {'name': u'Property Value 65', 'pyname': u'property_value_65', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 66', {'name': u'Property Value 66', 'pyname': u'property_value_66', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 67', {'name': u'Property Value 67', 'pyname': u'property_value_67', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 68', {'name': u'Property Value 68', 'pyname': u'property_value_68', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 69', {'name': u'Property Value 69', 'pyname': u'property_value_69', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 70', {'name': u'Property Value 70', 'pyname': u'property_value_70', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 71', {'name': u'Property Value 71', 'pyname': u'property_value_71', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 72', {'name': u'Property Value 72', 'pyname': u'property_value_72', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 73', {'name': u'Property Value 73', 'pyname': u'property_value_73', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 74', {'name': u'Property Value 74', 'pyname': u'property_value_74', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 75', {'name': u'Property Value 75', 'pyname': u'property_value_75', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 76', {'name': u'Property Value 76', 'pyname': u'property_value_76', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 77', {'name': u'Property Value 77', 'pyname': u'property_value_77', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 78', {'name': u'Property Value 78', 'pyname': u'property_value_78', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 79', {'name': u'Property Value 79', 'pyname': u'property_value_79', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 80', {'name': u'Property Value 80', 'pyname': u'property_value_80', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 81', {'name': u'Property Value 81', 'pyname': u'property_value_81', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 82', {'name': u'Property Value 82', 'pyname': u'property_value_82', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 83', {'name': u'Property Value 83', 'pyname': u'property_value_83', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 84', {'name': u'Property Value 84', 'pyname': u'property_value_84', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 85', {'name': u'Property Value 85', 'pyname': u'property_value_85', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 86', {'name': u'Property Value 86', 'pyname': u'property_value_86', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 87', {'name': u'Property Value 87', 'pyname': u'property_value_87', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 88', {'name': u'Property Value 88', 'pyname': u'property_value_88', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 89', {'name': u'Property Value 89', 'pyname': u'property_value_89', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 90', {'name': u'Property Value 90', 'pyname': u'property_value_90', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 91', {'name': u'Property Value 91', 'pyname': u'property_value_91', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 92', {'name': u'Property Value 92', 'pyname': u'property_value_92', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 93', {'name': u'Property Value 93', 'pyname': u'property_value_93', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 94', {'name': u'Property Value 94', 'pyname': u'property_value_94', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 95', {'name': u'Property Value 95', 'pyname': u'property_value_95', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 96', {'name': u'Property Value 96', 'pyname': u'property_value_96', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 97', {'name': u'Property Value 97', 'pyname': u'property_value_97', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 98', {'name': u'Property Value 98', 'pyname': u'property_value_98', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 99', {'name': u'Property Value 99', 'pyname': u'property_value_99', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 100', {'name': u'Property Value 100', 'pyname': u'property_value_100', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 101', {'name': u'Property Value 101', 'pyname': u'property_value_101', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 102', {'name': u'Property Value 102', 'pyname': u'property_value_102', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 103', {'name': u'Property Value 103', 'pyname': u'property_value_103', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 104', {'name': u'Property Value 104', 'pyname': u'property_value_104', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 105', {'name': u'Property Value 105', 'pyname': u'property_value_105', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 106', {'name': u'Property Value 106', 'pyname': u'property_value_106', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 107', {'name': u'Property Value 107', 'pyname': u'property_value_107', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 108', {'name': u'Property Value 108', 'pyname': u'property_value_108', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 109', {'name': u'Property Value 109', 'pyname': u'property_value_109', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 110', {'name': u'Property Value 110', 'pyname': u'property_value_110', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 111', {'name': u'Property Value 111', 'pyname': u'property_value_111', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 112', {'name': u'Property Value 112', 'pyname': u'property_value_112', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 113', {'name': u'Property Value 113', 'pyname': u'property_value_113', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 114', {'name': u'Property Value 114', 'pyname': u'property_value_114', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 115', {'name': u'Property Value 115', 'pyname': u'property_value_115', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 116', {'name': u'Property Value 116', 'pyname': u'property_value_116', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 117', {'name': u'Property Value 117', 'pyname': u'property_value_117', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 118', {'name': u'Property Value 118', 'pyname': u'property_value_118', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 119', {'name': u'Property Value 119', 'pyname': u'property_value_119', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 120', {'name': u'Property Value 120', 'pyname': u'property_value_120', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 121', {'name': u'Property Value 121', 'pyname': u'property_value_121', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 122', {'name': u'Property Value 122', 'pyname': u'property_value_122', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 123', {'name': u'Property Value 123', 'pyname': u'property_value_123', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 124', {'name': u'Property Value 124', 'pyname': u'property_value_124', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 125', {'name': u'Property Value 125', 'pyname': u'property_value_125', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 126', {'name': u'Property Value 126', 'pyname': u'property_value_126', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 127', {'name': u'Property Value 127', 'pyname': u'property_value_127', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 128', {'name': u'Property Value 128', 'pyname': u'property_value_128', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 129', {'name': u'Property Value 129', 'pyname': u'property_value_129', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 130', {'name': u'Property Value 130', 'pyname': u'property_value_130', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 131', {'name': u'Property Value 131', 'pyname': u'property_value_131', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 132', {'name': u'Property Value 132', 'pyname': u'property_value_132', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 133', {'name': u'Property Value 133', 'pyname': u'property_value_133', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 134', {'name': u'Property Value 134', 'pyname': u'property_value_134', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 135', {'name': u'Property Value 135', 'pyname': u'property_value_135', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 136', {'name': u'Property Value 136', 'pyname': u'property_value_136', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 137', {'name': u'Property Value 137', 'pyname': u'property_value_137', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 138', {'name': u'Property Value 138', 'pyname': u'property_value_138', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 139', {'name': u'Property Value 139', 'pyname': u'property_value_139', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 140', {'name': u'Property Value 140', 'pyname': u'property_value_140', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 141', {'name': u'Property Value 141', 'pyname': u'property_value_141', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 142', {'name': u'Property Value 142', 'pyname': u'property_value_142', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 143', {'name': u'Property Value 143', 'pyname': u'property_value_143', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 144', {'name': u'Property Value 144', 'pyname': u'property_value_144', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 145', {'name': u'Property Value 145', 'pyname': u'property_value_145', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 146', {'name': u'Property Value 146', 'pyname': u'property_value_146', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 147', {'name': u'Property Value 147', 'pyname': u'property_value_147', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 148', {'name': u'Property Value 148', 'pyname': u'property_value_148', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 149', {'name': u'Property Value 149', 'pyname': u'property_value_149', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 150', {'name': u'Property Value 150', 'pyname': u'property_value_150', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 151', {'name': u'Property Value 151', 'pyname': u'property_value_151', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 152', {'name': u'Property Value 152', 'pyname': u'property_value_152', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 153', {'name': u'Property Value 153', 'pyname': u'property_value_153', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 154', {'name': u'Property Value 154', 'pyname': u'property_value_154', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 155', {'name': u'Property Value 155', 'pyname': u'property_value_155', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 156', {'name': u'Property Value 156', 'pyname': u'property_value_156', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 157', {'name': u'Property Value 157', 'pyname': u'property_value_157', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 158', {'name': u'Property Value 158', 'pyname': u'property_value_158', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 159', {'name': u'Property Value 159', 'pyname': u'property_value_159', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 160', {'name': u'Property Value 160', 'pyname': u'property_value_160', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 161', {'name': u'Property Value 161', 'pyname': u'property_value_161', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 162', {'name': u'Property Value 162', 'pyname': u'property_value_162', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 163', {'name': u'Property Value 163', 'pyname': u'property_value_163', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 164', {'name': u'Property Value 164', 'pyname': u'property_value_164', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 165', {'name': u'Property Value 165', 'pyname': u'property_value_165', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 166', {'name': u'Property Value 166', 'pyname': u'property_value_166', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 167', {'name': u'Property Value 167', 'pyname': u'property_value_167', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 168', {'name': u'Property Value 168', 'pyname': u'property_value_168', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 169', {'name': u'Property Value 169', 'pyname': u'property_value_169', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 170', {'name': u'Property Value 170', 'pyname': u'property_value_170', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 171', {'name': u'Property Value 171', 'pyname': u'property_value_171', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 172', {'name': u'Property Value 172', 'pyname': u'property_value_172', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 173', {'name': u'Property Value 173', 'pyname': u'property_value_173', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 174', {'name': u'Property Value 174', 'pyname': u'property_value_174', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 175', {'name': u'Property Value 175', 'pyname': u'property_value_175', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 176', {'name': u'Property Value 176', 'pyname': u'property_value_176', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 177', {'name': u'Property Value 177', 'pyname': u'property_value_177', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 178', {'name': u'Property Value 178', 'pyname': u'property_value_178', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 179', {'name': u'Property Value 179', 'pyname': u'property_value_179', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 180', {'name': u'Property Value 180', 'pyname': u'property_value_180', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 181', {'name': u'Property Value 181', 'pyname': u'property_value_181', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 182', {'name': u'Property Value 182', 'pyname': u'property_value_182', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 183', {'name': u'Property Value 183', 'pyname': u'property_value_183', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 184', {'name': u'Property Value 184', 'pyname': u'property_value_184', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 185', {'name': u'Property Value 185', 'pyname': u'property_value_185', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 186', {'name': u'Property Value 186', 'pyname': u'property_value_186', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 187', {'name': u'Property Value 187', 'pyname': u'property_value_187', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 188', {'name': u'Property Value 188', 'pyname': u'property_value_188', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 189', {'name': u'Property Value 189', 'pyname': u'property_value_189', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 190', {'name': u'Property Value 190', 'pyname': u'property_value_190', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 191', {'name': u'Property Value 191', 'pyname': u'property_value_191', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 192', {'name': u'Property Value 192', 'pyname': u'property_value_192', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 193', {'name': u'Property Value 193', 'pyname': u'property_value_193', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 194', {'name': u'Property Value 194', 'pyname': u'property_value_194', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 195', {'name': u'Property Value 195', 'pyname': u'property_value_195', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 196', {'name': u'Property Value 196', 'pyname': u'property_value_196', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 197', {'name': u'Property Value 197', 'pyname': u'property_value_197', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 198', {'name': u'Property Value 198', 'pyname': u'property_value_198', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 199', {'name': u'Property Value 199', 'pyname': u'property_value_199', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 200', {'name': u'Property Value 200', 'pyname': u'property_value_200', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 201', {'name': u'Property Value 201', 'pyname': u'property_value_201', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 202', {'name': u'Property Value 202', 'pyname': u'property_value_202', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 203', {'name': u'Property Value 203', 'pyname': u'property_value_203', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 204', {'name': u'Property Value 204', 'pyname': u'property_value_204', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 205', {'name': u'Property Value 205', 'pyname': u'property_value_205', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 206', {'name': u'Property Value 206', 'pyname': u'property_value_206', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 207', {'name': u'Property Value 207', 'pyname': u'property_value_207', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 208', {'name': u'Property Value 208', 'pyname': u'property_value_208', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 209', {'name': u'Property Value 209', 'pyname': u'property_value_209', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 210', {'name': u'Property Value 210', 'pyname': u'property_value_210', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 211', {'name': u'Property Value 211', 'pyname': u'property_value_211', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 212', {'name': u'Property Value 212', 'pyname': u'property_value_212', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 213', {'name': u'Property Value 213', 'pyname': u'property_value_213', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 214', {'name': u'Property Value 214', 'pyname': u'property_value_214', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 215', {'name': u'Property Value 215', 'pyname': u'property_value_215', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 216', {'name': u'Property Value 216', 'pyname': u'property_value_216', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 217', {'name': u'Property Value 217', 'pyname': u'property_value_217', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 218', {'name': u'Property Value 218', 'pyname': u'property_value_218', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 219', {'name': u'Property Value 219', 'pyname': u'property_value_219', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 220', {'name': u'Property Value 220', 'pyname': u'property_value_220', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 221', {'name': u'Property Value 221', 'pyname': u'property_value_221', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 222', {'name': u'Property Value 222', 'pyname': u'property_value_222', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 223', {'name': u'Property Value 223', 'pyname': u'property_value_223', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 224', {'name': u'Property Value 224', 'pyname': u'property_value_224', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 225', {'name': u'Property Value 225', 'pyname': u'property_value_225', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 226', {'name': u'Property Value 226', 'pyname': u'property_value_226', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 227', {'name': u'Property Value 227', 'pyname': u'property_value_227', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 228', {'name': u'Property Value 228', 'pyname': u'property_value_228', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 229', {'name': u'Property Value 229', 'pyname': u'property_value_229', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 230', {'name': u'Property Value 230', 'pyname': u'property_value_230', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 231', {'name': u'Property Value 231', 'pyname': u'property_value_231', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 232', {'name': u'Property Value 232', 'pyname': u'property_value_232', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 233', {'name': u'Property Value 233', 'pyname': u'property_value_233', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 234', {'name': u'Property Value 234', 'pyname': u'property_value_234', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 235', {'name': u'Property Value 235', 'pyname': u'property_value_235', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 236', {'name': u'Property Value 236', 'pyname': u'property_value_236', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 237', {'name': u'Property Value 237', 'pyname': u'property_value_237', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 238', {'name': u'Property Value 238', 'pyname': u'property_value_238', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 239', {'name': u'Property Value 239', 'pyname': u'property_value_239', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 240', {'name': u'Property Value 240', 'pyname': u'property_value_240', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 241', {'name': u'Property Value 241', 'pyname': u'property_value_241', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 242', {'name': u'Property Value 242', 'pyname': u'property_value_242', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 243', {'name': u'Property Value 243', 'pyname': u'property_value_243', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 244', {'name': u'Property Value 244', 'pyname': u'property_value_244', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 245', {'name': u'Property Value 245', 'pyname': u'property_value_245', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 246', {'name': u'Property Value 246', 'pyname': u'property_value_246', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 247', {'name': u'Property Value 247', 'pyname': u'property_value_247', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 248', {'name': u'Property Value 248', 'pyname': u'property_value_248', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 249', {'name': u'Property Value 249', 'pyname': u'property_value_249', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 250', {'name': u'Property Value 250', 'pyname': u'property_value_250', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def fluid_name(self):
        """Get fluid_name

        Returns:
            str: the value of `fluid_name` or None if not set
        """
        return self["Fluid Name"]

    @fluid_name.setter
    def fluid_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Name`

        Args:
            value (str): value for IDD Field `Fluid Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Name"] = value

    @property
    def fluid_property_type(self):
        """Get fluid_property_type

        Returns:
            str: the value of `fluid_property_type` or None if not set
        """
        return self["Fluid Property Type"]

    @fluid_property_type.setter
    def fluid_property_type(self, value=None):
        """  Corresponds to IDD Field `Fluid Property Type`
        Enthalpy Units are J/kg
        Density Units are kg/m3

        Args:
            value (str): value for IDD Field `Fluid Property Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Property Type"] = value

    @property
    def temperature_values_name(self):
        """Get temperature_values_name

        Returns:
            str: the value of `temperature_values_name` or None if not set
        """
        return self["Temperature Values Name"]

    @temperature_values_name.setter
    def temperature_values_name(self, value=None):
        """  Corresponds to IDD Field `Temperature Values Name`
        Enter the name of a FluidProperties:Temperatures object.

        Args:
            value (str): value for IDD Field `Temperature Values Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Values Name"] = value

    @property
    def pressure(self):
        """Get pressure

        Returns:
            float: the value of `pressure` or None if not set
        """
        return self["Pressure"]

    @pressure.setter
    def pressure(self, value=None):
        """  Corresponds to IDD Field `Pressure`
        pressure for this list of properties

        Args:
            value (float): value for IDD Field `Pressure`
                Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Pressure"] = value

    @property
    def property_value_1(self):
        """Get property_value_1

        Returns:
            float: the value of `property_value_1` or None if not set
        """
        return self["Property Value 1"]

    @property_value_1.setter
    def property_value_1(self, value=None):
        """  Corresponds to IDD Field `Property Value 1`

        Args:
            value (float): value for IDD Field `Property Value 1`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 1"] = value

    @property
    def property_value_2(self):
        """Get property_value_2

        Returns:
            float: the value of `property_value_2` or None if not set
        """
        return self["Property Value 2"]

    @property_value_2.setter
    def property_value_2(self, value=None):
        """  Corresponds to IDD Field `Property Value 2`

        Args:
            value (float): value for IDD Field `Property Value 2`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 2"] = value

    @property
    def property_value_3(self):
        """Get property_value_3

        Returns:
            float: the value of `property_value_3` or None if not set
        """
        return self["Property Value 3"]

    @property_value_3.setter
    def property_value_3(self, value=None):
        """  Corresponds to IDD Field `Property Value 3`

        Args:
            value (float): value for IDD Field `Property Value 3`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 3"] = value

    @property
    def property_value_4(self):
        """Get property_value_4

        Returns:
            float: the value of `property_value_4` or None if not set
        """
        return self["Property Value 4"]

    @property_value_4.setter
    def property_value_4(self, value=None):
        """  Corresponds to IDD Field `Property Value 4`

        Args:
            value (float): value for IDD Field `Property Value 4`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 4"] = value

    @property
    def property_value_5(self):
        """Get property_value_5

        Returns:
            float: the value of `property_value_5` or None if not set
        """
        return self["Property Value 5"]

    @property_value_5.setter
    def property_value_5(self, value=None):
        """  Corresponds to IDD Field `Property Value 5`

        Args:
            value (float): value for IDD Field `Property Value 5`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 5"] = value

    @property
    def property_value_6(self):
        """Get property_value_6

        Returns:
            float: the value of `property_value_6` or None if not set
        """
        return self["Property Value 6"]

    @property_value_6.setter
    def property_value_6(self, value=None):
        """  Corresponds to IDD Field `Property Value 6`

        Args:
            value (float): value for IDD Field `Property Value 6`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 6"] = value

    @property
    def property_value_7(self):
        """Get property_value_7

        Returns:
            float: the value of `property_value_7` or None if not set
        """
        return self["Property Value 7"]

    @property_value_7.setter
    def property_value_7(self, value=None):
        """  Corresponds to IDD Field `Property Value 7`

        Args:
            value (float): value for IDD Field `Property Value 7`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 7"] = value

    @property
    def property_value_8(self):
        """Get property_value_8

        Returns:
            float: the value of `property_value_8` or None if not set
        """
        return self["Property Value 8"]

    @property_value_8.setter
    def property_value_8(self, value=None):
        """  Corresponds to IDD Field `Property Value 8`

        Args:
            value (float): value for IDD Field `Property Value 8`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 8"] = value

    @property
    def property_value_9(self):
        """Get property_value_9

        Returns:
            float: the value of `property_value_9` or None if not set
        """
        return self["Property Value 9"]

    @property_value_9.setter
    def property_value_9(self, value=None):
        """  Corresponds to IDD Field `Property Value 9`

        Args:
            value (float): value for IDD Field `Property Value 9`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 9"] = value

    @property
    def property_value_10(self):
        """Get property_value_10

        Returns:
            float: the value of `property_value_10` or None if not set
        """
        return self["Property Value 10"]

    @property_value_10.setter
    def property_value_10(self, value=None):
        """  Corresponds to IDD Field `Property Value 10`

        Args:
            value (float): value for IDD Field `Property Value 10`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 10"] = value

    @property
    def property_value_11(self):
        """Get property_value_11

        Returns:
            float: the value of `property_value_11` or None if not set
        """
        return self["Property Value 11"]

    @property_value_11.setter
    def property_value_11(self, value=None):
        """  Corresponds to IDD Field `Property Value 11`

        Args:
            value (float): value for IDD Field `Property Value 11`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 11"] = value

    @property
    def property_value_12(self):
        """Get property_value_12

        Returns:
            float: the value of `property_value_12` or None if not set
        """
        return self["Property Value 12"]

    @property_value_12.setter
    def property_value_12(self, value=None):
        """  Corresponds to IDD Field `Property Value 12`

        Args:
            value (float): value for IDD Field `Property Value 12`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 12"] = value

    @property
    def property_value_13(self):
        """Get property_value_13

        Returns:
            float: the value of `property_value_13` or None if not set
        """
        return self["Property Value 13"]

    @property_value_13.setter
    def property_value_13(self, value=None):
        """  Corresponds to IDD Field `Property Value 13`

        Args:
            value (float): value for IDD Field `Property Value 13`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 13"] = value

    @property
    def property_value_14(self):
        """Get property_value_14

        Returns:
            float: the value of `property_value_14` or None if not set
        """
        return self["Property Value 14"]

    @property_value_14.setter
    def property_value_14(self, value=None):
        """  Corresponds to IDD Field `Property Value 14`

        Args:
            value (float): value for IDD Field `Property Value 14`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 14"] = value

    @property
    def property_value_15(self):
        """Get property_value_15

        Returns:
            float: the value of `property_value_15` or None if not set
        """
        return self["Property Value 15"]

    @property_value_15.setter
    def property_value_15(self, value=None):
        """  Corresponds to IDD Field `Property Value 15`

        Args:
            value (float): value for IDD Field `Property Value 15`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 15"] = value

    @property
    def property_value_16(self):
        """Get property_value_16

        Returns:
            float: the value of `property_value_16` or None if not set
        """
        return self["Property Value 16"]

    @property_value_16.setter
    def property_value_16(self, value=None):
        """  Corresponds to IDD Field `Property Value 16`

        Args:
            value (float): value for IDD Field `Property Value 16`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 16"] = value

    @property
    def property_value_17(self):
        """Get property_value_17

        Returns:
            float: the value of `property_value_17` or None if not set
        """
        return self["Property Value 17"]

    @property_value_17.setter
    def property_value_17(self, value=None):
        """  Corresponds to IDD Field `Property Value 17`

        Args:
            value (float): value for IDD Field `Property Value 17`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 17"] = value

    @property
    def property_value_18(self):
        """Get property_value_18

        Returns:
            float: the value of `property_value_18` or None if not set
        """
        return self["Property Value 18"]

    @property_value_18.setter
    def property_value_18(self, value=None):
        """  Corresponds to IDD Field `Property Value 18`

        Args:
            value (float): value for IDD Field `Property Value 18`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 18"] = value

    @property
    def property_value_19(self):
        """Get property_value_19

        Returns:
            float: the value of `property_value_19` or None if not set
        """
        return self["Property Value 19"]

    @property_value_19.setter
    def property_value_19(self, value=None):
        """  Corresponds to IDD Field `Property Value 19`

        Args:
            value (float): value for IDD Field `Property Value 19`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 19"] = value

    @property
    def property_value_20(self):
        """Get property_value_20

        Returns:
            float: the value of `property_value_20` or None if not set
        """
        return self["Property Value 20"]

    @property_value_20.setter
    def property_value_20(self, value=None):
        """  Corresponds to IDD Field `Property Value 20`

        Args:
            value (float): value for IDD Field `Property Value 20`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 20"] = value

    @property
    def property_value_21(self):
        """Get property_value_21

        Returns:
            float: the value of `property_value_21` or None if not set
        """
        return self["Property Value 21"]

    @property_value_21.setter
    def property_value_21(self, value=None):
        """  Corresponds to IDD Field `Property Value 21`

        Args:
            value (float): value for IDD Field `Property Value 21`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 21"] = value

    @property
    def property_value_22(self):
        """Get property_value_22

        Returns:
            float: the value of `property_value_22` or None if not set
        """
        return self["Property Value 22"]

    @property_value_22.setter
    def property_value_22(self, value=None):
        """  Corresponds to IDD Field `Property Value 22`

        Args:
            value (float): value for IDD Field `Property Value 22`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 22"] = value

    @property
    def property_value_23(self):
        """Get property_value_23

        Returns:
            float: the value of `property_value_23` or None if not set
        """
        return self["Property Value 23"]

    @property_value_23.setter
    def property_value_23(self, value=None):
        """  Corresponds to IDD Field `Property Value 23`

        Args:
            value (float): value for IDD Field `Property Value 23`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 23"] = value

    @property
    def property_value_24(self):
        """Get property_value_24

        Returns:
            float: the value of `property_value_24` or None if not set
        """
        return self["Property Value 24"]

    @property_value_24.setter
    def property_value_24(self, value=None):
        """  Corresponds to IDD Field `Property Value 24`

        Args:
            value (float): value for IDD Field `Property Value 24`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 24"] = value

    @property
    def property_value_25(self):
        """Get property_value_25

        Returns:
            float: the value of `property_value_25` or None if not set
        """
        return self["Property Value 25"]

    @property_value_25.setter
    def property_value_25(self, value=None):
        """  Corresponds to IDD Field `Property Value 25`

        Args:
            value (float): value for IDD Field `Property Value 25`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 25"] = value

    @property
    def property_value_26(self):
        """Get property_value_26

        Returns:
            float: the value of `property_value_26` or None if not set
        """
        return self["Property Value 26"]

    @property_value_26.setter
    def property_value_26(self, value=None):
        """  Corresponds to IDD Field `Property Value 26`

        Args:
            value (float): value for IDD Field `Property Value 26`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 26"] = value

    @property
    def property_value_27(self):
        """Get property_value_27

        Returns:
            float: the value of `property_value_27` or None if not set
        """
        return self["Property Value 27"]

    @property_value_27.setter
    def property_value_27(self, value=None):
        """  Corresponds to IDD Field `Property Value 27`

        Args:
            value (float): value for IDD Field `Property Value 27`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 27"] = value

    @property
    def property_value_28(self):
        """Get property_value_28

        Returns:
            float: the value of `property_value_28` or None if not set
        """
        return self["Property Value 28"]

    @property_value_28.setter
    def property_value_28(self, value=None):
        """  Corresponds to IDD Field `Property Value 28`

        Args:
            value (float): value for IDD Field `Property Value 28`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 28"] = value

    @property
    def property_value_29(self):
        """Get property_value_29

        Returns:
            float: the value of `property_value_29` or None if not set
        """
        return self["Property Value 29"]

    @property_value_29.setter
    def property_value_29(self, value=None):
        """  Corresponds to IDD Field `Property Value 29`

        Args:
            value (float): value for IDD Field `Property Value 29`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 29"] = value

    @property
    def property_value_30(self):
        """Get property_value_30

        Returns:
            float: the value of `property_value_30` or None if not set
        """
        return self["Property Value 30"]

    @property_value_30.setter
    def property_value_30(self, value=None):
        """  Corresponds to IDD Field `Property Value 30`

        Args:
            value (float): value for IDD Field `Property Value 30`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 30"] = value

    @property
    def property_value_31(self):
        """Get property_value_31

        Returns:
            float: the value of `property_value_31` or None if not set
        """
        return self["Property Value 31"]

    @property_value_31.setter
    def property_value_31(self, value=None):
        """  Corresponds to IDD Field `Property Value 31`

        Args:
            value (float): value for IDD Field `Property Value 31`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 31"] = value

    @property
    def property_value_32(self):
        """Get property_value_32

        Returns:
            float: the value of `property_value_32` or None if not set
        """
        return self["Property Value 32"]

    @property_value_32.setter
    def property_value_32(self, value=None):
        """  Corresponds to IDD Field `Property Value 32`

        Args:
            value (float): value for IDD Field `Property Value 32`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 32"] = value

    @property
    def property_value_33(self):
        """Get property_value_33

        Returns:
            float: the value of `property_value_33` or None if not set
        """
        return self["Property Value 33"]

    @property_value_33.setter
    def property_value_33(self, value=None):
        """  Corresponds to IDD Field `Property Value 33`

        Args:
            value (float): value for IDD Field `Property Value 33`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 33"] = value

    @property
    def property_value_34(self):
        """Get property_value_34

        Returns:
            float: the value of `property_value_34` or None if not set
        """
        return self["Property Value 34"]

    @property_value_34.setter
    def property_value_34(self, value=None):
        """  Corresponds to IDD Field `Property Value 34`

        Args:
            value (float): value for IDD Field `Property Value 34`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 34"] = value

    @property
    def property_value_35(self):
        """Get property_value_35

        Returns:
            float: the value of `property_value_35` or None if not set
        """
        return self["Property Value 35"]

    @property_value_35.setter
    def property_value_35(self, value=None):
        """  Corresponds to IDD Field `Property Value 35`

        Args:
            value (float): value for IDD Field `Property Value 35`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 35"] = value

    @property
    def property_value_36(self):
        """Get property_value_36

        Returns:
            float: the value of `property_value_36` or None if not set
        """
        return self["Property Value 36"]

    @property_value_36.setter
    def property_value_36(self, value=None):
        """  Corresponds to IDD Field `Property Value 36`

        Args:
            value (float): value for IDD Field `Property Value 36`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 36"] = value

    @property
    def property_value_37(self):
        """Get property_value_37

        Returns:
            float: the value of `property_value_37` or None if not set
        """
        return self["Property Value 37"]

    @property_value_37.setter
    def property_value_37(self, value=None):
        """  Corresponds to IDD Field `Property Value 37`

        Args:
            value (float): value for IDD Field `Property Value 37`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 37"] = value

    @property
    def property_value_38(self):
        """Get property_value_38

        Returns:
            float: the value of `property_value_38` or None if not set
        """
        return self["Property Value 38"]

    @property_value_38.setter
    def property_value_38(self, value=None):
        """  Corresponds to IDD Field `Property Value 38`

        Args:
            value (float): value for IDD Field `Property Value 38`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 38"] = value

    @property
    def property_value_39(self):
        """Get property_value_39

        Returns:
            float: the value of `property_value_39` or None if not set
        """
        return self["Property Value 39"]

    @property_value_39.setter
    def property_value_39(self, value=None):
        """  Corresponds to IDD Field `Property Value 39`

        Args:
            value (float): value for IDD Field `Property Value 39`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 39"] = value

    @property
    def property_value_40(self):
        """Get property_value_40

        Returns:
            float: the value of `property_value_40` or None if not set
        """
        return self["Property Value 40"]

    @property_value_40.setter
    def property_value_40(self, value=None):
        """  Corresponds to IDD Field `Property Value 40`

        Args:
            value (float): value for IDD Field `Property Value 40`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 40"] = value

    @property
    def property_value_41(self):
        """Get property_value_41

        Returns:
            float: the value of `property_value_41` or None if not set
        """
        return self["Property Value 41"]

    @property_value_41.setter
    def property_value_41(self, value=None):
        """  Corresponds to IDD Field `Property Value 41`

        Args:
            value (float): value for IDD Field `Property Value 41`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 41"] = value

    @property
    def property_value_42(self):
        """Get property_value_42

        Returns:
            float: the value of `property_value_42` or None if not set
        """
        return self["Property Value 42"]

    @property_value_42.setter
    def property_value_42(self, value=None):
        """  Corresponds to IDD Field `Property Value 42`

        Args:
            value (float): value for IDD Field `Property Value 42`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 42"] = value

    @property
    def property_value_43(self):
        """Get property_value_43

        Returns:
            float: the value of `property_value_43` or None if not set
        """
        return self["Property Value 43"]

    @property_value_43.setter
    def property_value_43(self, value=None):
        """  Corresponds to IDD Field `Property Value 43`

        Args:
            value (float): value for IDD Field `Property Value 43`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 43"] = value

    @property
    def property_value_44(self):
        """Get property_value_44

        Returns:
            float: the value of `property_value_44` or None if not set
        """
        return self["Property Value 44"]

    @property_value_44.setter
    def property_value_44(self, value=None):
        """  Corresponds to IDD Field `Property Value 44`

        Args:
            value (float): value for IDD Field `Property Value 44`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 44"] = value

    @property
    def property_value_45(self):
        """Get property_value_45

        Returns:
            float: the value of `property_value_45` or None if not set
        """
        return self["Property Value 45"]

    @property_value_45.setter
    def property_value_45(self, value=None):
        """  Corresponds to IDD Field `Property Value 45`

        Args:
            value (float): value for IDD Field `Property Value 45`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 45"] = value

    @property
    def property_value_46(self):
        """Get property_value_46

        Returns:
            float: the value of `property_value_46` or None if not set
        """
        return self["Property Value 46"]

    @property_value_46.setter
    def property_value_46(self, value=None):
        """  Corresponds to IDD Field `Property Value 46`

        Args:
            value (float): value for IDD Field `Property Value 46`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 46"] = value

    @property
    def property_value_47(self):
        """Get property_value_47

        Returns:
            float: the value of `property_value_47` or None if not set
        """
        return self["Property Value 47"]

    @property_value_47.setter
    def property_value_47(self, value=None):
        """  Corresponds to IDD Field `Property Value 47`

        Args:
            value (float): value for IDD Field `Property Value 47`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 47"] = value

    @property
    def property_value_48(self):
        """Get property_value_48

        Returns:
            float: the value of `property_value_48` or None if not set
        """
        return self["Property Value 48"]

    @property_value_48.setter
    def property_value_48(self, value=None):
        """  Corresponds to IDD Field `Property Value 48`

        Args:
            value (float): value for IDD Field `Property Value 48`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 48"] = value

    @property
    def property_value_49(self):
        """Get property_value_49

        Returns:
            float: the value of `property_value_49` or None if not set
        """
        return self["Property Value 49"]

    @property_value_49.setter
    def property_value_49(self, value=None):
        """  Corresponds to IDD Field `Property Value 49`

        Args:
            value (float): value for IDD Field `Property Value 49`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 49"] = value

    @property
    def property_value_50(self):
        """Get property_value_50

        Returns:
            float: the value of `property_value_50` or None if not set
        """
        return self["Property Value 50"]

    @property_value_50.setter
    def property_value_50(self, value=None):
        """  Corresponds to IDD Field `Property Value 50`

        Args:
            value (float): value for IDD Field `Property Value 50`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 50"] = value

    @property
    def property_value_51(self):
        """Get property_value_51

        Returns:
            float: the value of `property_value_51` or None if not set
        """
        return self["Property Value 51"]

    @property_value_51.setter
    def property_value_51(self, value=None):
        """  Corresponds to IDD Field `Property Value 51`

        Args:
            value (float): value for IDD Field `Property Value 51`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 51"] = value

    @property
    def property_value_52(self):
        """Get property_value_52

        Returns:
            float: the value of `property_value_52` or None if not set
        """
        return self["Property Value 52"]

    @property_value_52.setter
    def property_value_52(self, value=None):
        """  Corresponds to IDD Field `Property Value 52`

        Args:
            value (float): value for IDD Field `Property Value 52`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 52"] = value

    @property
    def property_value_53(self):
        """Get property_value_53

        Returns:
            float: the value of `property_value_53` or None if not set
        """
        return self["Property Value 53"]

    @property_value_53.setter
    def property_value_53(self, value=None):
        """  Corresponds to IDD Field `Property Value 53`

        Args:
            value (float): value for IDD Field `Property Value 53`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 53"] = value

    @property
    def property_value_54(self):
        """Get property_value_54

        Returns:
            float: the value of `property_value_54` or None if not set
        """
        return self["Property Value 54"]

    @property_value_54.setter
    def property_value_54(self, value=None):
        """  Corresponds to IDD Field `Property Value 54`

        Args:
            value (float): value for IDD Field `Property Value 54`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 54"] = value

    @property
    def property_value_55(self):
        """Get property_value_55

        Returns:
            float: the value of `property_value_55` or None if not set
        """
        return self["Property Value 55"]

    @property_value_55.setter
    def property_value_55(self, value=None):
        """  Corresponds to IDD Field `Property Value 55`

        Args:
            value (float): value for IDD Field `Property Value 55`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 55"] = value

    @property
    def property_value_56(self):
        """Get property_value_56

        Returns:
            float: the value of `property_value_56` or None if not set
        """
        return self["Property Value 56"]

    @property_value_56.setter
    def property_value_56(self, value=None):
        """  Corresponds to IDD Field `Property Value 56`

        Args:
            value (float): value for IDD Field `Property Value 56`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 56"] = value

    @property
    def property_value_57(self):
        """Get property_value_57

        Returns:
            float: the value of `property_value_57` or None if not set
        """
        return self["Property Value 57"]

    @property_value_57.setter
    def property_value_57(self, value=None):
        """  Corresponds to IDD Field `Property Value 57`

        Args:
            value (float): value for IDD Field `Property Value 57`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 57"] = value

    @property
    def property_value_58(self):
        """Get property_value_58

        Returns:
            float: the value of `property_value_58` or None if not set
        """
        return self["Property Value 58"]

    @property_value_58.setter
    def property_value_58(self, value=None):
        """  Corresponds to IDD Field `Property Value 58`

        Args:
            value (float): value for IDD Field `Property Value 58`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 58"] = value

    @property
    def property_value_59(self):
        """Get property_value_59

        Returns:
            float: the value of `property_value_59` or None if not set
        """
        return self["Property Value 59"]

    @property_value_59.setter
    def property_value_59(self, value=None):
        """  Corresponds to IDD Field `Property Value 59`

        Args:
            value (float): value for IDD Field `Property Value 59`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 59"] = value

    @property
    def property_value_60(self):
        """Get property_value_60

        Returns:
            float: the value of `property_value_60` or None if not set
        """
        return self["Property Value 60"]

    @property_value_60.setter
    def property_value_60(self, value=None):
        """  Corresponds to IDD Field `Property Value 60`

        Args:
            value (float): value for IDD Field `Property Value 60`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 60"] = value

    @property
    def property_value_61(self):
        """Get property_value_61

        Returns:
            float: the value of `property_value_61` or None if not set
        """
        return self["Property Value 61"]

    @property_value_61.setter
    def property_value_61(self, value=None):
        """  Corresponds to IDD Field `Property Value 61`

        Args:
            value (float): value for IDD Field `Property Value 61`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 61"] = value

    @property
    def property_value_62(self):
        """Get property_value_62

        Returns:
            float: the value of `property_value_62` or None if not set
        """
        return self["Property Value 62"]

    @property_value_62.setter
    def property_value_62(self, value=None):
        """  Corresponds to IDD Field `Property Value 62`

        Args:
            value (float): value for IDD Field `Property Value 62`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 62"] = value

    @property
    def property_value_63(self):
        """Get property_value_63

        Returns:
            float: the value of `property_value_63` or None if not set
        """
        return self["Property Value 63"]

    @property_value_63.setter
    def property_value_63(self, value=None):
        """  Corresponds to IDD Field `Property Value 63`

        Args:
            value (float): value for IDD Field `Property Value 63`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 63"] = value

    @property
    def property_value_64(self):
        """Get property_value_64

        Returns:
            float: the value of `property_value_64` or None if not set
        """
        return self["Property Value 64"]

    @property_value_64.setter
    def property_value_64(self, value=None):
        """  Corresponds to IDD Field `Property Value 64`

        Args:
            value (float): value for IDD Field `Property Value 64`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 64"] = value

    @property
    def property_value_65(self):
        """Get property_value_65

        Returns:
            float: the value of `property_value_65` or None if not set
        """
        return self["Property Value 65"]

    @property_value_65.setter
    def property_value_65(self, value=None):
        """  Corresponds to IDD Field `Property Value 65`

        Args:
            value (float): value for IDD Field `Property Value 65`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 65"] = value

    @property
    def property_value_66(self):
        """Get property_value_66

        Returns:
            float: the value of `property_value_66` or None if not set
        """
        return self["Property Value 66"]

    @property_value_66.setter
    def property_value_66(self, value=None):
        """  Corresponds to IDD Field `Property Value 66`

        Args:
            value (float): value for IDD Field `Property Value 66`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 66"] = value

    @property
    def property_value_67(self):
        """Get property_value_67

        Returns:
            float: the value of `property_value_67` or None if not set
        """
        return self["Property Value 67"]

    @property_value_67.setter
    def property_value_67(self, value=None):
        """  Corresponds to IDD Field `Property Value 67`

        Args:
            value (float): value for IDD Field `Property Value 67`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 67"] = value

    @property
    def property_value_68(self):
        """Get property_value_68

        Returns:
            float: the value of `property_value_68` or None if not set
        """
        return self["Property Value 68"]

    @property_value_68.setter
    def property_value_68(self, value=None):
        """  Corresponds to IDD Field `Property Value 68`

        Args:
            value (float): value for IDD Field `Property Value 68`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 68"] = value

    @property
    def property_value_69(self):
        """Get property_value_69

        Returns:
            float: the value of `property_value_69` or None if not set
        """
        return self["Property Value 69"]

    @property_value_69.setter
    def property_value_69(self, value=None):
        """  Corresponds to IDD Field `Property Value 69`

        Args:
            value (float): value for IDD Field `Property Value 69`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 69"] = value

    @property
    def property_value_70(self):
        """Get property_value_70

        Returns:
            float: the value of `property_value_70` or None if not set
        """
        return self["Property Value 70"]

    @property_value_70.setter
    def property_value_70(self, value=None):
        """  Corresponds to IDD Field `Property Value 70`

        Args:
            value (float): value for IDD Field `Property Value 70`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 70"] = value

    @property
    def property_value_71(self):
        """Get property_value_71

        Returns:
            float: the value of `property_value_71` or None if not set
        """
        return self["Property Value 71"]

    @property_value_71.setter
    def property_value_71(self, value=None):
        """  Corresponds to IDD Field `Property Value 71`

        Args:
            value (float): value for IDD Field `Property Value 71`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 71"] = value

    @property
    def property_value_72(self):
        """Get property_value_72

        Returns:
            float: the value of `property_value_72` or None if not set
        """
        return self["Property Value 72"]

    @property_value_72.setter
    def property_value_72(self, value=None):
        """  Corresponds to IDD Field `Property Value 72`

        Args:
            value (float): value for IDD Field `Property Value 72`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 72"] = value

    @property
    def property_value_73(self):
        """Get property_value_73

        Returns:
            float: the value of `property_value_73` or None if not set
        """
        return self["Property Value 73"]

    @property_value_73.setter
    def property_value_73(self, value=None):
        """  Corresponds to IDD Field `Property Value 73`

        Args:
            value (float): value for IDD Field `Property Value 73`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 73"] = value

    @property
    def property_value_74(self):
        """Get property_value_74

        Returns:
            float: the value of `property_value_74` or None if not set
        """
        return self["Property Value 74"]

    @property_value_74.setter
    def property_value_74(self, value=None):
        """  Corresponds to IDD Field `Property Value 74`

        Args:
            value (float): value for IDD Field `Property Value 74`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 74"] = value

    @property
    def property_value_75(self):
        """Get property_value_75

        Returns:
            float: the value of `property_value_75` or None if not set
        """
        return self["Property Value 75"]

    @property_value_75.setter
    def property_value_75(self, value=None):
        """  Corresponds to IDD Field `Property Value 75`

        Args:
            value (float): value for IDD Field `Property Value 75`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 75"] = value

    @property
    def property_value_76(self):
        """Get property_value_76

        Returns:
            float: the value of `property_value_76` or None if not set
        """
        return self["Property Value 76"]

    @property_value_76.setter
    def property_value_76(self, value=None):
        """  Corresponds to IDD Field `Property Value 76`

        Args:
            value (float): value for IDD Field `Property Value 76`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 76"] = value

    @property
    def property_value_77(self):
        """Get property_value_77

        Returns:
            float: the value of `property_value_77` or None if not set
        """
        return self["Property Value 77"]

    @property_value_77.setter
    def property_value_77(self, value=None):
        """  Corresponds to IDD Field `Property Value 77`

        Args:
            value (float): value for IDD Field `Property Value 77`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 77"] = value

    @property
    def property_value_78(self):
        """Get property_value_78

        Returns:
            float: the value of `property_value_78` or None if not set
        """
        return self["Property Value 78"]

    @property_value_78.setter
    def property_value_78(self, value=None):
        """  Corresponds to IDD Field `Property Value 78`

        Args:
            value (float): value for IDD Field `Property Value 78`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 78"] = value

    @property
    def property_value_79(self):
        """Get property_value_79

        Returns:
            float: the value of `property_value_79` or None if not set
        """
        return self["Property Value 79"]

    @property_value_79.setter
    def property_value_79(self, value=None):
        """  Corresponds to IDD Field `Property Value 79`

        Args:
            value (float): value for IDD Field `Property Value 79`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 79"] = value

    @property
    def property_value_80(self):
        """Get property_value_80

        Returns:
            float: the value of `property_value_80` or None if not set
        """
        return self["Property Value 80"]

    @property_value_80.setter
    def property_value_80(self, value=None):
        """  Corresponds to IDD Field `Property Value 80`

        Args:
            value (float): value for IDD Field `Property Value 80`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 80"] = value

    @property
    def property_value_81(self):
        """Get property_value_81

        Returns:
            float: the value of `property_value_81` or None if not set
        """
        return self["Property Value 81"]

    @property_value_81.setter
    def property_value_81(self, value=None):
        """  Corresponds to IDD Field `Property Value 81`

        Args:
            value (float): value for IDD Field `Property Value 81`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 81"] = value

    @property
    def property_value_82(self):
        """Get property_value_82

        Returns:
            float: the value of `property_value_82` or None if not set
        """
        return self["Property Value 82"]

    @property_value_82.setter
    def property_value_82(self, value=None):
        """  Corresponds to IDD Field `Property Value 82`

        Args:
            value (float): value for IDD Field `Property Value 82`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 82"] = value

    @property
    def property_value_83(self):
        """Get property_value_83

        Returns:
            float: the value of `property_value_83` or None if not set
        """
        return self["Property Value 83"]

    @property_value_83.setter
    def property_value_83(self, value=None):
        """  Corresponds to IDD Field `Property Value 83`

        Args:
            value (float): value for IDD Field `Property Value 83`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 83"] = value

    @property
    def property_value_84(self):
        """Get property_value_84

        Returns:
            float: the value of `property_value_84` or None if not set
        """
        return self["Property Value 84"]

    @property_value_84.setter
    def property_value_84(self, value=None):
        """  Corresponds to IDD Field `Property Value 84`

        Args:
            value (float): value for IDD Field `Property Value 84`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 84"] = value

    @property
    def property_value_85(self):
        """Get property_value_85

        Returns:
            float: the value of `property_value_85` or None if not set
        """
        return self["Property Value 85"]

    @property_value_85.setter
    def property_value_85(self, value=None):
        """  Corresponds to IDD Field `Property Value 85`

        Args:
            value (float): value for IDD Field `Property Value 85`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 85"] = value

    @property
    def property_value_86(self):
        """Get property_value_86

        Returns:
            float: the value of `property_value_86` or None if not set
        """
        return self["Property Value 86"]

    @property_value_86.setter
    def property_value_86(self, value=None):
        """  Corresponds to IDD Field `Property Value 86`

        Args:
            value (float): value for IDD Field `Property Value 86`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 86"] = value

    @property
    def property_value_87(self):
        """Get property_value_87

        Returns:
            float: the value of `property_value_87` or None if not set
        """
        return self["Property Value 87"]

    @property_value_87.setter
    def property_value_87(self, value=None):
        """  Corresponds to IDD Field `Property Value 87`

        Args:
            value (float): value for IDD Field `Property Value 87`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 87"] = value

    @property
    def property_value_88(self):
        """Get property_value_88

        Returns:
            float: the value of `property_value_88` or None if not set
        """
        return self["Property Value 88"]

    @property_value_88.setter
    def property_value_88(self, value=None):
        """  Corresponds to IDD Field `Property Value 88`

        Args:
            value (float): value for IDD Field `Property Value 88`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 88"] = value

    @property
    def property_value_89(self):
        """Get property_value_89

        Returns:
            float: the value of `property_value_89` or None if not set
        """
        return self["Property Value 89"]

    @property_value_89.setter
    def property_value_89(self, value=None):
        """  Corresponds to IDD Field `Property Value 89`

        Args:
            value (float): value for IDD Field `Property Value 89`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 89"] = value

    @property
    def property_value_90(self):
        """Get property_value_90

        Returns:
            float: the value of `property_value_90` or None if not set
        """
        return self["Property Value 90"]

    @property_value_90.setter
    def property_value_90(self, value=None):
        """  Corresponds to IDD Field `Property Value 90`

        Args:
            value (float): value for IDD Field `Property Value 90`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 90"] = value

    @property
    def property_value_91(self):
        """Get property_value_91

        Returns:
            float: the value of `property_value_91` or None if not set
        """
        return self["Property Value 91"]

    @property_value_91.setter
    def property_value_91(self, value=None):
        """  Corresponds to IDD Field `Property Value 91`

        Args:
            value (float): value for IDD Field `Property Value 91`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 91"] = value

    @property
    def property_value_92(self):
        """Get property_value_92

        Returns:
            float: the value of `property_value_92` or None if not set
        """
        return self["Property Value 92"]

    @property_value_92.setter
    def property_value_92(self, value=None):
        """  Corresponds to IDD Field `Property Value 92`

        Args:
            value (float): value for IDD Field `Property Value 92`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 92"] = value

    @property
    def property_value_93(self):
        """Get property_value_93

        Returns:
            float: the value of `property_value_93` or None if not set
        """
        return self["Property Value 93"]

    @property_value_93.setter
    def property_value_93(self, value=None):
        """  Corresponds to IDD Field `Property Value 93`

        Args:
            value (float): value for IDD Field `Property Value 93`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 93"] = value

    @property
    def property_value_94(self):
        """Get property_value_94

        Returns:
            float: the value of `property_value_94` or None if not set
        """
        return self["Property Value 94"]

    @property_value_94.setter
    def property_value_94(self, value=None):
        """  Corresponds to IDD Field `Property Value 94`

        Args:
            value (float): value for IDD Field `Property Value 94`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 94"] = value

    @property
    def property_value_95(self):
        """Get property_value_95

        Returns:
            float: the value of `property_value_95` or None if not set
        """
        return self["Property Value 95"]

    @property_value_95.setter
    def property_value_95(self, value=None):
        """  Corresponds to IDD Field `Property Value 95`

        Args:
            value (float): value for IDD Field `Property Value 95`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 95"] = value

    @property
    def property_value_96(self):
        """Get property_value_96

        Returns:
            float: the value of `property_value_96` or None if not set
        """
        return self["Property Value 96"]

    @property_value_96.setter
    def property_value_96(self, value=None):
        """  Corresponds to IDD Field `Property Value 96`

        Args:
            value (float): value for IDD Field `Property Value 96`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 96"] = value

    @property
    def property_value_97(self):
        """Get property_value_97

        Returns:
            float: the value of `property_value_97` or None if not set
        """
        return self["Property Value 97"]

    @property_value_97.setter
    def property_value_97(self, value=None):
        """  Corresponds to IDD Field `Property Value 97`

        Args:
            value (float): value for IDD Field `Property Value 97`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 97"] = value

    @property
    def property_value_98(self):
        """Get property_value_98

        Returns:
            float: the value of `property_value_98` or None if not set
        """
        return self["Property Value 98"]

    @property_value_98.setter
    def property_value_98(self, value=None):
        """  Corresponds to IDD Field `Property Value 98`

        Args:
            value (float): value for IDD Field `Property Value 98`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 98"] = value

    @property
    def property_value_99(self):
        """Get property_value_99

        Returns:
            float: the value of `property_value_99` or None if not set
        """
        return self["Property Value 99"]

    @property_value_99.setter
    def property_value_99(self, value=None):
        """  Corresponds to IDD Field `Property Value 99`

        Args:
            value (float): value for IDD Field `Property Value 99`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 99"] = value

    @property
    def property_value_100(self):
        """Get property_value_100

        Returns:
            float: the value of `property_value_100` or None if not set
        """
        return self["Property Value 100"]

    @property_value_100.setter
    def property_value_100(self, value=None):
        """  Corresponds to IDD Field `Property Value 100`

        Args:
            value (float): value for IDD Field `Property Value 100`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 100"] = value

    @property
    def property_value_101(self):
        """Get property_value_101

        Returns:
            float: the value of `property_value_101` or None if not set
        """
        return self["Property Value 101"]

    @property_value_101.setter
    def property_value_101(self, value=None):
        """  Corresponds to IDD Field `Property Value 101`

        Args:
            value (float): value for IDD Field `Property Value 101`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 101"] = value

    @property
    def property_value_102(self):
        """Get property_value_102

        Returns:
            float: the value of `property_value_102` or None if not set
        """
        return self["Property Value 102"]

    @property_value_102.setter
    def property_value_102(self, value=None):
        """  Corresponds to IDD Field `Property Value 102`

        Args:
            value (float): value for IDD Field `Property Value 102`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 102"] = value

    @property
    def property_value_103(self):
        """Get property_value_103

        Returns:
            float: the value of `property_value_103` or None if not set
        """
        return self["Property Value 103"]

    @property_value_103.setter
    def property_value_103(self, value=None):
        """  Corresponds to IDD Field `Property Value 103`

        Args:
            value (float): value for IDD Field `Property Value 103`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 103"] = value

    @property
    def property_value_104(self):
        """Get property_value_104

        Returns:
            float: the value of `property_value_104` or None if not set
        """
        return self["Property Value 104"]

    @property_value_104.setter
    def property_value_104(self, value=None):
        """  Corresponds to IDD Field `Property Value 104`

        Args:
            value (float): value for IDD Field `Property Value 104`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 104"] = value

    @property
    def property_value_105(self):
        """Get property_value_105

        Returns:
            float: the value of `property_value_105` or None if not set
        """
        return self["Property Value 105"]

    @property_value_105.setter
    def property_value_105(self, value=None):
        """  Corresponds to IDD Field `Property Value 105`

        Args:
            value (float): value for IDD Field `Property Value 105`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 105"] = value

    @property
    def property_value_106(self):
        """Get property_value_106

        Returns:
            float: the value of `property_value_106` or None if not set
        """
        return self["Property Value 106"]

    @property_value_106.setter
    def property_value_106(self, value=None):
        """  Corresponds to IDD Field `Property Value 106`

        Args:
            value (float): value for IDD Field `Property Value 106`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 106"] = value

    @property
    def property_value_107(self):
        """Get property_value_107

        Returns:
            float: the value of `property_value_107` or None if not set
        """
        return self["Property Value 107"]

    @property_value_107.setter
    def property_value_107(self, value=None):
        """  Corresponds to IDD Field `Property Value 107`

        Args:
            value (float): value for IDD Field `Property Value 107`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 107"] = value

    @property
    def property_value_108(self):
        """Get property_value_108

        Returns:
            float: the value of `property_value_108` or None if not set
        """
        return self["Property Value 108"]

    @property_value_108.setter
    def property_value_108(self, value=None):
        """  Corresponds to IDD Field `Property Value 108`

        Args:
            value (float): value for IDD Field `Property Value 108`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 108"] = value

    @property
    def property_value_109(self):
        """Get property_value_109

        Returns:
            float: the value of `property_value_109` or None if not set
        """
        return self["Property Value 109"]

    @property_value_109.setter
    def property_value_109(self, value=None):
        """  Corresponds to IDD Field `Property Value 109`

        Args:
            value (float): value for IDD Field `Property Value 109`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 109"] = value

    @property
    def property_value_110(self):
        """Get property_value_110

        Returns:
            float: the value of `property_value_110` or None if not set
        """
        return self["Property Value 110"]

    @property_value_110.setter
    def property_value_110(self, value=None):
        """  Corresponds to IDD Field `Property Value 110`

        Args:
            value (float): value for IDD Field `Property Value 110`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 110"] = value

    @property
    def property_value_111(self):
        """Get property_value_111

        Returns:
            float: the value of `property_value_111` or None if not set
        """
        return self["Property Value 111"]

    @property_value_111.setter
    def property_value_111(self, value=None):
        """  Corresponds to IDD Field `Property Value 111`

        Args:
            value (float): value for IDD Field `Property Value 111`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 111"] = value

    @property
    def property_value_112(self):
        """Get property_value_112

        Returns:
            float: the value of `property_value_112` or None if not set
        """
        return self["Property Value 112"]

    @property_value_112.setter
    def property_value_112(self, value=None):
        """  Corresponds to IDD Field `Property Value 112`

        Args:
            value (float): value for IDD Field `Property Value 112`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 112"] = value

    @property
    def property_value_113(self):
        """Get property_value_113

        Returns:
            float: the value of `property_value_113` or None if not set
        """
        return self["Property Value 113"]

    @property_value_113.setter
    def property_value_113(self, value=None):
        """  Corresponds to IDD Field `Property Value 113`

        Args:
            value (float): value for IDD Field `Property Value 113`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 113"] = value

    @property
    def property_value_114(self):
        """Get property_value_114

        Returns:
            float: the value of `property_value_114` or None if not set
        """
        return self["Property Value 114"]

    @property_value_114.setter
    def property_value_114(self, value=None):
        """  Corresponds to IDD Field `Property Value 114`

        Args:
            value (float): value for IDD Field `Property Value 114`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 114"] = value

    @property
    def property_value_115(self):
        """Get property_value_115

        Returns:
            float: the value of `property_value_115` or None if not set
        """
        return self["Property Value 115"]

    @property_value_115.setter
    def property_value_115(self, value=None):
        """  Corresponds to IDD Field `Property Value 115`

        Args:
            value (float): value for IDD Field `Property Value 115`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 115"] = value

    @property
    def property_value_116(self):
        """Get property_value_116

        Returns:
            float: the value of `property_value_116` or None if not set
        """
        return self["Property Value 116"]

    @property_value_116.setter
    def property_value_116(self, value=None):
        """  Corresponds to IDD Field `Property Value 116`

        Args:
            value (float): value for IDD Field `Property Value 116`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 116"] = value

    @property
    def property_value_117(self):
        """Get property_value_117

        Returns:
            float: the value of `property_value_117` or None if not set
        """
        return self["Property Value 117"]

    @property_value_117.setter
    def property_value_117(self, value=None):
        """  Corresponds to IDD Field `Property Value 117`

        Args:
            value (float): value for IDD Field `Property Value 117`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 117"] = value

    @property
    def property_value_118(self):
        """Get property_value_118

        Returns:
            float: the value of `property_value_118` or None if not set
        """
        return self["Property Value 118"]

    @property_value_118.setter
    def property_value_118(self, value=None):
        """  Corresponds to IDD Field `Property Value 118`

        Args:
            value (float): value for IDD Field `Property Value 118`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 118"] = value

    @property
    def property_value_119(self):
        """Get property_value_119

        Returns:
            float: the value of `property_value_119` or None if not set
        """
        return self["Property Value 119"]

    @property_value_119.setter
    def property_value_119(self, value=None):
        """  Corresponds to IDD Field `Property Value 119`

        Args:
            value (float): value for IDD Field `Property Value 119`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 119"] = value

    @property
    def property_value_120(self):
        """Get property_value_120

        Returns:
            float: the value of `property_value_120` or None if not set
        """
        return self["Property Value 120"]

    @property_value_120.setter
    def property_value_120(self, value=None):
        """  Corresponds to IDD Field `Property Value 120`

        Args:
            value (float): value for IDD Field `Property Value 120`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 120"] = value

    @property
    def property_value_121(self):
        """Get property_value_121

        Returns:
            float: the value of `property_value_121` or None if not set
        """
        return self["Property Value 121"]

    @property_value_121.setter
    def property_value_121(self, value=None):
        """  Corresponds to IDD Field `Property Value 121`

        Args:
            value (float): value for IDD Field `Property Value 121`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 121"] = value

    @property
    def property_value_122(self):
        """Get property_value_122

        Returns:
            float: the value of `property_value_122` or None if not set
        """
        return self["Property Value 122"]

    @property_value_122.setter
    def property_value_122(self, value=None):
        """  Corresponds to IDD Field `Property Value 122`

        Args:
            value (float): value for IDD Field `Property Value 122`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 122"] = value

    @property
    def property_value_123(self):
        """Get property_value_123

        Returns:
            float: the value of `property_value_123` or None if not set
        """
        return self["Property Value 123"]

    @property_value_123.setter
    def property_value_123(self, value=None):
        """  Corresponds to IDD Field `Property Value 123`

        Args:
            value (float): value for IDD Field `Property Value 123`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 123"] = value

    @property
    def property_value_124(self):
        """Get property_value_124

        Returns:
            float: the value of `property_value_124` or None if not set
        """
        return self["Property Value 124"]

    @property_value_124.setter
    def property_value_124(self, value=None):
        """  Corresponds to IDD Field `Property Value 124`

        Args:
            value (float): value for IDD Field `Property Value 124`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 124"] = value

    @property
    def property_value_125(self):
        """Get property_value_125

        Returns:
            float: the value of `property_value_125` or None if not set
        """
        return self["Property Value 125"]

    @property_value_125.setter
    def property_value_125(self, value=None):
        """  Corresponds to IDD Field `Property Value 125`

        Args:
            value (float): value for IDD Field `Property Value 125`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 125"] = value

    @property
    def property_value_126(self):
        """Get property_value_126

        Returns:
            float: the value of `property_value_126` or None if not set
        """
        return self["Property Value 126"]

    @property_value_126.setter
    def property_value_126(self, value=None):
        """  Corresponds to IDD Field `Property Value 126`

        Args:
            value (float): value for IDD Field `Property Value 126`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 126"] = value

    @property
    def property_value_127(self):
        """Get property_value_127

        Returns:
            float: the value of `property_value_127` or None if not set
        """
        return self["Property Value 127"]

    @property_value_127.setter
    def property_value_127(self, value=None):
        """  Corresponds to IDD Field `Property Value 127`

        Args:
            value (float): value for IDD Field `Property Value 127`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 127"] = value

    @property
    def property_value_128(self):
        """Get property_value_128

        Returns:
            float: the value of `property_value_128` or None if not set
        """
        return self["Property Value 128"]

    @property_value_128.setter
    def property_value_128(self, value=None):
        """  Corresponds to IDD Field `Property Value 128`

        Args:
            value (float): value for IDD Field `Property Value 128`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 128"] = value

    @property
    def property_value_129(self):
        """Get property_value_129

        Returns:
            float: the value of `property_value_129` or None if not set
        """
        return self["Property Value 129"]

    @property_value_129.setter
    def property_value_129(self, value=None):
        """  Corresponds to IDD Field `Property Value 129`

        Args:
            value (float): value for IDD Field `Property Value 129`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 129"] = value

    @property
    def property_value_130(self):
        """Get property_value_130

        Returns:
            float: the value of `property_value_130` or None if not set
        """
        return self["Property Value 130"]

    @property_value_130.setter
    def property_value_130(self, value=None):
        """  Corresponds to IDD Field `Property Value 130`

        Args:
            value (float): value for IDD Field `Property Value 130`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 130"] = value

    @property
    def property_value_131(self):
        """Get property_value_131

        Returns:
            float: the value of `property_value_131` or None if not set
        """
        return self["Property Value 131"]

    @property_value_131.setter
    def property_value_131(self, value=None):
        """  Corresponds to IDD Field `Property Value 131`

        Args:
            value (float): value for IDD Field `Property Value 131`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 131"] = value

    @property
    def property_value_132(self):
        """Get property_value_132

        Returns:
            float: the value of `property_value_132` or None if not set
        """
        return self["Property Value 132"]

    @property_value_132.setter
    def property_value_132(self, value=None):
        """  Corresponds to IDD Field `Property Value 132`

        Args:
            value (float): value for IDD Field `Property Value 132`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 132"] = value

    @property
    def property_value_133(self):
        """Get property_value_133

        Returns:
            float: the value of `property_value_133` or None if not set
        """
        return self["Property Value 133"]

    @property_value_133.setter
    def property_value_133(self, value=None):
        """  Corresponds to IDD Field `Property Value 133`

        Args:
            value (float): value for IDD Field `Property Value 133`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 133"] = value

    @property
    def property_value_134(self):
        """Get property_value_134

        Returns:
            float: the value of `property_value_134` or None if not set
        """
        return self["Property Value 134"]

    @property_value_134.setter
    def property_value_134(self, value=None):
        """  Corresponds to IDD Field `Property Value 134`

        Args:
            value (float): value for IDD Field `Property Value 134`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 134"] = value

    @property
    def property_value_135(self):
        """Get property_value_135

        Returns:
            float: the value of `property_value_135` or None if not set
        """
        return self["Property Value 135"]

    @property_value_135.setter
    def property_value_135(self, value=None):
        """  Corresponds to IDD Field `Property Value 135`

        Args:
            value (float): value for IDD Field `Property Value 135`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 135"] = value

    @property
    def property_value_136(self):
        """Get property_value_136

        Returns:
            float: the value of `property_value_136` or None if not set
        """
        return self["Property Value 136"]

    @property_value_136.setter
    def property_value_136(self, value=None):
        """  Corresponds to IDD Field `Property Value 136`

        Args:
            value (float): value for IDD Field `Property Value 136`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 136"] = value

    @property
    def property_value_137(self):
        """Get property_value_137

        Returns:
            float: the value of `property_value_137` or None if not set
        """
        return self["Property Value 137"]

    @property_value_137.setter
    def property_value_137(self, value=None):
        """  Corresponds to IDD Field `Property Value 137`

        Args:
            value (float): value for IDD Field `Property Value 137`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 137"] = value

    @property
    def property_value_138(self):
        """Get property_value_138

        Returns:
            float: the value of `property_value_138` or None if not set
        """
        return self["Property Value 138"]

    @property_value_138.setter
    def property_value_138(self, value=None):
        """  Corresponds to IDD Field `Property Value 138`

        Args:
            value (float): value for IDD Field `Property Value 138`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 138"] = value

    @property
    def property_value_139(self):
        """Get property_value_139

        Returns:
            float: the value of `property_value_139` or None if not set
        """
        return self["Property Value 139"]

    @property_value_139.setter
    def property_value_139(self, value=None):
        """  Corresponds to IDD Field `Property Value 139`

        Args:
            value (float): value for IDD Field `Property Value 139`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 139"] = value

    @property
    def property_value_140(self):
        """Get property_value_140

        Returns:
            float: the value of `property_value_140` or None if not set
        """
        return self["Property Value 140"]

    @property_value_140.setter
    def property_value_140(self, value=None):
        """  Corresponds to IDD Field `Property Value 140`

        Args:
            value (float): value for IDD Field `Property Value 140`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 140"] = value

    @property
    def property_value_141(self):
        """Get property_value_141

        Returns:
            float: the value of `property_value_141` or None if not set
        """
        return self["Property Value 141"]

    @property_value_141.setter
    def property_value_141(self, value=None):
        """  Corresponds to IDD Field `Property Value 141`

        Args:
            value (float): value for IDD Field `Property Value 141`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 141"] = value

    @property
    def property_value_142(self):
        """Get property_value_142

        Returns:
            float: the value of `property_value_142` or None if not set
        """
        return self["Property Value 142"]

    @property_value_142.setter
    def property_value_142(self, value=None):
        """  Corresponds to IDD Field `Property Value 142`

        Args:
            value (float): value for IDD Field `Property Value 142`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 142"] = value

    @property
    def property_value_143(self):
        """Get property_value_143

        Returns:
            float: the value of `property_value_143` or None if not set
        """
        return self["Property Value 143"]

    @property_value_143.setter
    def property_value_143(self, value=None):
        """  Corresponds to IDD Field `Property Value 143`

        Args:
            value (float): value for IDD Field `Property Value 143`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 143"] = value

    @property
    def property_value_144(self):
        """Get property_value_144

        Returns:
            float: the value of `property_value_144` or None if not set
        """
        return self["Property Value 144"]

    @property_value_144.setter
    def property_value_144(self, value=None):
        """  Corresponds to IDD Field `Property Value 144`

        Args:
            value (float): value for IDD Field `Property Value 144`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 144"] = value

    @property
    def property_value_145(self):
        """Get property_value_145

        Returns:
            float: the value of `property_value_145` or None if not set
        """
        return self["Property Value 145"]

    @property_value_145.setter
    def property_value_145(self, value=None):
        """  Corresponds to IDD Field `Property Value 145`

        Args:
            value (float): value for IDD Field `Property Value 145`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 145"] = value

    @property
    def property_value_146(self):
        """Get property_value_146

        Returns:
            float: the value of `property_value_146` or None if not set
        """
        return self["Property Value 146"]

    @property_value_146.setter
    def property_value_146(self, value=None):
        """  Corresponds to IDD Field `Property Value 146`

        Args:
            value (float): value for IDD Field `Property Value 146`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 146"] = value

    @property
    def property_value_147(self):
        """Get property_value_147

        Returns:
            float: the value of `property_value_147` or None if not set
        """
        return self["Property Value 147"]

    @property_value_147.setter
    def property_value_147(self, value=None):
        """  Corresponds to IDD Field `Property Value 147`

        Args:
            value (float): value for IDD Field `Property Value 147`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 147"] = value

    @property
    def property_value_148(self):
        """Get property_value_148

        Returns:
            float: the value of `property_value_148` or None if not set
        """
        return self["Property Value 148"]

    @property_value_148.setter
    def property_value_148(self, value=None):
        """  Corresponds to IDD Field `Property Value 148`

        Args:
            value (float): value for IDD Field `Property Value 148`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 148"] = value

    @property
    def property_value_149(self):
        """Get property_value_149

        Returns:
            float: the value of `property_value_149` or None if not set
        """
        return self["Property Value 149"]

    @property_value_149.setter
    def property_value_149(self, value=None):
        """  Corresponds to IDD Field `Property Value 149`

        Args:
            value (float): value for IDD Field `Property Value 149`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 149"] = value

    @property
    def property_value_150(self):
        """Get property_value_150

        Returns:
            float: the value of `property_value_150` or None if not set
        """
        return self["Property Value 150"]

    @property_value_150.setter
    def property_value_150(self, value=None):
        """  Corresponds to IDD Field `Property Value 150`

        Args:
            value (float): value for IDD Field `Property Value 150`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 150"] = value

    @property
    def property_value_151(self):
        """Get property_value_151

        Returns:
            float: the value of `property_value_151` or None if not set
        """
        return self["Property Value 151"]

    @property_value_151.setter
    def property_value_151(self, value=None):
        """  Corresponds to IDD Field `Property Value 151`

        Args:
            value (float): value for IDD Field `Property Value 151`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 151"] = value

    @property
    def property_value_152(self):
        """Get property_value_152

        Returns:
            float: the value of `property_value_152` or None if not set
        """
        return self["Property Value 152"]

    @property_value_152.setter
    def property_value_152(self, value=None):
        """  Corresponds to IDD Field `Property Value 152`

        Args:
            value (float): value for IDD Field `Property Value 152`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 152"] = value

    @property
    def property_value_153(self):
        """Get property_value_153

        Returns:
            float: the value of `property_value_153` or None if not set
        """
        return self["Property Value 153"]

    @property_value_153.setter
    def property_value_153(self, value=None):
        """  Corresponds to IDD Field `Property Value 153`

        Args:
            value (float): value for IDD Field `Property Value 153`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 153"] = value

    @property
    def property_value_154(self):
        """Get property_value_154

        Returns:
            float: the value of `property_value_154` or None if not set
        """
        return self["Property Value 154"]

    @property_value_154.setter
    def property_value_154(self, value=None):
        """  Corresponds to IDD Field `Property Value 154`

        Args:
            value (float): value for IDD Field `Property Value 154`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 154"] = value

    @property
    def property_value_155(self):
        """Get property_value_155

        Returns:
            float: the value of `property_value_155` or None if not set
        """
        return self["Property Value 155"]

    @property_value_155.setter
    def property_value_155(self, value=None):
        """  Corresponds to IDD Field `Property Value 155`

        Args:
            value (float): value for IDD Field `Property Value 155`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 155"] = value

    @property
    def property_value_156(self):
        """Get property_value_156

        Returns:
            float: the value of `property_value_156` or None if not set
        """
        return self["Property Value 156"]

    @property_value_156.setter
    def property_value_156(self, value=None):
        """  Corresponds to IDD Field `Property Value 156`

        Args:
            value (float): value for IDD Field `Property Value 156`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 156"] = value

    @property
    def property_value_157(self):
        """Get property_value_157

        Returns:
            float: the value of `property_value_157` or None if not set
        """
        return self["Property Value 157"]

    @property_value_157.setter
    def property_value_157(self, value=None):
        """  Corresponds to IDD Field `Property Value 157`

        Args:
            value (float): value for IDD Field `Property Value 157`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 157"] = value

    @property
    def property_value_158(self):
        """Get property_value_158

        Returns:
            float: the value of `property_value_158` or None if not set
        """
        return self["Property Value 158"]

    @property_value_158.setter
    def property_value_158(self, value=None):
        """  Corresponds to IDD Field `Property Value 158`

        Args:
            value (float): value for IDD Field `Property Value 158`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 158"] = value

    @property
    def property_value_159(self):
        """Get property_value_159

        Returns:
            float: the value of `property_value_159` or None if not set
        """
        return self["Property Value 159"]

    @property_value_159.setter
    def property_value_159(self, value=None):
        """  Corresponds to IDD Field `Property Value 159`

        Args:
            value (float): value for IDD Field `Property Value 159`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 159"] = value

    @property
    def property_value_160(self):
        """Get property_value_160

        Returns:
            float: the value of `property_value_160` or None if not set
        """
        return self["Property Value 160"]

    @property_value_160.setter
    def property_value_160(self, value=None):
        """  Corresponds to IDD Field `Property Value 160`

        Args:
            value (float): value for IDD Field `Property Value 160`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 160"] = value

    @property
    def property_value_161(self):
        """Get property_value_161

        Returns:
            float: the value of `property_value_161` or None if not set
        """
        return self["Property Value 161"]

    @property_value_161.setter
    def property_value_161(self, value=None):
        """  Corresponds to IDD Field `Property Value 161`

        Args:
            value (float): value for IDD Field `Property Value 161`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 161"] = value

    @property
    def property_value_162(self):
        """Get property_value_162

        Returns:
            float: the value of `property_value_162` or None if not set
        """
        return self["Property Value 162"]

    @property_value_162.setter
    def property_value_162(self, value=None):
        """  Corresponds to IDD Field `Property Value 162`

        Args:
            value (float): value for IDD Field `Property Value 162`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 162"] = value

    @property
    def property_value_163(self):
        """Get property_value_163

        Returns:
            float: the value of `property_value_163` or None if not set
        """
        return self["Property Value 163"]

    @property_value_163.setter
    def property_value_163(self, value=None):
        """  Corresponds to IDD Field `Property Value 163`

        Args:
            value (float): value for IDD Field `Property Value 163`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 163"] = value

    @property
    def property_value_164(self):
        """Get property_value_164

        Returns:
            float: the value of `property_value_164` or None if not set
        """
        return self["Property Value 164"]

    @property_value_164.setter
    def property_value_164(self, value=None):
        """  Corresponds to IDD Field `Property Value 164`

        Args:
            value (float): value for IDD Field `Property Value 164`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 164"] = value

    @property
    def property_value_165(self):
        """Get property_value_165

        Returns:
            float: the value of `property_value_165` or None if not set
        """
        return self["Property Value 165"]

    @property_value_165.setter
    def property_value_165(self, value=None):
        """  Corresponds to IDD Field `Property Value 165`

        Args:
            value (float): value for IDD Field `Property Value 165`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 165"] = value

    @property
    def property_value_166(self):
        """Get property_value_166

        Returns:
            float: the value of `property_value_166` or None if not set
        """
        return self["Property Value 166"]

    @property_value_166.setter
    def property_value_166(self, value=None):
        """  Corresponds to IDD Field `Property Value 166`

        Args:
            value (float): value for IDD Field `Property Value 166`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 166"] = value

    @property
    def property_value_167(self):
        """Get property_value_167

        Returns:
            float: the value of `property_value_167` or None if not set
        """
        return self["Property Value 167"]

    @property_value_167.setter
    def property_value_167(self, value=None):
        """  Corresponds to IDD Field `Property Value 167`

        Args:
            value (float): value for IDD Field `Property Value 167`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 167"] = value

    @property
    def property_value_168(self):
        """Get property_value_168

        Returns:
            float: the value of `property_value_168` or None if not set
        """
        return self["Property Value 168"]

    @property_value_168.setter
    def property_value_168(self, value=None):
        """  Corresponds to IDD Field `Property Value 168`

        Args:
            value (float): value for IDD Field `Property Value 168`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 168"] = value

    @property
    def property_value_169(self):
        """Get property_value_169

        Returns:
            float: the value of `property_value_169` or None if not set
        """
        return self["Property Value 169"]

    @property_value_169.setter
    def property_value_169(self, value=None):
        """  Corresponds to IDD Field `Property Value 169`

        Args:
            value (float): value for IDD Field `Property Value 169`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 169"] = value

    @property
    def property_value_170(self):
        """Get property_value_170

        Returns:
            float: the value of `property_value_170` or None if not set
        """
        return self["Property Value 170"]

    @property_value_170.setter
    def property_value_170(self, value=None):
        """  Corresponds to IDD Field `Property Value 170`

        Args:
            value (float): value for IDD Field `Property Value 170`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 170"] = value

    @property
    def property_value_171(self):
        """Get property_value_171

        Returns:
            float: the value of `property_value_171` or None if not set
        """
        return self["Property Value 171"]

    @property_value_171.setter
    def property_value_171(self, value=None):
        """  Corresponds to IDD Field `Property Value 171`

        Args:
            value (float): value for IDD Field `Property Value 171`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 171"] = value

    @property
    def property_value_172(self):
        """Get property_value_172

        Returns:
            float: the value of `property_value_172` or None if not set
        """
        return self["Property Value 172"]

    @property_value_172.setter
    def property_value_172(self, value=None):
        """  Corresponds to IDD Field `Property Value 172`

        Args:
            value (float): value for IDD Field `Property Value 172`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 172"] = value

    @property
    def property_value_173(self):
        """Get property_value_173

        Returns:
            float: the value of `property_value_173` or None if not set
        """
        return self["Property Value 173"]

    @property_value_173.setter
    def property_value_173(self, value=None):
        """  Corresponds to IDD Field `Property Value 173`

        Args:
            value (float): value for IDD Field `Property Value 173`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 173"] = value

    @property
    def property_value_174(self):
        """Get property_value_174

        Returns:
            float: the value of `property_value_174` or None if not set
        """
        return self["Property Value 174"]

    @property_value_174.setter
    def property_value_174(self, value=None):
        """  Corresponds to IDD Field `Property Value 174`

        Args:
            value (float): value for IDD Field `Property Value 174`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 174"] = value

    @property
    def property_value_175(self):
        """Get property_value_175

        Returns:
            float: the value of `property_value_175` or None if not set
        """
        return self["Property Value 175"]

    @property_value_175.setter
    def property_value_175(self, value=None):
        """  Corresponds to IDD Field `Property Value 175`

        Args:
            value (float): value for IDD Field `Property Value 175`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 175"] = value

    @property
    def property_value_176(self):
        """Get property_value_176

        Returns:
            float: the value of `property_value_176` or None if not set
        """
        return self["Property Value 176"]

    @property_value_176.setter
    def property_value_176(self, value=None):
        """  Corresponds to IDD Field `Property Value 176`

        Args:
            value (float): value for IDD Field `Property Value 176`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 176"] = value

    @property
    def property_value_177(self):
        """Get property_value_177

        Returns:
            float: the value of `property_value_177` or None if not set
        """
        return self["Property Value 177"]

    @property_value_177.setter
    def property_value_177(self, value=None):
        """  Corresponds to IDD Field `Property Value 177`

        Args:
            value (float): value for IDD Field `Property Value 177`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 177"] = value

    @property
    def property_value_178(self):
        """Get property_value_178

        Returns:
            float: the value of `property_value_178` or None if not set
        """
        return self["Property Value 178"]

    @property_value_178.setter
    def property_value_178(self, value=None):
        """  Corresponds to IDD Field `Property Value 178`

        Args:
            value (float): value for IDD Field `Property Value 178`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 178"] = value

    @property
    def property_value_179(self):
        """Get property_value_179

        Returns:
            float: the value of `property_value_179` or None if not set
        """
        return self["Property Value 179"]

    @property_value_179.setter
    def property_value_179(self, value=None):
        """  Corresponds to IDD Field `Property Value 179`

        Args:
            value (float): value for IDD Field `Property Value 179`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 179"] = value

    @property
    def property_value_180(self):
        """Get property_value_180

        Returns:
            float: the value of `property_value_180` or None if not set
        """
        return self["Property Value 180"]

    @property_value_180.setter
    def property_value_180(self, value=None):
        """  Corresponds to IDD Field `Property Value 180`

        Args:
            value (float): value for IDD Field `Property Value 180`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 180"] = value

    @property
    def property_value_181(self):
        """Get property_value_181

        Returns:
            float: the value of `property_value_181` or None if not set
        """
        return self["Property Value 181"]

    @property_value_181.setter
    def property_value_181(self, value=None):
        """  Corresponds to IDD Field `Property Value 181`

        Args:
            value (float): value for IDD Field `Property Value 181`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 181"] = value

    @property
    def property_value_182(self):
        """Get property_value_182

        Returns:
            float: the value of `property_value_182` or None if not set
        """
        return self["Property Value 182"]

    @property_value_182.setter
    def property_value_182(self, value=None):
        """  Corresponds to IDD Field `Property Value 182`

        Args:
            value (float): value for IDD Field `Property Value 182`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 182"] = value

    @property
    def property_value_183(self):
        """Get property_value_183

        Returns:
            float: the value of `property_value_183` or None if not set
        """
        return self["Property Value 183"]

    @property_value_183.setter
    def property_value_183(self, value=None):
        """  Corresponds to IDD Field `Property Value 183`

        Args:
            value (float): value for IDD Field `Property Value 183`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 183"] = value

    @property
    def property_value_184(self):
        """Get property_value_184

        Returns:
            float: the value of `property_value_184` or None if not set
        """
        return self["Property Value 184"]

    @property_value_184.setter
    def property_value_184(self, value=None):
        """  Corresponds to IDD Field `Property Value 184`

        Args:
            value (float): value for IDD Field `Property Value 184`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 184"] = value

    @property
    def property_value_185(self):
        """Get property_value_185

        Returns:
            float: the value of `property_value_185` or None if not set
        """
        return self["Property Value 185"]

    @property_value_185.setter
    def property_value_185(self, value=None):
        """  Corresponds to IDD Field `Property Value 185`

        Args:
            value (float): value for IDD Field `Property Value 185`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 185"] = value

    @property
    def property_value_186(self):
        """Get property_value_186

        Returns:
            float: the value of `property_value_186` or None if not set
        """
        return self["Property Value 186"]

    @property_value_186.setter
    def property_value_186(self, value=None):
        """  Corresponds to IDD Field `Property Value 186`

        Args:
            value (float): value for IDD Field `Property Value 186`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 186"] = value

    @property
    def property_value_187(self):
        """Get property_value_187

        Returns:
            float: the value of `property_value_187` or None if not set
        """
        return self["Property Value 187"]

    @property_value_187.setter
    def property_value_187(self, value=None):
        """  Corresponds to IDD Field `Property Value 187`

        Args:
            value (float): value for IDD Field `Property Value 187`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 187"] = value

    @property
    def property_value_188(self):
        """Get property_value_188

        Returns:
            float: the value of `property_value_188` or None if not set
        """
        return self["Property Value 188"]

    @property_value_188.setter
    def property_value_188(self, value=None):
        """  Corresponds to IDD Field `Property Value 188`

        Args:
            value (float): value for IDD Field `Property Value 188`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 188"] = value

    @property
    def property_value_189(self):
        """Get property_value_189

        Returns:
            float: the value of `property_value_189` or None if not set
        """
        return self["Property Value 189"]

    @property_value_189.setter
    def property_value_189(self, value=None):
        """  Corresponds to IDD Field `Property Value 189`

        Args:
            value (float): value for IDD Field `Property Value 189`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 189"] = value

    @property
    def property_value_190(self):
        """Get property_value_190

        Returns:
            float: the value of `property_value_190` or None if not set
        """
        return self["Property Value 190"]

    @property_value_190.setter
    def property_value_190(self, value=None):
        """  Corresponds to IDD Field `Property Value 190`

        Args:
            value (float): value for IDD Field `Property Value 190`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 190"] = value

    @property
    def property_value_191(self):
        """Get property_value_191

        Returns:
            float: the value of `property_value_191` or None if not set
        """
        return self["Property Value 191"]

    @property_value_191.setter
    def property_value_191(self, value=None):
        """  Corresponds to IDD Field `Property Value 191`

        Args:
            value (float): value for IDD Field `Property Value 191`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 191"] = value

    @property
    def property_value_192(self):
        """Get property_value_192

        Returns:
            float: the value of `property_value_192` or None if not set
        """
        return self["Property Value 192"]

    @property_value_192.setter
    def property_value_192(self, value=None):
        """  Corresponds to IDD Field `Property Value 192`

        Args:
            value (float): value for IDD Field `Property Value 192`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 192"] = value

    @property
    def property_value_193(self):
        """Get property_value_193

        Returns:
            float: the value of `property_value_193` or None if not set
        """
        return self["Property Value 193"]

    @property_value_193.setter
    def property_value_193(self, value=None):
        """  Corresponds to IDD Field `Property Value 193`

        Args:
            value (float): value for IDD Field `Property Value 193`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 193"] = value

    @property
    def property_value_194(self):
        """Get property_value_194

        Returns:
            float: the value of `property_value_194` or None if not set
        """
        return self["Property Value 194"]

    @property_value_194.setter
    def property_value_194(self, value=None):
        """  Corresponds to IDD Field `Property Value 194`

        Args:
            value (float): value for IDD Field `Property Value 194`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 194"] = value

    @property
    def property_value_195(self):
        """Get property_value_195

        Returns:
            float: the value of `property_value_195` or None if not set
        """
        return self["Property Value 195"]

    @property_value_195.setter
    def property_value_195(self, value=None):
        """  Corresponds to IDD Field `Property Value 195`

        Args:
            value (float): value for IDD Field `Property Value 195`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 195"] = value

    @property
    def property_value_196(self):
        """Get property_value_196

        Returns:
            float: the value of `property_value_196` or None if not set
        """
        return self["Property Value 196"]

    @property_value_196.setter
    def property_value_196(self, value=None):
        """  Corresponds to IDD Field `Property Value 196`

        Args:
            value (float): value for IDD Field `Property Value 196`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 196"] = value

    @property
    def property_value_197(self):
        """Get property_value_197

        Returns:
            float: the value of `property_value_197` or None if not set
        """
        return self["Property Value 197"]

    @property_value_197.setter
    def property_value_197(self, value=None):
        """  Corresponds to IDD Field `Property Value 197`

        Args:
            value (float): value for IDD Field `Property Value 197`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 197"] = value

    @property
    def property_value_198(self):
        """Get property_value_198

        Returns:
            float: the value of `property_value_198` or None if not set
        """
        return self["Property Value 198"]

    @property_value_198.setter
    def property_value_198(self, value=None):
        """  Corresponds to IDD Field `Property Value 198`

        Args:
            value (float): value for IDD Field `Property Value 198`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 198"] = value

    @property
    def property_value_199(self):
        """Get property_value_199

        Returns:
            float: the value of `property_value_199` or None if not set
        """
        return self["Property Value 199"]

    @property_value_199.setter
    def property_value_199(self, value=None):
        """  Corresponds to IDD Field `Property Value 199`

        Args:
            value (float): value for IDD Field `Property Value 199`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 199"] = value

    @property
    def property_value_200(self):
        """Get property_value_200

        Returns:
            float: the value of `property_value_200` or None if not set
        """
        return self["Property Value 200"]

    @property_value_200.setter
    def property_value_200(self, value=None):
        """  Corresponds to IDD Field `Property Value 200`

        Args:
            value (float): value for IDD Field `Property Value 200`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 200"] = value

    @property
    def property_value_201(self):
        """Get property_value_201

        Returns:
            float: the value of `property_value_201` or None if not set
        """
        return self["Property Value 201"]

    @property_value_201.setter
    def property_value_201(self, value=None):
        """  Corresponds to IDD Field `Property Value 201`

        Args:
            value (float): value for IDD Field `Property Value 201`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 201"] = value

    @property
    def property_value_202(self):
        """Get property_value_202

        Returns:
            float: the value of `property_value_202` or None if not set
        """
        return self["Property Value 202"]

    @property_value_202.setter
    def property_value_202(self, value=None):
        """  Corresponds to IDD Field `Property Value 202`

        Args:
            value (float): value for IDD Field `Property Value 202`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 202"] = value

    @property
    def property_value_203(self):
        """Get property_value_203

        Returns:
            float: the value of `property_value_203` or None if not set
        """
        return self["Property Value 203"]

    @property_value_203.setter
    def property_value_203(self, value=None):
        """  Corresponds to IDD Field `Property Value 203`

        Args:
            value (float): value for IDD Field `Property Value 203`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 203"] = value

    @property
    def property_value_204(self):
        """Get property_value_204

        Returns:
            float: the value of `property_value_204` or None if not set
        """
        return self["Property Value 204"]

    @property_value_204.setter
    def property_value_204(self, value=None):
        """  Corresponds to IDD Field `Property Value 204`

        Args:
            value (float): value for IDD Field `Property Value 204`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 204"] = value

    @property
    def property_value_205(self):
        """Get property_value_205

        Returns:
            float: the value of `property_value_205` or None if not set
        """
        return self["Property Value 205"]

    @property_value_205.setter
    def property_value_205(self, value=None):
        """  Corresponds to IDD Field `Property Value 205`

        Args:
            value (float): value for IDD Field `Property Value 205`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 205"] = value

    @property
    def property_value_206(self):
        """Get property_value_206

        Returns:
            float: the value of `property_value_206` or None if not set
        """
        return self["Property Value 206"]

    @property_value_206.setter
    def property_value_206(self, value=None):
        """  Corresponds to IDD Field `Property Value 206`

        Args:
            value (float): value for IDD Field `Property Value 206`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 206"] = value

    @property
    def property_value_207(self):
        """Get property_value_207

        Returns:
            float: the value of `property_value_207` or None if not set
        """
        return self["Property Value 207"]

    @property_value_207.setter
    def property_value_207(self, value=None):
        """  Corresponds to IDD Field `Property Value 207`

        Args:
            value (float): value for IDD Field `Property Value 207`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 207"] = value

    @property
    def property_value_208(self):
        """Get property_value_208

        Returns:
            float: the value of `property_value_208` or None if not set
        """
        return self["Property Value 208"]

    @property_value_208.setter
    def property_value_208(self, value=None):
        """  Corresponds to IDD Field `Property Value 208`

        Args:
            value (float): value for IDD Field `Property Value 208`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 208"] = value

    @property
    def property_value_209(self):
        """Get property_value_209

        Returns:
            float: the value of `property_value_209` or None if not set
        """
        return self["Property Value 209"]

    @property_value_209.setter
    def property_value_209(self, value=None):
        """  Corresponds to IDD Field `Property Value 209`

        Args:
            value (float): value for IDD Field `Property Value 209`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 209"] = value

    @property
    def property_value_210(self):
        """Get property_value_210

        Returns:
            float: the value of `property_value_210` or None if not set
        """
        return self["Property Value 210"]

    @property_value_210.setter
    def property_value_210(self, value=None):
        """  Corresponds to IDD Field `Property Value 210`

        Args:
            value (float): value for IDD Field `Property Value 210`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 210"] = value

    @property
    def property_value_211(self):
        """Get property_value_211

        Returns:
            float: the value of `property_value_211` or None if not set
        """
        return self["Property Value 211"]

    @property_value_211.setter
    def property_value_211(self, value=None):
        """  Corresponds to IDD Field `Property Value 211`

        Args:
            value (float): value for IDD Field `Property Value 211`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 211"] = value

    @property
    def property_value_212(self):
        """Get property_value_212

        Returns:
            float: the value of `property_value_212` or None if not set
        """
        return self["Property Value 212"]

    @property_value_212.setter
    def property_value_212(self, value=None):
        """  Corresponds to IDD Field `Property Value 212`

        Args:
            value (float): value for IDD Field `Property Value 212`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 212"] = value

    @property
    def property_value_213(self):
        """Get property_value_213

        Returns:
            float: the value of `property_value_213` or None if not set
        """
        return self["Property Value 213"]

    @property_value_213.setter
    def property_value_213(self, value=None):
        """  Corresponds to IDD Field `Property Value 213`

        Args:
            value (float): value for IDD Field `Property Value 213`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 213"] = value

    @property
    def property_value_214(self):
        """Get property_value_214

        Returns:
            float: the value of `property_value_214` or None if not set
        """
        return self["Property Value 214"]

    @property_value_214.setter
    def property_value_214(self, value=None):
        """  Corresponds to IDD Field `Property Value 214`

        Args:
            value (float): value for IDD Field `Property Value 214`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 214"] = value

    @property
    def property_value_215(self):
        """Get property_value_215

        Returns:
            float: the value of `property_value_215` or None if not set
        """
        return self["Property Value 215"]

    @property_value_215.setter
    def property_value_215(self, value=None):
        """  Corresponds to IDD Field `Property Value 215`

        Args:
            value (float): value for IDD Field `Property Value 215`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 215"] = value

    @property
    def property_value_216(self):
        """Get property_value_216

        Returns:
            float: the value of `property_value_216` or None if not set
        """
        return self["Property Value 216"]

    @property_value_216.setter
    def property_value_216(self, value=None):
        """  Corresponds to IDD Field `Property Value 216`

        Args:
            value (float): value for IDD Field `Property Value 216`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 216"] = value

    @property
    def property_value_217(self):
        """Get property_value_217

        Returns:
            float: the value of `property_value_217` or None if not set
        """
        return self["Property Value 217"]

    @property_value_217.setter
    def property_value_217(self, value=None):
        """  Corresponds to IDD Field `Property Value 217`

        Args:
            value (float): value for IDD Field `Property Value 217`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 217"] = value

    @property
    def property_value_218(self):
        """Get property_value_218

        Returns:
            float: the value of `property_value_218` or None if not set
        """
        return self["Property Value 218"]

    @property_value_218.setter
    def property_value_218(self, value=None):
        """  Corresponds to IDD Field `Property Value 218`

        Args:
            value (float): value for IDD Field `Property Value 218`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 218"] = value

    @property
    def property_value_219(self):
        """Get property_value_219

        Returns:
            float: the value of `property_value_219` or None if not set
        """
        return self["Property Value 219"]

    @property_value_219.setter
    def property_value_219(self, value=None):
        """  Corresponds to IDD Field `Property Value 219`

        Args:
            value (float): value for IDD Field `Property Value 219`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 219"] = value

    @property
    def property_value_220(self):
        """Get property_value_220

        Returns:
            float: the value of `property_value_220` or None if not set
        """
        return self["Property Value 220"]

    @property_value_220.setter
    def property_value_220(self, value=None):
        """  Corresponds to IDD Field `Property Value 220`

        Args:
            value (float): value for IDD Field `Property Value 220`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 220"] = value

    @property
    def property_value_221(self):
        """Get property_value_221

        Returns:
            float: the value of `property_value_221` or None if not set
        """
        return self["Property Value 221"]

    @property_value_221.setter
    def property_value_221(self, value=None):
        """  Corresponds to IDD Field `Property Value 221`

        Args:
            value (float): value for IDD Field `Property Value 221`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 221"] = value

    @property
    def property_value_222(self):
        """Get property_value_222

        Returns:
            float: the value of `property_value_222` or None if not set
        """
        return self["Property Value 222"]

    @property_value_222.setter
    def property_value_222(self, value=None):
        """  Corresponds to IDD Field `Property Value 222`

        Args:
            value (float): value for IDD Field `Property Value 222`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 222"] = value

    @property
    def property_value_223(self):
        """Get property_value_223

        Returns:
            float: the value of `property_value_223` or None if not set
        """
        return self["Property Value 223"]

    @property_value_223.setter
    def property_value_223(self, value=None):
        """  Corresponds to IDD Field `Property Value 223`

        Args:
            value (float): value for IDD Field `Property Value 223`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 223"] = value

    @property
    def property_value_224(self):
        """Get property_value_224

        Returns:
            float: the value of `property_value_224` or None if not set
        """
        return self["Property Value 224"]

    @property_value_224.setter
    def property_value_224(self, value=None):
        """  Corresponds to IDD Field `Property Value 224`

        Args:
            value (float): value for IDD Field `Property Value 224`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 224"] = value

    @property
    def property_value_225(self):
        """Get property_value_225

        Returns:
            float: the value of `property_value_225` or None if not set
        """
        return self["Property Value 225"]

    @property_value_225.setter
    def property_value_225(self, value=None):
        """  Corresponds to IDD Field `Property Value 225`

        Args:
            value (float): value for IDD Field `Property Value 225`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 225"] = value

    @property
    def property_value_226(self):
        """Get property_value_226

        Returns:
            float: the value of `property_value_226` or None if not set
        """
        return self["Property Value 226"]

    @property_value_226.setter
    def property_value_226(self, value=None):
        """  Corresponds to IDD Field `Property Value 226`

        Args:
            value (float): value for IDD Field `Property Value 226`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 226"] = value

    @property
    def property_value_227(self):
        """Get property_value_227

        Returns:
            float: the value of `property_value_227` or None if not set
        """
        return self["Property Value 227"]

    @property_value_227.setter
    def property_value_227(self, value=None):
        """  Corresponds to IDD Field `Property Value 227`

        Args:
            value (float): value for IDD Field `Property Value 227`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 227"] = value

    @property
    def property_value_228(self):
        """Get property_value_228

        Returns:
            float: the value of `property_value_228` or None if not set
        """
        return self["Property Value 228"]

    @property_value_228.setter
    def property_value_228(self, value=None):
        """  Corresponds to IDD Field `Property Value 228`

        Args:
            value (float): value for IDD Field `Property Value 228`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 228"] = value

    @property
    def property_value_229(self):
        """Get property_value_229

        Returns:
            float: the value of `property_value_229` or None if not set
        """
        return self["Property Value 229"]

    @property_value_229.setter
    def property_value_229(self, value=None):
        """  Corresponds to IDD Field `Property Value 229`

        Args:
            value (float): value for IDD Field `Property Value 229`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 229"] = value

    @property
    def property_value_230(self):
        """Get property_value_230

        Returns:
            float: the value of `property_value_230` or None if not set
        """
        return self["Property Value 230"]

    @property_value_230.setter
    def property_value_230(self, value=None):
        """  Corresponds to IDD Field `Property Value 230`

        Args:
            value (float): value for IDD Field `Property Value 230`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 230"] = value

    @property
    def property_value_231(self):
        """Get property_value_231

        Returns:
            float: the value of `property_value_231` or None if not set
        """
        return self["Property Value 231"]

    @property_value_231.setter
    def property_value_231(self, value=None):
        """  Corresponds to IDD Field `Property Value 231`

        Args:
            value (float): value for IDD Field `Property Value 231`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 231"] = value

    @property
    def property_value_232(self):
        """Get property_value_232

        Returns:
            float: the value of `property_value_232` or None if not set
        """
        return self["Property Value 232"]

    @property_value_232.setter
    def property_value_232(self, value=None):
        """  Corresponds to IDD Field `Property Value 232`

        Args:
            value (float): value for IDD Field `Property Value 232`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 232"] = value

    @property
    def property_value_233(self):
        """Get property_value_233

        Returns:
            float: the value of `property_value_233` or None if not set
        """
        return self["Property Value 233"]

    @property_value_233.setter
    def property_value_233(self, value=None):
        """  Corresponds to IDD Field `Property Value 233`

        Args:
            value (float): value for IDD Field `Property Value 233`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 233"] = value

    @property
    def property_value_234(self):
        """Get property_value_234

        Returns:
            float: the value of `property_value_234` or None if not set
        """
        return self["Property Value 234"]

    @property_value_234.setter
    def property_value_234(self, value=None):
        """  Corresponds to IDD Field `Property Value 234`

        Args:
            value (float): value for IDD Field `Property Value 234`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 234"] = value

    @property
    def property_value_235(self):
        """Get property_value_235

        Returns:
            float: the value of `property_value_235` or None if not set
        """
        return self["Property Value 235"]

    @property_value_235.setter
    def property_value_235(self, value=None):
        """  Corresponds to IDD Field `Property Value 235`

        Args:
            value (float): value for IDD Field `Property Value 235`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 235"] = value

    @property
    def property_value_236(self):
        """Get property_value_236

        Returns:
            float: the value of `property_value_236` or None if not set
        """
        return self["Property Value 236"]

    @property_value_236.setter
    def property_value_236(self, value=None):
        """  Corresponds to IDD Field `Property Value 236`

        Args:
            value (float): value for IDD Field `Property Value 236`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 236"] = value

    @property
    def property_value_237(self):
        """Get property_value_237

        Returns:
            float: the value of `property_value_237` or None if not set
        """
        return self["Property Value 237"]

    @property_value_237.setter
    def property_value_237(self, value=None):
        """  Corresponds to IDD Field `Property Value 237`

        Args:
            value (float): value for IDD Field `Property Value 237`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 237"] = value

    @property
    def property_value_238(self):
        """Get property_value_238

        Returns:
            float: the value of `property_value_238` or None if not set
        """
        return self["Property Value 238"]

    @property_value_238.setter
    def property_value_238(self, value=None):
        """  Corresponds to IDD Field `Property Value 238`

        Args:
            value (float): value for IDD Field `Property Value 238`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 238"] = value

    @property
    def property_value_239(self):
        """Get property_value_239

        Returns:
            float: the value of `property_value_239` or None if not set
        """
        return self["Property Value 239"]

    @property_value_239.setter
    def property_value_239(self, value=None):
        """  Corresponds to IDD Field `Property Value 239`

        Args:
            value (float): value for IDD Field `Property Value 239`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 239"] = value

    @property
    def property_value_240(self):
        """Get property_value_240

        Returns:
            float: the value of `property_value_240` or None if not set
        """
        return self["Property Value 240"]

    @property_value_240.setter
    def property_value_240(self, value=None):
        """  Corresponds to IDD Field `Property Value 240`

        Args:
            value (float): value for IDD Field `Property Value 240`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 240"] = value

    @property
    def property_value_241(self):
        """Get property_value_241

        Returns:
            float: the value of `property_value_241` or None if not set
        """
        return self["Property Value 241"]

    @property_value_241.setter
    def property_value_241(self, value=None):
        """  Corresponds to IDD Field `Property Value 241`

        Args:
            value (float): value for IDD Field `Property Value 241`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 241"] = value

    @property
    def property_value_242(self):
        """Get property_value_242

        Returns:
            float: the value of `property_value_242` or None if not set
        """
        return self["Property Value 242"]

    @property_value_242.setter
    def property_value_242(self, value=None):
        """  Corresponds to IDD Field `Property Value 242`

        Args:
            value (float): value for IDD Field `Property Value 242`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 242"] = value

    @property
    def property_value_243(self):
        """Get property_value_243

        Returns:
            float: the value of `property_value_243` or None if not set
        """
        return self["Property Value 243"]

    @property_value_243.setter
    def property_value_243(self, value=None):
        """  Corresponds to IDD Field `Property Value 243`

        Args:
            value (float): value for IDD Field `Property Value 243`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 243"] = value

    @property
    def property_value_244(self):
        """Get property_value_244

        Returns:
            float: the value of `property_value_244` or None if not set
        """
        return self["Property Value 244"]

    @property_value_244.setter
    def property_value_244(self, value=None):
        """  Corresponds to IDD Field `Property Value 244`

        Args:
            value (float): value for IDD Field `Property Value 244`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 244"] = value

    @property
    def property_value_245(self):
        """Get property_value_245

        Returns:
            float: the value of `property_value_245` or None if not set
        """
        return self["Property Value 245"]

    @property_value_245.setter
    def property_value_245(self, value=None):
        """  Corresponds to IDD Field `Property Value 245`

        Args:
            value (float): value for IDD Field `Property Value 245`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 245"] = value

    @property
    def property_value_246(self):
        """Get property_value_246

        Returns:
            float: the value of `property_value_246` or None if not set
        """
        return self["Property Value 246"]

    @property_value_246.setter
    def property_value_246(self, value=None):
        """  Corresponds to IDD Field `Property Value 246`

        Args:
            value (float): value for IDD Field `Property Value 246`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 246"] = value

    @property
    def property_value_247(self):
        """Get property_value_247

        Returns:
            float: the value of `property_value_247` or None if not set
        """
        return self["Property Value 247"]

    @property_value_247.setter
    def property_value_247(self, value=None):
        """  Corresponds to IDD Field `Property Value 247`

        Args:
            value (float): value for IDD Field `Property Value 247`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 247"] = value

    @property
    def property_value_248(self):
        """Get property_value_248

        Returns:
            float: the value of `property_value_248` or None if not set
        """
        return self["Property Value 248"]

    @property_value_248.setter
    def property_value_248(self, value=None):
        """  Corresponds to IDD Field `Property Value 248`

        Args:
            value (float): value for IDD Field `Property Value 248`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 248"] = value

    @property
    def property_value_249(self):
        """Get property_value_249

        Returns:
            float: the value of `property_value_249` or None if not set
        """
        return self["Property Value 249"]

    @property_value_249.setter
    def property_value_249(self, value=None):
        """  Corresponds to IDD Field `Property Value 249`

        Args:
            value (float): value for IDD Field `Property Value 249`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 249"] = value

    @property
    def property_value_250(self):
        """Get property_value_250

        Returns:
            float: the value of `property_value_250` or None if not set
        """
        return self["Property Value 250"]

    @property_value_250.setter
    def property_value_250(self, value=None):
        """  Corresponds to IDD Field `Property Value 250`

        Args:
            value (float): value for IDD Field `Property Value 250`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 250"] = value


class FluidPropertiesConcentration(DataObject):
    """ Corresponds to IDD object `FluidProperties:Concentration`
        fluid properties for water/other fluid mixtures
    """
    schema = {'min-fields': 0, 'name': u'FluidProperties:Concentration', 'pyname': u'FluidPropertiesConcentration', 'format': None, 'fields': OrderedDict([(u'fluid name', {'name': u'Fluid Name', 'pyname': u'fluid_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'fluid property type', {'name': u'Fluid Property Type', 'pyname': u'fluid_property_type', 'required-field': False, 'autosizable': False, 'accepted-values': [u'Density', u'SpecificHeat', u'Conductivity', u'Viscosity'], 'autocalculatable': False, 'type': 'alpha'}), (u'temperature values name', {'name': u'Temperature Values Name', 'pyname': u'temperature_values_name', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'object-list'}), (u'concentration', {'name': u'Concentration', 'pyname': u'concentration', 'maximum': 1.0, 'required-field': False, 'autosizable': False, 'minimum': 0.0, 'autocalculatable': False, 'type': u'real', 'unit': u'dimensionless'}), (u'property value 1', {'name': u'Property Value 1', 'pyname': u'property_value_1', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 2', {'name': u'Property Value 2', 'pyname': u'property_value_2', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 3', {'name': u'Property Value 3', 'pyname': u'property_value_3', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 4', {'name': u'Property Value 4', 'pyname': u'property_value_4', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 5', {'name': u'Property Value 5', 'pyname': u'property_value_5', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 6', {'name': u'Property Value 6', 'pyname': u'property_value_6', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 7', {'name': u'Property Value 7', 'pyname': u'property_value_7', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 8', {'name': u'Property Value 8', 'pyname': u'property_value_8', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 9', {'name': u'Property Value 9', 'pyname': u'property_value_9', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 10', {'name': u'Property Value 10', 'pyname': u'property_value_10', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 11', {'name': u'Property Value 11', 'pyname': u'property_value_11', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 12', {'name': u'Property Value 12', 'pyname': u'property_value_12', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 13', {'name': u'Property Value 13', 'pyname': u'property_value_13', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 14', {'name': u'Property Value 14', 'pyname': u'property_value_14', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 15', {'name': u'Property Value 15', 'pyname': u'property_value_15', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 16', {'name': u'Property Value 16', 'pyname': u'property_value_16', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 17', {'name': u'Property Value 17', 'pyname': u'property_value_17', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 18', {'name': u'Property Value 18', 'pyname': u'property_value_18', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 19', {'name': u'Property Value 19', 'pyname': u'property_value_19', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 20', {'name': u'Property Value 20', 'pyname': u'property_value_20', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 21', {'name': u'Property Value 21', 'pyname': u'property_value_21', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 22', {'name': u'Property Value 22', 'pyname': u'property_value_22', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 23', {'name': u'Property Value 23', 'pyname': u'property_value_23', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 24', {'name': u'Property Value 24', 'pyname': u'property_value_24', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 25', {'name': u'Property Value 25', 'pyname': u'property_value_25', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 26', {'name': u'Property Value 26', 'pyname': u'property_value_26', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 27', {'name': u'Property Value 27', 'pyname': u'property_value_27', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 28', {'name': u'Property Value 28', 'pyname': u'property_value_28', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 29', {'name': u'Property Value 29', 'pyname': u'property_value_29', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 30', {'name': u'Property Value 30', 'pyname': u'property_value_30', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 31', {'name': u'Property Value 31', 'pyname': u'property_value_31', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 32', {'name': u'Property Value 32', 'pyname': u'property_value_32', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 33', {'name': u'Property Value 33', 'pyname': u'property_value_33', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 34', {'name': u'Property Value 34', 'pyname': u'property_value_34', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 35', {'name': u'Property Value 35', 'pyname': u'property_value_35', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 36', {'name': u'Property Value 36', 'pyname': u'property_value_36', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 37', {'name': u'Property Value 37', 'pyname': u'property_value_37', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 38', {'name': u'Property Value 38', 'pyname': u'property_value_38', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 39', {'name': u'Property Value 39', 'pyname': u'property_value_39', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 40', {'name': u'Property Value 40', 'pyname': u'property_value_40', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 41', {'name': u'Property Value 41', 'pyname': u'property_value_41', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 42', {'name': u'Property Value 42', 'pyname': u'property_value_42', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 43', {'name': u'Property Value 43', 'pyname': u'property_value_43', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 44', {'name': u'Property Value 44', 'pyname': u'property_value_44', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 45', {'name': u'Property Value 45', 'pyname': u'property_value_45', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 46', {'name': u'Property Value 46', 'pyname': u'property_value_46', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 47', {'name': u'Property Value 47', 'pyname': u'property_value_47', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 48', {'name': u'Property Value 48', 'pyname': u'property_value_48', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 49', {'name': u'Property Value 49', 'pyname': u'property_value_49', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 50', {'name': u'Property Value 50', 'pyname': u'property_value_50', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 51', {'name': u'Property Value 51', 'pyname': u'property_value_51', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 52', {'name': u'Property Value 52', 'pyname': u'property_value_52', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 53', {'name': u'Property Value 53', 'pyname': u'property_value_53', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 54', {'name': u'Property Value 54', 'pyname': u'property_value_54', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 55', {'name': u'Property Value 55', 'pyname': u'property_value_55', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 56', {'name': u'Property Value 56', 'pyname': u'property_value_56', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 57', {'name': u'Property Value 57', 'pyname': u'property_value_57', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 58', {'name': u'Property Value 58', 'pyname': u'property_value_58', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 59', {'name': u'Property Value 59', 'pyname': u'property_value_59', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 60', {'name': u'Property Value 60', 'pyname': u'property_value_60', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 61', {'name': u'Property Value 61', 'pyname': u'property_value_61', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 62', {'name': u'Property Value 62', 'pyname': u'property_value_62', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 63', {'name': u'Property Value 63', 'pyname': u'property_value_63', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 64', {'name': u'Property Value 64', 'pyname': u'property_value_64', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 65', {'name': u'Property Value 65', 'pyname': u'property_value_65', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 66', {'name': u'Property Value 66', 'pyname': u'property_value_66', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 67', {'name': u'Property Value 67', 'pyname': u'property_value_67', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 68', {'name': u'Property Value 68', 'pyname': u'property_value_68', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 69', {'name': u'Property Value 69', 'pyname': u'property_value_69', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 70', {'name': u'Property Value 70', 'pyname': u'property_value_70', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 71', {'name': u'Property Value 71', 'pyname': u'property_value_71', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 72', {'name': u'Property Value 72', 'pyname': u'property_value_72', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 73', {'name': u'Property Value 73', 'pyname': u'property_value_73', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 74', {'name': u'Property Value 74', 'pyname': u'property_value_74', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 75', {'name': u'Property Value 75', 'pyname': u'property_value_75', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 76', {'name': u'Property Value 76', 'pyname': u'property_value_76', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 77', {'name': u'Property Value 77', 'pyname': u'property_value_77', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 78', {'name': u'Property Value 78', 'pyname': u'property_value_78', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 79', {'name': u'Property Value 79', 'pyname': u'property_value_79', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 80', {'name': u'Property Value 80', 'pyname': u'property_value_80', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 81', {'name': u'Property Value 81', 'pyname': u'property_value_81', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 82', {'name': u'Property Value 82', 'pyname': u'property_value_82', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 83', {'name': u'Property Value 83', 'pyname': u'property_value_83', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 84', {'name': u'Property Value 84', 'pyname': u'property_value_84', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 85', {'name': u'Property Value 85', 'pyname': u'property_value_85', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 86', {'name': u'Property Value 86', 'pyname': u'property_value_86', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 87', {'name': u'Property Value 87', 'pyname': u'property_value_87', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 88', {'name': u'Property Value 88', 'pyname': u'property_value_88', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 89', {'name': u'Property Value 89', 'pyname': u'property_value_89', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 90', {'name': u'Property Value 90', 'pyname': u'property_value_90', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 91', {'name': u'Property Value 91', 'pyname': u'property_value_91', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 92', {'name': u'Property Value 92', 'pyname': u'property_value_92', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 93', {'name': u'Property Value 93', 'pyname': u'property_value_93', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 94', {'name': u'Property Value 94', 'pyname': u'property_value_94', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 95', {'name': u'Property Value 95', 'pyname': u'property_value_95', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 96', {'name': u'Property Value 96', 'pyname': u'property_value_96', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 97', {'name': u'Property Value 97', 'pyname': u'property_value_97', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 98', {'name': u'Property Value 98', 'pyname': u'property_value_98', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 99', {'name': u'Property Value 99', 'pyname': u'property_value_99', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 100', {'name': u'Property Value 100', 'pyname': u'property_value_100', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 101', {'name': u'Property Value 101', 'pyname': u'property_value_101', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 102', {'name': u'Property Value 102', 'pyname': u'property_value_102', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 103', {'name': u'Property Value 103', 'pyname': u'property_value_103', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 104', {'name': u'Property Value 104', 'pyname': u'property_value_104', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 105', {'name': u'Property Value 105', 'pyname': u'property_value_105', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 106', {'name': u'Property Value 106', 'pyname': u'property_value_106', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 107', {'name': u'Property Value 107', 'pyname': u'property_value_107', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 108', {'name': u'Property Value 108', 'pyname': u'property_value_108', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 109', {'name': u'Property Value 109', 'pyname': u'property_value_109', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 110', {'name': u'Property Value 110', 'pyname': u'property_value_110', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 111', {'name': u'Property Value 111', 'pyname': u'property_value_111', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 112', {'name': u'Property Value 112', 'pyname': u'property_value_112', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 113', {'name': u'Property Value 113', 'pyname': u'property_value_113', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 114', {'name': u'Property Value 114', 'pyname': u'property_value_114', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 115', {'name': u'Property Value 115', 'pyname': u'property_value_115', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 116', {'name': u'Property Value 116', 'pyname': u'property_value_116', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 117', {'name': u'Property Value 117', 'pyname': u'property_value_117', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 118', {'name': u'Property Value 118', 'pyname': u'property_value_118', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 119', {'name': u'Property Value 119', 'pyname': u'property_value_119', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 120', {'name': u'Property Value 120', 'pyname': u'property_value_120', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 121', {'name': u'Property Value 121', 'pyname': u'property_value_121', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 122', {'name': u'Property Value 122', 'pyname': u'property_value_122', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 123', {'name': u'Property Value 123', 'pyname': u'property_value_123', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 124', {'name': u'Property Value 124', 'pyname': u'property_value_124', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 125', {'name': u'Property Value 125', 'pyname': u'property_value_125', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 126', {'name': u'Property Value 126', 'pyname': u'property_value_126', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 127', {'name': u'Property Value 127', 'pyname': u'property_value_127', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 128', {'name': u'Property Value 128', 'pyname': u'property_value_128', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 129', {'name': u'Property Value 129', 'pyname': u'property_value_129', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 130', {'name': u'Property Value 130', 'pyname': u'property_value_130', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 131', {'name': u'Property Value 131', 'pyname': u'property_value_131', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 132', {'name': u'Property Value 132', 'pyname': u'property_value_132', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 133', {'name': u'Property Value 133', 'pyname': u'property_value_133', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 134', {'name': u'Property Value 134', 'pyname': u'property_value_134', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 135', {'name': u'Property Value 135', 'pyname': u'property_value_135', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 136', {'name': u'Property Value 136', 'pyname': u'property_value_136', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 137', {'name': u'Property Value 137', 'pyname': u'property_value_137', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 138', {'name': u'Property Value 138', 'pyname': u'property_value_138', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 139', {'name': u'Property Value 139', 'pyname': u'property_value_139', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 140', {'name': u'Property Value 140', 'pyname': u'property_value_140', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 141', {'name': u'Property Value 141', 'pyname': u'property_value_141', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 142', {'name': u'Property Value 142', 'pyname': u'property_value_142', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 143', {'name': u'Property Value 143', 'pyname': u'property_value_143', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 144', {'name': u'Property Value 144', 'pyname': u'property_value_144', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 145', {'name': u'Property Value 145', 'pyname': u'property_value_145', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 146', {'name': u'Property Value 146', 'pyname': u'property_value_146', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 147', {'name': u'Property Value 147', 'pyname': u'property_value_147', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 148', {'name': u'Property Value 148', 'pyname': u'property_value_148', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 149', {'name': u'Property Value 149', 'pyname': u'property_value_149', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 150', {'name': u'Property Value 150', 'pyname': u'property_value_150', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 151', {'name': u'Property Value 151', 'pyname': u'property_value_151', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 152', {'name': u'Property Value 152', 'pyname': u'property_value_152', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 153', {'name': u'Property Value 153', 'pyname': u'property_value_153', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 154', {'name': u'Property Value 154', 'pyname': u'property_value_154', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 155', {'name': u'Property Value 155', 'pyname': u'property_value_155', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 156', {'name': u'Property Value 156', 'pyname': u'property_value_156', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 157', {'name': u'Property Value 157', 'pyname': u'property_value_157', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 158', {'name': u'Property Value 158', 'pyname': u'property_value_158', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 159', {'name': u'Property Value 159', 'pyname': u'property_value_159', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 160', {'name': u'Property Value 160', 'pyname': u'property_value_160', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 161', {'name': u'Property Value 161', 'pyname': u'property_value_161', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 162', {'name': u'Property Value 162', 'pyname': u'property_value_162', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 163', {'name': u'Property Value 163', 'pyname': u'property_value_163', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 164', {'name': u'Property Value 164', 'pyname': u'property_value_164', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 165', {'name': u'Property Value 165', 'pyname': u'property_value_165', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 166', {'name': u'Property Value 166', 'pyname': u'property_value_166', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 167', {'name': u'Property Value 167', 'pyname': u'property_value_167', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 168', {'name': u'Property Value 168', 'pyname': u'property_value_168', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 169', {'name': u'Property Value 169', 'pyname': u'property_value_169', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 170', {'name': u'Property Value 170', 'pyname': u'property_value_170', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 171', {'name': u'Property Value 171', 'pyname': u'property_value_171', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 172', {'name': u'Property Value 172', 'pyname': u'property_value_172', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 173', {'name': u'Property Value 173', 'pyname': u'property_value_173', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 174', {'name': u'Property Value 174', 'pyname': u'property_value_174', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 175', {'name': u'Property Value 175', 'pyname': u'property_value_175', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 176', {'name': u'Property Value 176', 'pyname': u'property_value_176', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 177', {'name': u'Property Value 177', 'pyname': u'property_value_177', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 178', {'name': u'Property Value 178', 'pyname': u'property_value_178', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 179', {'name': u'Property Value 179', 'pyname': u'property_value_179', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 180', {'name': u'Property Value 180', 'pyname': u'property_value_180', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 181', {'name': u'Property Value 181', 'pyname': u'property_value_181', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 182', {'name': u'Property Value 182', 'pyname': u'property_value_182', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 183', {'name': u'Property Value 183', 'pyname': u'property_value_183', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 184', {'name': u'Property Value 184', 'pyname': u'property_value_184', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 185', {'name': u'Property Value 185', 'pyname': u'property_value_185', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 186', {'name': u'Property Value 186', 'pyname': u'property_value_186', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 187', {'name': u'Property Value 187', 'pyname': u'property_value_187', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 188', {'name': u'Property Value 188', 'pyname': u'property_value_188', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 189', {'name': u'Property Value 189', 'pyname': u'property_value_189', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 190', {'name': u'Property Value 190', 'pyname': u'property_value_190', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 191', {'name': u'Property Value 191', 'pyname': u'property_value_191', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 192', {'name': u'Property Value 192', 'pyname': u'property_value_192', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 193', {'name': u'Property Value 193', 'pyname': u'property_value_193', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 194', {'name': u'Property Value 194', 'pyname': u'property_value_194', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 195', {'name': u'Property Value 195', 'pyname': u'property_value_195', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 196', {'name': u'Property Value 196', 'pyname': u'property_value_196', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 197', {'name': u'Property Value 197', 'pyname': u'property_value_197', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 198', {'name': u'Property Value 198', 'pyname': u'property_value_198', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 199', {'name': u'Property Value 199', 'pyname': u'property_value_199', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 200', {'name': u'Property Value 200', 'pyname': u'property_value_200', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 201', {'name': u'Property Value 201', 'pyname': u'property_value_201', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 202', {'name': u'Property Value 202', 'pyname': u'property_value_202', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 203', {'name': u'Property Value 203', 'pyname': u'property_value_203', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 204', {'name': u'Property Value 204', 'pyname': u'property_value_204', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 205', {'name': u'Property Value 205', 'pyname': u'property_value_205', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 206', {'name': u'Property Value 206', 'pyname': u'property_value_206', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 207', {'name': u'Property Value 207', 'pyname': u'property_value_207', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 208', {'name': u'Property Value 208', 'pyname': u'property_value_208', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 209', {'name': u'Property Value 209', 'pyname': u'property_value_209', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 210', {'name': u'Property Value 210', 'pyname': u'property_value_210', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 211', {'name': u'Property Value 211', 'pyname': u'property_value_211', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 212', {'name': u'Property Value 212', 'pyname': u'property_value_212', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 213', {'name': u'Property Value 213', 'pyname': u'property_value_213', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 214', {'name': u'Property Value 214', 'pyname': u'property_value_214', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 215', {'name': u'Property Value 215', 'pyname': u'property_value_215', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 216', {'name': u'Property Value 216', 'pyname': u'property_value_216', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 217', {'name': u'Property Value 217', 'pyname': u'property_value_217', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 218', {'name': u'Property Value 218', 'pyname': u'property_value_218', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 219', {'name': u'Property Value 219', 'pyname': u'property_value_219', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 220', {'name': u'Property Value 220', 'pyname': u'property_value_220', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 221', {'name': u'Property Value 221', 'pyname': u'property_value_221', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 222', {'name': u'Property Value 222', 'pyname': u'property_value_222', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 223', {'name': u'Property Value 223', 'pyname': u'property_value_223', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 224', {'name': u'Property Value 224', 'pyname': u'property_value_224', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 225', {'name': u'Property Value 225', 'pyname': u'property_value_225', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 226', {'name': u'Property Value 226', 'pyname': u'property_value_226', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 227', {'name': u'Property Value 227', 'pyname': u'property_value_227', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 228', {'name': u'Property Value 228', 'pyname': u'property_value_228', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 229', {'name': u'Property Value 229', 'pyname': u'property_value_229', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 230', {'name': u'Property Value 230', 'pyname': u'property_value_230', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 231', {'name': u'Property Value 231', 'pyname': u'property_value_231', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 232', {'name': u'Property Value 232', 'pyname': u'property_value_232', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 233', {'name': u'Property Value 233', 'pyname': u'property_value_233', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 234', {'name': u'Property Value 234', 'pyname': u'property_value_234', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 235', {'name': u'Property Value 235', 'pyname': u'property_value_235', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 236', {'name': u'Property Value 236', 'pyname': u'property_value_236', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 237', {'name': u'Property Value 237', 'pyname': u'property_value_237', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 238', {'name': u'Property Value 238', 'pyname': u'property_value_238', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 239', {'name': u'Property Value 239', 'pyname': u'property_value_239', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 240', {'name': u'Property Value 240', 'pyname': u'property_value_240', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 241', {'name': u'Property Value 241', 'pyname': u'property_value_241', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 242', {'name': u'Property Value 242', 'pyname': u'property_value_242', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 243', {'name': u'Property Value 243', 'pyname': u'property_value_243', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 244', {'name': u'Property Value 244', 'pyname': u'property_value_244', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 245', {'name': u'Property Value 245', 'pyname': u'property_value_245', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 246', {'name': u'Property Value 246', 'pyname': u'property_value_246', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 247', {'name': u'Property Value 247', 'pyname': u'property_value_247', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 248', {'name': u'Property Value 248', 'pyname': u'property_value_248', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 249', {'name': u'Property Value 249', 'pyname': u'property_value_249', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'}), (u'property value 250', {'name': u'Property Value 250', 'pyname': u'property_value_250', 'required-field': False, 'autosizable': False, 'autocalculatable': False, 'type': u'real'})]), 'extensible-fields': OrderedDict(), 'unique-object': False, 'required-object': False}

    @property
    def fluid_name(self):
        """Get fluid_name

        Returns:
            str: the value of `fluid_name` or None if not set
        """
        return self["Fluid Name"]

    @fluid_name.setter
    def fluid_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Name`
        should not be any of the defaults (Water, EthyleneGlycol, or PropyleneGlycol)

        Args:
            value (str): value for IDD Field `Fluid Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Name"] = value

    @property
    def fluid_property_type(self):
        """Get fluid_property_type

        Returns:
            str: the value of `fluid_property_type` or None if not set
        """
        return self["Fluid Property Type"]

    @fluid_property_type.setter
    def fluid_property_type(self, value=None):
        """  Corresponds to IDD Field `Fluid Property Type`
        Density Units are kg/m3
        SpecificHeat Units are J/kg-K
        Conductivity Units are W/m-K
        Viscosity Units are N-s/m2

        Args:
            value (str): value for IDD Field `Fluid Property Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fluid Property Type"] = value

    @property
    def temperature_values_name(self):
        """Get temperature_values_name

        Returns:
            str: the value of `temperature_values_name` or None if not set
        """
        return self["Temperature Values Name"]

    @temperature_values_name.setter
    def temperature_values_name(self, value=None):
        """  Corresponds to IDD Field `Temperature Values Name`
        Enter the name of a FluidProperties:Temperatures object.

        Args:
            value (str): value for IDD Field `Temperature Values Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Temperature Values Name"] = value

    @property
    def concentration(self):
        """Get concentration

        Returns:
            float: the value of `concentration` or None if not set
        """
        return self["Concentration"]

    @concentration.setter
    def concentration(self, value=None):
        """  Corresponds to IDD Field `Concentration`
        Glycol concentration for this list of properties entered as a fraction

        Args:
            value (float): value for IDD Field `Concentration`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Concentration"] = value

    @property
    def property_value_1(self):
        """Get property_value_1

        Returns:
            float: the value of `property_value_1` or None if not set
        """
        return self["Property Value 1"]

    @property_value_1.setter
    def property_value_1(self, value=None):
        """  Corresponds to IDD Field `Property Value 1`

        Args:
            value (float): value for IDD Field `Property Value 1`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 1"] = value

    @property
    def property_value_2(self):
        """Get property_value_2

        Returns:
            float: the value of `property_value_2` or None if not set
        """
        return self["Property Value 2"]

    @property_value_2.setter
    def property_value_2(self, value=None):
        """  Corresponds to IDD Field `Property Value 2`

        Args:
            value (float): value for IDD Field `Property Value 2`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 2"] = value

    @property
    def property_value_3(self):
        """Get property_value_3

        Returns:
            float: the value of `property_value_3` or None if not set
        """
        return self["Property Value 3"]

    @property_value_3.setter
    def property_value_3(self, value=None):
        """  Corresponds to IDD Field `Property Value 3`

        Args:
            value (float): value for IDD Field `Property Value 3`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 3"] = value

    @property
    def property_value_4(self):
        """Get property_value_4

        Returns:
            float: the value of `property_value_4` or None if not set
        """
        return self["Property Value 4"]

    @property_value_4.setter
    def property_value_4(self, value=None):
        """  Corresponds to IDD Field `Property Value 4`

        Args:
            value (float): value for IDD Field `Property Value 4`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 4"] = value

    @property
    def property_value_5(self):
        """Get property_value_5

        Returns:
            float: the value of `property_value_5` or None if not set
        """
        return self["Property Value 5"]

    @property_value_5.setter
    def property_value_5(self, value=None):
        """  Corresponds to IDD Field `Property Value 5`

        Args:
            value (float): value for IDD Field `Property Value 5`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 5"] = value

    @property
    def property_value_6(self):
        """Get property_value_6

        Returns:
            float: the value of `property_value_6` or None if not set
        """
        return self["Property Value 6"]

    @property_value_6.setter
    def property_value_6(self, value=None):
        """  Corresponds to IDD Field `Property Value 6`

        Args:
            value (float): value for IDD Field `Property Value 6`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 6"] = value

    @property
    def property_value_7(self):
        """Get property_value_7

        Returns:
            float: the value of `property_value_7` or None if not set
        """
        return self["Property Value 7"]

    @property_value_7.setter
    def property_value_7(self, value=None):
        """  Corresponds to IDD Field `Property Value 7`

        Args:
            value (float): value for IDD Field `Property Value 7`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 7"] = value

    @property
    def property_value_8(self):
        """Get property_value_8

        Returns:
            float: the value of `property_value_8` or None if not set
        """
        return self["Property Value 8"]

    @property_value_8.setter
    def property_value_8(self, value=None):
        """  Corresponds to IDD Field `Property Value 8`

        Args:
            value (float): value for IDD Field `Property Value 8`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 8"] = value

    @property
    def property_value_9(self):
        """Get property_value_9

        Returns:
            float: the value of `property_value_9` or None if not set
        """
        return self["Property Value 9"]

    @property_value_9.setter
    def property_value_9(self, value=None):
        """  Corresponds to IDD Field `Property Value 9`

        Args:
            value (float): value for IDD Field `Property Value 9`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 9"] = value

    @property
    def property_value_10(self):
        """Get property_value_10

        Returns:
            float: the value of `property_value_10` or None if not set
        """
        return self["Property Value 10"]

    @property_value_10.setter
    def property_value_10(self, value=None):
        """  Corresponds to IDD Field `Property Value 10`

        Args:
            value (float): value for IDD Field `Property Value 10`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 10"] = value

    @property
    def property_value_11(self):
        """Get property_value_11

        Returns:
            float: the value of `property_value_11` or None if not set
        """
        return self["Property Value 11"]

    @property_value_11.setter
    def property_value_11(self, value=None):
        """  Corresponds to IDD Field `Property Value 11`

        Args:
            value (float): value for IDD Field `Property Value 11`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 11"] = value

    @property
    def property_value_12(self):
        """Get property_value_12

        Returns:
            float: the value of `property_value_12` or None if not set
        """
        return self["Property Value 12"]

    @property_value_12.setter
    def property_value_12(self, value=None):
        """  Corresponds to IDD Field `Property Value 12`

        Args:
            value (float): value for IDD Field `Property Value 12`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 12"] = value

    @property
    def property_value_13(self):
        """Get property_value_13

        Returns:
            float: the value of `property_value_13` or None if not set
        """
        return self["Property Value 13"]

    @property_value_13.setter
    def property_value_13(self, value=None):
        """  Corresponds to IDD Field `Property Value 13`

        Args:
            value (float): value for IDD Field `Property Value 13`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 13"] = value

    @property
    def property_value_14(self):
        """Get property_value_14

        Returns:
            float: the value of `property_value_14` or None if not set
        """
        return self["Property Value 14"]

    @property_value_14.setter
    def property_value_14(self, value=None):
        """  Corresponds to IDD Field `Property Value 14`

        Args:
            value (float): value for IDD Field `Property Value 14`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 14"] = value

    @property
    def property_value_15(self):
        """Get property_value_15

        Returns:
            float: the value of `property_value_15` or None if not set
        """
        return self["Property Value 15"]

    @property_value_15.setter
    def property_value_15(self, value=None):
        """  Corresponds to IDD Field `Property Value 15`

        Args:
            value (float): value for IDD Field `Property Value 15`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 15"] = value

    @property
    def property_value_16(self):
        """Get property_value_16

        Returns:
            float: the value of `property_value_16` or None if not set
        """
        return self["Property Value 16"]

    @property_value_16.setter
    def property_value_16(self, value=None):
        """  Corresponds to IDD Field `Property Value 16`

        Args:
            value (float): value for IDD Field `Property Value 16`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 16"] = value

    @property
    def property_value_17(self):
        """Get property_value_17

        Returns:
            float: the value of `property_value_17` or None if not set
        """
        return self["Property Value 17"]

    @property_value_17.setter
    def property_value_17(self, value=None):
        """  Corresponds to IDD Field `Property Value 17`

        Args:
            value (float): value for IDD Field `Property Value 17`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 17"] = value

    @property
    def property_value_18(self):
        """Get property_value_18

        Returns:
            float: the value of `property_value_18` or None if not set
        """
        return self["Property Value 18"]

    @property_value_18.setter
    def property_value_18(self, value=None):
        """  Corresponds to IDD Field `Property Value 18`

        Args:
            value (float): value for IDD Field `Property Value 18`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 18"] = value

    @property
    def property_value_19(self):
        """Get property_value_19

        Returns:
            float: the value of `property_value_19` or None if not set
        """
        return self["Property Value 19"]

    @property_value_19.setter
    def property_value_19(self, value=None):
        """  Corresponds to IDD Field `Property Value 19`

        Args:
            value (float): value for IDD Field `Property Value 19`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 19"] = value

    @property
    def property_value_20(self):
        """Get property_value_20

        Returns:
            float: the value of `property_value_20` or None if not set
        """
        return self["Property Value 20"]

    @property_value_20.setter
    def property_value_20(self, value=None):
        """  Corresponds to IDD Field `Property Value 20`

        Args:
            value (float): value for IDD Field `Property Value 20`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 20"] = value

    @property
    def property_value_21(self):
        """Get property_value_21

        Returns:
            float: the value of `property_value_21` or None if not set
        """
        return self["Property Value 21"]

    @property_value_21.setter
    def property_value_21(self, value=None):
        """  Corresponds to IDD Field `Property Value 21`

        Args:
            value (float): value for IDD Field `Property Value 21`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 21"] = value

    @property
    def property_value_22(self):
        """Get property_value_22

        Returns:
            float: the value of `property_value_22` or None if not set
        """
        return self["Property Value 22"]

    @property_value_22.setter
    def property_value_22(self, value=None):
        """  Corresponds to IDD Field `Property Value 22`

        Args:
            value (float): value for IDD Field `Property Value 22`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 22"] = value

    @property
    def property_value_23(self):
        """Get property_value_23

        Returns:
            float: the value of `property_value_23` or None if not set
        """
        return self["Property Value 23"]

    @property_value_23.setter
    def property_value_23(self, value=None):
        """  Corresponds to IDD Field `Property Value 23`

        Args:
            value (float): value for IDD Field `Property Value 23`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 23"] = value

    @property
    def property_value_24(self):
        """Get property_value_24

        Returns:
            float: the value of `property_value_24` or None if not set
        """
        return self["Property Value 24"]

    @property_value_24.setter
    def property_value_24(self, value=None):
        """  Corresponds to IDD Field `Property Value 24`

        Args:
            value (float): value for IDD Field `Property Value 24`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 24"] = value

    @property
    def property_value_25(self):
        """Get property_value_25

        Returns:
            float: the value of `property_value_25` or None if not set
        """
        return self["Property Value 25"]

    @property_value_25.setter
    def property_value_25(self, value=None):
        """  Corresponds to IDD Field `Property Value 25`

        Args:
            value (float): value for IDD Field `Property Value 25`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 25"] = value

    @property
    def property_value_26(self):
        """Get property_value_26

        Returns:
            float: the value of `property_value_26` or None if not set
        """
        return self["Property Value 26"]

    @property_value_26.setter
    def property_value_26(self, value=None):
        """  Corresponds to IDD Field `Property Value 26`

        Args:
            value (float): value for IDD Field `Property Value 26`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 26"] = value

    @property
    def property_value_27(self):
        """Get property_value_27

        Returns:
            float: the value of `property_value_27` or None if not set
        """
        return self["Property Value 27"]

    @property_value_27.setter
    def property_value_27(self, value=None):
        """  Corresponds to IDD Field `Property Value 27`

        Args:
            value (float): value for IDD Field `Property Value 27`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 27"] = value

    @property
    def property_value_28(self):
        """Get property_value_28

        Returns:
            float: the value of `property_value_28` or None if not set
        """
        return self["Property Value 28"]

    @property_value_28.setter
    def property_value_28(self, value=None):
        """  Corresponds to IDD Field `Property Value 28`

        Args:
            value (float): value for IDD Field `Property Value 28`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 28"] = value

    @property
    def property_value_29(self):
        """Get property_value_29

        Returns:
            float: the value of `property_value_29` or None if not set
        """
        return self["Property Value 29"]

    @property_value_29.setter
    def property_value_29(self, value=None):
        """  Corresponds to IDD Field `Property Value 29`

        Args:
            value (float): value for IDD Field `Property Value 29`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 29"] = value

    @property
    def property_value_30(self):
        """Get property_value_30

        Returns:
            float: the value of `property_value_30` or None if not set
        """
        return self["Property Value 30"]

    @property_value_30.setter
    def property_value_30(self, value=None):
        """  Corresponds to IDD Field `Property Value 30`

        Args:
            value (float): value for IDD Field `Property Value 30`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 30"] = value

    @property
    def property_value_31(self):
        """Get property_value_31

        Returns:
            float: the value of `property_value_31` or None if not set
        """
        return self["Property Value 31"]

    @property_value_31.setter
    def property_value_31(self, value=None):
        """  Corresponds to IDD Field `Property Value 31`

        Args:
            value (float): value for IDD Field `Property Value 31`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 31"] = value

    @property
    def property_value_32(self):
        """Get property_value_32

        Returns:
            float: the value of `property_value_32` or None if not set
        """
        return self["Property Value 32"]

    @property_value_32.setter
    def property_value_32(self, value=None):
        """  Corresponds to IDD Field `Property Value 32`

        Args:
            value (float): value for IDD Field `Property Value 32`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 32"] = value

    @property
    def property_value_33(self):
        """Get property_value_33

        Returns:
            float: the value of `property_value_33` or None if not set
        """
        return self["Property Value 33"]

    @property_value_33.setter
    def property_value_33(self, value=None):
        """  Corresponds to IDD Field `Property Value 33`

        Args:
            value (float): value for IDD Field `Property Value 33`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 33"] = value

    @property
    def property_value_34(self):
        """Get property_value_34

        Returns:
            float: the value of `property_value_34` or None if not set
        """
        return self["Property Value 34"]

    @property_value_34.setter
    def property_value_34(self, value=None):
        """  Corresponds to IDD Field `Property Value 34`

        Args:
            value (float): value for IDD Field `Property Value 34`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 34"] = value

    @property
    def property_value_35(self):
        """Get property_value_35

        Returns:
            float: the value of `property_value_35` or None if not set
        """
        return self["Property Value 35"]

    @property_value_35.setter
    def property_value_35(self, value=None):
        """  Corresponds to IDD Field `Property Value 35`

        Args:
            value (float): value for IDD Field `Property Value 35`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 35"] = value

    @property
    def property_value_36(self):
        """Get property_value_36

        Returns:
            float: the value of `property_value_36` or None if not set
        """
        return self["Property Value 36"]

    @property_value_36.setter
    def property_value_36(self, value=None):
        """  Corresponds to IDD Field `Property Value 36`

        Args:
            value (float): value for IDD Field `Property Value 36`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 36"] = value

    @property
    def property_value_37(self):
        """Get property_value_37

        Returns:
            float: the value of `property_value_37` or None if not set
        """
        return self["Property Value 37"]

    @property_value_37.setter
    def property_value_37(self, value=None):
        """  Corresponds to IDD Field `Property Value 37`

        Args:
            value (float): value for IDD Field `Property Value 37`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 37"] = value

    @property
    def property_value_38(self):
        """Get property_value_38

        Returns:
            float: the value of `property_value_38` or None if not set
        """
        return self["Property Value 38"]

    @property_value_38.setter
    def property_value_38(self, value=None):
        """  Corresponds to IDD Field `Property Value 38`

        Args:
            value (float): value for IDD Field `Property Value 38`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 38"] = value

    @property
    def property_value_39(self):
        """Get property_value_39

        Returns:
            float: the value of `property_value_39` or None if not set
        """
        return self["Property Value 39"]

    @property_value_39.setter
    def property_value_39(self, value=None):
        """  Corresponds to IDD Field `Property Value 39`

        Args:
            value (float): value for IDD Field `Property Value 39`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 39"] = value

    @property
    def property_value_40(self):
        """Get property_value_40

        Returns:
            float: the value of `property_value_40` or None if not set
        """
        return self["Property Value 40"]

    @property_value_40.setter
    def property_value_40(self, value=None):
        """  Corresponds to IDD Field `Property Value 40`

        Args:
            value (float): value for IDD Field `Property Value 40`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 40"] = value

    @property
    def property_value_41(self):
        """Get property_value_41

        Returns:
            float: the value of `property_value_41` or None if not set
        """
        return self["Property Value 41"]

    @property_value_41.setter
    def property_value_41(self, value=None):
        """  Corresponds to IDD Field `Property Value 41`

        Args:
            value (float): value for IDD Field `Property Value 41`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 41"] = value

    @property
    def property_value_42(self):
        """Get property_value_42

        Returns:
            float: the value of `property_value_42` or None if not set
        """
        return self["Property Value 42"]

    @property_value_42.setter
    def property_value_42(self, value=None):
        """  Corresponds to IDD Field `Property Value 42`

        Args:
            value (float): value for IDD Field `Property Value 42`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 42"] = value

    @property
    def property_value_43(self):
        """Get property_value_43

        Returns:
            float: the value of `property_value_43` or None if not set
        """
        return self["Property Value 43"]

    @property_value_43.setter
    def property_value_43(self, value=None):
        """  Corresponds to IDD Field `Property Value 43`

        Args:
            value (float): value for IDD Field `Property Value 43`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 43"] = value

    @property
    def property_value_44(self):
        """Get property_value_44

        Returns:
            float: the value of `property_value_44` or None if not set
        """
        return self["Property Value 44"]

    @property_value_44.setter
    def property_value_44(self, value=None):
        """  Corresponds to IDD Field `Property Value 44`

        Args:
            value (float): value for IDD Field `Property Value 44`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 44"] = value

    @property
    def property_value_45(self):
        """Get property_value_45

        Returns:
            float: the value of `property_value_45` or None if not set
        """
        return self["Property Value 45"]

    @property_value_45.setter
    def property_value_45(self, value=None):
        """  Corresponds to IDD Field `Property Value 45`

        Args:
            value (float): value for IDD Field `Property Value 45`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 45"] = value

    @property
    def property_value_46(self):
        """Get property_value_46

        Returns:
            float: the value of `property_value_46` or None if not set
        """
        return self["Property Value 46"]

    @property_value_46.setter
    def property_value_46(self, value=None):
        """  Corresponds to IDD Field `Property Value 46`

        Args:
            value (float): value for IDD Field `Property Value 46`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 46"] = value

    @property
    def property_value_47(self):
        """Get property_value_47

        Returns:
            float: the value of `property_value_47` or None if not set
        """
        return self["Property Value 47"]

    @property_value_47.setter
    def property_value_47(self, value=None):
        """  Corresponds to IDD Field `Property Value 47`

        Args:
            value (float): value for IDD Field `Property Value 47`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 47"] = value

    @property
    def property_value_48(self):
        """Get property_value_48

        Returns:
            float: the value of `property_value_48` or None if not set
        """
        return self["Property Value 48"]

    @property_value_48.setter
    def property_value_48(self, value=None):
        """  Corresponds to IDD Field `Property Value 48`

        Args:
            value (float): value for IDD Field `Property Value 48`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 48"] = value

    @property
    def property_value_49(self):
        """Get property_value_49

        Returns:
            float: the value of `property_value_49` or None if not set
        """
        return self["Property Value 49"]

    @property_value_49.setter
    def property_value_49(self, value=None):
        """  Corresponds to IDD Field `Property Value 49`

        Args:
            value (float): value for IDD Field `Property Value 49`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 49"] = value

    @property
    def property_value_50(self):
        """Get property_value_50

        Returns:
            float: the value of `property_value_50` or None if not set
        """
        return self["Property Value 50"]

    @property_value_50.setter
    def property_value_50(self, value=None):
        """  Corresponds to IDD Field `Property Value 50`

        Args:
            value (float): value for IDD Field `Property Value 50`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 50"] = value

    @property
    def property_value_51(self):
        """Get property_value_51

        Returns:
            float: the value of `property_value_51` or None if not set
        """
        return self["Property Value 51"]

    @property_value_51.setter
    def property_value_51(self, value=None):
        """  Corresponds to IDD Field `Property Value 51`

        Args:
            value (float): value for IDD Field `Property Value 51`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 51"] = value

    @property
    def property_value_52(self):
        """Get property_value_52

        Returns:
            float: the value of `property_value_52` or None if not set
        """
        return self["Property Value 52"]

    @property_value_52.setter
    def property_value_52(self, value=None):
        """  Corresponds to IDD Field `Property Value 52`

        Args:
            value (float): value for IDD Field `Property Value 52`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 52"] = value

    @property
    def property_value_53(self):
        """Get property_value_53

        Returns:
            float: the value of `property_value_53` or None if not set
        """
        return self["Property Value 53"]

    @property_value_53.setter
    def property_value_53(self, value=None):
        """  Corresponds to IDD Field `Property Value 53`

        Args:
            value (float): value for IDD Field `Property Value 53`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 53"] = value

    @property
    def property_value_54(self):
        """Get property_value_54

        Returns:
            float: the value of `property_value_54` or None if not set
        """
        return self["Property Value 54"]

    @property_value_54.setter
    def property_value_54(self, value=None):
        """  Corresponds to IDD Field `Property Value 54`

        Args:
            value (float): value for IDD Field `Property Value 54`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 54"] = value

    @property
    def property_value_55(self):
        """Get property_value_55

        Returns:
            float: the value of `property_value_55` or None if not set
        """
        return self["Property Value 55"]

    @property_value_55.setter
    def property_value_55(self, value=None):
        """  Corresponds to IDD Field `Property Value 55`

        Args:
            value (float): value for IDD Field `Property Value 55`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 55"] = value

    @property
    def property_value_56(self):
        """Get property_value_56

        Returns:
            float: the value of `property_value_56` or None if not set
        """
        return self["Property Value 56"]

    @property_value_56.setter
    def property_value_56(self, value=None):
        """  Corresponds to IDD Field `Property Value 56`

        Args:
            value (float): value for IDD Field `Property Value 56`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 56"] = value

    @property
    def property_value_57(self):
        """Get property_value_57

        Returns:
            float: the value of `property_value_57` or None if not set
        """
        return self["Property Value 57"]

    @property_value_57.setter
    def property_value_57(self, value=None):
        """  Corresponds to IDD Field `Property Value 57`

        Args:
            value (float): value for IDD Field `Property Value 57`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 57"] = value

    @property
    def property_value_58(self):
        """Get property_value_58

        Returns:
            float: the value of `property_value_58` or None if not set
        """
        return self["Property Value 58"]

    @property_value_58.setter
    def property_value_58(self, value=None):
        """  Corresponds to IDD Field `Property Value 58`

        Args:
            value (float): value for IDD Field `Property Value 58`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 58"] = value

    @property
    def property_value_59(self):
        """Get property_value_59

        Returns:
            float: the value of `property_value_59` or None if not set
        """
        return self["Property Value 59"]

    @property_value_59.setter
    def property_value_59(self, value=None):
        """  Corresponds to IDD Field `Property Value 59`

        Args:
            value (float): value for IDD Field `Property Value 59`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 59"] = value

    @property
    def property_value_60(self):
        """Get property_value_60

        Returns:
            float: the value of `property_value_60` or None if not set
        """
        return self["Property Value 60"]

    @property_value_60.setter
    def property_value_60(self, value=None):
        """  Corresponds to IDD Field `Property Value 60`

        Args:
            value (float): value for IDD Field `Property Value 60`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 60"] = value

    @property
    def property_value_61(self):
        """Get property_value_61

        Returns:
            float: the value of `property_value_61` or None if not set
        """
        return self["Property Value 61"]

    @property_value_61.setter
    def property_value_61(self, value=None):
        """  Corresponds to IDD Field `Property Value 61`

        Args:
            value (float): value for IDD Field `Property Value 61`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 61"] = value

    @property
    def property_value_62(self):
        """Get property_value_62

        Returns:
            float: the value of `property_value_62` or None if not set
        """
        return self["Property Value 62"]

    @property_value_62.setter
    def property_value_62(self, value=None):
        """  Corresponds to IDD Field `Property Value 62`

        Args:
            value (float): value for IDD Field `Property Value 62`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 62"] = value

    @property
    def property_value_63(self):
        """Get property_value_63

        Returns:
            float: the value of `property_value_63` or None if not set
        """
        return self["Property Value 63"]

    @property_value_63.setter
    def property_value_63(self, value=None):
        """  Corresponds to IDD Field `Property Value 63`

        Args:
            value (float): value for IDD Field `Property Value 63`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 63"] = value

    @property
    def property_value_64(self):
        """Get property_value_64

        Returns:
            float: the value of `property_value_64` or None if not set
        """
        return self["Property Value 64"]

    @property_value_64.setter
    def property_value_64(self, value=None):
        """  Corresponds to IDD Field `Property Value 64`

        Args:
            value (float): value for IDD Field `Property Value 64`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 64"] = value

    @property
    def property_value_65(self):
        """Get property_value_65

        Returns:
            float: the value of `property_value_65` or None if not set
        """
        return self["Property Value 65"]

    @property_value_65.setter
    def property_value_65(self, value=None):
        """  Corresponds to IDD Field `Property Value 65`

        Args:
            value (float): value for IDD Field `Property Value 65`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 65"] = value

    @property
    def property_value_66(self):
        """Get property_value_66

        Returns:
            float: the value of `property_value_66` or None if not set
        """
        return self["Property Value 66"]

    @property_value_66.setter
    def property_value_66(self, value=None):
        """  Corresponds to IDD Field `Property Value 66`

        Args:
            value (float): value for IDD Field `Property Value 66`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 66"] = value

    @property
    def property_value_67(self):
        """Get property_value_67

        Returns:
            float: the value of `property_value_67` or None if not set
        """
        return self["Property Value 67"]

    @property_value_67.setter
    def property_value_67(self, value=None):
        """  Corresponds to IDD Field `Property Value 67`

        Args:
            value (float): value for IDD Field `Property Value 67`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 67"] = value

    @property
    def property_value_68(self):
        """Get property_value_68

        Returns:
            float: the value of `property_value_68` or None if not set
        """
        return self["Property Value 68"]

    @property_value_68.setter
    def property_value_68(self, value=None):
        """  Corresponds to IDD Field `Property Value 68`

        Args:
            value (float): value for IDD Field `Property Value 68`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 68"] = value

    @property
    def property_value_69(self):
        """Get property_value_69

        Returns:
            float: the value of `property_value_69` or None if not set
        """
        return self["Property Value 69"]

    @property_value_69.setter
    def property_value_69(self, value=None):
        """  Corresponds to IDD Field `Property Value 69`

        Args:
            value (float): value for IDD Field `Property Value 69`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 69"] = value

    @property
    def property_value_70(self):
        """Get property_value_70

        Returns:
            float: the value of `property_value_70` or None if not set
        """
        return self["Property Value 70"]

    @property_value_70.setter
    def property_value_70(self, value=None):
        """  Corresponds to IDD Field `Property Value 70`

        Args:
            value (float): value for IDD Field `Property Value 70`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 70"] = value

    @property
    def property_value_71(self):
        """Get property_value_71

        Returns:
            float: the value of `property_value_71` or None if not set
        """
        return self["Property Value 71"]

    @property_value_71.setter
    def property_value_71(self, value=None):
        """  Corresponds to IDD Field `Property Value 71`

        Args:
            value (float): value for IDD Field `Property Value 71`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 71"] = value

    @property
    def property_value_72(self):
        """Get property_value_72

        Returns:
            float: the value of `property_value_72` or None if not set
        """
        return self["Property Value 72"]

    @property_value_72.setter
    def property_value_72(self, value=None):
        """  Corresponds to IDD Field `Property Value 72`

        Args:
            value (float): value for IDD Field `Property Value 72`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 72"] = value

    @property
    def property_value_73(self):
        """Get property_value_73

        Returns:
            float: the value of `property_value_73` or None if not set
        """
        return self["Property Value 73"]

    @property_value_73.setter
    def property_value_73(self, value=None):
        """  Corresponds to IDD Field `Property Value 73`

        Args:
            value (float): value for IDD Field `Property Value 73`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 73"] = value

    @property
    def property_value_74(self):
        """Get property_value_74

        Returns:
            float: the value of `property_value_74` or None if not set
        """
        return self["Property Value 74"]

    @property_value_74.setter
    def property_value_74(self, value=None):
        """  Corresponds to IDD Field `Property Value 74`

        Args:
            value (float): value for IDD Field `Property Value 74`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 74"] = value

    @property
    def property_value_75(self):
        """Get property_value_75

        Returns:
            float: the value of `property_value_75` or None if not set
        """
        return self["Property Value 75"]

    @property_value_75.setter
    def property_value_75(self, value=None):
        """  Corresponds to IDD Field `Property Value 75`

        Args:
            value (float): value for IDD Field `Property Value 75`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 75"] = value

    @property
    def property_value_76(self):
        """Get property_value_76

        Returns:
            float: the value of `property_value_76` or None if not set
        """
        return self["Property Value 76"]

    @property_value_76.setter
    def property_value_76(self, value=None):
        """  Corresponds to IDD Field `Property Value 76`

        Args:
            value (float): value for IDD Field `Property Value 76`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 76"] = value

    @property
    def property_value_77(self):
        """Get property_value_77

        Returns:
            float: the value of `property_value_77` or None if not set
        """
        return self["Property Value 77"]

    @property_value_77.setter
    def property_value_77(self, value=None):
        """  Corresponds to IDD Field `Property Value 77`

        Args:
            value (float): value for IDD Field `Property Value 77`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 77"] = value

    @property
    def property_value_78(self):
        """Get property_value_78

        Returns:
            float: the value of `property_value_78` or None if not set
        """
        return self["Property Value 78"]

    @property_value_78.setter
    def property_value_78(self, value=None):
        """  Corresponds to IDD Field `Property Value 78`

        Args:
            value (float): value for IDD Field `Property Value 78`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 78"] = value

    @property
    def property_value_79(self):
        """Get property_value_79

        Returns:
            float: the value of `property_value_79` or None if not set
        """
        return self["Property Value 79"]

    @property_value_79.setter
    def property_value_79(self, value=None):
        """  Corresponds to IDD Field `Property Value 79`

        Args:
            value (float): value for IDD Field `Property Value 79`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 79"] = value

    @property
    def property_value_80(self):
        """Get property_value_80

        Returns:
            float: the value of `property_value_80` or None if not set
        """
        return self["Property Value 80"]

    @property_value_80.setter
    def property_value_80(self, value=None):
        """  Corresponds to IDD Field `Property Value 80`

        Args:
            value (float): value for IDD Field `Property Value 80`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 80"] = value

    @property
    def property_value_81(self):
        """Get property_value_81

        Returns:
            float: the value of `property_value_81` or None if not set
        """
        return self["Property Value 81"]

    @property_value_81.setter
    def property_value_81(self, value=None):
        """  Corresponds to IDD Field `Property Value 81`

        Args:
            value (float): value for IDD Field `Property Value 81`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 81"] = value

    @property
    def property_value_82(self):
        """Get property_value_82

        Returns:
            float: the value of `property_value_82` or None if not set
        """
        return self["Property Value 82"]

    @property_value_82.setter
    def property_value_82(self, value=None):
        """  Corresponds to IDD Field `Property Value 82`

        Args:
            value (float): value for IDD Field `Property Value 82`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 82"] = value

    @property
    def property_value_83(self):
        """Get property_value_83

        Returns:
            float: the value of `property_value_83` or None if not set
        """
        return self["Property Value 83"]

    @property_value_83.setter
    def property_value_83(self, value=None):
        """  Corresponds to IDD Field `Property Value 83`

        Args:
            value (float): value for IDD Field `Property Value 83`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 83"] = value

    @property
    def property_value_84(self):
        """Get property_value_84

        Returns:
            float: the value of `property_value_84` or None if not set
        """
        return self["Property Value 84"]

    @property_value_84.setter
    def property_value_84(self, value=None):
        """  Corresponds to IDD Field `Property Value 84`

        Args:
            value (float): value for IDD Field `Property Value 84`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 84"] = value

    @property
    def property_value_85(self):
        """Get property_value_85

        Returns:
            float: the value of `property_value_85` or None if not set
        """
        return self["Property Value 85"]

    @property_value_85.setter
    def property_value_85(self, value=None):
        """  Corresponds to IDD Field `Property Value 85`

        Args:
            value (float): value for IDD Field `Property Value 85`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 85"] = value

    @property
    def property_value_86(self):
        """Get property_value_86

        Returns:
            float: the value of `property_value_86` or None if not set
        """
        return self["Property Value 86"]

    @property_value_86.setter
    def property_value_86(self, value=None):
        """  Corresponds to IDD Field `Property Value 86`

        Args:
            value (float): value for IDD Field `Property Value 86`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 86"] = value

    @property
    def property_value_87(self):
        """Get property_value_87

        Returns:
            float: the value of `property_value_87` or None if not set
        """
        return self["Property Value 87"]

    @property_value_87.setter
    def property_value_87(self, value=None):
        """  Corresponds to IDD Field `Property Value 87`

        Args:
            value (float): value for IDD Field `Property Value 87`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 87"] = value

    @property
    def property_value_88(self):
        """Get property_value_88

        Returns:
            float: the value of `property_value_88` or None if not set
        """
        return self["Property Value 88"]

    @property_value_88.setter
    def property_value_88(self, value=None):
        """  Corresponds to IDD Field `Property Value 88`

        Args:
            value (float): value for IDD Field `Property Value 88`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 88"] = value

    @property
    def property_value_89(self):
        """Get property_value_89

        Returns:
            float: the value of `property_value_89` or None if not set
        """
        return self["Property Value 89"]

    @property_value_89.setter
    def property_value_89(self, value=None):
        """  Corresponds to IDD Field `Property Value 89`

        Args:
            value (float): value for IDD Field `Property Value 89`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 89"] = value

    @property
    def property_value_90(self):
        """Get property_value_90

        Returns:
            float: the value of `property_value_90` or None if not set
        """
        return self["Property Value 90"]

    @property_value_90.setter
    def property_value_90(self, value=None):
        """  Corresponds to IDD Field `Property Value 90`

        Args:
            value (float): value for IDD Field `Property Value 90`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 90"] = value

    @property
    def property_value_91(self):
        """Get property_value_91

        Returns:
            float: the value of `property_value_91` or None if not set
        """
        return self["Property Value 91"]

    @property_value_91.setter
    def property_value_91(self, value=None):
        """  Corresponds to IDD Field `Property Value 91`

        Args:
            value (float): value for IDD Field `Property Value 91`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 91"] = value

    @property
    def property_value_92(self):
        """Get property_value_92

        Returns:
            float: the value of `property_value_92` or None if not set
        """
        return self["Property Value 92"]

    @property_value_92.setter
    def property_value_92(self, value=None):
        """  Corresponds to IDD Field `Property Value 92`

        Args:
            value (float): value for IDD Field `Property Value 92`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 92"] = value

    @property
    def property_value_93(self):
        """Get property_value_93

        Returns:
            float: the value of `property_value_93` or None if not set
        """
        return self["Property Value 93"]

    @property_value_93.setter
    def property_value_93(self, value=None):
        """  Corresponds to IDD Field `Property Value 93`

        Args:
            value (float): value for IDD Field `Property Value 93`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 93"] = value

    @property
    def property_value_94(self):
        """Get property_value_94

        Returns:
            float: the value of `property_value_94` or None if not set
        """
        return self["Property Value 94"]

    @property_value_94.setter
    def property_value_94(self, value=None):
        """  Corresponds to IDD Field `Property Value 94`

        Args:
            value (float): value for IDD Field `Property Value 94`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 94"] = value

    @property
    def property_value_95(self):
        """Get property_value_95

        Returns:
            float: the value of `property_value_95` or None if not set
        """
        return self["Property Value 95"]

    @property_value_95.setter
    def property_value_95(self, value=None):
        """  Corresponds to IDD Field `Property Value 95`

        Args:
            value (float): value for IDD Field `Property Value 95`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 95"] = value

    @property
    def property_value_96(self):
        """Get property_value_96

        Returns:
            float: the value of `property_value_96` or None if not set
        """
        return self["Property Value 96"]

    @property_value_96.setter
    def property_value_96(self, value=None):
        """  Corresponds to IDD Field `Property Value 96`

        Args:
            value (float): value for IDD Field `Property Value 96`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 96"] = value

    @property
    def property_value_97(self):
        """Get property_value_97

        Returns:
            float: the value of `property_value_97` or None if not set
        """
        return self["Property Value 97"]

    @property_value_97.setter
    def property_value_97(self, value=None):
        """  Corresponds to IDD Field `Property Value 97`

        Args:
            value (float): value for IDD Field `Property Value 97`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 97"] = value

    @property
    def property_value_98(self):
        """Get property_value_98

        Returns:
            float: the value of `property_value_98` or None if not set
        """
        return self["Property Value 98"]

    @property_value_98.setter
    def property_value_98(self, value=None):
        """  Corresponds to IDD Field `Property Value 98`

        Args:
            value (float): value for IDD Field `Property Value 98`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 98"] = value

    @property
    def property_value_99(self):
        """Get property_value_99

        Returns:
            float: the value of `property_value_99` or None if not set
        """
        return self["Property Value 99"]

    @property_value_99.setter
    def property_value_99(self, value=None):
        """  Corresponds to IDD Field `Property Value 99`

        Args:
            value (float): value for IDD Field `Property Value 99`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 99"] = value

    @property
    def property_value_100(self):
        """Get property_value_100

        Returns:
            float: the value of `property_value_100` or None if not set
        """
        return self["Property Value 100"]

    @property_value_100.setter
    def property_value_100(self, value=None):
        """  Corresponds to IDD Field `Property Value 100`

        Args:
            value (float): value for IDD Field `Property Value 100`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 100"] = value

    @property
    def property_value_101(self):
        """Get property_value_101

        Returns:
            float: the value of `property_value_101` or None if not set
        """
        return self["Property Value 101"]

    @property_value_101.setter
    def property_value_101(self, value=None):
        """  Corresponds to IDD Field `Property Value 101`

        Args:
            value (float): value for IDD Field `Property Value 101`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 101"] = value

    @property
    def property_value_102(self):
        """Get property_value_102

        Returns:
            float: the value of `property_value_102` or None if not set
        """
        return self["Property Value 102"]

    @property_value_102.setter
    def property_value_102(self, value=None):
        """  Corresponds to IDD Field `Property Value 102`

        Args:
            value (float): value for IDD Field `Property Value 102`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 102"] = value

    @property
    def property_value_103(self):
        """Get property_value_103

        Returns:
            float: the value of `property_value_103` or None if not set
        """
        return self["Property Value 103"]

    @property_value_103.setter
    def property_value_103(self, value=None):
        """  Corresponds to IDD Field `Property Value 103`

        Args:
            value (float): value for IDD Field `Property Value 103`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 103"] = value

    @property
    def property_value_104(self):
        """Get property_value_104

        Returns:
            float: the value of `property_value_104` or None if not set
        """
        return self["Property Value 104"]

    @property_value_104.setter
    def property_value_104(self, value=None):
        """  Corresponds to IDD Field `Property Value 104`

        Args:
            value (float): value for IDD Field `Property Value 104`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 104"] = value

    @property
    def property_value_105(self):
        """Get property_value_105

        Returns:
            float: the value of `property_value_105` or None if not set
        """
        return self["Property Value 105"]

    @property_value_105.setter
    def property_value_105(self, value=None):
        """  Corresponds to IDD Field `Property Value 105`

        Args:
            value (float): value for IDD Field `Property Value 105`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 105"] = value

    @property
    def property_value_106(self):
        """Get property_value_106

        Returns:
            float: the value of `property_value_106` or None if not set
        """
        return self["Property Value 106"]

    @property_value_106.setter
    def property_value_106(self, value=None):
        """  Corresponds to IDD Field `Property Value 106`

        Args:
            value (float): value for IDD Field `Property Value 106`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 106"] = value

    @property
    def property_value_107(self):
        """Get property_value_107

        Returns:
            float: the value of `property_value_107` or None if not set
        """
        return self["Property Value 107"]

    @property_value_107.setter
    def property_value_107(self, value=None):
        """  Corresponds to IDD Field `Property Value 107`

        Args:
            value (float): value for IDD Field `Property Value 107`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 107"] = value

    @property
    def property_value_108(self):
        """Get property_value_108

        Returns:
            float: the value of `property_value_108` or None if not set
        """
        return self["Property Value 108"]

    @property_value_108.setter
    def property_value_108(self, value=None):
        """  Corresponds to IDD Field `Property Value 108`

        Args:
            value (float): value for IDD Field `Property Value 108`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 108"] = value

    @property
    def property_value_109(self):
        """Get property_value_109

        Returns:
            float: the value of `property_value_109` or None if not set
        """
        return self["Property Value 109"]

    @property_value_109.setter
    def property_value_109(self, value=None):
        """  Corresponds to IDD Field `Property Value 109`

        Args:
            value (float): value for IDD Field `Property Value 109`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 109"] = value

    @property
    def property_value_110(self):
        """Get property_value_110

        Returns:
            float: the value of `property_value_110` or None if not set
        """
        return self["Property Value 110"]

    @property_value_110.setter
    def property_value_110(self, value=None):
        """  Corresponds to IDD Field `Property Value 110`

        Args:
            value (float): value for IDD Field `Property Value 110`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 110"] = value

    @property
    def property_value_111(self):
        """Get property_value_111

        Returns:
            float: the value of `property_value_111` or None if not set
        """
        return self["Property Value 111"]

    @property_value_111.setter
    def property_value_111(self, value=None):
        """  Corresponds to IDD Field `Property Value 111`

        Args:
            value (float): value for IDD Field `Property Value 111`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 111"] = value

    @property
    def property_value_112(self):
        """Get property_value_112

        Returns:
            float: the value of `property_value_112` or None if not set
        """
        return self["Property Value 112"]

    @property_value_112.setter
    def property_value_112(self, value=None):
        """  Corresponds to IDD Field `Property Value 112`

        Args:
            value (float): value for IDD Field `Property Value 112`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 112"] = value

    @property
    def property_value_113(self):
        """Get property_value_113

        Returns:
            float: the value of `property_value_113` or None if not set
        """
        return self["Property Value 113"]

    @property_value_113.setter
    def property_value_113(self, value=None):
        """  Corresponds to IDD Field `Property Value 113`

        Args:
            value (float): value for IDD Field `Property Value 113`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 113"] = value

    @property
    def property_value_114(self):
        """Get property_value_114

        Returns:
            float: the value of `property_value_114` or None if not set
        """
        return self["Property Value 114"]

    @property_value_114.setter
    def property_value_114(self, value=None):
        """  Corresponds to IDD Field `Property Value 114`

        Args:
            value (float): value for IDD Field `Property Value 114`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 114"] = value

    @property
    def property_value_115(self):
        """Get property_value_115

        Returns:
            float: the value of `property_value_115` or None if not set
        """
        return self["Property Value 115"]

    @property_value_115.setter
    def property_value_115(self, value=None):
        """  Corresponds to IDD Field `Property Value 115`

        Args:
            value (float): value for IDD Field `Property Value 115`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 115"] = value

    @property
    def property_value_116(self):
        """Get property_value_116

        Returns:
            float: the value of `property_value_116` or None if not set
        """
        return self["Property Value 116"]

    @property_value_116.setter
    def property_value_116(self, value=None):
        """  Corresponds to IDD Field `Property Value 116`

        Args:
            value (float): value for IDD Field `Property Value 116`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 116"] = value

    @property
    def property_value_117(self):
        """Get property_value_117

        Returns:
            float: the value of `property_value_117` or None if not set
        """
        return self["Property Value 117"]

    @property_value_117.setter
    def property_value_117(self, value=None):
        """  Corresponds to IDD Field `Property Value 117`

        Args:
            value (float): value for IDD Field `Property Value 117`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 117"] = value

    @property
    def property_value_118(self):
        """Get property_value_118

        Returns:
            float: the value of `property_value_118` or None if not set
        """
        return self["Property Value 118"]

    @property_value_118.setter
    def property_value_118(self, value=None):
        """  Corresponds to IDD Field `Property Value 118`

        Args:
            value (float): value for IDD Field `Property Value 118`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 118"] = value

    @property
    def property_value_119(self):
        """Get property_value_119

        Returns:
            float: the value of `property_value_119` or None if not set
        """
        return self["Property Value 119"]

    @property_value_119.setter
    def property_value_119(self, value=None):
        """  Corresponds to IDD Field `Property Value 119`

        Args:
            value (float): value for IDD Field `Property Value 119`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 119"] = value

    @property
    def property_value_120(self):
        """Get property_value_120

        Returns:
            float: the value of `property_value_120` or None if not set
        """
        return self["Property Value 120"]

    @property_value_120.setter
    def property_value_120(self, value=None):
        """  Corresponds to IDD Field `Property Value 120`

        Args:
            value (float): value for IDD Field `Property Value 120`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 120"] = value

    @property
    def property_value_121(self):
        """Get property_value_121

        Returns:
            float: the value of `property_value_121` or None if not set
        """
        return self["Property Value 121"]

    @property_value_121.setter
    def property_value_121(self, value=None):
        """  Corresponds to IDD Field `Property Value 121`

        Args:
            value (float): value for IDD Field `Property Value 121`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 121"] = value

    @property
    def property_value_122(self):
        """Get property_value_122

        Returns:
            float: the value of `property_value_122` or None if not set
        """
        return self["Property Value 122"]

    @property_value_122.setter
    def property_value_122(self, value=None):
        """  Corresponds to IDD Field `Property Value 122`

        Args:
            value (float): value for IDD Field `Property Value 122`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 122"] = value

    @property
    def property_value_123(self):
        """Get property_value_123

        Returns:
            float: the value of `property_value_123` or None if not set
        """
        return self["Property Value 123"]

    @property_value_123.setter
    def property_value_123(self, value=None):
        """  Corresponds to IDD Field `Property Value 123`

        Args:
            value (float): value for IDD Field `Property Value 123`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 123"] = value

    @property
    def property_value_124(self):
        """Get property_value_124

        Returns:
            float: the value of `property_value_124` or None if not set
        """
        return self["Property Value 124"]

    @property_value_124.setter
    def property_value_124(self, value=None):
        """  Corresponds to IDD Field `Property Value 124`

        Args:
            value (float): value for IDD Field `Property Value 124`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 124"] = value

    @property
    def property_value_125(self):
        """Get property_value_125

        Returns:
            float: the value of `property_value_125` or None if not set
        """
        return self["Property Value 125"]

    @property_value_125.setter
    def property_value_125(self, value=None):
        """  Corresponds to IDD Field `Property Value 125`

        Args:
            value (float): value for IDD Field `Property Value 125`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 125"] = value

    @property
    def property_value_126(self):
        """Get property_value_126

        Returns:
            float: the value of `property_value_126` or None if not set
        """
        return self["Property Value 126"]

    @property_value_126.setter
    def property_value_126(self, value=None):
        """  Corresponds to IDD Field `Property Value 126`

        Args:
            value (float): value for IDD Field `Property Value 126`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 126"] = value

    @property
    def property_value_127(self):
        """Get property_value_127

        Returns:
            float: the value of `property_value_127` or None if not set
        """
        return self["Property Value 127"]

    @property_value_127.setter
    def property_value_127(self, value=None):
        """  Corresponds to IDD Field `Property Value 127`

        Args:
            value (float): value for IDD Field `Property Value 127`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 127"] = value

    @property
    def property_value_128(self):
        """Get property_value_128

        Returns:
            float: the value of `property_value_128` or None if not set
        """
        return self["Property Value 128"]

    @property_value_128.setter
    def property_value_128(self, value=None):
        """  Corresponds to IDD Field `Property Value 128`

        Args:
            value (float): value for IDD Field `Property Value 128`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 128"] = value

    @property
    def property_value_129(self):
        """Get property_value_129

        Returns:
            float: the value of `property_value_129` or None if not set
        """
        return self["Property Value 129"]

    @property_value_129.setter
    def property_value_129(self, value=None):
        """  Corresponds to IDD Field `Property Value 129`

        Args:
            value (float): value for IDD Field `Property Value 129`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 129"] = value

    @property
    def property_value_130(self):
        """Get property_value_130

        Returns:
            float: the value of `property_value_130` or None if not set
        """
        return self["Property Value 130"]

    @property_value_130.setter
    def property_value_130(self, value=None):
        """  Corresponds to IDD Field `Property Value 130`

        Args:
            value (float): value for IDD Field `Property Value 130`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 130"] = value

    @property
    def property_value_131(self):
        """Get property_value_131

        Returns:
            float: the value of `property_value_131` or None if not set
        """
        return self["Property Value 131"]

    @property_value_131.setter
    def property_value_131(self, value=None):
        """  Corresponds to IDD Field `Property Value 131`

        Args:
            value (float): value for IDD Field `Property Value 131`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 131"] = value

    @property
    def property_value_132(self):
        """Get property_value_132

        Returns:
            float: the value of `property_value_132` or None if not set
        """
        return self["Property Value 132"]

    @property_value_132.setter
    def property_value_132(self, value=None):
        """  Corresponds to IDD Field `Property Value 132`

        Args:
            value (float): value for IDD Field `Property Value 132`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 132"] = value

    @property
    def property_value_133(self):
        """Get property_value_133

        Returns:
            float: the value of `property_value_133` or None if not set
        """
        return self["Property Value 133"]

    @property_value_133.setter
    def property_value_133(self, value=None):
        """  Corresponds to IDD Field `Property Value 133`

        Args:
            value (float): value for IDD Field `Property Value 133`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 133"] = value

    @property
    def property_value_134(self):
        """Get property_value_134

        Returns:
            float: the value of `property_value_134` or None if not set
        """
        return self["Property Value 134"]

    @property_value_134.setter
    def property_value_134(self, value=None):
        """  Corresponds to IDD Field `Property Value 134`

        Args:
            value (float): value for IDD Field `Property Value 134`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 134"] = value

    @property
    def property_value_135(self):
        """Get property_value_135

        Returns:
            float: the value of `property_value_135` or None if not set
        """
        return self["Property Value 135"]

    @property_value_135.setter
    def property_value_135(self, value=None):
        """  Corresponds to IDD Field `Property Value 135`

        Args:
            value (float): value for IDD Field `Property Value 135`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 135"] = value

    @property
    def property_value_136(self):
        """Get property_value_136

        Returns:
            float: the value of `property_value_136` or None if not set
        """
        return self["Property Value 136"]

    @property_value_136.setter
    def property_value_136(self, value=None):
        """  Corresponds to IDD Field `Property Value 136`

        Args:
            value (float): value for IDD Field `Property Value 136`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 136"] = value

    @property
    def property_value_137(self):
        """Get property_value_137

        Returns:
            float: the value of `property_value_137` or None if not set
        """
        return self["Property Value 137"]

    @property_value_137.setter
    def property_value_137(self, value=None):
        """  Corresponds to IDD Field `Property Value 137`

        Args:
            value (float): value for IDD Field `Property Value 137`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 137"] = value

    @property
    def property_value_138(self):
        """Get property_value_138

        Returns:
            float: the value of `property_value_138` or None if not set
        """
        return self["Property Value 138"]

    @property_value_138.setter
    def property_value_138(self, value=None):
        """  Corresponds to IDD Field `Property Value 138`

        Args:
            value (float): value for IDD Field `Property Value 138`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 138"] = value

    @property
    def property_value_139(self):
        """Get property_value_139

        Returns:
            float: the value of `property_value_139` or None if not set
        """
        return self["Property Value 139"]

    @property_value_139.setter
    def property_value_139(self, value=None):
        """  Corresponds to IDD Field `Property Value 139`

        Args:
            value (float): value for IDD Field `Property Value 139`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 139"] = value

    @property
    def property_value_140(self):
        """Get property_value_140

        Returns:
            float: the value of `property_value_140` or None if not set
        """
        return self["Property Value 140"]

    @property_value_140.setter
    def property_value_140(self, value=None):
        """  Corresponds to IDD Field `Property Value 140`

        Args:
            value (float): value for IDD Field `Property Value 140`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 140"] = value

    @property
    def property_value_141(self):
        """Get property_value_141

        Returns:
            float: the value of `property_value_141` or None if not set
        """
        return self["Property Value 141"]

    @property_value_141.setter
    def property_value_141(self, value=None):
        """  Corresponds to IDD Field `Property Value 141`

        Args:
            value (float): value for IDD Field `Property Value 141`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 141"] = value

    @property
    def property_value_142(self):
        """Get property_value_142

        Returns:
            float: the value of `property_value_142` or None if not set
        """
        return self["Property Value 142"]

    @property_value_142.setter
    def property_value_142(self, value=None):
        """  Corresponds to IDD Field `Property Value 142`

        Args:
            value (float): value for IDD Field `Property Value 142`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 142"] = value

    @property
    def property_value_143(self):
        """Get property_value_143

        Returns:
            float: the value of `property_value_143` or None if not set
        """
        return self["Property Value 143"]

    @property_value_143.setter
    def property_value_143(self, value=None):
        """  Corresponds to IDD Field `Property Value 143`

        Args:
            value (float): value for IDD Field `Property Value 143`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 143"] = value

    @property
    def property_value_144(self):
        """Get property_value_144

        Returns:
            float: the value of `property_value_144` or None if not set
        """
        return self["Property Value 144"]

    @property_value_144.setter
    def property_value_144(self, value=None):
        """  Corresponds to IDD Field `Property Value 144`

        Args:
            value (float): value for IDD Field `Property Value 144`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 144"] = value

    @property
    def property_value_145(self):
        """Get property_value_145

        Returns:
            float: the value of `property_value_145` or None if not set
        """
        return self["Property Value 145"]

    @property_value_145.setter
    def property_value_145(self, value=None):
        """  Corresponds to IDD Field `Property Value 145`

        Args:
            value (float): value for IDD Field `Property Value 145`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 145"] = value

    @property
    def property_value_146(self):
        """Get property_value_146

        Returns:
            float: the value of `property_value_146` or None if not set
        """
        return self["Property Value 146"]

    @property_value_146.setter
    def property_value_146(self, value=None):
        """  Corresponds to IDD Field `Property Value 146`

        Args:
            value (float): value for IDD Field `Property Value 146`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 146"] = value

    @property
    def property_value_147(self):
        """Get property_value_147

        Returns:
            float: the value of `property_value_147` or None if not set
        """
        return self["Property Value 147"]

    @property_value_147.setter
    def property_value_147(self, value=None):
        """  Corresponds to IDD Field `Property Value 147`

        Args:
            value (float): value for IDD Field `Property Value 147`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 147"] = value

    @property
    def property_value_148(self):
        """Get property_value_148

        Returns:
            float: the value of `property_value_148` or None if not set
        """
        return self["Property Value 148"]

    @property_value_148.setter
    def property_value_148(self, value=None):
        """  Corresponds to IDD Field `Property Value 148`

        Args:
            value (float): value for IDD Field `Property Value 148`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 148"] = value

    @property
    def property_value_149(self):
        """Get property_value_149

        Returns:
            float: the value of `property_value_149` or None if not set
        """
        return self["Property Value 149"]

    @property_value_149.setter
    def property_value_149(self, value=None):
        """  Corresponds to IDD Field `Property Value 149`

        Args:
            value (float): value for IDD Field `Property Value 149`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 149"] = value

    @property
    def property_value_150(self):
        """Get property_value_150

        Returns:
            float: the value of `property_value_150` or None if not set
        """
        return self["Property Value 150"]

    @property_value_150.setter
    def property_value_150(self, value=None):
        """  Corresponds to IDD Field `Property Value 150`

        Args:
            value (float): value for IDD Field `Property Value 150`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 150"] = value

    @property
    def property_value_151(self):
        """Get property_value_151

        Returns:
            float: the value of `property_value_151` or None if not set
        """
        return self["Property Value 151"]

    @property_value_151.setter
    def property_value_151(self, value=None):
        """  Corresponds to IDD Field `Property Value 151`

        Args:
            value (float): value for IDD Field `Property Value 151`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 151"] = value

    @property
    def property_value_152(self):
        """Get property_value_152

        Returns:
            float: the value of `property_value_152` or None if not set
        """
        return self["Property Value 152"]

    @property_value_152.setter
    def property_value_152(self, value=None):
        """  Corresponds to IDD Field `Property Value 152`

        Args:
            value (float): value for IDD Field `Property Value 152`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 152"] = value

    @property
    def property_value_153(self):
        """Get property_value_153

        Returns:
            float: the value of `property_value_153` or None if not set
        """
        return self["Property Value 153"]

    @property_value_153.setter
    def property_value_153(self, value=None):
        """  Corresponds to IDD Field `Property Value 153`

        Args:
            value (float): value for IDD Field `Property Value 153`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 153"] = value

    @property
    def property_value_154(self):
        """Get property_value_154

        Returns:
            float: the value of `property_value_154` or None if not set
        """
        return self["Property Value 154"]

    @property_value_154.setter
    def property_value_154(self, value=None):
        """  Corresponds to IDD Field `Property Value 154`

        Args:
            value (float): value for IDD Field `Property Value 154`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 154"] = value

    @property
    def property_value_155(self):
        """Get property_value_155

        Returns:
            float: the value of `property_value_155` or None if not set
        """
        return self["Property Value 155"]

    @property_value_155.setter
    def property_value_155(self, value=None):
        """  Corresponds to IDD Field `Property Value 155`

        Args:
            value (float): value for IDD Field `Property Value 155`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 155"] = value

    @property
    def property_value_156(self):
        """Get property_value_156

        Returns:
            float: the value of `property_value_156` or None if not set
        """
        return self["Property Value 156"]

    @property_value_156.setter
    def property_value_156(self, value=None):
        """  Corresponds to IDD Field `Property Value 156`

        Args:
            value (float): value for IDD Field `Property Value 156`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 156"] = value

    @property
    def property_value_157(self):
        """Get property_value_157

        Returns:
            float: the value of `property_value_157` or None if not set
        """
        return self["Property Value 157"]

    @property_value_157.setter
    def property_value_157(self, value=None):
        """  Corresponds to IDD Field `Property Value 157`

        Args:
            value (float): value for IDD Field `Property Value 157`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 157"] = value

    @property
    def property_value_158(self):
        """Get property_value_158

        Returns:
            float: the value of `property_value_158` or None if not set
        """
        return self["Property Value 158"]

    @property_value_158.setter
    def property_value_158(self, value=None):
        """  Corresponds to IDD Field `Property Value 158`

        Args:
            value (float): value for IDD Field `Property Value 158`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 158"] = value

    @property
    def property_value_159(self):
        """Get property_value_159

        Returns:
            float: the value of `property_value_159` or None if not set
        """
        return self["Property Value 159"]

    @property_value_159.setter
    def property_value_159(self, value=None):
        """  Corresponds to IDD Field `Property Value 159`

        Args:
            value (float): value for IDD Field `Property Value 159`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 159"] = value

    @property
    def property_value_160(self):
        """Get property_value_160

        Returns:
            float: the value of `property_value_160` or None if not set
        """
        return self["Property Value 160"]

    @property_value_160.setter
    def property_value_160(self, value=None):
        """  Corresponds to IDD Field `Property Value 160`

        Args:
            value (float): value for IDD Field `Property Value 160`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 160"] = value

    @property
    def property_value_161(self):
        """Get property_value_161

        Returns:
            float: the value of `property_value_161` or None if not set
        """
        return self["Property Value 161"]

    @property_value_161.setter
    def property_value_161(self, value=None):
        """  Corresponds to IDD Field `Property Value 161`

        Args:
            value (float): value for IDD Field `Property Value 161`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 161"] = value

    @property
    def property_value_162(self):
        """Get property_value_162

        Returns:
            float: the value of `property_value_162` or None if not set
        """
        return self["Property Value 162"]

    @property_value_162.setter
    def property_value_162(self, value=None):
        """  Corresponds to IDD Field `Property Value 162`

        Args:
            value (float): value for IDD Field `Property Value 162`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 162"] = value

    @property
    def property_value_163(self):
        """Get property_value_163

        Returns:
            float: the value of `property_value_163` or None if not set
        """
        return self["Property Value 163"]

    @property_value_163.setter
    def property_value_163(self, value=None):
        """  Corresponds to IDD Field `Property Value 163`

        Args:
            value (float): value for IDD Field `Property Value 163`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 163"] = value

    @property
    def property_value_164(self):
        """Get property_value_164

        Returns:
            float: the value of `property_value_164` or None if not set
        """
        return self["Property Value 164"]

    @property_value_164.setter
    def property_value_164(self, value=None):
        """  Corresponds to IDD Field `Property Value 164`

        Args:
            value (float): value for IDD Field `Property Value 164`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 164"] = value

    @property
    def property_value_165(self):
        """Get property_value_165

        Returns:
            float: the value of `property_value_165` or None if not set
        """
        return self["Property Value 165"]

    @property_value_165.setter
    def property_value_165(self, value=None):
        """  Corresponds to IDD Field `Property Value 165`

        Args:
            value (float): value for IDD Field `Property Value 165`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 165"] = value

    @property
    def property_value_166(self):
        """Get property_value_166

        Returns:
            float: the value of `property_value_166` or None if not set
        """
        return self["Property Value 166"]

    @property_value_166.setter
    def property_value_166(self, value=None):
        """  Corresponds to IDD Field `Property Value 166`

        Args:
            value (float): value for IDD Field `Property Value 166`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 166"] = value

    @property
    def property_value_167(self):
        """Get property_value_167

        Returns:
            float: the value of `property_value_167` or None if not set
        """
        return self["Property Value 167"]

    @property_value_167.setter
    def property_value_167(self, value=None):
        """  Corresponds to IDD Field `Property Value 167`

        Args:
            value (float): value for IDD Field `Property Value 167`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 167"] = value

    @property
    def property_value_168(self):
        """Get property_value_168

        Returns:
            float: the value of `property_value_168` or None if not set
        """
        return self["Property Value 168"]

    @property_value_168.setter
    def property_value_168(self, value=None):
        """  Corresponds to IDD Field `Property Value 168`

        Args:
            value (float): value for IDD Field `Property Value 168`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 168"] = value

    @property
    def property_value_169(self):
        """Get property_value_169

        Returns:
            float: the value of `property_value_169` or None if not set
        """
        return self["Property Value 169"]

    @property_value_169.setter
    def property_value_169(self, value=None):
        """  Corresponds to IDD Field `Property Value 169`

        Args:
            value (float): value for IDD Field `Property Value 169`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 169"] = value

    @property
    def property_value_170(self):
        """Get property_value_170

        Returns:
            float: the value of `property_value_170` or None if not set
        """
        return self["Property Value 170"]

    @property_value_170.setter
    def property_value_170(self, value=None):
        """  Corresponds to IDD Field `Property Value 170`

        Args:
            value (float): value for IDD Field `Property Value 170`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 170"] = value

    @property
    def property_value_171(self):
        """Get property_value_171

        Returns:
            float: the value of `property_value_171` or None if not set
        """
        return self["Property Value 171"]

    @property_value_171.setter
    def property_value_171(self, value=None):
        """  Corresponds to IDD Field `Property Value 171`

        Args:
            value (float): value for IDD Field `Property Value 171`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 171"] = value

    @property
    def property_value_172(self):
        """Get property_value_172

        Returns:
            float: the value of `property_value_172` or None if not set
        """
        return self["Property Value 172"]

    @property_value_172.setter
    def property_value_172(self, value=None):
        """  Corresponds to IDD Field `Property Value 172`

        Args:
            value (float): value for IDD Field `Property Value 172`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 172"] = value

    @property
    def property_value_173(self):
        """Get property_value_173

        Returns:
            float: the value of `property_value_173` or None if not set
        """
        return self["Property Value 173"]

    @property_value_173.setter
    def property_value_173(self, value=None):
        """  Corresponds to IDD Field `Property Value 173`

        Args:
            value (float): value for IDD Field `Property Value 173`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 173"] = value

    @property
    def property_value_174(self):
        """Get property_value_174

        Returns:
            float: the value of `property_value_174` or None if not set
        """
        return self["Property Value 174"]

    @property_value_174.setter
    def property_value_174(self, value=None):
        """  Corresponds to IDD Field `Property Value 174`

        Args:
            value (float): value for IDD Field `Property Value 174`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 174"] = value

    @property
    def property_value_175(self):
        """Get property_value_175

        Returns:
            float: the value of `property_value_175` or None if not set
        """
        return self["Property Value 175"]

    @property_value_175.setter
    def property_value_175(self, value=None):
        """  Corresponds to IDD Field `Property Value 175`

        Args:
            value (float): value for IDD Field `Property Value 175`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 175"] = value

    @property
    def property_value_176(self):
        """Get property_value_176

        Returns:
            float: the value of `property_value_176` or None if not set
        """
        return self["Property Value 176"]

    @property_value_176.setter
    def property_value_176(self, value=None):
        """  Corresponds to IDD Field `Property Value 176`

        Args:
            value (float): value for IDD Field `Property Value 176`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 176"] = value

    @property
    def property_value_177(self):
        """Get property_value_177

        Returns:
            float: the value of `property_value_177` or None if not set
        """
        return self["Property Value 177"]

    @property_value_177.setter
    def property_value_177(self, value=None):
        """  Corresponds to IDD Field `Property Value 177`

        Args:
            value (float): value for IDD Field `Property Value 177`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 177"] = value

    @property
    def property_value_178(self):
        """Get property_value_178

        Returns:
            float: the value of `property_value_178` or None if not set
        """
        return self["Property Value 178"]

    @property_value_178.setter
    def property_value_178(self, value=None):
        """  Corresponds to IDD Field `Property Value 178`

        Args:
            value (float): value for IDD Field `Property Value 178`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 178"] = value

    @property
    def property_value_179(self):
        """Get property_value_179

        Returns:
            float: the value of `property_value_179` or None if not set
        """
        return self["Property Value 179"]

    @property_value_179.setter
    def property_value_179(self, value=None):
        """  Corresponds to IDD Field `Property Value 179`

        Args:
            value (float): value for IDD Field `Property Value 179`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 179"] = value

    @property
    def property_value_180(self):
        """Get property_value_180

        Returns:
            float: the value of `property_value_180` or None if not set
        """
        return self["Property Value 180"]

    @property_value_180.setter
    def property_value_180(self, value=None):
        """  Corresponds to IDD Field `Property Value 180`

        Args:
            value (float): value for IDD Field `Property Value 180`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 180"] = value

    @property
    def property_value_181(self):
        """Get property_value_181

        Returns:
            float: the value of `property_value_181` or None if not set
        """
        return self["Property Value 181"]

    @property_value_181.setter
    def property_value_181(self, value=None):
        """  Corresponds to IDD Field `Property Value 181`

        Args:
            value (float): value for IDD Field `Property Value 181`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 181"] = value

    @property
    def property_value_182(self):
        """Get property_value_182

        Returns:
            float: the value of `property_value_182` or None if not set
        """
        return self["Property Value 182"]

    @property_value_182.setter
    def property_value_182(self, value=None):
        """  Corresponds to IDD Field `Property Value 182`

        Args:
            value (float): value for IDD Field `Property Value 182`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 182"] = value

    @property
    def property_value_183(self):
        """Get property_value_183

        Returns:
            float: the value of `property_value_183` or None if not set
        """
        return self["Property Value 183"]

    @property_value_183.setter
    def property_value_183(self, value=None):
        """  Corresponds to IDD Field `Property Value 183`

        Args:
            value (float): value for IDD Field `Property Value 183`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 183"] = value

    @property
    def property_value_184(self):
        """Get property_value_184

        Returns:
            float: the value of `property_value_184` or None if not set
        """
        return self["Property Value 184"]

    @property_value_184.setter
    def property_value_184(self, value=None):
        """  Corresponds to IDD Field `Property Value 184`

        Args:
            value (float): value for IDD Field `Property Value 184`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 184"] = value

    @property
    def property_value_185(self):
        """Get property_value_185

        Returns:
            float: the value of `property_value_185` or None if not set
        """
        return self["Property Value 185"]

    @property_value_185.setter
    def property_value_185(self, value=None):
        """  Corresponds to IDD Field `Property Value 185`

        Args:
            value (float): value for IDD Field `Property Value 185`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 185"] = value

    @property
    def property_value_186(self):
        """Get property_value_186

        Returns:
            float: the value of `property_value_186` or None if not set
        """
        return self["Property Value 186"]

    @property_value_186.setter
    def property_value_186(self, value=None):
        """  Corresponds to IDD Field `Property Value 186`

        Args:
            value (float): value for IDD Field `Property Value 186`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 186"] = value

    @property
    def property_value_187(self):
        """Get property_value_187

        Returns:
            float: the value of `property_value_187` or None if not set
        """
        return self["Property Value 187"]

    @property_value_187.setter
    def property_value_187(self, value=None):
        """  Corresponds to IDD Field `Property Value 187`

        Args:
            value (float): value for IDD Field `Property Value 187`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 187"] = value

    @property
    def property_value_188(self):
        """Get property_value_188

        Returns:
            float: the value of `property_value_188` or None if not set
        """
        return self["Property Value 188"]

    @property_value_188.setter
    def property_value_188(self, value=None):
        """  Corresponds to IDD Field `Property Value 188`

        Args:
            value (float): value for IDD Field `Property Value 188`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 188"] = value

    @property
    def property_value_189(self):
        """Get property_value_189

        Returns:
            float: the value of `property_value_189` or None if not set
        """
        return self["Property Value 189"]

    @property_value_189.setter
    def property_value_189(self, value=None):
        """  Corresponds to IDD Field `Property Value 189`

        Args:
            value (float): value for IDD Field `Property Value 189`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 189"] = value

    @property
    def property_value_190(self):
        """Get property_value_190

        Returns:
            float: the value of `property_value_190` or None if not set
        """
        return self["Property Value 190"]

    @property_value_190.setter
    def property_value_190(self, value=None):
        """  Corresponds to IDD Field `Property Value 190`

        Args:
            value (float): value for IDD Field `Property Value 190`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 190"] = value

    @property
    def property_value_191(self):
        """Get property_value_191

        Returns:
            float: the value of `property_value_191` or None if not set
        """
        return self["Property Value 191"]

    @property_value_191.setter
    def property_value_191(self, value=None):
        """  Corresponds to IDD Field `Property Value 191`

        Args:
            value (float): value for IDD Field `Property Value 191`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 191"] = value

    @property
    def property_value_192(self):
        """Get property_value_192

        Returns:
            float: the value of `property_value_192` or None if not set
        """
        return self["Property Value 192"]

    @property_value_192.setter
    def property_value_192(self, value=None):
        """  Corresponds to IDD Field `Property Value 192`

        Args:
            value (float): value for IDD Field `Property Value 192`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 192"] = value

    @property
    def property_value_193(self):
        """Get property_value_193

        Returns:
            float: the value of `property_value_193` or None if not set
        """
        return self["Property Value 193"]

    @property_value_193.setter
    def property_value_193(self, value=None):
        """  Corresponds to IDD Field `Property Value 193`

        Args:
            value (float): value for IDD Field `Property Value 193`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 193"] = value

    @property
    def property_value_194(self):
        """Get property_value_194

        Returns:
            float: the value of `property_value_194` or None if not set
        """
        return self["Property Value 194"]

    @property_value_194.setter
    def property_value_194(self, value=None):
        """  Corresponds to IDD Field `Property Value 194`

        Args:
            value (float): value for IDD Field `Property Value 194`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 194"] = value

    @property
    def property_value_195(self):
        """Get property_value_195

        Returns:
            float: the value of `property_value_195` or None if not set
        """
        return self["Property Value 195"]

    @property_value_195.setter
    def property_value_195(self, value=None):
        """  Corresponds to IDD Field `Property Value 195`

        Args:
            value (float): value for IDD Field `Property Value 195`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 195"] = value

    @property
    def property_value_196(self):
        """Get property_value_196

        Returns:
            float: the value of `property_value_196` or None if not set
        """
        return self["Property Value 196"]

    @property_value_196.setter
    def property_value_196(self, value=None):
        """  Corresponds to IDD Field `Property Value 196`

        Args:
            value (float): value for IDD Field `Property Value 196`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 196"] = value

    @property
    def property_value_197(self):
        """Get property_value_197

        Returns:
            float: the value of `property_value_197` or None if not set
        """
        return self["Property Value 197"]

    @property_value_197.setter
    def property_value_197(self, value=None):
        """  Corresponds to IDD Field `Property Value 197`

        Args:
            value (float): value for IDD Field `Property Value 197`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 197"] = value

    @property
    def property_value_198(self):
        """Get property_value_198

        Returns:
            float: the value of `property_value_198` or None if not set
        """
        return self["Property Value 198"]

    @property_value_198.setter
    def property_value_198(self, value=None):
        """  Corresponds to IDD Field `Property Value 198`

        Args:
            value (float): value for IDD Field `Property Value 198`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 198"] = value

    @property
    def property_value_199(self):
        """Get property_value_199

        Returns:
            float: the value of `property_value_199` or None if not set
        """
        return self["Property Value 199"]

    @property_value_199.setter
    def property_value_199(self, value=None):
        """  Corresponds to IDD Field `Property Value 199`

        Args:
            value (float): value for IDD Field `Property Value 199`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 199"] = value

    @property
    def property_value_200(self):
        """Get property_value_200

        Returns:
            float: the value of `property_value_200` or None if not set
        """
        return self["Property Value 200"]

    @property_value_200.setter
    def property_value_200(self, value=None):
        """  Corresponds to IDD Field `Property Value 200`

        Args:
            value (float): value for IDD Field `Property Value 200`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 200"] = value

    @property
    def property_value_201(self):
        """Get property_value_201

        Returns:
            float: the value of `property_value_201` or None if not set
        """
        return self["Property Value 201"]

    @property_value_201.setter
    def property_value_201(self, value=None):
        """  Corresponds to IDD Field `Property Value 201`

        Args:
            value (float): value for IDD Field `Property Value 201`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 201"] = value

    @property
    def property_value_202(self):
        """Get property_value_202

        Returns:
            float: the value of `property_value_202` or None if not set
        """
        return self["Property Value 202"]

    @property_value_202.setter
    def property_value_202(self, value=None):
        """  Corresponds to IDD Field `Property Value 202`

        Args:
            value (float): value for IDD Field `Property Value 202`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 202"] = value

    @property
    def property_value_203(self):
        """Get property_value_203

        Returns:
            float: the value of `property_value_203` or None if not set
        """
        return self["Property Value 203"]

    @property_value_203.setter
    def property_value_203(self, value=None):
        """  Corresponds to IDD Field `Property Value 203`

        Args:
            value (float): value for IDD Field `Property Value 203`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 203"] = value

    @property
    def property_value_204(self):
        """Get property_value_204

        Returns:
            float: the value of `property_value_204` or None if not set
        """
        return self["Property Value 204"]

    @property_value_204.setter
    def property_value_204(self, value=None):
        """  Corresponds to IDD Field `Property Value 204`

        Args:
            value (float): value for IDD Field `Property Value 204`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 204"] = value

    @property
    def property_value_205(self):
        """Get property_value_205

        Returns:
            float: the value of `property_value_205` or None if not set
        """
        return self["Property Value 205"]

    @property_value_205.setter
    def property_value_205(self, value=None):
        """  Corresponds to IDD Field `Property Value 205`

        Args:
            value (float): value for IDD Field `Property Value 205`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 205"] = value

    @property
    def property_value_206(self):
        """Get property_value_206

        Returns:
            float: the value of `property_value_206` or None if not set
        """
        return self["Property Value 206"]

    @property_value_206.setter
    def property_value_206(self, value=None):
        """  Corresponds to IDD Field `Property Value 206`

        Args:
            value (float): value for IDD Field `Property Value 206`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 206"] = value

    @property
    def property_value_207(self):
        """Get property_value_207

        Returns:
            float: the value of `property_value_207` or None if not set
        """
        return self["Property Value 207"]

    @property_value_207.setter
    def property_value_207(self, value=None):
        """  Corresponds to IDD Field `Property Value 207`

        Args:
            value (float): value for IDD Field `Property Value 207`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 207"] = value

    @property
    def property_value_208(self):
        """Get property_value_208

        Returns:
            float: the value of `property_value_208` or None if not set
        """
        return self["Property Value 208"]

    @property_value_208.setter
    def property_value_208(self, value=None):
        """  Corresponds to IDD Field `Property Value 208`

        Args:
            value (float): value for IDD Field `Property Value 208`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 208"] = value

    @property
    def property_value_209(self):
        """Get property_value_209

        Returns:
            float: the value of `property_value_209` or None if not set
        """
        return self["Property Value 209"]

    @property_value_209.setter
    def property_value_209(self, value=None):
        """  Corresponds to IDD Field `Property Value 209`

        Args:
            value (float): value for IDD Field `Property Value 209`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 209"] = value

    @property
    def property_value_210(self):
        """Get property_value_210

        Returns:
            float: the value of `property_value_210` or None if not set
        """
        return self["Property Value 210"]

    @property_value_210.setter
    def property_value_210(self, value=None):
        """  Corresponds to IDD Field `Property Value 210`

        Args:
            value (float): value for IDD Field `Property Value 210`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 210"] = value

    @property
    def property_value_211(self):
        """Get property_value_211

        Returns:
            float: the value of `property_value_211` or None if not set
        """
        return self["Property Value 211"]

    @property_value_211.setter
    def property_value_211(self, value=None):
        """  Corresponds to IDD Field `Property Value 211`

        Args:
            value (float): value for IDD Field `Property Value 211`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 211"] = value

    @property
    def property_value_212(self):
        """Get property_value_212

        Returns:
            float: the value of `property_value_212` or None if not set
        """
        return self["Property Value 212"]

    @property_value_212.setter
    def property_value_212(self, value=None):
        """  Corresponds to IDD Field `Property Value 212`

        Args:
            value (float): value for IDD Field `Property Value 212`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 212"] = value

    @property
    def property_value_213(self):
        """Get property_value_213

        Returns:
            float: the value of `property_value_213` or None if not set
        """
        return self["Property Value 213"]

    @property_value_213.setter
    def property_value_213(self, value=None):
        """  Corresponds to IDD Field `Property Value 213`

        Args:
            value (float): value for IDD Field `Property Value 213`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 213"] = value

    @property
    def property_value_214(self):
        """Get property_value_214

        Returns:
            float: the value of `property_value_214` or None if not set
        """
        return self["Property Value 214"]

    @property_value_214.setter
    def property_value_214(self, value=None):
        """  Corresponds to IDD Field `Property Value 214`

        Args:
            value (float): value for IDD Field `Property Value 214`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 214"] = value

    @property
    def property_value_215(self):
        """Get property_value_215

        Returns:
            float: the value of `property_value_215` or None if not set
        """
        return self["Property Value 215"]

    @property_value_215.setter
    def property_value_215(self, value=None):
        """  Corresponds to IDD Field `Property Value 215`

        Args:
            value (float): value for IDD Field `Property Value 215`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 215"] = value

    @property
    def property_value_216(self):
        """Get property_value_216

        Returns:
            float: the value of `property_value_216` or None if not set
        """
        return self["Property Value 216"]

    @property_value_216.setter
    def property_value_216(self, value=None):
        """  Corresponds to IDD Field `Property Value 216`

        Args:
            value (float): value for IDD Field `Property Value 216`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 216"] = value

    @property
    def property_value_217(self):
        """Get property_value_217

        Returns:
            float: the value of `property_value_217` or None if not set
        """
        return self["Property Value 217"]

    @property_value_217.setter
    def property_value_217(self, value=None):
        """  Corresponds to IDD Field `Property Value 217`

        Args:
            value (float): value for IDD Field `Property Value 217`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 217"] = value

    @property
    def property_value_218(self):
        """Get property_value_218

        Returns:
            float: the value of `property_value_218` or None if not set
        """
        return self["Property Value 218"]

    @property_value_218.setter
    def property_value_218(self, value=None):
        """  Corresponds to IDD Field `Property Value 218`

        Args:
            value (float): value for IDD Field `Property Value 218`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 218"] = value

    @property
    def property_value_219(self):
        """Get property_value_219

        Returns:
            float: the value of `property_value_219` or None if not set
        """
        return self["Property Value 219"]

    @property_value_219.setter
    def property_value_219(self, value=None):
        """  Corresponds to IDD Field `Property Value 219`

        Args:
            value (float): value for IDD Field `Property Value 219`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 219"] = value

    @property
    def property_value_220(self):
        """Get property_value_220

        Returns:
            float: the value of `property_value_220` or None if not set
        """
        return self["Property Value 220"]

    @property_value_220.setter
    def property_value_220(self, value=None):
        """  Corresponds to IDD Field `Property Value 220`

        Args:
            value (float): value for IDD Field `Property Value 220`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 220"] = value

    @property
    def property_value_221(self):
        """Get property_value_221

        Returns:
            float: the value of `property_value_221` or None if not set
        """
        return self["Property Value 221"]

    @property_value_221.setter
    def property_value_221(self, value=None):
        """  Corresponds to IDD Field `Property Value 221`

        Args:
            value (float): value for IDD Field `Property Value 221`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 221"] = value

    @property
    def property_value_222(self):
        """Get property_value_222

        Returns:
            float: the value of `property_value_222` or None if not set
        """
        return self["Property Value 222"]

    @property_value_222.setter
    def property_value_222(self, value=None):
        """  Corresponds to IDD Field `Property Value 222`

        Args:
            value (float): value for IDD Field `Property Value 222`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 222"] = value

    @property
    def property_value_223(self):
        """Get property_value_223

        Returns:
            float: the value of `property_value_223` or None if not set
        """
        return self["Property Value 223"]

    @property_value_223.setter
    def property_value_223(self, value=None):
        """  Corresponds to IDD Field `Property Value 223`

        Args:
            value (float): value for IDD Field `Property Value 223`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 223"] = value

    @property
    def property_value_224(self):
        """Get property_value_224

        Returns:
            float: the value of `property_value_224` or None if not set
        """
        return self["Property Value 224"]

    @property_value_224.setter
    def property_value_224(self, value=None):
        """  Corresponds to IDD Field `Property Value 224`

        Args:
            value (float): value for IDD Field `Property Value 224`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 224"] = value

    @property
    def property_value_225(self):
        """Get property_value_225

        Returns:
            float: the value of `property_value_225` or None if not set
        """
        return self["Property Value 225"]

    @property_value_225.setter
    def property_value_225(self, value=None):
        """  Corresponds to IDD Field `Property Value 225`

        Args:
            value (float): value for IDD Field `Property Value 225`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 225"] = value

    @property
    def property_value_226(self):
        """Get property_value_226

        Returns:
            float: the value of `property_value_226` or None if not set
        """
        return self["Property Value 226"]

    @property_value_226.setter
    def property_value_226(self, value=None):
        """  Corresponds to IDD Field `Property Value 226`

        Args:
            value (float): value for IDD Field `Property Value 226`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 226"] = value

    @property
    def property_value_227(self):
        """Get property_value_227

        Returns:
            float: the value of `property_value_227` or None if not set
        """
        return self["Property Value 227"]

    @property_value_227.setter
    def property_value_227(self, value=None):
        """  Corresponds to IDD Field `Property Value 227`

        Args:
            value (float): value for IDD Field `Property Value 227`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 227"] = value

    @property
    def property_value_228(self):
        """Get property_value_228

        Returns:
            float: the value of `property_value_228` or None if not set
        """
        return self["Property Value 228"]

    @property_value_228.setter
    def property_value_228(self, value=None):
        """  Corresponds to IDD Field `Property Value 228`

        Args:
            value (float): value for IDD Field `Property Value 228`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 228"] = value

    @property
    def property_value_229(self):
        """Get property_value_229

        Returns:
            float: the value of `property_value_229` or None if not set
        """
        return self["Property Value 229"]

    @property_value_229.setter
    def property_value_229(self, value=None):
        """  Corresponds to IDD Field `Property Value 229`

        Args:
            value (float): value for IDD Field `Property Value 229`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 229"] = value

    @property
    def property_value_230(self):
        """Get property_value_230

        Returns:
            float: the value of `property_value_230` or None if not set
        """
        return self["Property Value 230"]

    @property_value_230.setter
    def property_value_230(self, value=None):
        """  Corresponds to IDD Field `Property Value 230`

        Args:
            value (float): value for IDD Field `Property Value 230`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 230"] = value

    @property
    def property_value_231(self):
        """Get property_value_231

        Returns:
            float: the value of `property_value_231` or None if not set
        """
        return self["Property Value 231"]

    @property_value_231.setter
    def property_value_231(self, value=None):
        """  Corresponds to IDD Field `Property Value 231`

        Args:
            value (float): value for IDD Field `Property Value 231`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 231"] = value

    @property
    def property_value_232(self):
        """Get property_value_232

        Returns:
            float: the value of `property_value_232` or None if not set
        """
        return self["Property Value 232"]

    @property_value_232.setter
    def property_value_232(self, value=None):
        """  Corresponds to IDD Field `Property Value 232`

        Args:
            value (float): value for IDD Field `Property Value 232`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 232"] = value

    @property
    def property_value_233(self):
        """Get property_value_233

        Returns:
            float: the value of `property_value_233` or None if not set
        """
        return self["Property Value 233"]

    @property_value_233.setter
    def property_value_233(self, value=None):
        """  Corresponds to IDD Field `Property Value 233`

        Args:
            value (float): value for IDD Field `Property Value 233`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 233"] = value

    @property
    def property_value_234(self):
        """Get property_value_234

        Returns:
            float: the value of `property_value_234` or None if not set
        """
        return self["Property Value 234"]

    @property_value_234.setter
    def property_value_234(self, value=None):
        """  Corresponds to IDD Field `Property Value 234`

        Args:
            value (float): value for IDD Field `Property Value 234`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 234"] = value

    @property
    def property_value_235(self):
        """Get property_value_235

        Returns:
            float: the value of `property_value_235` or None if not set
        """
        return self["Property Value 235"]

    @property_value_235.setter
    def property_value_235(self, value=None):
        """  Corresponds to IDD Field `Property Value 235`

        Args:
            value (float): value for IDD Field `Property Value 235`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 235"] = value

    @property
    def property_value_236(self):
        """Get property_value_236

        Returns:
            float: the value of `property_value_236` or None if not set
        """
        return self["Property Value 236"]

    @property_value_236.setter
    def property_value_236(self, value=None):
        """  Corresponds to IDD Field `Property Value 236`

        Args:
            value (float): value for IDD Field `Property Value 236`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 236"] = value

    @property
    def property_value_237(self):
        """Get property_value_237

        Returns:
            float: the value of `property_value_237` or None if not set
        """
        return self["Property Value 237"]

    @property_value_237.setter
    def property_value_237(self, value=None):
        """  Corresponds to IDD Field `Property Value 237`

        Args:
            value (float): value for IDD Field `Property Value 237`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 237"] = value

    @property
    def property_value_238(self):
        """Get property_value_238

        Returns:
            float: the value of `property_value_238` or None if not set
        """
        return self["Property Value 238"]

    @property_value_238.setter
    def property_value_238(self, value=None):
        """  Corresponds to IDD Field `Property Value 238`

        Args:
            value (float): value for IDD Field `Property Value 238`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 238"] = value

    @property
    def property_value_239(self):
        """Get property_value_239

        Returns:
            float: the value of `property_value_239` or None if not set
        """
        return self["Property Value 239"]

    @property_value_239.setter
    def property_value_239(self, value=None):
        """  Corresponds to IDD Field `Property Value 239`

        Args:
            value (float): value for IDD Field `Property Value 239`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 239"] = value

    @property
    def property_value_240(self):
        """Get property_value_240

        Returns:
            float: the value of `property_value_240` or None if not set
        """
        return self["Property Value 240"]

    @property_value_240.setter
    def property_value_240(self, value=None):
        """  Corresponds to IDD Field `Property Value 240`

        Args:
            value (float): value for IDD Field `Property Value 240`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 240"] = value

    @property
    def property_value_241(self):
        """Get property_value_241

        Returns:
            float: the value of `property_value_241` or None if not set
        """
        return self["Property Value 241"]

    @property_value_241.setter
    def property_value_241(self, value=None):
        """  Corresponds to IDD Field `Property Value 241`

        Args:
            value (float): value for IDD Field `Property Value 241`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 241"] = value

    @property
    def property_value_242(self):
        """Get property_value_242

        Returns:
            float: the value of `property_value_242` or None if not set
        """
        return self["Property Value 242"]

    @property_value_242.setter
    def property_value_242(self, value=None):
        """  Corresponds to IDD Field `Property Value 242`

        Args:
            value (float): value for IDD Field `Property Value 242`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 242"] = value

    @property
    def property_value_243(self):
        """Get property_value_243

        Returns:
            float: the value of `property_value_243` or None if not set
        """
        return self["Property Value 243"]

    @property_value_243.setter
    def property_value_243(self, value=None):
        """  Corresponds to IDD Field `Property Value 243`

        Args:
            value (float): value for IDD Field `Property Value 243`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 243"] = value

    @property
    def property_value_244(self):
        """Get property_value_244

        Returns:
            float: the value of `property_value_244` or None if not set
        """
        return self["Property Value 244"]

    @property_value_244.setter
    def property_value_244(self, value=None):
        """  Corresponds to IDD Field `Property Value 244`

        Args:
            value (float): value for IDD Field `Property Value 244`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 244"] = value

    @property
    def property_value_245(self):
        """Get property_value_245

        Returns:
            float: the value of `property_value_245` or None if not set
        """
        return self["Property Value 245"]

    @property_value_245.setter
    def property_value_245(self, value=None):
        """  Corresponds to IDD Field `Property Value 245`

        Args:
            value (float): value for IDD Field `Property Value 245`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 245"] = value

    @property
    def property_value_246(self):
        """Get property_value_246

        Returns:
            float: the value of `property_value_246` or None if not set
        """
        return self["Property Value 246"]

    @property_value_246.setter
    def property_value_246(self, value=None):
        """  Corresponds to IDD Field `Property Value 246`

        Args:
            value (float): value for IDD Field `Property Value 246`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 246"] = value

    @property
    def property_value_247(self):
        """Get property_value_247

        Returns:
            float: the value of `property_value_247` or None if not set
        """
        return self["Property Value 247"]

    @property_value_247.setter
    def property_value_247(self, value=None):
        """  Corresponds to IDD Field `Property Value 247`

        Args:
            value (float): value for IDD Field `Property Value 247`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 247"] = value

    @property
    def property_value_248(self):
        """Get property_value_248

        Returns:
            float: the value of `property_value_248` or None if not set
        """
        return self["Property Value 248"]

    @property_value_248.setter
    def property_value_248(self, value=None):
        """  Corresponds to IDD Field `Property Value 248`

        Args:
            value (float): value for IDD Field `Property Value 248`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 248"] = value

    @property
    def property_value_249(self):
        """Get property_value_249

        Returns:
            float: the value of `property_value_249` or None if not set
        """
        return self["Property Value 249"]

    @property_value_249.setter
    def property_value_249(self, value=None):
        """  Corresponds to IDD Field `Property Value 249`

        Args:
            value (float): value for IDD Field `Property Value 249`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 249"] = value

    @property
    def property_value_250(self):
        """Get property_value_250

        Returns:
            float: the value of `property_value_250` or None if not set
        """
        return self["Property Value 250"]

    @property_value_250.setter
    def property_value_250(self, value=None):
        """  Corresponds to IDD Field `Property Value 250`

        Args:
            value (float): value for IDD Field `Property Value 250`
                Units are based on field `A2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Property Value 250"] = value