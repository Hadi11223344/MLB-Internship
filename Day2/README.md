
# Day 2 - File Handling, JSON, NumPy & Pandas

## Overview

Day 2 focused on file handling, structured data storage,
numerical computing, and dataset analysis using Python.

## Topics Covered

### 1. File Handling

- Opening and closing files.
- Reading, writing, and appending data.
- File modes: r, w, a.
- Using context managers with `with`.
- Counting lines.
- Handling file-related exceptions.

### 2. JSON

- Understanding JSON structure.
- Python dictionaries and JSON objects.
- Serialization using json.dump() and json.dumps().
- Deserialization using json.load() and json.loads().
- Reading and updating student records.

### 3. NumPy

- Creating 1D and 2D arrays.
- Array properties: shape, ndim, size, dtype.
- Indexing and slicing.
- Element-wise arithmetic.
- Mathematical operations.
- Reshaping arrays.
- Boolean filtering.

### 4. Pandas

- Series and DataFrames.
- Reading CSV datasets.
- Exploring datasets using head(), tail(), and info().
- Identifying missing values.
- Selecting columns and filtering rows.
- Calculating summary statistics.

## Projects

### Student Record Management System

Upgraded the previous in-memory application into a
persistent JSON-backed application.

Implemented:
- Add student.
- View students.
- Search student.
- Update student.
- Delete student.
- Save and load records using JSON.
- Validate user input.

### Student Performance Analysis

Used Pandas and NumPy to analyze student performance.

Implemented:
- Dataset loading.
- Dataset inspection.
- Missing-value detection.
- Missing-value imputation using column medians.
- Subject-wise average marks.
- Top five performing students.
- Below-average student identification.
- Performance categories.
- Exporting the processed dataset to CSV.

## File Handling and JSON

File handling provides the ability to read and write
information on disk.

JSON provides a structured format for storing data.

Together, they allow Python applications to preserve
structured information between program executions.

## Dataset Insights

The student dataset is synthetic and contains 30 records.

The analysis calculates subject averages, student averages,
top-performing students, and students below the overall average.

Missing values are intentionally included to demonstrate
data cleaning.

## Challenges and Solutions

| Challenge | Solution |
|---|---|
| Files may not exist | Handle FileNotFoundError |
| Resources may remain open | Use the with statement |
| JSON data must be converted | Use json.dump() and json.load() |
| Invalid user input | Validate input and handle exceptions |
| Numerical operations | Use NumPy arrays |
| Missing dataset values | Detect and impute missing values |
| Dataset inspection | Use Pandas DataFrame methods |

## Running the Projects

From the repository root:

```bash
python -m pip install -r Day-2/requirements.txt

python Day-2/File_Handling/main.py
python Day-2/JSON/main.py
python Day-2/NumPy/main.py
python Day-2/Pandas/main.py
python Day-2/Student_Record_Management/main.py
python Day-2/Student_Performance_Analysis/main.py
```

## Future Improvements

- Add automated unit tests.
- Use SQLite or PostgreSQL for persistent records.
- Add data visualizations.
- Explore advanced Pandas operations.
- Prepare datasets for machine learning pipelines.
