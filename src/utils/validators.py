def validate_student_id(student_id):
    """Validate and convert a student ID to an integer."""

    student_id = student_id.strip()

    if not student_id:
        raise ValueError("Student ID cannot be empty.")

    try:
        student_id = int(student_id)
    except ValueError as error:
        raise ValueError("Student ID must be a number.") from error

    if student_id <= 0:
        raise ValueError("Student ID must be greater than zero.")

    return student_id


def validate_name(name):
    """Validate a student's name."""

    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    if not all(character.isalpha() or character.isspace() for character in name):
        raise ValueError("Name can contain only letters and spaces.")

    return name


def validate_age(age):
    """Validate and convert a student's age to an integer."""

    age = age.strip()

    if not age:
        raise ValueError("Age cannot be empty.")

    try:
        age = int(age)
    except ValueError as error:
        raise ValueError("Age must be a number.") from error

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120.")

    return age


def validate_course(course):
    """Validate a student's course."""

    course = course.strip()

    if not course:
        raise ValueError("Course cannot be empty.")

    return course