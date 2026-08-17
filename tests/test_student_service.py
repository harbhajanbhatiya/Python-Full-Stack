import unittest
import os
from src.models.student import Student
from src.services.student_service import StudentService
from src.data.student_repository import StudentRepository
from src.exceptions.student_exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
)



class TestStudentService(unittest.TestCase):
    """Test StudentService functionality."""

    def setUp(self):
        """Create a fresh service for each test."""

        self.repository = StudentRepository(
            file_path="test_student_data.json"
        )

        self.repository.save_students([])

        self.service = StudentService(
            repository=self.repository
        )

    def tearDown(self):
        """Clean up test data."""


        if os.path.exists("test_student_data.json"):
            os.remove("test_student_data.json")

    def test_add_student(self):
        """Test adding a student."""

        student = Student(
            student_id=1,
            name="Rahul",
            age=21,
            course="AI & DS",
        )

        self.service.add_student(student)

        students = self.service.get_all_students()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].student_id, 1)

    def test_duplicate_student(self):
        """Test duplicate student ID."""

        student = Student(
            student_id=1,
            name="Rahul",
            age=21,
            course="AI & DS",
        )

        self.service.add_student(student)

        with self.assertRaises(StudentAlreadyExistsError):
            self.service.add_student(student)

    def test_search_student(self):
        """Test searching for a student."""

        student = Student(
            student_id=1,
            name="Rahul",
            age=21,
            course="AI & DS",
        )

        self.service.add_student(student)

        result = self.service.search_student(1)

        self.assertEqual(result.name, "Rahul")

    def test_search_missing_student(self):
        """Test searching for a student that does not exist."""

        with self.assertRaises(StudentNotFoundError):
            self.service.search_student(999)

    def test_update_student(self):
        """Test updating student information."""

        student = Student(
            student_id=1,
            name="Rahul",
            age=21,
            course="AI & DS",
        )

        self.service.add_student(student)

        self.service.update_student(
            student_id=1,
            name="Rahul Sharma",
            age=22,
            course="CSE",
        )

        updated_student = self.service.search_student(1)

        self.assertEqual(updated_student.name, "Rahul Sharma")
        self.assertEqual(updated_student.age, 22)
        self.assertEqual(updated_student.course, "CSE")

    def test_delete_student(self):
        """Test deleting a student."""

        student = Student(
            student_id=1,
            name="Rahul",
            age=21,
            course="AI & DS",
        )

        self.service.add_student(student)

        self.service.delete_student(1)

        self.assertEqual(
            len(self.service.get_all_students()),
            0,
        )

    def test_empty_json_file(self):
        """Test loading an empty JSON file."""

        with open(
            "test_student_data.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write("")

        with self.assertRaises(ValueError):
            self.repository.load_students()

    def test_invalid_json_file(self):
        """Test loading invalid JSON."""

        with open(
            "test_student_data.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write("This is not valid JSON")

        with self.assertRaises(ValueError):
            self.repository.load_students()


if __name__ == "__main__":
    unittest.main()