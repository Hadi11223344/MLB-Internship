
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "Day-4" / "Dataset" / "student_performance.csv"

FEATURES = ["Attendance"]
TARGET = "Average_Score"


def main():
    df = pd.read_csv(DATA_PATH)

    print("Dataset Shape:", df.shape)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDataset Preview:\n", df.head())

    # Select features and target
    X = df[FEATURES]
    y = df[TARGET]

    # Split BEFORE fitting transformations
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Demonstrate scaling correctly
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\nScaled Training Features:")
    print(X_train_scaled[:5])

    print("\nScaled Testing Features:")
    print(X_test_scaled[:5])

    print("\nPreprocessing completed!")


if __name__ == "__main__":
    main()
