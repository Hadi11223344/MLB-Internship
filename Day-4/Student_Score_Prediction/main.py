
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT / "Day-4" / "Dataset" / "student_performance.csv"
GRAPH_DIR = ROOT / "Day-4" / "Graphs"

FEATURES = ["Attendance"]
TARGET = "Average_Score"


def load_data():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)

    return df


def prepare_data(df):
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\n========== MODEL EVALUATION ==========")

    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"R2 Score: {r2:.4f}")

    comparison = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": predictions
    })

    comparison["Absolute_Error"] = (
        comparison["Actual"] - comparison["Predicted"]
    ).abs()

    comparison = comparison.round(2)

    print("\nActual vs Predicted:")
    print(comparison.to_string(index=False))

    return predictions, comparison


def visualize_predictions(y_test, predictions):
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_test,
        predictions,
        alpha=0.7
    )

    # Perfect prediction reference line
    min_value = min(y_test.min(), predictions.min())
    max_value = max(y_test.max(), predictions.max())

    plt.plot(
        [min_value, max_value],
        [min_value, max_value],
        linestyle="--"
    )

    plt.xlabel("Actual Average Score")
    plt.ylabel("Predicted Average Score")
    plt.title("Actual vs Predicted Student Scores")

    plt.tight_layout()

    output_path = GRAPH_DIR / "actual_vs_predicted.png"

    plt.savefig(output_path, dpi=300)
    plt.show()

    print(f"\nGraph saved at: {output_path}")


def main():
    df = load_data()

    X_train, X_test, y_train, y_test = prepare_data(df)

    print("\nTraining Samples:", len(X_train))
    print("Testing Samples:", len(X_test))

    model = train_model(X_train, y_train)

    print("\nModel trained successfully!")

    print("\nModel Coefficient:", model.coef_[0])
    print("Model Intercept:", model.intercept_)

    predictions, comparison = evaluate_model(
        model,
        X_test,
        y_test
    )

    visualize_predictions(y_test, predictions)

    print("\nStudent Score Prediction System Completed!")


if __name__ == "__main__":
    main()
