"""
main.py
-------
Entry point for the Student Grade Management System (CLI).

Run with:
    python main.py

Demonstrates:
- Python fundamentals (variables, syntax)
- Input/Output operations (input(), print(), f-strings)
- Control flow statements (if/elif/else, while, for, break, continue)
- Functions (modular design, default/keyword usage)
- Type conversion (str -> int/float and back)
- Core data structures (dict of Student objects, lists for ranking)
- Array-style structure (sorted list built from dict values)
- Object Oriented Programming (Student class from student.py)
- Modules (data_manager.py, student.py imported as local modules)
"""

from student import Student
from data_manager import load_students, save_students


def print_header(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def print_menu():
    print_header("STUDENT GRADE MANAGEMENT SYSTEM")
    menu_items = [
        "1. Add Student",
        "2. View All Students",
        "3. Search Student by Roll Number",
        "4. Update Student Marks",
        "5. Delete Student",
        "6. Rank Students by Average",
        "7. Exit",
    ]
    for item in menu_items:
        print(item)
    print("-" * 50)


def get_valid_int(prompt):
    """Loop until the user provides a valid integer. Demonstrates
    type conversion + control flow (while loop, try/except)."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if 0 <= value <= 100:
                return value
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    roll = input("Enter Roll Number: ").strip()

    if roll in students:
        print(f"A student with roll number {roll} already exists.")
        return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    student = Student(roll, name)

    num_subjects = get_valid_int("How many subjects? ")
    for i in range(num_subjects):
        subject = input(f"  Subject {i + 1} name: ").strip()
        marks = get_valid_float(f"  Marks in {subject}: ")
        student.add_marks(subject, marks)

    students[roll] = student
    print(f"\nStudent '{name}' added successfully!")


def view_all_students(students):
    if not students:
        print("No student records found.")
        return

    print_header("ALL STUDENTS")
    for student in students.values():
        print(student)


def search_student(students):
    roll = input("Enter Roll Number to search: ").strip()
    student = students.get(roll)

    if student is None:
        print(f"No student found with roll number {roll}.")
        return

    print_header("STUDENT FOUND")
    print(student)
    print("Subject-wise marks:")
    for subject, score in student.get_marks().items():
        print(f"  {subject}: {score}")


def update_student(students):
    roll = input("Enter Roll Number to update: ").strip()
    student = students.get(roll)

    if student is None:
        print(f"No student found with roll number {roll}.")
        return

    print(f"Updating marks for {student.name}. Existing subjects: "
          f"{list(student.get_marks().keys())}")

    while True:
        subject = input("Subject to add/update (blank to stop): ").strip()
        if subject == "":
            break
        marks = get_valid_float(f"New marks for {subject}: ")
        student.add_marks(subject, marks)

    print("Student record updated.")


def delete_student(students):
    roll = input("Enter Roll Number to delete: ").strip()

    if roll not in students:
        print(f"No student found with roll number {roll}.")
        return

    confirm = input(f"Are you sure you want to delete {students[roll].name}? (y/n): ")
    if confirm.lower() == "y":
        del students[roll]
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")


def rank_students(students):
    if not students:
        print("No student records found.")
        return

    # Build a list from the dict's values, then sort it (array-style
    # data structure + control flow), ranking highest average first.
    student_list = list(students.values())
    student_list.sort(key=lambda s: s.average(), reverse=True)

    print_header("STUDENT RANKINGS")
    for rank, student in enumerate(student_list, start=1):
        print(f"{rank}. {student}")


def main():
    students = load_students()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            rank_students(students)
        elif choice == "7":
            save_students(students)
            print("\nData saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        # Save after every operation so data isn't lost on crash/close
        save_students(students)


if __name__ == "__main__":
    main()
