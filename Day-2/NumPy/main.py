
"""
Day 2 - NumPy Fundamentals
"""

import numpy as np


def main():

    # 1. Creating arrays

    array_1d = np.array([10, 20, 30, 40, 50])

    array_2d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print("--- Array Creation ---")
    print("1D Array:", array_1d)
    print("2D Array:\n", array_2d)

    # 2. Array properties

    print("\n--- Array Properties ---")
    print("Shape:", array_2d.shape)
    print("Dimensions:", array_2d.ndim)
    print("Size:", array_2d.size)
    print("Data Type:", array_2d.dtype)

    # 3. Indexing

    print("\n--- Indexing ---")
    print("First element:", array_1d[0])
    print("Last element:", array_1d[-1])
    print("Element at row 1, column 2:", array_2d[0, 1])

    # 4. Slicing

    print("\n--- Slicing ---")
    print("First three elements:", array_1d[:3])
    print("Elements from index 1 to 3:", array_1d[1:4])
    print("First row:", array_2d[0, :])
    print("First two columns:\n", array_2d[:, :2])

    # 5. Arithmetic operations

    a = np.array([10, 20, 30])
    b = np.array([1, 2, 3])

    print("\n--- Arithmetic Operations ---")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Scalar multiplication:", a * 2)

    # 6. Mathematical functions

    scores = np.array([70, 80, 90, 60, 100])

    print("\n--- Mathematical Operations ---")
    print("Maximum:", np.max(scores))
    print("Minimum:", np.min(scores))
    print("Mean:", np.mean(scores))
    print("Sum:", np.sum(scores))
    print("Standard Deviation:", np.std(scores))

    # 7. Reshaping

    numbers = np.arange(1, 13)

    matrix = numbers.reshape(3, 4)

    print("\n--- Reshaping ---")
    print("Original:", numbers)
    print("Reshaped:\n", matrix)

    # 8. Boolean filtering

    print("\n--- Boolean Filtering ---")

    high_scores = scores[scores >= 80]

    print("Scores >= 80:", high_scores)


if __name__ == "__main__":
    main()
