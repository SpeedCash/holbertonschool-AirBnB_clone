#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test suite for the Place model."""

    def setUp(self):
        """Set up for the tests."""
        self.place = Place()

    def test_instance_creation(self):
        """Test instantiation of Place instance."""
        self.assertIsInstance(self.place, Place)

    def test_attributes_exist(self):
        """Test that Place has the required attributes."""
        expected_attrs = [
            "city_id", "user_id", "name", "description", "number_rooms",
            "number_bathrooms", "max_guest", "price_by_night", "latitude",
            "longitude", "amenity_ids"
        ]
        for attr in expected_attrs:
            self.assertTrue(hasattr(self.place, attr),
                            f"Missing attribute '{attr}'")

    def test_attribute_types(self):
        """Test the type of Place attributes."""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_attributes_initially_empty_or_zero(self):
        """Test that Place string attributes are initially empty and\
            numeric attributes are zero or None."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertIsNone(self.place.latitude)
        self.assertIsNone(self.place.longitude)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
