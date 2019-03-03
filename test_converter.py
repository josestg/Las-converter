
from unittest import TestCase
from converter import LasConverter


class LasConverterTest(TestCase):

    def setUp(self):
        self.cv = LasConverter("files/sample2.las")
        self.d = self.cv.get_dict()

    def test_file_supported(self):
        with self.assertRaises(Exception) as E:
            self.c = LasConverter("files/sample1.json")
        self.assertTrue("File format no supported!", E.exception)

    def test_version_supported(self):
        try:
            self.cv = LasConverter("files/sample0.las")
            self.cv.get_dict()
        except Exception as E:
            self.assertTrue("Version not supported!", E.exception)

    def test_keys_dict(self):
        d_keys = self.d.keys()
        self.assertEqual({"version", "well", "curve",
                          "parameter", "data", "other"}, d_keys)

    def test_data_keys_equal_curve_keys(self):
        curve = self.d["curve"].keys()
        data = self.d["data"].keys()
        curve = {e.lower() for e in curve}
        self.assertEqual(curve, data)
