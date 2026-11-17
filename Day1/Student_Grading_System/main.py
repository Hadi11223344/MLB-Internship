
def get_student_info():
    """Collect basic student information."""
    name = input("Enter student name: ").strip()
    student_class = input("Enter student class: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    while not student_class:
        print("Class cannot be empty.")
        student_class = input("Enter student class: ").strip()

    return {
        "name": name,
        "class": student_class
    }


def get_subjects():
    """Collect subject names and marks."""
    subjects = {}

    while True:
        try:
            number_of_subjects = int(input("How many subjects? "))

            if number_of_subjects <= 0:
                print("Enter at least one subject.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    while len(subjects) < number_of_subjects:
        subject_name = input(
            f"Enter subject {len(subjects) + 1} name: "
        ).strip()

        if not subject_name:
            print("Subject name cannot be empty.")
            continue

        if subject_name in subjects:
            print("Subject already exists. Enter a different name.")
            continue

        try:
            marks = float(input(f"Enter marks for {subject_name}: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue

        except ValueError:
            print("Please enter valid numerical marks.")
            continue

        subjects[subject_name] = marks

    return subjects


def calculate_total(subjects):
    return sum(subjects.values())


def calculate_average(subjects):
    total = calculate_total(subjects)
    number_of_subjects = len(subjects)

    return total / number_of_subjects


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        return "F"


def display_report(student, subjects, total, average, grade):
    print("\n" + "=" * 40)
    print("         STUDENT GRADE REPORT")
    print("=" * 40)

    print(f"Student Name : {student['name']}")
    print(f"Class        : {student['class']}")

    print("\nSubject-wise Marks:")

    for subject, marks in subjects.items():
        print(f"{subject:<25} {marks:>6.2f}")

    print("-" * 40)
    print(f"Total Marks  : {total:.2f}")
    print(f"Average      : {average:.2f}")
    print(f"Final Grade  : {grade}")
    print("=" * 40)


def main():
    print("STUDENT GRADING SYSTEM")
    print("-" * 40)

    student = get_student_info()
    subjects = get_subjects()

    total = calculate_total(subjects)
    average = calculate_average(subjects)
    grade = calculate_grade(average)

    display_report(student, subjects, total, average, grade)


if __name__ == "__main__":
    main()
