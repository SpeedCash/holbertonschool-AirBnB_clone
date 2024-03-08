import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test suite for the State model."""

    def test_instance_creation(self):
        """Test instantiation of State instance."""
        state = State()
        self.assertIsInstance(state, State)

    def test_name_attribute(self):
        """Test that State has a name attribute and can be set."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_id_unique(self):
        """Test that each State has a unique id."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_to_dict(self):
        """Test conversion of State attributes to dictionary."""
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "New York")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)

    def test_str(self):
        """Test the string representation of the State."""
        state = State()
        state.name = "Alaska"
        expected = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(expected, str(state))


if __name__ == "__main__":
    unittest.main()
