# ==================================================
# TASK 1.1: STUDENT GRADE MANAGER
# ==================================================

from typing import List


class StudentManager:
    """Manage student names and grades."""

    def __init__(self):
        self.students: List[dict] = []

    def add_student(self, name: str, grade: float) -> None:
        """Add a student with their grade."""
        self.students.append({"name": name, "grade": grade})
        print(f"✅ Added {name} with grade {grade}")

    def calculate_average(self) -> float:
        """Calculate average grade."""
        if not self.students:
            return 0.0
        return sum(s["grade"] for s in self.students) / len(self.students)

    def find_highest(self) -> float:
        """Find the highest grade."""
        if not self.students:
            return 0.0
        return max(s["grade"] for s in self.students)

    def display_all(self) -> None:
        """Display all students and their grades."""
        print("\n" + "=" * 40)
        print("STUDENT GRADES")
        print("=" * 40)
        if not self.students:
            print("No students added yet.")
            return

        for s in self.students:
            print(f"{s['name']}: {s['grade']}")

        print("\nAverage Grade: {:.2f}".format(self.calculate_average()))
        print("Highest Grade: {:.2f}".format(self.find_highest()))


# ==================================================
# TASK 1.2: LIST OPERATIONS PRACTICE
# ==================================================

def list_operations() -> None:
    """Practice various list operations."""
    numbers = [5, 2, 8, 1, 9, 3]
    print("\n" + "=" * 40)
    print("TASK 1.2: LIST OPERATIONS")
    print("=" * 40)
    print(f"Original list: {numbers}")

    sorted_numbers = sorted(numbers)
    print(f"Sorted list: {sorted_numbers}")

    total = sum(numbers)
    print(f"Sum: {total}")

    average = total / len(numbers)
    print(f"Average: {average:.2f}")

    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Length: {len(numbers)}")


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":
    print("=" * 40)
    print("TASK 1.1: STUDENT GRADE MANAGER")
    print("=" * 40)

    manager = StudentManager()
    manager.add_student("Alice", 85)
    manager.add_student("Bob", 92)
    manager.add_student("Charlie", 78)

    manager.display_all()

    list_operations()
