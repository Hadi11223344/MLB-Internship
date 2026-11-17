
# ==========================================
# DAY 1 - TUPLES
# Python Data Structures Practice
# ==========================================


# 1. Tuple Creation

student = ("Hammad", 21, "Computer Science", 3.76)

coordinates = (31.5204, 74.3587)
rgb_color = (255, 128, 0)
numbers = (10, 20, 30, 20, 40)


# 2. Accessing Tuple Elements

print("First element:", numbers[0])
print("Last element:", numbers[-1])


# 3. Tuple Methods and Operations

print("Occurrences of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))
print("Tuple length:", len(numbers))


# 4. Tuple Unpacking

name, age, department, cgpa = student

print("\nStudent Information")
print("Name:", name)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)


# 5. Single-Element Tuple

single_element = (10,)
print("\nSingle-element tuple:", single_element)


# ==========================================
# PRACTICE EXERCISES
# ==========================================


# Exercise 1: Create a tuple containing repeated values.

duplicate_tup = (1, 2, 2, 3, 4, 5, 5)

print("\nOriginal tuple:", duplicate_tup)


# Exercise 2: Count occurrences of a given element.

def find_occurrences(nums, target):
    counter = 0

    for num in nums:
        if num == target:
            counter += 1

    return counter


print("Occurrences of 2:", find_occurrences(duplicate_tup, 2))


# Exercise 3: Find the index of an element.

def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


print("Index of 3:", find_index(duplicate_tup, 3))


# Exercise 4: Convert a tuple into a list.

my_list = list(duplicate_tup)

print("Converted list:", my_list)


# Exercise 5: Convert a list into a tuple.

my_tuple = tuple(my_list)

print("Converted tuple:", my_tuple)


# Exercise 6: Unpack a tuple into individual variables.

student_record = ("Hammad", 21, "Computer Science", 3.76)

name, age, department, cgpa = student_record

print("\nUnpacked Student Record")
print("Name:", name)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)
