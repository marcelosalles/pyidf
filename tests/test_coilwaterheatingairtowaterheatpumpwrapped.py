import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilWaterHeatingAirToWaterHeatPumpWrapped

log = logging.getLogger(__name__)

class TestCoilWaterHeatingAirToWaterHeatPumpWrapped(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilwaterheatingairtowaterheatpumpwrapped(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilWaterHeatingAirToWaterHeatPumpWrapped()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_rated_heating_capacity = 0.0001
        obj.rated_heating_capacity = var_rated_heating_capacity
        # real
        var_rated_cop = 0.0001
        obj.rated_cop = var_rated_cop
        # real
        var_rated_sensible_heat_ratio = 0.75
        obj.rated_sensible_heat_ratio = var_rated_sensible_heat_ratio
        # real
        var_rated_evaporator_inlet_air_drybulb_temperature = 5.0001
        obj.rated_evaporator_inlet_air_drybulb_temperature = var_rated_evaporator_inlet_air_drybulb_temperature
        # real
        var_rated_evaporator_inlet_air_wetbulb_temperature = 5.0001
        obj.rated_evaporator_inlet_air_wetbulb_temperature = var_rated_evaporator_inlet_air_wetbulb_temperature
        # real
        var_rated_condenser_water_temperature = 25.0001
        obj.rated_condenser_water_temperature = var_rated_condenser_water_temperature
        # real
        var_rated_evaporator_air_flow_rate = 0.0001
        obj.rated_evaporator_air_flow_rate = var_rated_evaporator_air_flow_rate
        # alpha
        var_evaporator_fan_power_included_in_rated_cop = "Yes"
        obj.evaporator_fan_power_included_in_rated_cop = var_evaporator_fan_power_included_in_rated_cop
        # node
        var_evaporator_air_inlet_node_name = "node|Evaporator Air Inlet Node Name"
        obj.evaporator_air_inlet_node_name = var_evaporator_air_inlet_node_name
        # node
        var_evaporator_air_outlet_node_name = "node|Evaporator Air Outlet Node Name"
        obj.evaporator_air_outlet_node_name = var_evaporator_air_outlet_node_name
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_ambient_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_ambient_temperature_for_crankcase_heater_operation = var_maximum_ambient_temperature_for_crankcase_heater_operation
        # alpha
        var_evaporator_air_temperature_type_for_curve_objects = "DryBulbTemperature"
        obj.evaporator_air_temperature_type_for_curve_objects = var_evaporator_air_temperature_type_for_curve_objects
        # object-list
        var_heating_capacity_function_of_temperature_curve_name = "object-list|Heating Capacity Function of Temperature Curve Name"
        obj.heating_capacity_function_of_temperature_curve_name = var_heating_capacity_function_of_temperature_curve_name
        # object-list
        var_heating_capacity_function_of_air_flow_fraction_curve_name = "object-list|Heating Capacity Function of Air Flow Fraction Curve Name"
        obj.heating_capacity_function_of_air_flow_fraction_curve_name = var_heating_capacity_function_of_air_flow_fraction_curve_name
        # object-list
        var_heating_cop_function_of_temperature_curve_name = "object-list|Heating COP Function of Temperature Curve Name"
        obj.heating_cop_function_of_temperature_curve_name = var_heating_cop_function_of_temperature_curve_name
        # object-list
        var_heating_cop_function_of_air_flow_fraction_curve_name = "object-list|Heating COP Function of Air Flow Fraction Curve Name"
        obj.heating_cop_function_of_air_flow_fraction_curve_name = var_heating_cop_function_of_air_flow_fraction_curve_name
        # object-list
        var_part_load_fraction_correlation_curve_name = "object-list|Part Load Fraction Correlation Curve Name"
        obj.part_load_fraction_correlation_curve_name = var_part_load_fraction_correlation_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].name, var_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_heating_capacity, var_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_cop, var_rated_cop)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_sensible_heat_ratio, var_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_evaporator_inlet_air_drybulb_temperature, var_rated_evaporator_inlet_air_drybulb_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_evaporator_inlet_air_wetbulb_temperature, var_rated_evaporator_inlet_air_wetbulb_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_condenser_water_temperature, var_rated_condenser_water_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].rated_evaporator_air_flow_rate, var_rated_evaporator_air_flow_rate)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].evaporator_fan_power_included_in_rated_cop, var_evaporator_fan_power_included_in_rated_cop)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].evaporator_air_inlet_node_name, var_evaporator_air_inlet_node_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].evaporator_air_outlet_node_name, var_evaporator_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].maximum_ambient_temperature_for_crankcase_heater_operation, var_maximum_ambient_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].evaporator_air_temperature_type_for_curve_objects, var_evaporator_air_temperature_type_for_curve_objects)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].heating_capacity_function_of_temperature_curve_name, var_heating_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].heating_capacity_function_of_air_flow_fraction_curve_name, var_heating_capacity_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].heating_cop_function_of_temperature_curve_name, var_heating_cop_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].heating_cop_function_of_air_flow_fraction_curve_name, var_heating_cop_function_of_air_flow_fraction_curve_name)
        self.assertEqual(idf2.coilwaterheatingairtowaterheatpumpwrappeds[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)