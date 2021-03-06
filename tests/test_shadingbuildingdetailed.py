import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import ShadingBuildingDetailed

log = logging.getLogger(__name__)

class TestShadingBuildingDetailed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_shadingbuildingdetailed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ShadingBuildingDetailed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_transmittance_schedule_name = "object-list|Transmittance Schedule Name"
        obj.transmittance_schedule_name = var_transmittance_schedule_name
        # real
        var_number_of_vertices = 3.0
        obj.number_of_vertices = var_number_of_vertices
        paras = []
        var_vertex_1_xcoordinate = 4.4
        paras.append(var_vertex_1_xcoordinate)
        var_vertex_1_ycoordinate = 5.5
        paras.append(var_vertex_1_ycoordinate)
        var_vertex_1_zcoordinate = 6.6
        paras.append(var_vertex_1_zcoordinate)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.shadingbuildingdetaileds[0].name, var_name)
        self.assertEqual(idf2.shadingbuildingdetaileds[0].transmittance_schedule_name, var_transmittance_schedule_name)
        self.assertAlmostEqual(idf2.shadingbuildingdetaileds[0].number_of_vertices, var_number_of_vertices)
        index = obj.extensible_field_index("Vertex 1 X-coordinate")
        self.assertAlmostEqual(idf2.shadingbuildingdetaileds[0].extensibles[0][index], var_vertex_1_xcoordinate)
        index = obj.extensible_field_index("Vertex 1 Y-coordinate")
        self.assertAlmostEqual(idf2.shadingbuildingdetaileds[0].extensibles[0][index], var_vertex_1_ycoordinate)
        index = obj.extensible_field_index("Vertex 1 Z-coordinate")
        self.assertAlmostEqual(idf2.shadingbuildingdetaileds[0].extensibles[0][index], var_vertex_1_zcoordinate)