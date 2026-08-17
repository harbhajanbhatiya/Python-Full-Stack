import json
from pathlib import Path

from src.models.student import Student


class StudentRepository:
    """Handle saving and loading students from a JSON file."""

    def __init__(self, file_path="student_data.json"):
        self.file_path = Path(file_path)

    def save_students(self, students):
        """Save a list of students to the JSON file."""

        student_data = [
            student.to_dict()
            for student in students
        ]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                student_data,
                file,
                indent=4,
            )

    def load_students(self):
        """Load students from the JSON file."""

        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                student_data = json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(
                "Student data file contains invalid JSON."
            ) from error

        if not isinstance(student_data, list):
            raise ValueError(
                "Student data file must contain a JSON list."
            )

        try:
            return [
                Student.from_dict(data)
                for data in student_data
            ]

        except (KeyError, TypeError) as error:
            raise ValueError(
                "Student data contains an invalid record."
            ) from error