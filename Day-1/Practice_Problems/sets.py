
# ==========================================
# DAY 1 - SETS
# Python Data Structures Practice
# ==========================================


# 1. Set Creation

numbers = {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()

print("Numbers:", numbers)
print("Empty set:", empty_set)


# 2. Set Operations

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 8}


# Union: Elements present in either set.

print("\nUnion:", A | B)


# Intersection: Elements common to both sets.

print("Intersection:", A & B)


# Difference: Elements present in A but not B.

print("Difference (A - B):", A - B)


# Symmetric Difference: Elements present in either
# set, but not in both.

print("Symmetric Difference:", A ^ B)


# 3. Adding and Removing Elements

A.add(10)
print("\nAfter adding 10:", A)

A.remove(2)
print("After removing 2:", A)

# discard() does not raise an error if the element
# does not exist in the set.

A.discard(102)
print("After discarding 102:", A)


# ==========================================
# PRACTICE EXERCISES
# ==========================================


# Exercise 1: Remove duplicate values from a list.

labels = ["cat", "dog", "cat", "bird", "dog"]

unique_labels = set(labels)

print("\nOriginal labels:", labels)
print("Unique labels:", unique_labels)


# Exercise 2: Check whether an element exists in a set.

if "car" in unique_labels:
    print("Class exists.")
else:
    print("Class does not exist.")


# Exercise 3: Find the union of two sets.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_result = set_a.union(set_b)

print("\nUnion result:", union_result)


# Exercise 4: Find the intersection of two sets.

intersection_result = set_a.intersection(set_b)

print("Intersection result:", intersection_result)
