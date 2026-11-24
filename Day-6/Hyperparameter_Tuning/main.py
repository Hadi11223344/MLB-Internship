
import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    GridSearchCV
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    make_scorer
)


def load_data():
    """Load the Breast Cancer Wisconsin dataset."""

    dataset = load_breast_cancer(as_frame=True)

    X = dataset.data
    y = dataset.target

    return X, y, dataset


def split_data(X, y):
    """Create stratified training and testing sets."""

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def create_pipeline():
    """Create preprocessing and classification pipeline."""

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ])

    return pipeline


def tune_model(pipeline, X_train, y_train):
    """Perform hyperparameter tuning using GridSearchCV."""

    param_grid = {
        "model__C": [0.001, 0.01, 0.1, 1, 10, 100]
    }

    cv_strategy = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    malignant_recall_scorer = make_scorer(
        recall_score,
        pos_label=0
    )

    scoring = {
        "accuracy": "accuracy",
        "precision_macro": "precision_macro",
        "recall_macro": "recall_macro",
        "f1_macro": "f1_macro",
        "malignant_recall": malignant_recall_scorer
    }

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        scoring=scoring,
        refit="malignant_recall",
        cv=cv_strategy,
        n_jobs=-1,
        verbose=1,
        return_train_score=True
    )

    grid_search.fit(X_train, y_train)

    return grid_search


def display_results(grid_search):
    """Display tuning results."""

    print("\n" + "=" * 60)
    print("GRID SEARCH RESULTS")
    print("=" * 60)

    print("\nBest Parameters:")
    print(grid_search.best_params_)

    print("\nBest Cross-Validation Malignant Recall:")
    print(grid_search.best_score_)

    results = pd.DataFrame(grid_search.cv_results_)

    selected_columns = [
        "param_model__C",
        "mean_test_accuracy",
        "mean_test_precision_macro",
        "mean_test_recall_macro",
        "mean_test_f1_macro",
        "mean_test_malignant_recall",
        "std_test_malignant_recall"
    ]

    results = results[selected_columns].sort_values(
        by="mean_test_malignant_recall",
        ascending=False
    )

    print("\nAll Hyperparameter Results:")
    print(results.to_string(index=False))


def evaluate_model(model, X_test, y_test):
    """Evaluate the tuned model on the untouched test set."""

    y_pred = model.predict(X_test)

    print("\n" + "=" * 60)
    print("FINAL TUNED MODEL TEST EVALUATION")
    print("=" * 60)

    print("\nAccuracy:")
    print(accuracy_score(y_test, y_pred))

    print("\nPrecision (Macro):")
    print(precision_score(y_test, y_pred, average="macro"))

    print("\nRecall (Macro):")
    print(recall_score(y_test, y_pred, average="macro"))

    print("\nF1-Score (Macro):")
    print(f1_score(y_test, y_pred, average="macro"))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["malignant", "benign"],
            digits=4
        )
    )

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


def main():

    X, y, dataset = load_data()

    X_train, X_test, y_train, y_test = split_data(X, y)

    pipeline = create_pipeline()

    grid_search = tune_model(
        pipeline,
        X_train,
        y_train
    )

    display_results(grid_search)

    evaluate_model(
        grid_search.best_estimator_,
        X_test,
        y_test
    )


if __name__ == "__main__":
    main()
