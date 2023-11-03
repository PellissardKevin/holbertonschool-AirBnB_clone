#!/usr/bin/python3
"""Unittest for class Amenity"""
import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """Test cases for Amenity class"""
    def test_name(self):
        hotel = Amenity()
        self.assertEqual(hotel.name,"")
        hotel.name = "hotel"
        self.assertEqual(hotel.name, "hotel")


if __name__ == "__main__":
    unittest.main()
