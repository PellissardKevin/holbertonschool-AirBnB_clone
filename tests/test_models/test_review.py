#!/usr/bin/python3
"""Unittest for class Rewiew"""
import unittest
import pep8
import os
from models.review import Review


class test_amenity(unittest.TestCase):
    """Test cases for City class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.reviewInstance = Review()
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
        lake = Review()
        self.assertEqual(lake.text, "")
        self.assertEqual(lake.place_id, "")
        lake.text = "a beautiful lake"
        lake.place_id = "place id"
        lake.user_id = "Nice person id"
        self.assertEqual(lake.text, "a beautiful lake")
        self.assertEqual(lake.place_id, "place id")
        self.assertEqual(lake.user_id, "Nice person id")

    def test_pep8_conformance_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_father(self):
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))

if __name__ == "__main__":
    unittest.main()
