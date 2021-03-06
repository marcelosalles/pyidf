import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerScheduledOff

log = logging.getLogger(__name__)

class TestAvailabilityManagerScheduledOff(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagerscheduledoff(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerScheduledOff()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagerscheduledoffs[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagerscheduledoffs[0].schedule_name, var_schedule_name)