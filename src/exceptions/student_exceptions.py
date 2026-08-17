class StudentError(Exception):
    """Base exception for student-related errors."""


class StudentAlreadyExistsError(StudentError):
    """Raised when a student ID already exists."""

    def __init__(self, student_id):
        super().__init__(
            f"Student with ID {student_id} already exists."
        )


class StudentNotFoundError(StudentError):
    """Raised when a student cannot be found."""

    def __init__(self, student_id):
        super().__init__(
            f"Student with ID {student_id} was not found."
        )