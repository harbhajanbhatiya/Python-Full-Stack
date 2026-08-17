class Student:
    """Represents a student in the Student Management System."""

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        """Convert student object into a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
        )

    def __str__(self):
        """Return a readable representation of the student."""
        return (
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Course: {self.course}"
        )