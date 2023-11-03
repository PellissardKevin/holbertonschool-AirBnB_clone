#!/usr/bin/python3
"""Unittest for class State"""
import unittest
import os
import pep8
from models.state import State


class test_state(unittest.TestCase):
    """Test cases for State class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.stateInstance = State()
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
        texas = State()
        self.assertEqual(texas.name, "")
        texas.name = "Texas"
        self.assertEqual(texas.name, "Texas")

    def test_pep8_conformance_state(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_father(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")


if __name__ == "__main__":
    unittest.main()
