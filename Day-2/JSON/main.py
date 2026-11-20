
"""
Day 2 - JSON Practice
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "students.json"


def save_students(students):
    """Save Python student data into a JSON file."""

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    print("Student data saved successfully.")


def load_students():
    """Load student data from JSON."""

    if not JSON_FILE.exists():
        return []

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            students = json.load(file)

        return students

    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return []


def add_student(students):
    """Add a new student."""

    roll_no = input("Enter roll number: ").strip()

    if any(student["roll_no"] == roll_no for student in students):
        print("Student already exists.")
        return

    name = input("Enter student name: ").strip()

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Age must be a valid integer.")
        return

    course = input("Enter course: ").strip()

    if not roll_no or not name or not course:
        print("Fields cannot be empty.")
        return

    if age <= 0:
        print("Age must be positive.")
        return

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)


def display_students(students):
    """Display all student records."""

    if not students:
        print("No student records available.")
        return

    for student in students:
        print(student)


def update_student(students):
    """Update an existing student's information."""

    roll_no = input("Enter roll number to update: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            name = input("New name (press Enter to skip): ").strip()
            course = input("New course (press Enter to skip): ").strip()
            age_input = input("New age (press Enter to skip): ").strip()

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if age_input:
                try:
                    age = int(age_input)

                    if age <= 0:
                        print("Age must be positive.")
                        return

                    student["age"] = age

                except ValueError:
                    print("Invalid age.")
                    return

            save_students(students)
            print("Student updated.")
            return

    print("Student not found.")


def main():
    students = load_students()

    print("\n--- JSON Student Management ---")

    while True:

        print("\n1. View Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Save and Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            add_student(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            save_students(students)
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
