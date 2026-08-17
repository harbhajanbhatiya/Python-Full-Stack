# Console-Based Student Management System

## 1. Project Overview

The **Console-Based Student Management System** is a Python application developed as part of **Python Full Stack Development Internship – Task 1**.

The project demonstrates core Python programming concepts, Object-Oriented Programming (OOP), data structures, exception handling, input validation, JSON-based file handling, modular application architecture, automated testing, and Git/GitHub practices.

The application allows administrators to manage student records through a simple console-based interface.

---

## 2. Objectives

The main objectives of this project are:

* Apply Python programming fundamentals.
* Implement Object-Oriented Programming concepts.
* Work with Python data structures.
* Build reusable and modular code.
* Implement input validation.
* Handle application exceptions gracefully.
* Store student records using JSON.
* Implement CRUD operations.
* Write automated tests.
* Follow clean coding and PEP 8 practices.
* Prepare the project for future database and web application development.

---

## 3. Features

The system provides the following functionality:

* Add Student
* View All Students
* Search Student
* Update Student
* Delete Student
* Save Student Records
* Load Student Records
* JSON-based data persistence
* Input validation
* Custom exception handling
* Duplicate student ID detection
* Student-not-found handling
* Modular project architecture
* Automated unit testing

---

## 4. Technologies Used

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Application development  |
| JSON       | Student data persistence |
| `unittest` | Automated testing        |
| Git        | Version control          |
| GitHub     | Source code hosting      |
| VS Code    | Development environment  |
| `venv`     | Virtual environment      |

---

## 5. Project Architecture

The project follows a modular architecture where different responsibilities are separated into different components.

```text
User
 │
 ▼
src/main.py
 │
 ▼
StudentService
 │
 ├──────────────► Student Model
 │
 ├──────────────► Validators
 │
 ├──────────────► Custom Exceptions
 │
 ▼
StudentRepository
 │
 ▼
student_data.json
```

### Responsibilities

**`main.py`**

Handles the console interface, menu and user interaction.

**`models/student.py`**

Defines the `Student` class and represents student data.

**`services/student_service.py`**

Contains the main business logic for adding, searching, updating and deleting students.

**`data/student_repository.py`**

Handles saving and loading student records using JSON.

**`utils/validators.py`**

Validates student IDs, names, ages and courses.

**`exceptions/student_exceptions.py`**

Contains custom exceptions used by the application.

**`tests/`**

Contains automated tests for application functionality and validation.

---

## 6. Project Structure

```text
TASK 1/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_service.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── student_repository.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py
│   │
│   └── exceptions/
│       ├── __init__.py
│       └── student_exceptions.py
│
├── tests/
│   ├── test_student_service.py
│   └── test_validators.py
│
├── student_data.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 7. OOP Concepts Used

### Class

The `Student` class represents a student in the application.

### Object

Individual student records are represented as objects created from the `Student` class.

### Constructor

The `__init__()` method initializes student attributes such as:

* Student ID
* Name
* Age
* Course

### Encapsulation

Student-related data and behavior are organized within the `Student` class.

### Class Method

The `from_dict()` class method creates a `Student` object from dictionary data loaded from JSON.

### Object Representation

The `__str__()` method provides a readable representation of a student object.

---

## 8. CRUD Operations

The application implements the following CRUD-related operations:

### Create

Adds a new student record.

### Read

Displays all students or searches for a specific student.

### Update

Modifies an existing student's information.

### Delete

Removes a student record from the system.

---

## 9. JSON Data Persistence

Student records are stored in:

```text
student_data.json
```

Example:

```json
[
    {
        "student_id": 101,
        "name": "Rahul Sharma",
        "age": 21,
        "course": "Artificial Intelligence and Data Science"
    }
]
```

The application converts `Student` objects into dictionaries before storing them as JSON.

When loading the data, the JSON records are converted back into `Student` objects.

---

## 10. Input Validation

The application validates:

* Student ID
* Student name
* Student age
* Student course

Examples of invalid input handled by the application include:

```text
abc
-5
empty values
invalid characters
duplicate student IDs
```

Invalid input does not cause the application to terminate unexpectedly.

---

## 11. Exception Handling

Custom exceptions are implemented for student-related errors.

### StudentAlreadyExistsError

Raised when a student with the same ID already exists.

### StudentNotFoundError

Raised when a requested student cannot be found.

The application also handles invalid input and JSON-related errors.

---

## 12. Automated Testing

The project uses Python's built-in `unittest` framework.

The test suite covers:

* Adding students
* Searching students
* Updating students
* Deleting students
* Duplicate student detection
* Missing student detection
* JSON error handling
* Student ID validation
* Name validation
* Age validation
* Course validation

The complete test suite contains **19 automated tests**.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 19 tests

OK
```

---

## 13. Installation

### Step 1 — Clone the repository

```bash
git clone (https://github.com/harbhajanbhatiya/Python-Full-Stack.git)
```

### Step 2 — Enter the project directory

```bash
cd "TASK 1"
```

### Step 3 — Create a virtual environment

```bash
py -3.14 -m venv venv
```

### Step 4 — Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### Step 5 — Run the application

```bash
python -m src.main
```

---

## 14. How to Use

After starting the application, the following menu is displayed:

```text
==================================================
          STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Save Students
7. Load Students
8. Exit
==================================================
```

Enter the corresponding number to perform an operation.

---

## 15. Screenshots

Add project screenshots in this section after capturing them from the working application.

Recommended screenshots:

1. Main menu
2. Adding a student
3. Viewing students
4. Searching for a student
5. Updating a student
6. Deleting a student
7. Validation/error handling
8. JSON data file
9. Automated test results

Example:

```text
screenshots/
├── main-menu.png
├── add-student.png
├── view-students.png
├── search-student.png
├── update-student.png
├── delete-student.png
├── validation-error.png
├── json-data.png
└── tests-passed.png
```

---

## 16. Testing Results

The project was manually tested for:

* Student creation
* Student viewing
* Student searching
* Student updating
* Student deletion
* Duplicate IDs
* Invalid IDs
* Invalid ages
* Empty names
* Empty courses
* Delete cancellation
* JSON persistence
* JSON error handling

Automated testing was also performed using Python's `unittest` framework.

**Result: 19 tests passed successfully.**

---

## 17. Code Quality

The project follows clean coding practices including:

* Meaningful variable and function names
* Modular architecture
* Function documentation
* Class documentation
* Separation of responsibilities
* Reusable functions
* Exception handling
* JSON persistence
* PEP 8-oriented formatting

---

## 18. Future Enhancements

Possible future improvements include:

* SQL database integration
* PostgreSQL support
* Django backend
* Django REST Framework API
* Web-based frontend
* User authentication
* Role-based access control
* Student attendance management
* Advanced reporting
* Search and filtering
* Cloud deployment

These improvements can be implemented in later stages of the Python Full Stack Development internship.

---

## 19. Learning Outcomes

This project provided practical experience with:

* Python programming
* Object-Oriented Programming
* Data structures
* Functions and modules
* Exception handling
* File handling
* JSON data persistence
* Input validation
* Automated testing
* Modular application design
* Git and GitHub
* Clean coding practices

---

## 20. Conclusion

The Console-Based Student Management System demonstrates the application of Python fundamentals and Object-Oriented Programming concepts in a practical software project.

The project provides a functional student record management system while following modular architecture, JSON persistence, input validation, exception handling and automated testing.

It also establishes a foundation for future development using databases, Django, REST APIs and frontend technologies.
