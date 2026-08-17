import unittest

from src.utils.validators import (
    validate_student_id,
    validate_name,
    validate_age,
    validate_course,
)


class TestValidators(unittest.TestCase):
    """Test student input validation."""

    def test_valid_student_id(self):
        """Test a valid student ID."""

        self.assertEqual(
            validate_student_id("101"),
            101,
        )

    def test_invalid_student_id(self):
        """Test an invalid student ID."""

        with self.assertRaises(ValueError):
            validate_student_id("abc")

    def test_negative_student_id(self):
        """Test a negative student ID."""

        with self.assertRaises(ValueError):
            validate_student_id("-1")

    def test_valid_name(self):
        """Test a valid student name."""

        self.assertEqual(
            validate_name("Rahul Sharma"),
            "Rahul Sharma",
        )

    def test_empty_name(self):
        """Test an empty name."""

        with self.assertRaises(ValueError):
            validate_name("")

    def test_invalid_name(self):
        """Test a name containing invalid characters."""

        with self.assertRaises(ValueError):
            validate_name("Rahul123")

    def test_valid_age(self):
        """Test a valid age."""

        self.assertEqual(
            validate_age("21"),
            21,
        )

    def test_invalid_age(self):
        """Test a non-numeric age."""

        with self.assertRaises(ValueError):
            validate_age("abc")

    def test_age_out_of_range(self):
        """Test an age outside the allowed range."""

        with self.assertRaises(ValueError):
            validate_age("-5")

    def test_valid_course(self):
        """Test a valid course."""

        self.assertEqual(
            validate_course("AI & DS"),
            "AI & DS",
        )

    def test_empty_course(self):
        """Test an empty course."""

        with self.assertRaises(ValueError):
            validate_course("")


if __name__ == "__main__":
    unittest.main()