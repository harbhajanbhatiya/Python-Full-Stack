from src.data.student_repository import StudentRepository
from src.exceptions.student_exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
)
from src.models.student import Student


class StudentService:
    """Provides business operations for managing students."""

    def __init__(self, repository=None):
        self.repository = repository or StudentRepository()
        self.students = self.repository.load_students()

    def add_student(self, student):
        """Add a new student."""

        if self._find_student(student.student_id) is not None:
            raise StudentAlreadyExistsError(student.student_id)

        self.students.append(student)
        self.repository.save_students(self.students)

    def get_all_students(self):
        """Return all students."""

        return self.students

    def search_student(self, student_id):
        """Find and return a student by ID."""

        student = self._find_student(student_id)

        if student is None:
            raise StudentNotFoundError(student_id)

        return student

    def update_student(self, student_id, name, age, course):
        """Update an existing student's information."""

        student = self.search_student(student_id)

        student.name = name
        student.age = age
        student.course = course

        self.repository.save_students(self.students)

    def delete_student(self, student_id):
        """Delete a student by ID."""

        student = self.search_student(student_id)

        self.students.remove(student)
        self.repository.save_students(self.students)

    def save_students(self):
        """Save the current student list."""

        self.repository.save_students(self.students)

    def load_students(self):
        """Reload students from JSON."""

        self.students = self.repository.load_students()
        return self.students

    def _find_student(self, student_id):
        """Find a student without raising an exception."""

        for student in self.students:
            if student.student_id == student_id:
                return student

        return None