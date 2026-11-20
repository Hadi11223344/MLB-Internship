# Day 1 — Python Fundamentals, Data Structures & GitHub

## Overview

This directory contains my Day 1 tasks for the ML Bench Internship Program. The focus was on strengthening Python programming fundamentals, understanding core data structures, solving programming problems, building console-based applications, and learning Git and GitHub workflows.

## 1. Topics Covered

### Python Fundamentals
- Variables and data types
- Conditional statements and operators
- Functions and loops
- Virtual environments
- Basic input handling and validation

### Python Data Structures

**Lists**
- List creation, indexing and slicing
- Adding and removing elements
- List methods and comprehensions
- Basic list problem-solving

**Tuples**
- Tuple creation and operations
- Indexing, counting and unpacking
- Tuple immutability
- Converting between lists and tuples

**Sets**
- Set creation and uniqueness
- Union, intersection and difference
- Symmetric difference
- Removing duplicates from collections

**Dictionaries**
- Key-value pairs
- Accessing, updating and removing values
- Dictionary methods and iteration
- Nested dictionaries
- Word-frequency counting

## 2. Practice Problems

The `Practice_Problems` directory contains Python implementations covering the concepts and exercises studied during Day 1.

| File | Description |
|---|---|
| `lists.py` | List operations and problem-solving exercises |
| `tuples.py` | Tuple operations, counting and conversions |
| `sets.py` | Set operations and duplicate removal |
| `dictionaries.py` | Student records, average calculation and word frequency |

## 3. Mini Projects

### Student Grading System

A console-based Python application that collects student information and subject marks, calculates total and average marks, and assigns a grade according to predefined grading criteria.

**Features:**
- Student name and class input
- Dynamic subject and marks collection
- Marks validation
- Total and average calculation
- Grade assignment
- Formatted student report

**Concepts used:** Functions, dictionaries, loops, conditional statements, exception handling and built-in functions.

### Student Record Management System — Version 1

A console-based application for managing student records using Python dictionaries.

**Features:**
- Add student records
- View all students
- Search students by roll number
- Update student information
- Delete student records
- Input validation
- Menu-driven interface
- Display total student count

**Concepts used:** Nested dictionaries, CRUD operations, functions, loops, conditional statements and input validation.

Note: Student records are stored in memory and are not persisted after the application exits.

## 4. Repository Structure

```text
MLB-Internship/
│
├── .gitignore
│
└── Day1/
    ├── README.md
    │
    ├── Practice_Problems/
    │   ├── lists.py
    │   ├── tuples.py
    │   ├── sets.py
    │   └── dictionaries.py
    │
    ├── Student_Grading_System/
    │   └── main.py
    │
    └── Student_Record_Management/
        └── main.py
```

## 5. How to Run the Projects

Make sure Python 3 is installed.

Check the installation:

```bash
python3 --version
```

Navigate to the repository directory and run the following commands.

**Student Grading System**

```bash
python3 Day1/Student_Grading_System/main.py
```

**Student Record Management System**

```bash
python3 Day1/Student_Record_Management/main.py
```

**Practice files**

```bash
python3 Day1/Practice_Problems/lists.py
python3 Day1/Practice_Problems/tuples.py
python3 Day1/Practice_Problems/sets.py
python3 Day1/Practice_Problems/dictionaries.py
```

## 6. Challenges Faced and Solutions

### Understanding Python Data Structures
Understanding the differences between lists, tuples, sets and dictionaries, particularly their mutability, uniqueness and use cases.

**Solution:** Practised each structure through individual exercises and explored how different data structures can be used to represent and manipulate information.

### Working with Nested Dictionaries
Organizing student records and accessing information stored inside nested dictionaries.

**Solution:** Used roll numbers as dictionary keys and stored individual student details as nested dictionaries.

### Input Validation and Exception Handling
Handling invalid user inputs, duplicate records and unexpected numerical values.

**Solution:** Applied conditional checks and `try/except` blocks to handle invalid inputs and improve application reliability.

### Breaking Problems into Smaller Components
Organizing application logic rather than writing the entire program in one block.

**Solution:** Divided functionality into reusable functions with clearly defined responsibilities.

### Understanding Git and GitHub
Learning the difference between staging, committing and pushing changes.

**Solution:** Practised initializing a repository, staging files, creating commits, configuring a remote repository and pushing code to GitHub.

## 7. Key Learnings

- Developed a stronger understanding of Python fundamentals.
- Learned when and why to use different Python data structures.
- Practised solving problems using loops, functions and conditional logic.
- Gained experience working with nested dictionaries.
- Implemented basic CRUD functionality in a console application.
- Practised input validation and exception handling.
- Learned the fundamentals of Git version control and GitHub repository management.

## 8. Future Improvements

- Introduce JSON-based storage for persistent student records.
- Improve validation and error handling.
- Add additional search and filtering functionality.
- Expand practice with more complex data-structure problems.

---

**Program:** ML Bench Winter Talent Development Program 2026  
**Day:** 01  
**Focus:** Python Fundamentals, Data Structures & GitHub Basics