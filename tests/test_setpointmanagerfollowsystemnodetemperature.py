import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerFollowSystemNodeTemperature

log = logging.getLogger(__name__)

class TestSetpointManagerFollowSystemNodeTemperature(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagerfollowsystemnodetemperature(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerFollowSystemNodeTemperature()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # node
        var_reference_node_name = "node|Reference Node Name"
        obj.reference_node_name = var_reference_node_name
        # alpha
        var_reference_temperature_type = "NodeWetBulb"
        obj.reference_temperature_type = var_reference_temperature_type
        # real
        var_offset_temperature_difference = 5.5
        obj.offset_temperature_difference = var_offset_temperature_difference
        # real
        var_maximum_limit_setpoint_temperature = 6.6
        obj.maximum_limit_setpoint_temperature = var_maximum_limit_setpoint_temperature
        # real
        var_minimum_limit_setpoint_temperature = 7.7
        obj.minimum_limit_setpoint_temperature = var_minimum_limit_setpoint_temperature
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].name, var_name)
        self.assertEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].reference_node_name, var_reference_node_name)
        self.assertEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].reference_temperature_type, var_reference_temperature_type)
        self.assertAlmostEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].offset_temperature_difference, var_offset_temperature_difference)
        self.assertAlmostEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].maximum_limit_setpoint_temperature, var_maximum_limit_setpoint_temperature)
        self.assertAlmostEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].minimum_limit_setpoint_temperature, var_minimum_limit_setpoint_temperature)
        self.assertEqual(idf2.setpointmanagerfollowsystemnodetemperatures[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)