import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        """Test creation of User instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test that User has specific attributes."""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "First"
        user.last_name = "Last"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "First")
        self.assertEqual(user.last_name, "Last")


if __name__ == "__main__":
    unittest.main()
