from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "Dataset" / "student_performance.csv"
OUTPUT_PATH = BASE_DIR / "cleaned_student_performance.csv"

SUBJECTS = [
    "Python",
    "Machine_Learning",
    "Statistics",
    "Data_Preprocessing"
]


def load_data():
    df = pd.read_csv(DATASET_PATH)

    # Introduce a few controlled data-quality issues for practice
    df.loc[2, "Statistics"] = np.nan
    df.loc[7, "Python"] = np.nan
    df.loc[10, "Attendance"] = np.nan

    # Duplicate an existing record
    df = pd.concat([df, df.iloc[[16]]], ignore_index=True)

    # Introduce a column-name inconsistency
    df.rename(columns={"Machine_Learning": "Machine Learning"}, inplace=True)

    return df


def inspect_data(df):
    print("\n--- Dataset Preview ---")
    print(df.head())

    print("\n--- Dataset Info ---")
    df.info()

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Duplicate Rows ---")
    print(df.duplicated().sum())


def clean_data(df):
    # 1. Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # 2. Remove duplicate records
    df = df.drop_duplicates().copy()

    # 3. Convert numerical columns to numeric types
    numerical_columns = SUBJECTS + ["Attendance"]

    for column in numerical_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # 4. Handle missing numerical values using median
    for column in numerical_columns:
        df[column] = df[column].fillna(df[column].median())

    # 5. Create Average_Score
    df["Average_Score"] = df[SUBJECTS].mean(axis=1)

    # 6. Assign performance categories
    conditions = [
        df["Average_Score"] >= 90,
        df["Average_Score"] >= 80,
        df["Average_Score"] >= 70
    ]

    categories = [
        "Excellent",
        "Good",
        "Average"
    ]

    df["Performance"] = np.select(
        conditions,
        categories,
        default="Needs Improvement"
    )

    # 7. Sort students by average score
    df = df.sort_values(
        by="Average_Score",
        ascending=False
    ).reset_index(drop=True)

    return df


def main():
    df = load_data()

    inspect_data(df)

    cleaned_df = clean_data(df)

    print("\n--- Cleaned Dataset ---")
    print(cleaned_df.head())

    print("\n--- Missing Values After Cleaning ---")
    print(cleaned_df.isnull().sum())

    cleaned_df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nCleaned dataset saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()