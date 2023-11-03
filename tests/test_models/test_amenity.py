#!/usr/bin/python3
"""Unittest for class Amenity"""
import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """Test cases for Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.amenityInstance = Amenity()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_name(self):
        hotel = Amenity()
        self.assertEqual(hotel.name, "")
        hotel.name = "hotel"
        self.assertEqual(hotel.name, "hotel")

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_father(self):
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

if __name__ == "__main__":
    unittest.main()
