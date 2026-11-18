
"""
Day 2 - Persistent Student Record Management System

Features:
- Add student
- View students
- Search student
- Update student
- Delete student
- Persistent JSON storage
- Input validation and exception handling
"""

import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "students.json"


def load_students() -> dict[str, dict[str, Any]]:
    """Load student records from JSON."""

    if not JSON_FILE.exists():
        return {}

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            students = json.load(file)

        if not isinstance(students, dict):
            raise ValueError("Expected a dictionary of student records.")

        return students

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        return {}

    except OSError as error:
        print("File loading error:", error)
        return {}


def save_students(students):
    """Persist student records to JSON."""

    try:
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        print("Records saved successfully.")

    except OSError as error:
        print("Unable to save records:", error)


def add_student(students):

    roll_no = input("Enter roll number: ").strip()

    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter name: ").strip()
    course = input("Enter course: ").strip()

    try:
        age = int(input("Enter age: "))

        if age <= 0 or age > 120:
            print("Age must be between 1 and 120.")
            return

    except ValueError:
        print("Invalid age. Enter a whole number.")
        return

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    students[roll_no] = {
        "name": name,
        "age": age,
        "course": course
    }

    save_students(students)


def view_students(students):

    if not students:
        print("No records available.")
        return

    print("\n--- All Student Records ---")

    for roll_no, student in students.items():

        print(f"\nRoll Number: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")


def search_student(students):

    roll_no = input("Enter roll number: ").strip()

    student = students.get(roll_no)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Found:")
    print(student)


def update_student(students):

    roll_no = input("Enter roll number: ").strip()

    if roll_no not in students:
        print("Student not found.")
        return

    student = students[roll_no]

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()
    age = input(f"Age [{student['age']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()

    if name:
        student["name"] = name

    if age:
        try:
            new_age = int(age)

            if new_age <= 0 or new_age > 120:
                print("Invalid age.")
                return

            student["age"] = new_age

        except ValueError:
            print("Age must be an integer.")
            return

    if course:
        student["course"] = course

    save_students(students)


def delete_student(students):

    roll_no = input("Enter roll number: ").strip()

    if roll_no not in students:
        print("Student not found.")
        return

    confirmation = input("Are you sure? (y/n): ").strip().lower()

    if confirmation == "y":

        del students[roll_no]

        save_students(students)

        print("Student deleted successfully.")

    else:
        print("Deletion cancelled.")


def display_menu():

    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():

    students = load_students()

    print(f"Loaded {len(students)} student records.")

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
