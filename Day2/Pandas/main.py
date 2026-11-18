
"""
Day 2 - Pandas Fundamentals
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

# Use the original CSV dataset from the analysis project.
DATA_FILE = (
    BASE_DIR.parent
    / "Student_Performance_Analysis"
    / "students.csv"
)


def main():

    # 1. Load dataset

    df = pd.read_csv(DATA_FILE)

    print("--- First Five Rows ---")
    print(df.head())

    print("\n--- Last Five Rows ---")
    print(df.tail())

    # 2. Dataset information

    print("\n--- Dataset Information ---")
    df.info()

    # 3. Dataset dimensions

    print("\n--- Dataset Shape ---")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # 4. Column names

    print("\n--- Column Names ---")
    print(df.columns.tolist())

    # 5. Missing values

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # 6. Summary statistics

    print("\n--- Statistical Summary ---")
    print(df.describe())

    # 7. Select columns

    print("\n--- Selected Columns ---")
    print(df[["name", "math", "science"]].head())

    # 8. Filter records

    print("\n--- Students with Math Marks >= 80 ---")

    high_math_scores = df[df["math"] >= 80]

    print(high_math_scores[["name", "math"]])

    # 9. Calculate subject averages

    subjects = ["math", "science", "english", "computer"]

    print("\n--- Average Marks ---")
    print(df[subjects].mean())

    # 10. Total number of students

    print("\nTotal Students:", len(df))


if __name__ == "__main__":
    main()
