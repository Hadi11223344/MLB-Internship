
"""
Day 2 - File Handling Practice
"""

from pathlib import Path

# Store the text file in the same folder as this Python script.
BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "notes.txt"


def write_file():
    """Create a file and write initial content."""

    lines = [
        "Welcome to Day 2 of ML Bench Internship.",
        "Today we are learning Python File Handling.",
        "Files allow data to persist after program termination."
    ]

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print("File created and data written successfully.")


def read_file():
    """Read and display the complete file."""

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            content = file.read()

        print("\n--- File Contents ---")
        print(content)

    except FileNotFoundError:
        print("Error: File does not exist.")


def append_file():
    """Append additional information without deleting old content."""

    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write("We will also learn JSON, NumPy and Pandas.\n")

    print("New information appended successfully.")


def count_lines():
    """Count the number of lines in the file."""

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            line_count = sum(1 for line in file)

        print(f"Total number of lines: {line_count}")

    except FileNotFoundError:
        print("Error: File does not exist.")


def main():
    write_file()
    read_file()

    append_file()
    read_file()

    count_lines()


if __name__ == "__main__":
    main()
