# ============================================================
# DAY 6 - BASELINE CLASSIFICATION MODEL
# Breast Cancer Wisconsin Dataset
# Logistic Regression
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

def load_dataset():

    dataset = load_breast_cancer(as_frame=True)

    X = dataset.data.copy()
    y = dataset.target.copy()

    return X, y, dataset


# ============================================================
# 2. SPLIT DATASET
# ============================================================

def split_dataset(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


# ============================================================
# 3. BUILD MODEL PIPELINE
# ============================================================

def build_model():

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ])

    return pipeline


# ============================================================
# 4. TRAIN MODEL
# ============================================================

def train_model(pipeline, X_train, y_train):

    pipeline.fit(X_train, y_train)

    return pipeline


# ============================================================
# 5. EVALUATE MODEL
# ============================================================

def evaluate_model(model, X_test, y_test, dataset):

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 60)
    print("BASELINE LOGISTIC REGRESSION")
    print("=" * 60)

    print(f"\nAccuracy: {accuracy:.4f}")
    print(f"Accuracy (%): {accuracy * 100:.2f}%")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred,
            target_names=dataset.target_names,
            digits=4
        )
    )

    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    return y_pred, cm, accuracy


# ============================================================
# 6. VISUALIZE CONFUSION MATRIX
# ============================================================

def plot_confusion_matrix(cm, dataset):

    labels = dataset.target_names

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels
    )

    plt.title("Baseline Logistic Regression - Confusion Matrix")
    plt.xlabel("Predicted Diagnosis")
    plt.ylabel("Actual Diagnosis")

    plt.tight_layout()

    # Save graph relative to this script's directory structure
    project_root = Path(__file__).resolve().parents[1]

    graph_dir = project_root / "Graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)

    graph_path = graph_dir / "baseline_confusion_matrix.png"

    plt.savefig(graph_path, dpi=300)

    print(f"\nConfusion matrix saved to: {graph_path}")

    plt.show()


# ============================================================
# 7. MAIN
# ============================================================

def main():

    X, y, dataset = load_dataset()

    X_train, X_test, y_train, y_test = split_dataset(X, y)

    print("Dataset Shape:", X.shape)

    print("\nTraining Set Shape:", X_train.shape)
    print("Testing Set Shape:", X_test.shape)

    print("\nTraining Target Distribution:")
    print(y_train.value_counts())

    print("\nTesting Target Distribution:")
    print(y_test.value_counts())

    pipeline = build_model()

    pipeline = train_model(
        pipeline,
        X_train,
        y_train
    )

    y_pred, cm, accuracy = evaluate_model(
        pipeline,
        X_test,
        y_test,
        dataset
    )

    plot_confusion_matrix(cm, dataset)


if __name__ == "__main__":
    main()