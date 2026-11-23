# Day 5 – Model Evaluation & Classification

## Overview
Learned fundamental model evaluation metrics and classification algorithms using the Iris dataset.

## Topics Covered
- Classification vs Regression
- Training vs Testing Performance
- Overfitting and Underfitting
- Accuracy, Precision, Recall, and F1-Score
- Confusion Matrix
- Logistic Regression
- Decision Trees
- Gini Impurity, Entropy, and Information Gain

## Projects
### Iris Flower Classification
Built classification models to predict Iris flower species using the four flower features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Models trained:
- Logistic Regression (with StandardScaler)
- Decision Tree Classifier

## Model Results

| Metric | Logistic Regression | Decision Tree |
|---|---:|---:|
| Accuracy | 93.33% | 96.67% |
| Macro Precision | 93.33% | 96.97% |
| Macro Recall | 93.33% | 96.67% |
| Macro F1-Score | 93.33% | 96.66% |

Both models were evaluated using the same train-test split.

## Observations
- Setosa was correctly classified by both models.
- Petal length and petal width were highly informative features.
- The Decision Tree achieved one additional correct prediction on the test set.
- Results on a small test set should not be used to conclude that one model is universally better.

## Tools
Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

---
**ML Bench – Winter Talent Development Program 2026**