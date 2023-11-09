
from unittest import TestCase
from converter import LasConverter


class LasConverterTest(TestCase):

    def setUp(self):
        self.cv = LasConverter()

    def test_file_supported(self):
        with self.assertRaises(Exception) as E:
            self.cv = self.cv.set_file("../files/sample1.json")
        self.assertTrue("File format no supported!", E.exception)

    def test_version_supported(self):
        with self.assertRaises(Exception) as E:
            self.cv = self.cv.set_file("../files/sample0.las")
        self.assertTrue("Version not supported!", E.exception)

    def test_keys_dict(self):
        log = self.cv.set_file("../files/sample2.las").get_dict()
        d_keys = log.keys()
        self.assertEqual({"version", "well", "curve",
                          "parameter", "data", "other"}, d_keys)

    def test_data_keys_equal_curve_keys(self):
        log = self.cv.set_file("../files/sample2.las").get_dict()
        curve = log["curve"].keys()
        data = log["data"].keys()
        curve = {e.lower() for e in curve}
        self.assertEqual(curve, data)
