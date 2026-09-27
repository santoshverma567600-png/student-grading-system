"""
student.py
-----------
Defines the Student class used throughout the Student Grade
Management System.

Demonstrates:
- Object Oriented Programming (class, __init__, self, methods)
- Encapsulation (using a leading underscore for internal data)
- Core data structures (dict for subject-wise marks)
- Operators (arithmetic for averages, comparison for grading)
- Precedence and associativity (grade threshold expressions)
- Type conversion (marks stored/converted as float)
"""


class Student:
    """Represents a single student and their subject-wise marks."""

    def __init__(self, roll_number, name, marks=None):
        """
        roll_number : str or int, unique identifier
        name        : str, student's full name
        marks       : dict, e.g. {"Math": 85, "Science": 90}
        """
        self.roll_number = str(roll_number)
        self.name = name
        # Encapsulated internal data — accessed via methods below
        self._marks = {}

        if marks:
            for subject, score in marks.items():
                self.add_marks(subject, score)

    def add_marks(self, subject, score):
        """Add or update marks for a subject. Converts input to float."""
        try:
            score = float(score)  # explicit type conversion
        except (TypeError, ValueError):
            raise ValueError(f"Marks for {subject} must be numeric.")

        if not (0 <= score <= 100):
            raise ValueError("Marks must be between 0 and 100.")

        self._marks[subject] = score

    def remove_subject(self, subject):
        """Remove a subject's marks if present."""
        self._marks.pop(subject, None)

    def get_marks(self):
        """Return a copy of the marks dictionary."""
        return dict(self._marks)

    def total_marks(self):
        """Sum of all subject marks (arithmetic operator: +)."""
        return sum(self._marks.values())

    def subject_count(self):
        return len(self._marks)

    def average(self):
        """Average percentage across all subjects."""
        if self.subject_count() == 0:
            return 0.0
        # Precedence: division happens after sum() is fully evaluated
        return self.total_marks() / self.subject_count()

    def grade(self):
        """
        Determine letter grade from average using comparison
        and logical operators. Demonstrates precedence: comparison
        operators evaluate before the implicit elif chaining logic.
        """
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def to_dict(self):
        """Convert student object to a plain dict for JSON storage."""
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "marks": self._marks,
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstruct a Student object from a stored dict (used on load)."""
        return cls(data["roll_number"], data["name"], data.get("marks", {}))

    def __str__(self):
        """Human-readable representation used by print()."""
        return (
            f"Roll No: {self.roll_number} | Name: {self.name} | "
            f"Average: {self.average():.2f} | Grade: {self.grade()}"
        )

    def __repr__(self):
        return f"Student({self.roll_number!r}, {self.name!r}, {self._marks!r})"
