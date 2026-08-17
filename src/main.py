from src.models.student import Student
from src.services.student_service import StudentService
from src.exceptions.student_exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
)
from src.utils.validators import (
    validate_student_id,
    validate_name,
    validate_age,
    validate_course,
)


def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 50)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7. Load Students")
    print("8. Exit")
    print("=" * 50)


def add_student(service):
    """Collect student information and add a student."""

    print("\n--- Add Student ---")

    try:
        student_id = validate_student_id(
            input("Enter Student ID: ")
        )
        name = validate_name(
            input("Enter Name: ")
        )
        age = validate_age(
            input("Enter Age: ")
        )
        course = validate_course(
            input("Enter Course: ")
        )

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            course=course,
        )

        service.add_student(student)
        print("\nStudent added successfully.")

    except StudentAlreadyExistsError as error:
        print(f"\nError: {error}")

    except ValueError as error:
        print(f"\nInvalid input: {error}")


def view_students(service):
    """Display all students."""

    print("\n--- All Students ---")

    students = service.get_all_students()

    if not students:
        print("No students found.")
        return

    print("-" * 80)
    print(
        f"{'ID':<10}"
        f"{'Name':<25}"
        f"{'Age':<10}"
        f"{'Course':<30}"
    )
    print("-" * 80)

    for student in students:
        print(
            f"{student.student_id:<10}"
            f"{student.name:<25}"
            f"{student.age:<10}"
            f"{student.course:<30}"
        )

    print("-" * 80)


def search_student(service):
    """Search for a student by ID."""

    print("\n--- Search Student ---")

    try:
        student_id = validate_student_id(
            input("Enter Student ID: ")
        )

        student = service.search_student(student_id)

        print("\nStudent Found")
        print("-" * 40)
        print(f"ID     : {student.student_id}")
        print(f"Name   : {student.name}")
        print(f"Age    : {student.age}")
        print(f"Course : {student.course}")
        print("-" * 40)

    except StudentNotFoundError as error:
        print(f"\nError: {error}")

    except ValueError as error:
        print(f"\nInvalid input: {error}")


def update_student(service):
    """Update an existing student's information."""

    print("\n--- Update Student ---")

    try:
        student_id = validate_student_id(
            input("Enter Student ID: ")
        )

        student = service.search_student(student_id)

        print("\nCurrent Information:")
        print(f"Name   : {student.name}")
        print(f"Age    : {student.age}")
        print(f"Course : {student.course}")

        name = validate_name(
            input("\nEnter New Name: ")
        )
        age = validate_age(
            input("Enter New Age: ")
        )
        course = validate_course(
            input("Enter New Course: ")
        )

        service.update_student(
            student_id=student_id,
            name=name,
            age=age,
            course=course,
        )

        print("\nStudent updated successfully.")

    except StudentNotFoundError as error:
        print(f"\nError: {error}")

    except ValueError as error:
        print(f"\nInvalid input: {error}")


def delete_student(service):
    """Delete a student by ID."""

    print("\n--- Delete Student ---")

    try:
        student_id = validate_student_id(
            input("Enter Student ID: ")
        )

        student = service.search_student(student_id)

        print("\nStudent to delete:")
        print(student)

        confirmation = input(
            "Are you sure you want to delete this student? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            service.delete_student(student_id)
            print("\nStudent deleted successfully.")
        else:
            print("\nDelete operation cancelled.")

    except StudentNotFoundError as error:
        print(f"\nError: {error}")

    except ValueError as error:
        print(f"\nInvalid input: {error}")


def save_students(service):
    """Save students to JSON."""

    try:
        service.save_students()
        print("\nStudents saved successfully.")

    except OSError as error:
        print(f"\nUnable to save students: {error}")


def load_students(service):
    """Load students from JSON."""

    try:
        students = service.load_students()
        print(
            f"\nSuccessfully loaded {len(students)} student(s)."
        )

    except (OSError, ValueError) as error:
        print(f"\nUnable to load students: {error}")


def main():
    """Run the Student Management System."""

    service = StudentService()

    print("\nWelcome to the Student Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student(service)

        elif choice == "2":
            view_students(service)

        elif choice == "3":
            search_student(service)

        elif choice == "4":
            update_student(service)

        elif choice == "5":
            delete_student(service)

        elif choice == "6":
            save_students(service)

        elif choice == "7":
            load_students(service)

        elif choice == "8":
            print(
                "\nThank you for using the Student Management System."
            )
            print("Goodbye!")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select a number from 1 to 8."
            )


if __name__ == "__main__":
    main()