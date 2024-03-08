import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test suite for the Review model."""

    def setUp(self):
        """Set up method to start each test."""
        self.review = Review()

    def test_instance_creation(self):
        """Test instantiation of Review instance."""
        self.assertIsInstance(self.review, Review)

    def test_attributes_exist(self):
        """Test that Review has specific attributes and can be assigned."""
        self.review.place_id = "place.id"
        self.review.user_id = "user.id"
        self.review.text = "Great place!"
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "place.id")
        self.assertEqual(self.review.user_id, "user.id")
        self.assertEqual(self.review.text, "Great place!")

    def test_id_unique(self):
        """Test that each Review has a unique id."""
        review2 = Review()
        self.assertNotEqual(self.review.id, review2.id)

    def test_to_dict(self):
        """Test conversion of Review attributes to dictionary."""
        self.review.place_id = "another.place.id"
        self.review.text = "Amazing atmosphere."
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "another.place.id")
        self.assertEqual(review_dict["text"], "Amazing atmosphere.")
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)

    def test_str(self):
        """Test the string representation of the Review."""
        expected = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(expected, str(self.review))


if __name__ == "__main__":
    unittest.main()
