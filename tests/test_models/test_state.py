#!/usr/bin/python3
"""Unittest for class State"""
import unittest
from models.state import State


class test_state(unittest.TestCase):
    """Test cases for State class"""
    def test_name(self):
        texas = State()
        self.assertEqual(texas.name,"")
        texas.name = "Texas"
        self.assertEqual(texas.name, "Texas")


if __name__ == "__main__":
    unittest.main()
