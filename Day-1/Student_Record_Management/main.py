
students = {}


def add_student():
    print("\n--- ADD STUDENT ---")

    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return

    if roll_number in students:
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter student age: "))

        if age <= 0:
            print("Age must be positive.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    students[roll_number] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("Student added successfully!")


def view_students():
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No student records found.")
        return

    for roll_number, details in students.items():
        print("-" * 35)
        print(f"Roll Number: {roll_number}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Course     : {details['course']}")

    print("-" * 35)
    print(f"Total Students: {len(students)}")


def search_student():
    print("\n--- SEARCH STUDENT ---")

    roll_number = input("Enter roll number: ").strip()

    student = students.get(roll_number)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Found!")
    print(f"Roll Number: {roll_number}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Course     : {student['course']}")


def update_student():
    print("\n--- UPDATE STUDENT ---")

    roll_number = input("Enter roll number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]

    print("\nLeave a field empty to keep its existing value.")

    new_name = input(
        f"Enter new name [{student['name']}]: "
    ).strip()

    if new_name:
        student["name"] = new_name

    new_age = input(
        f"Enter new age [{student['age']}]: "
    ).strip()

    if new_age:
        try:
            age = int(new_age)

            if age <= 0:
                print("Invalid age. Keeping previous age.")
            else:
                student["age"] = age

        except ValueError:
            print("Invalid age. Keeping previous age.")

    new_course = input(
        f"Enter new course [{student['course']}]: "
    ).strip()

    if new_course:
        student["course"] = new_course

    print("Student record updated successfully!")


def delete_student():
    print("\n--- DELETE STUDENT ---")

    roll_number = input("Enter roll number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    confirmation = input(
        f"Delete {students[roll_number]['name']}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        del students[roll_number]
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def display_menu():
    print("\n" + "=" * 40)
    print("      STUDENT RECORD MANAGEMENT")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 40)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
