#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity model."""

    def setUp(self):
        """Set up method to start each test with a fresh Amenity instance."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test instantiation of Amenity instance."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inherits_BaseModel(self):
        """Test if instances of Amenity inherit from BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), Amenity))

    def test_attributes(self):
        """Test Amenity attributes and their defaults."""
        self.assertTrue(hasattr(self.amenity, "name"),
                        "Amenity missing 'name'")
        self.assertEqual(self.amenity.name, "",
                         "'name' should be empty string")

    def test_attribute_types(self):
        """Test the type of Amenity attributes."""
        self.assertIsInstance(self.amenity.name, str,
                              "'name' should be str")


if __name__ == "__main__":
    unittest.main()
