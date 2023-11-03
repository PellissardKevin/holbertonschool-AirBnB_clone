#!/usr/bin/python3
"""Unittest for class Rewiew"""
import unittest
from models.review import Review


class test_amenity(unittest.TestCase):
    """Test cases for City class"""
    def test_name(self):
        lake = Review()
        self.assertEqual(lake.text, "")
        self.assertEqual(lake.place_id, "")
        lake.text = "a beautiful lake"
        lake.place_id = "place id"
        lake.user_id = "Nice person id"
        self.assertEqual(lake.text, "a beautiful lake")
        self.assertEqual(lake.place_id, "place id")
        self.assertEqual(lake.user_id, "Nice person id")



if __name__ == "__main__":
    unittest.main()
