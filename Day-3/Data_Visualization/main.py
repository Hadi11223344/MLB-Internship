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


def load_data():
    return pd.read_csv(DATA_PATH)


# --------------------------------------------------
# 1. BAR CHART — Average score per student
# --------------------------------------------------

def create_bar_chart(df):

    plt.figure(figsize=(12, 7))

    sns.barplot(
        data=df,
        x="Average_Score",
        y="Name",
        hue="Name",
        legend=False,
        palette="viridis"
    )

    plt.title("Average Score per Student")
    plt.xlabel("Average Score")
    plt.ylabel("Student")

    plt.tight_layout()

    plt.savefig(CHART_DIR / "student_average_bar.png", dpi=300)
    plt.show()


# --------------------------------------------------
# 2. HISTOGRAM — Distribution of average scores
# --------------------------------------------------

def create_histogram(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df,
        x="Average_Score",
        bins=10,
        kde=True
    )

    plt.title("Distribution of Student Average Scores")
    plt.xlabel("Average Score")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig(CHART_DIR / "average_score_histogram.png", dpi=300)
    plt.show()


# --------------------------------------------------
# 3. SCATTER PLOT — Python vs Machine Learning
# --------------------------------------------------

def create_scatter_plot(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Python",
        y="Machine_Learning",
        hue="Performance",
        s=100
    )

    plt.title("Python vs Machine Learning Scores")
    plt.xlabel("Python Score")
    plt.ylabel("Machine Learning Score")

    plt.tight_layout()

    plt.savefig(CHART_DIR / "python_vs_ml_scatter.png", dpi=300)
    plt.show()

    correlation = df["Python"].corr(df["Machine_Learning"])

    print("\nPython vs Machine Learning Correlation:")
    print(round(correlation, 3))


# --------------------------------------------------
# 4. PIE CHART — Performance category distribution
# --------------------------------------------------

def create_pie_chart(df):

    performance_counts = df["Performance"].value_counts()

    plt.figure(figsize=(8, 8))

    plt.pie(
        performance_counts,
        labels=performance_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Student Performance Distribution")

    plt.tight_layout()

    plt.savefig(CHART_DIR / "performance_distribution_pie.png", dpi=300)
    plt.show()


# --------------------------------------------------
# 5. BOX PLOT — Subject score distributions
# --------------------------------------------------

def create_box_plot(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df[SUBJECTS]
    )

    plt.title("Score Distribution Across Subjects")
    plt.ylabel("Score")
    plt.xlabel("Subjects")

    plt.tight_layout()

    plt.savefig(CHART_DIR / "subject_scores_boxplot.png", dpi=300)
    plt.show()


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    df = load_data()

    create_bar_chart(df)
    create_histogram(df)
    create_scatter_plot(df)
    create_pie_chart(df)
    create_box_plot(df)

    print("\nAll charts generated successfully!")


if __name__ == "__main__":
    main()