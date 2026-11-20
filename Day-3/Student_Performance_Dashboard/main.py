from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "cleaned_student_performance.csv"
CHART_DIR = BASE_DIR / "Charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

SUBJECTS = [
    "Python",
    "Machine_Learning",
    "Statistics",
    "Data_Preprocessing"
]

sns.set_theme(style="whitegrid")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

def load_data():
    return pd.read_csv(DATA_PATH)


# --------------------------------------------------
# BASIC DATASET INFORMATION
# --------------------------------------------------

def dataset_overview(df):

    print("\n" + "=" * 50)
    print("STUDENT PERFORMANCE DASHBOARD")
    print("=" * 50)

    print(f"\nTotal Students: {len(df)}")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nPerformance Category Counts:")
    print(df["Performance"].value_counts())


# --------------------------------------------------
# SUBJECT ANALYSIS
# --------------------------------------------------

def subject_analysis(df):

    subject_averages = df[SUBJECTS].mean()

    print("\n--- Subject Class Averages ---")
    print(subject_averages.round(2))

    highest_subject = subject_averages.idxmax()

    highest_average = subject_averages.max()

    print(
        f"\nHighest Performing Subject: {highest_subject}"
    )

    print(
        f"Class Average: {highest_average:.2f}"
    )

    # Subject averages chart

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=subject_averages.index,
        y=subject_averages.values
    )

    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "subject_class_averages.png",
        dpi=300
    )

    plt.show()

    return subject_averages


# --------------------------------------------------
# TOP 5 STUDENTS
# --------------------------------------------------

def top_students(df):

    top_5 = df.nlargest(5, "Average_Score")

    print("\n--- Top 5 Students ---")

    print(
        top_5[
            ["Name", "Average_Score", "Performance"]
        ].to_string(index=False)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=top_5,
        x="Average_Score",
        y="Name"
    )

    plt.title("Top 5 Performing Students")
    plt.xlabel("Average Score")
    plt.ylabel("Student")

    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "top_5_students.png",
        dpi=300
    )

    plt.show()

    return top_5


# --------------------------------------------------
# STUDENTS NEEDING IMPROVEMENT
# --------------------------------------------------

def students_needing_improvement(df):

    students = df[
        df["Performance"] == "Needs Improvement"
    ]

    print("\n--- Students Needing Improvement ---")

    if students.empty:
        print("No students in this category.")
    else:
        print(
            students[
                ["Name", "Average_Score", "Performance"]
            ].to_string(index=False)
        )

    return students


# --------------------------------------------------
# PERFORMANCE CATEGORY ANALYSIS
# --------------------------------------------------

def performance_analysis(df):

    counts = df["Performance"].value_counts()

    print("\n--- Performance Distribution ---")

    print(counts)

    print("\nPercentage Distribution:")

    percentages = (
        df["Performance"].value_counts(normalize=True) * 100
    )

    print(percentages.round(2))

    return percentages


# --------------------------------------------------
# AUTOMATIC INSIGHTS
# --------------------------------------------------

def generate_insights(df, subject_averages, top_5, students):

    print("\n" + "=" * 50)
    print("KEY INSIGHTS")
    print("=" * 50)

    # Insight 1

    best_subject = subject_averages.idxmax()

    print(
        f"\n1. {best_subject} has the highest class average "
        f"({subject_averages.max():.2f})."
    )

    # Insight 2

    weakest_subject = subject_averages.idxmin()

    print(
        f"\n2. {weakest_subject} has the lowest class average "
        f"({subject_averages.min():.2f})."
    )

    # Insight 3

    improvement_percentage = (
        len(students) / len(df) * 100
    )

    print(
        f"\n3. {len(students)} students "
        f"({improvement_percentage:.2f}%) "
        "fall into the Needs Improvement category."
    )

    # Additional insight

    print(
        f"\n4. The Top 5 students have an average score of "
        f"{top_5['Average_Score'].mean():.2f}."
    )


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    df = load_data()

    dataset_overview(df)

    subject_averages = subject_analysis(df)

    top_5 = top_students(df)

    students = students_needing_improvement(df)

    performance_analysis(df)

    generate_insights(
        df,
        subject_averages,
        top_5,
        students
    )

    print("\n" + "=" * 50)
    print("DASHBOARD ANALYSIS COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()