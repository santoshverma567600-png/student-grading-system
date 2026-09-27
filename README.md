# Student Grade Management System

A command-line application to manage student records: add students, record
subject-wise marks, calculate averages and letter grades, rank students,
and persist data between sessions using a local JSON file.

This project is written in pure Python (no external libraries required) and
runs entirely from the terminal.

## Features

- Add a student with roll number, name, and marks for any number of subjects
- View all student records
- Search for a student by roll number
- Update or add marks for an existing student
- Delete a student record
- Rank all students by their average score (highest first)
- Automatic letter grading (A+, A, B, C, D, F) based on average marks
- Data is saved automatically to `students_data.json` after every action

## Project Structure

```
student-grade-system/
├── main.py              # CLI entry point and menu logic
├── student.py            # Student class (OOP: attributes, methods, grading logic)
├── data_manager.py       # Handles saving/loading records to/from JSON
├── requirements.txt      # Python dependencies (none external)
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.8 or higher installed on your system
- No external packages required (standard library only)

To check your Python version:

```bash
python --version
```

(On some systems you may need to use `python3` instead of `python`.)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/{your-username}/{repo-name}.git
cd {repo-name}
```

### 2. Create a virtual environment (recommended)

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

This project has no external dependencies, but the command is included for
completeness (and in case you extend the project later):

```bash
pip install -r requirements.txt
```

## Running the Project

From the project root, with your virtual environment activated:

```bash
python main.py
```

You will see a menu like this:

```
==================================================
         STUDENT GRADE MANAGEMENT SYSTEM
==================================================
1. Add Student
2. View All Students
3. Search Student by Roll Number
4. Update Student Marks
5. Delete Student
6. Rank Students by Average
7. Exit
--------------------------------------------------
Enter your choice (1-7):
```

Enter a number (1–7) and follow the on-screen prompts. All data is
automatically saved to `students_data.json` in the project folder after
every operation, so your records persist the next time you run the program.

## Example Usage

```
Enter your choice (1-7): 1
Enter Roll Number: 101
Enter Student Name: Alice
How many subjects? 2
  Subject 1 name: Math
  Marks in Math: 85
  Subject 2 name: Science
  Marks in Science: 92

Student 'Alice' added successfully!
```

## Grading Scale

| Average Marks | Grade |
|----------------|-------|
| 90 - 100       | A+    |
| 80 - 89        | A     |
| 70 - 79        | B     |
| 60 - 69        | C     |
| 50 - 59        | D     |
| Below 50       | F     |

## Notes

- Data is stored in plain JSON (`students_data.json`) so it's human-readable
  and easy to inspect or back up.
- The `students_data.json` file is excluded from version control via
  `.gitignore` — it will be created automatically the first time you run
  the program.
