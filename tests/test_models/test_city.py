#!/usr/bin/python3
"""Unittest for class City"""
import unittest
from models.city import City


class test_amenity(unittest.TestCase):
    """Test cases for City class"""
    def test_name(self):
        Chicago = City()
        self.assertEqual(Chicago.name,"")
        self.assertEqual(Chicago.state_id, "")
        Chicago.name = "Chicago"
        self.assertEqual(Chicago.name, "Chicago")
        Chicago.state_id = "illinois id"
        self.assertEqual(Chicago.state_id, "illinois id")



if __name__ == "__main__":
    unittest.main()
