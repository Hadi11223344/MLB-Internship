# Day 3 — Data Cleaning, Visualization & Student Performance Dashboard

## Overview

Day 3 focused on developing practical data preparation and analytical skills using **Pandas, NumPy, Matplotlib, and Seaborn**. Before building Machine Learning models, datasets must be inspected, cleaned, analyzed, and visualized to understand their quality, distributions, and patterns.

This day involved applying data cleaning techniques, generating visualizations, and building a small analytical dashboard using a student performance dataset.

## Learning Objectives

- Identify and handle missing values.
- Detect and remove duplicate records.
- Rename and standardize column names.
- Convert columns to appropriate data types.
- Create new features using Pandas.
- Sort and filter datasets.
- Understand data visualization and its importance.
- Use Matplotlib and Seaborn for visualization.
- Analyze distributions, relationships, and patterns.
- Extract insights from a dataset through a dashboard.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
Day-3/
├── Data_Cleaning/
│   └── main.py
├── Data_Visualization/
│   └── main.py
├── Student_Performance_Dashboard/
│   └── main.py
├── Dataset/
│   └── student_performance.csv
├── Charts/
├── cleaned_student_performance.csv
├── README.md
└── requirements.txt
```

## 1. Data Cleaning with Pandas

Using the `student_performance.csv` dataset, we implemented a data cleaning workflow.

### Tasks Performed

- Inspected the dataset.
- Identified missing values.
- Introduced controlled missing values for cleaning practice.
- Detected and removed duplicate records.
- Renamed and standardized column names.
- Converted numerical columns to appropriate data types.
- Handled missing numerical values using median imputation.
- Created a new column named `Average_Score`.
- Created a new column named `Performance`.
- Sorted records based on average performance.
- Exported the cleaned dataset.

### Feature Creation

#### Average_Score

Calculated the average score across the following subjects:

- Python
- Machine Learning
- Statistics
- Data Preprocessing

#### Performance Classification

| Average Score | Performance |
|---|---|
| >= 90 | Excellent |
| >= 80 and < 90 | Good |
| >= 70 and < 80 | Average |
| < 70 | Needs Improvement |

### Output

The cleaned dataset was saved as:

`cleaned_student_performance.csv`

## 2. Data Visualization

Explored data visualization using Matplotlib and Seaborn to understand student performance, distributions, comparisons, and relationships.

### Visualizations Created

#### 1. Student Average Score — Bar Chart

- Visualized average marks for each student.
- Compared student performance.
- Identified students with relatively higher and lower scores.

#### 2. Average Score Distribution — Histogram

- Examined the distribution of student average scores.
- Observed the spread and concentration of scores.
- Used histogram bins and KDE for distribution visualization.

#### 3. Python vs Machine Learning — Scatter Plot

- Investigated the relationship between Python and Machine Learning scores.
- Visualized observations across performance categories.
- Calculated Pearson correlation to examine linear association.

#### 4. Performance Distribution — Pie Chart

- Visualized the proportion of students across performance categories.
- Examined the composition of Excellent, Good, Average, and Needs Improvement students.

#### 5. Subject Scores — Box Plot

- Compared score distributions across subjects.
- Examined medians, variability, spread, and potential outliers.

## 3. Student Performance Dashboard

Developed a small analytical dashboard using Pandas and Seaborn/Matplotlib to summarize the dataset and generate useful insights.

### Dashboard Analysis

- Total number of students.
- Dataset dimensions.
- Average score by subject.
- Highest-performing subject.
- Lowest-performing subject.
- Top 5 students based on `Average_Score`.
- Students classified as `Needs Improvement`.
- Performance category distribution.
- Performance category percentages.
- Key analytical insights.

### Additional Dashboard Visualizations

- Subject Class Average Chart
- Top 5 Students Chart

## 4. Data Analysis Techniques Practiced

- DataFrame inspection
- Missing value detection
- Median imputation
- Duplicate detection and removal
- Column renaming
- Data type conversion
- Feature creation
- Conditional classification using NumPy
- Sorting and filtering
- Statistical summaries
- Value counts and percentage distributions
- `nlargest()`
- `idxmax()` and `idxmin()`
- Pearson correlation
- Data visualization

## 5. Key Concepts Learned

- Data cleaning is an essential step before Machine Learning.
- Missing values require thoughtful handling rather than blindly removing records.
- Duplicate records can affect analysis and model training.
- Feature creation can help transform raw data into more informative representations.
- Histograms help understand numerical distributions.
- Bar charts are useful for categorical comparisons.
- Scatter plots help investigate relationships between numerical variables.
- Box plots help examine distributions, variability, and potential outliers.
- Pie charts can illustrate proportions across a small number of categories.
- Correlation measures association, not causation.
- Outliers are not automatically errors and require investigation.
- Analytical findings should be interpreted in context.

## 6. Deliverables

- Data cleaning script
- Cleaned dataset
- Data visualization script
- Five core visualization charts
- Student Performance Dashboard
- Subject average visualization
- Top 5 students visualization
- Analytical insights

## 7. Conclusion

Day 3 strengthened practical data preparation and exploratory analysis skills using Python's data science ecosystem. The exercises covered data cleaning, feature creation, data visualization, statistical interpretation, and dashboard-based analysis.

These skills form an essential foundation for the next stage of Machine Learning development, where datasets must be investigated, prepared, and transformed before model training.

---

**Internship Learning Progress — Day 3 Completed**

