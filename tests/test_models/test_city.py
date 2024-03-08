#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the City model."""

    def setUp(self):
        """Set up method to start each test."""
        self.city = City()

    def test_instance_creation(self):
        """Test instantiation of City instance."""
        self.assertIsInstance(self.city, City)

    def test_inherits_BaseModel(self):
        """Test if instances of City inherit from BaseModel."""
        self.assertTrue(issubclass(type(self.city), City))

    def test_attributes(self):
        """Test City attributes and their default values."""
        self.assertTrue(hasattr(self.city, "state_id"),
                        "City should have 'state_id'")
        self.assertTrue(hasattr(self.city, "name"),
                        "City should have 'name'")
        self.assertEqual(self.city.state_id, "",
                         "'state_id' should be empty string")
        self.assertEqual(self.city.name, "",
                         "'name' should be empty string")

    def test_attribute_types(self):
        """Test the type of City attributes."""
        self.assertIsInstance(self.city.state_id, str,
                              "'state_id' should be str")
        self.assertIsInstance(self.city.name, str,
                              "'name' should be str")


if __name__ == "__main__":
    unittest.main()
