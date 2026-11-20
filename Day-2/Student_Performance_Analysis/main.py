
"""
Day 2 - Student Performance Analysis
"""

from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "students.csv"
OUTPUT_FILE = BASE_DIR / "processed_students.csv"

SUBJECTS = ["math", "science", "english", "computer"]


def load_dataset():

    return pd.read_csv(INPUT_FILE)


def explore_dataset(df):

    print("\n--- First Five Records ---")
    print(df.head())

    print("\n--- Last Five Records ---")
    print(df.tail())

    print("\n--- Dataset Information ---")
    df.info()

    print("\n--- Dataset Shape ---")
    print(df.shape)

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Statistical Summary ---")
    print(df.describe())


def clean_dataset(df):

    # Work on a copy so the original DataFrame remains unchanged.
    cleaned_df = df.copy()

    # Remove duplicate student IDs.
    cleaned_df = cleaned_df.drop_duplicates(
        subset="student_id",
        keep="first"
    )

    # Convert numerical columns to numeric data.
    for column in SUBJECTS + ["attendance"]:

        cleaned_df[column] = pd.to_numeric(
            cleaned_df[column],
            errors="coerce"
        )

        # Replace missing values using the column median.
        median_value = cleaned_df[column].median()

        cleaned_df[column] = cleaned_df[column].fillna(
            median_value
        )

    # Ensure percentage values stay within 0-100.
    for column in SUBJECTS + ["attendance"]:
        cleaned_df[column] = cleaned_df[column].clip(0, 100)

    return cleaned_df


def calculate_subject_averages(df):

    print("\n--- Subject Average Marks ---")

    averages = df[SUBJECTS].mean()

    print(averages.round(2))

    return averages


def calculate_student_average(df):

    df["average_marks"] = df[SUBJECTS].mean(axis=1)

    return df


def find_top_students(df):

    print("\n--- Top 5 Performing Students ---")

    top_students = df.nlargest(
        5,
        "average_marks"
    )

    print(
        top_students[
            ["student_id", "name", "average_marks"]
        ].to_string(index=False)
    )

    return top_students


def find_below_average_students(df):

    overall_average = df["average_marks"].mean()

    below_average = df[
        df["average_marks"] < overall_average
    ]

    print("\n--- Below Average Students ---")
    print(
        below_average[
            ["student_id", "name", "average_marks"]
        ].to_string(index=False)
    )

    return below_average


def save_processed_dataset(df):

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"\nProcessed dataset saved to: {OUTPUT_FILE}")


def main():

    df = load_dataset()

    explore_dataset(df)

    cleaned_df = clean_dataset(df)

    cleaned_df = calculate_student_average(cleaned_df)

    calculate_subject_averages(cleaned_df)

    find_top_students(cleaned_df)

    find_below_average_students(cleaned_df)

    print("\nTotal Students:", len(cleaned_df))

    # Add a simple performance category.
    cleaned_df["performance_band"] = np.select(
        [
            cleaned_df["average_marks"] >= 85,
            cleaned_df["average_marks"] >= 70,
            cleaned_df["average_marks"] >= 50
        ],
        [
            "Excellent",
            "Good",
            "Pass"
        ],
        default="Needs Support"
    )

    cleaned_df["average_marks"] = cleaned_df[
        "average_marks"
    ].round(2)

    save_processed_dataset(cleaned_df)


if __name__ == "__main__":
    main()
