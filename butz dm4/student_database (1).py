import string
from collections import Counter
from typing import Optional


# -----------------------------
# TASK 3.1: STUDENT DATABASE
# -----------------------------

class StudentDatabase:
    """A simple student database using dictionaries."""

    def __init__(self):
        self.students = {}

    def add_student(self, student_id: str, name: str, grade: str, major: str) -> None:
        """Add a student with ID, name, grade, and major."""
        self.students[student_id] = {
            'name': name,
            'grade': grade,
            'major': major
        }
        print(f"✅ Added student: {name} (ID: {student_id})")

    def get_student(self, student_id: str) -> Optional[dict]:
        """Retrieve student information by ID."""
        return self.students.get(student_id)

    def update_grade(self, student_id: str, new_grade: str) -> None:
        """Update a student's grade."""
        student = self.get_student(student_id)
        if student:
            old_grade = student['grade']
            student['grade'] = new_grade
            print(f"✅ Updated {student['name']}'s grade from {old_grade} to {new_grade}")
        else:
            print(f"❌ Student ID {student_id} not found!")

    def display_all_students(self) -> None:
        """Display all students."""
        print("\n" + "=" * 50)
        print("ALL STUDENTS")
        print("=" * 50)
        if not self.students:
            print("No students in the database.")
            return

        for student_id, info in self.students.items():
            print(f"ID: {student_id}")
            print(f"  Name : {info['name']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Major: {info['major']}")
            print("-" * 50)


# -----------------------------
# TASK 3.2: WORD FREQUENCY COUNTER
# -----------------------------

def count_word_frequency(text: str) -> None:
    """Count and display word frequencies in text."""
    print("\n" + "=" * 50)
    print("TASK 3.2: WORD FREQUENCY COUNTER")
    print("=" * 50)

    # Remove punctuation and normalize
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)
    words = cleaned_text.split()

    word_count = Counter(words)
    sorted_words = word_count.most_common()

    print(f"Original text: {text}")
    print(f"\nTotal words  : {len(words)}")
    print(f"Unique words : {len(word_count)}")

    print("\nWord frequencies (sorted by count):")
    for word, count in sorted_words:
        print(f"  '{word}': {count}")

    most_common_word, count = sorted_words[0]
    print(f"\nMost common word: '{most_common_word}' appears {count} times")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

if __name__ == "__main__":
    print("=" * 50)
    print("TASK 3.1: STUDENT DATABASE DEMO")
    print("=" * 50)

    db = StudentDatabase()

    # Adding students
    db.add_student("S001", "Alice Johnson", "A", "Computer Science")
    db.add_student("S002", "Bob Smith", "B+", "Engineering")
    db.add_student("S003", "Charlie Brown", "A-", "Mathematics")

    # Display all students
    db.display_all_students()

    # Retrieve a student
    print("\n" + "=" * 50)
    print("RETRIEVING STUDENT S002")
    print("=" * 50)
    student = db.get_student("S002")
    if student:
        print(f"Name : {student['name']}")
        print(f"Grade: {student['grade']}")
        print(f"Major: {student['major']}")
    else:
        print("Student not found!")

    # Update grade
    print("\n" + "=" * 50)
    print("UPDATING GRADE")
    print("=" * 50)
    db.update_grade("S002", "A")
    db.display_all_students()

    # Task 3.2: Word Frequency Counter
    sample_text = "Python is amazing. Python makes programming easy. Programming with Python is fun."
    count_word_frequency(sample_text)
