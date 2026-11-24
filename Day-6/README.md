# Day 6 – Model Evaluation, Cross-Validation & Hyperparameter Tuning

## Overview

Day 6 focused on model evaluation, generalization, cross-validation, learning curves, and hyperparameter optimization using the Breast Cancer Wisconsin Diagnostic dataset.

The objective was to develop a reliable classification workflow, evaluate Logistic Regression, and systematically tune its hyperparameters.

## Dataset

The Breast Cancer Wisconsin dataset provided by Scikit-learn was used.

- Samples: 569
- Features: 30
- Classes: 2
- Malignant: 212
- Benign: 357

Target encoding:

- `0` — Malignant
- `1` — Benign

## Topics Covered

- Training vs Testing Performance
- Underfitting and Overfitting
- Cross-Validation
- Stratified K-Fold
- Learning Curves
- Accuracy, Precision, Recall, and F1-Score
- Confusion Matrix
- Hyperparameters and Regularization
- GridSearchCV
- Model Selection
- Pipeline-based Preprocessing

## Exploratory Data Analysis

Performed dataset exploration and visualization, including:

- Dataset structure and statistical summaries
- Target distribution
- Feature distributions
- Class-wise feature distributions
- Outlier analysis using boxplots
- Feature correlation analysis
- Correlation with the encoded target

## Baseline Model

A Logistic Regression classification pipeline was implemented using:

- StandardScaler
- Logistic Regression

The model was evaluated using a stratified train-test split.

### Baseline Test Results

| Metric | Score |
|---|---:|
| Accuracy | 98.25% |
| Malignant Precision | 97.62% |
| Malignant Recall | 97.62% |
| Malignant F1-Score | 97.62% |
| Benign Precision | 98.61% |
| Benign Recall | 98.61% |
| Benign F1-Score | 98.61% |

## Cross-Validation

The model was evaluated using stratified 5-fold cross-validation.

Cross-validation metrics included:

- Accuracy
- Macro Precision
- Macro Recall
- Macro F1-Score
- Malignant Recall

Mean cross-validation accuracy: **97.80%**

Mean cross-validation malignant recall: **96.47%**

## Learning Curves

Learning curves were used to analyze training and validation performance as the training dataset size increased.

The experiment helped examine model generalization, performance variability, and the potential benefits of additional training data.

## Hyperparameter Tuning

GridSearchCV was used to optimize the Logistic Regression regularization parameter `C`.

Candidate values:

- 0.001
- 0.01
- 0.1
- 1
- 10
- 100

The search used stratified five-fold cross-validation and selected the configuration based on malignant recall.

### Best Configuration

```python
C = 1
```

Mean cross-validation malignant recall:

**96.47%**

## Final Tuned Model Results

| Metric | Score |
|---|---:|
| Accuracy | 98.25% |
| Malignant Precision | 97.62% |
| Malignant Recall | 97.62% |
| Malignant F1-Score | 97.62% |
| Benign Precision | 98.61% |
| Benign Recall | 98.61% |
| Benign F1-Score | 98.61% |

### Confusion Matrix

```text
[[41, 1],
 [ 1, 71]]
```

- 41 malignant samples correctly classified.
- 1 malignant sample classified as benign.
- 1 benign sample classified as malignant.
- 71 benign samples correctly classified.

## Key Observations

- Logistic Regression achieved strong classification performance on the test set.
- Malignant recall was explicitly considered during model selection.
- Stratified cross-validation provided a more robust estimate of performance than a single train-test split.
- GridSearchCV selected `C = 1`, the same regularization configuration used by the baseline model.
- Hyperparameter tuning did not change the test-set performance in this experiment.
- Feature scaling was incorporated within a Pipeline to prevent preprocessing leakage during cross-validation.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Disclaimer

This project is educational and demonstrates machine learning classification and evaluation techniques. It is not intended for clinical diagnosis or medical decision-making.

---

**ML Bench – Winter Talent Development Program 2026**
