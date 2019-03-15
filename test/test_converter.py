
from unittest import TestCase
from LAS import Converter
from test import expected


class ConverterTest(TestCase):

    def setUp(self):
        self.cv = Converter()
        self.log_input_file = self.cv.set_file("files/sample3.las")

    def test_version(self):
        """LAS version is 2.0"""
        self.assertEqual(self.log_input_file.version, 2.0)

    def test_version_section(self):
        version_section = expected.version
        self.assertDictEqual(
            version_section, self.log_input_file.version_section)

    def test_well_section(self):
        well = expected.well
        self.assertDictEqual(well, self.log_input_file.well)

    def test_data_section(self):
        data = expected.data
        self.assertDictEqual(data, self.log_input_file.data)

    def test_parameter_section(self):
        parameter = expected.parameter
        self.assertDictEqual(parameter, self.log_input_file.parameter)

    def test_curve_section(self):
        curve = expected.curve
        self.assertDictEqual(curve, self.log_input_file.curve)

    def test_data_keys_equal_curve_keys(self):
        curve = self.log_input_file.curve.keys()
        data = self.log_input_file.data.keys()
        curve = {e.lower() for e in curve}
        self.assertEqual(curve, data)

    def test_data_keys_equal_curve_keys_sample_2(self):
        log_input_file = self.cv.set_file("files/sample2.las")
        curve = log_input_file.curve.keys()
        data = log_input_file.data.keys()
        curve = {e.lower() for e in curve}
        self.assertEqual(curve, data)

    def test_file_supported(self):
        with self.assertRaises(Exception) as E:
            self.cv = self.cv.set_file("files/sample1.json")
        self.assertTrue("File format no supported!", E.exception)

    def test_version_supported(self):
        with self.assertRaises(Exception) as E:
            self.cv = self.cv.set_file("files/sample0.las")
        self.assertTrue("Version not supported!", E.exception)

    def test_input_bytes_equal_input_file(self):
        log_input_bytes = self.cv.set_stream(expected.bytes_list)
        self.assertDictEqual(log_input_bytes.get_dict(),
                             self.log_input_file.get_dict())

    def test_out_sampel_1_not_equal_out_sample_3(self):
        log_sample_1 = self.cv.set_file("files/sample1.las").get_dict()
        log_sample_3 = self.cv.set_file("files/sample3.las").get_dict()
        self.assertNotEqual(log_sample_1, log_sample_3)
