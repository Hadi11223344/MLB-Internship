
import joblib
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, recall_score, make_scorer


def train_final_model():

    dataset = load_breast_cancer(as_frame=True)

    X = dataset.data
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ])

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

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        scoring={
            "accuracy": "accuracy",
            "malignant_recall": malignant_recall_scorer,
            "f1_macro": "f1_macro"
        },
        refit="malignant_recall",
        cv=cv_strategy,
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    print("\nBest Parameters:")
    print(grid_search.best_params_)

    print("\nBest CV Malignant Recall:")
    print(grid_search.best_score_)

    y_pred = best_model.predict(X_test)

    print("\nTest Classification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["malignant", "benign"],
            digits=4
        )
    )

    print("\nTest Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    joblib.dump(
        best_model,
        "../../Day-6/Breast_Cancer_Prediction/breast_cancer_model.pkl"
    )

    print("\nModel saved successfully!")

    return best_model, X_test, y_test


def demonstrate_prediction(model, X_test, y_test):

    sample = X_test.iloc[[0]]

    actual_label = y_test.iloc[0]
    prediction = model.predict(sample)[0]
    probabilities = model.predict_proba(sample)[0]

    class_names = {
        0: "malignant",
        1: "benign"
    }

    print("\n" + "=" * 60)
    print("SAMPLE PREDICTION DEMONSTRATION")
    print("=" * 60)

    print("\nActual Class:")
    print(class_names[actual_label])

    print("\nPredicted Class:")
    print(class_names[prediction])

    print("\nPrediction Probabilities:")

    for class_index, class_name in class_names.items():

        print(
            f"{class_name}: "
            f"{probabilities[class_index]:.10f}"
        )

    print("\nPrediction Correct:")

    print(actual_label == prediction)

def main():

    model, X_test, y_test = train_final_model()

    demonstrate_prediction(model, X_test,y_test)


if __name__ == "__main__":
    main()
