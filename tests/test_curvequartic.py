import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.performance_curves import CurveQuartic

log = logging.getLogger(__name__)

class TestCurveQuartic(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvequartic(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveQuartic()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_constant = 2.2
        obj.coefficient1_constant = var_coefficient1_constant
        # real
        var_coefficient2_x = 3.3
        obj.coefficient2_x = var_coefficient2_x
        # real
        var_coefficient3_x2 = 4.4
        obj.coefficient3_x2 = var_coefficient3_x2
        # real
        var_coefficient4_x3 = 5.5
        obj.coefficient4_x3 = var_coefficient4_x3
        # real
        var_coefficient5_x4 = 6.6
        obj.coefficient5_x4 = var_coefficient5_x4
        # real
        var_minimum_value_of_x = 7.7
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 8.8
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_curve_output = 9.9
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 10.1
        obj.maximum_curve_output = var_maximum_curve_output
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvequartics[0].name, var_name)
        self.assertAlmostEqual(idf2.curvequartics[0].coefficient1_constant, var_coefficient1_constant)
        self.assertAlmostEqual(idf2.curvequartics[0].coefficient2_x, var_coefficient2_x)
        self.assertAlmostEqual(idf2.curvequartics[0].coefficient3_x2, var_coefficient3_x2)
        self.assertAlmostEqual(idf2.curvequartics[0].coefficient4_x3, var_coefficient4_x3)
        self.assertAlmostEqual(idf2.curvequartics[0].coefficient5_x4, var_coefficient5_x4)
        self.assertAlmostEqual(idf2.curvequartics[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvequartics[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvequartics[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvequartics[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvequartics[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvequartics[0].output_unit_type, var_output_unit_type)