# PROJECT DOCUMENTATION

# Console-Based Student Management System

### Python Full Stack Development Internship – Task 1

## 1. Project Information


Project Title: Console-Based Student Management System
Internship Domain: Python Full Stack Development
Task Number: Task 1
Application Type: Console-Based Application
Programming Language: Python
Data Storage: JSON 
Testing Framework: Python unittest
Version Control: Git
Repository Hosting: GitHub


# 2. Introduction

The Student Management System is a console-based Python application developed as part of the Python Full Stack Development Internship – Task 1.

The purpose of this project is to build a simple but properly structured application for managing student records. The system allows the user to add, view, search, update and delete student information through a command-line interface.

Instead of keeping the complete program in one large Python file, the project is divided into separate modules. Student-related data, business logic, validation, exception handling and JSON file operations are handled independently.

This approach makes the project easier to understand, test, maintain and extend in the future.

The project also helped in applying Python fundamentals, Object-Oriented Programming, data structures, file handling, exception handling, input validation, automated testing and Git/GitHub practices.


# 3. Problem Statement

Managing student information manually can become difficult when the number of records increases.

A basic student management system should provide a way to:

- Add new student records
- View existing students
- Search for a particular student
- Update student information
- Delete student records
- Save student information for future use
- Load previously saved information
- Validate incorrect user input
- Handle errors without terminating the application unexpectedly

The objective of this project is to solve these problems using a simple Python console application with JSON-based data persistence.


# 4. Objectives

The main objectives of the project are:

1. To develop a functional console-based Student Management System.
2. To apply Python programming fundamentals in a practical project.
3. To understand and implement Object-Oriented Programming.
4. To use Python data structures for storing student records.
5. To separate application logic into reusable modules.
6. To implement CRUD operations.
7. To store student records using JSON.
8. To validate user input before processing it.
9. To handle application-specific exceptions.
10. To write automated tests using Python's `unittest` framework.
11. To follow clean and readable coding practices.
12. To use Git and GitHub for version control.
13. To prepare the application structure for future database and web development.

# 5. Scope of the Project

The current version of the project focuses on managing student records through a console interface.

The system supports:

- Student creation
- Student viewing
- Student searching
- Student updating
- Student deletion
- JSON data persistence
- Input validation
- Exception handling
- Automated testing

The project does not currently include:

- User authentication
- Database server
- Web interface
- Multiple user roles
- Cloud deployment
- REST APIs

These features can be added in future versions.

# 6. Technologies Used


Python: Main programming language
JSON: Persistent storage of student records
`pathlib`: File path management
`unittest`: Automated testing
Git: Version control
GitHub: Repository hosting
VS Code: Development environment
`venv`: Virtual environment

The project mainly uses Python's built-in libraries, which keeps the application lightweight and easy to set up.


# 7. System Requirements

## Hardware Requirements

The application has very low hardware requirements because it is a console-based Python application.

A basic computer capable of running Python is sufficient.

## Software Requirements

- Windows, Linux or macOS
- Python
- Visual Studio Code or another Python-compatible IDE
- Git
- GitHub account for repository hosting

### Python Environment

The development environment used for this project is Python 3.14 with a virtual environment.

Note: The internship document specifies Python 3.13. The project was ultimately developed and tested using Python 3.14.

# 8. Development Environment

A Python virtual environment was created for the project so that the project could have its own isolated Python environment.

The environment was created using:

powershell
py -3.14 -m venv venv