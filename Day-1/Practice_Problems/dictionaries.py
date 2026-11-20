
# ==========================================
# DAY 1 - DICTIONARIES
# Python Data Structures Practice
# ==========================================


# 1. Dictionary Creation

student = {
    "name": "Hammad",
    "age": 21,
    "roll_no": 2,
    "course": "Computer Science",
    "cgpa": 3.76
}

print("Student Record:", student)


# 2. Accessing Dictionary Values

print("\nStudent Name:", student["name"])
print("Student Age:", student["age"])

# get() provides a default value if the key is missing.

print("Student CGPA:", student.get("cgpa"))
print("Student Email:", student.get("email", "Not provided"))


# 3. Updating Dictionary Values

student["age"] = 22
student["email"] = "hammad@example.com"

print("\nUpdated Student Record:", student)


# 4. Removing Dictionary Elements

student.pop("email")

del student["roll_no"]

print("\nAfter Removing Elements:", student)


# 5. Iterating Through a Dictionary

print("\nStudent Information:")

for key, value in student.items():
    print(f"{key}: {value}")


# ==========================================
# NESTED DICTIONARIES
# ==========================================


students = {
    "101": {
        "name": "Ali",
        "age": 21,
        "course": "CS"
    },
    "102": {
        "name": "Sara",
        "age": 22,
        "course": "AI"
    }
}

print("\nNested Dictionary:")

for roll_number, details in students.items():
    print(f"\nRoll Number: {roll_number}")

    for key, value in details.items():
        print(f"{key}: {value}")


# Adding a new student.

students["103"] = {
    "name": "Ahmed",
    "age": 20,
    "course": "DS"
}

print("\nUpdated Student Records:", students)


# ==========================================
# PRACTICE EXERCISES
# ==========================================


# Exercise 1: Create a student record dictionary.

student_record = {
    "name": "Hammad",
    "age": 21,
    "roll_no": 2,
    "course": "Computer Science",
    "cgpa": 3.76
}

print("\nStudent Record:", student_record)


# Exercise 2: Calculate the average marks of students.

student_marks = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 78,
    "Usman": 88
}

total_marks = 0

for marks in student_marks.values():
    total_marks += marks

average_marks = total_marks / len(student_marks)

print("\nAverage Student Marks:", average_marks)


# ==========================================
# Exercise 3: Word Frequency Counter
# ==========================================

def word_frequency(text):
    frequency = {}

    for word in text.split():
        word = word.lower().strip(".,!?;:")

        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


sample_text = "Python is easy. Python is powerful and Python is popular!"

result = word_frequency(sample_text)

print("\nWord Frequency:")

for word, count in result.items():
    print(f"{word}: {count}")
