"""
data_manager.py
----------------
Handles saving and loading student records to/from a JSON file.

Demonstrates:
- Modules (json, os from the standard library)
- File input/output operations
- Core data structures (dict, list)
- Control flow (try/except, if)
"""

import json
import os

from student import Student

DATA_FILE = "students_data.json"


def load_students(filepath=DATA_FILE):
    """
    Load student records from a JSON file into a dict
    keyed by roll number. Returns an empty dict if the
    file doesn't exist yet or is empty/corrupted.
    """
    if not os.path.exists(filepath):
        return {}

    try:
        with open(filepath, "r") as f:
            raw_data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

    students = {}
    for roll, record in raw_data.items():
        students[roll] = Student.from_dict(record)
    return students


def save_students(students, filepath=DATA_FILE):
    """
    Save a dict of {roll_number: Student} objects to a JSON file.
    """
    serializable = {roll: student.to_dict() for roll, student in students.items()}
    with open(filepath, "w") as f:
        json.dump(serializable, f, indent=4)
