
# Day-6/Dataset_Exploration/main.py

import pandas as pd
from sklearn.datasets import load_breast_cancer


def load_dataset():
    """Load the Breast Cancer Wisconsin dataset into a DataFrame."""

    dataset = load_breast_cancer(as_frame=True)

    df = dataset.frame.copy()

    return df, dataset


def explore_dataset(df, dataset):
    """Perform basic exploratory analysis."""

    print("=" * 60)
    print("BREAST CANCER DATASET EXPLORATION")
    print("=" * 60)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nTarget Distribution:")
    print(df["target"].value_counts())

    print("\nTarget Distribution (%):")
    print(df["target"].value_counts(normalize=True) * 100)

    print("\nTarget Mapping:")
    for index, class_name in enumerate(dataset.target_names):
        print(f"{index} = {class_name}")


def main():
    df, dataset = load_dataset()

    explore_dataset(df, dataset)


if __name__ == "__main__":
    main()
