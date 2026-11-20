# Day 4 — Data Preprocessing & Machine Learning

## Overview

Day 4 focused on preparing datasets for Machine Learning and building the first predictive model using Scikit-learn.

The objective was to understand the complete Machine Learning workflow, from selecting features and targets to training, predicting, and evaluating a Linear Regression model.

## Learning Objectives

- Understand why data preprocessing is important.
- Identify features and target variables.
- Understand categorical encoding techniques.
- Learn Standardization and Normalization.
- Perform Train-Test Split.
- Understand and avoid Data Leakage.
- Understand Regression vs Classification.
- Learn the Scikit-learn workflow.
- Train a Linear Regression model.
- Evaluate predictions using MAE, MSE and R².

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Project Structure

```text
Day-4/
├── Dataset/
│   └── student_performance.csv
├── Data_Preprocessing/
│   └── main.py
├── Linear_Regression/
│   └── main.py
├── Student_Score_Prediction/
│   └── main.py
├── Graphs/
│   └── actual_vs_predicted.png
├── README.md
└── requirements.txt
```

## 1. Data Preprocessing

- Loaded the student performance dataset.
- Selected features and target variables.
- Performed an 80/20 Train-Test Split.
- Practiced feature scaling using StandardScaler.
- Applied scaling only after splitting the data to avoid leakage.

### Feature

`Attendance`

### Target

`Average_Score`

Attendance was selected as the input feature, while Average_Score was selected as the prediction target.

The subject scores were excluded because Average_Score was directly calculated from those subjects. Using them as predictors would introduce target leakage.

## 2. Train-Test Split

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

Training data was used to learn the relationship between the feature and target, while testing data was used to evaluate model performance on unseen observations.

## 3. Linear Regression

Built a Linear Regression model using Scikit-learn.

The model learned the relationship between Attendance and Average_Score to generate predictions.

### Workflow

1. Load dataset.
2. Select features and target.
3. Split into training and testing data.
4. Train Linear Regression.
5. Generate predictions.
6. Evaluate model.
7. Visualize Actual vs Predicted values.

## 4. Evaluation Metrics

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

### Mean Squared Error (MSE)

Measures the average squared prediction error and penalizes larger errors more heavily.

### R² Score

Evaluates how well the model explains variation in the target compared with a mean-based baseline.

### Model Results

Update these values after running the application:

| Metric | Result |
|---|---|
| MAE | Add result |
| MSE | Add result |
| R² Score | Add result |

## 5. Visualization

Generated an Actual vs Predicted scatter plot.

The visualization was used to compare model predictions against actual student scores and examine prediction errors.

The diagonal reference line represents perfect predictions.

## 6. Key Concepts Learned

- Features represent model inputs.
- Target represents the value we want to predict.
- Train-Test Split helps evaluate generalization.
- Data leakage can produce misleading model performance.
- Scaling transforms feature distributions or ranges.
- Linear Regression learns a relationship between variables.
- MAE, MSE and R² provide complementary evaluation perspectives.
- Model performance must be evaluated on unseen data.
- Correlation and prediction do not imply causation.

## 7. Observations

The model used Attendance as a predictor of Average_Score.

The results should be interpreted cautiously because the dataset is small and Attendance alone may not explain student performance sufficiently.

The purpose of this exercise was to understand the Machine Learning workflow rather than build a high-performing production model.

## Conclusion

Day 4 introduced the fundamental Machine Learning pipeline using Scikit-learn. The exercise covered preprocessing, feature selection, train-test splitting, Linear Regression, prediction, evaluation, and visualization.

This provided a practical foundation for building more sophisticated models and understanding the importance of data preparation before Machine Learning.

---

**Internship Learning Progress — Day 4 Completed**
