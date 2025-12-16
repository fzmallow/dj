import pickle
from typing import Dict, Any, Optional

# ==================================================
# TASK 4.1: STUDENT RECORDS FILE SYSTEM
# ==================================================

class StudentFileSystem:
    """Manage saving, loading, and exporting student records."""

    def __init__(self, filename_pickle: str = "students.pkl", filename_text: str = "students.txt"):
        self.filename_pickle = filename_pickle
        self.filename_text = filename_text

    def save_records(self, records: Dict[str, Dict[str, Any]]) -> bool:
        """Save student records using pickle."""
        try:
            with open(self.filename_pickle, 'wb') as file:
                pickle.dump(records, file)
            print(f"✅ Records saved to '{self.filename_pickle}'")
            return True
        except Exception as e:
            print(f"❌ Error saving records: {e}")
            return False

    def load_records(self) -> Optional[Dict[str, Dict[str, Any]]]:
        """Load student records from pickle file."""
        try:
            with open(self.filename_pickle, 'rb') as file:
                records = pickle.load(file)
            print(f"✅ Records loaded from '{self.filename_pickle}'")
            return records
        except FileNotFoundError:
            print(f"❌ Error: File '{self.filename_pickle}' not found!")
            return None
        except Exception as e:
            print(f"❌ Error loading records: {e}")
            return None

    def export_to_text(self, records: Dict[str, Dict[str, Any]]) -> bool:
        """Export student records to a readable text file."""
        try:
            with open(self.filename_text, 'w') as file:
                file.write("="*60 + "\n")
                file.write("STUDENT RECORDS\n")
                file.write("="*60 + "\n\n")
                
                for student_id, info in records.items():
                    file.write(f"Student ID: {student_id}\n")
                    file.write(f"  Name : {info['name']}\n")
                    file.write(f"  Grade: {info['grade']}\n")
                    file.write(f"  Major: {info['major']}\n")
                    file.write("-"*60 + "\n")
            print(f"✅ Records exported to '{self.filename_text}'")
            return True
        except Exception as e:
            print(f"❌ Error exporting records: {e}")
            return False


# ==================================================
# TASK 4.2: FILE OPERATIONS PRACTICE
# ==================================================

def demonstrate_file_operations() -> None:
    """Demonstrate writing, reading, and appending to files."""
    print("\n" + "="*60)
    print("TASK 4.2: FILE OPERATIONS PRACTICE")
    print("="*60)

    filename = "sample.txt"

    # Writing to a file
    print("\n1. Writing to a new file (w mode)...")
    try:
        with open(filename, 'w') as file:
            file.writelines(["This is line 1\n", "This is line 2\n", "This is line 3\n"])
        print("✅ File written successfully")
    except Exception as e:
        print(f"❌ Error writing file: {e}")

    # Reading from a file
    print("\n2. Reading from the file (r mode)...")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("File contents:\n" + content)
    except FileNotFoundError:
        print("❌ Error: File not found!")
    except Exception as e:
        print(f"❌ Error reading file: {e}")

    # Appending to a file
    print("\n3. Appending to the file (a mode)...")
    try:
        with open(filename, 'a') as file:
            file.writelines(["This is line 4 (appended)\n", "This is line 5 (appended)\n"])
        print("✅ Content appended successfully")
    except Exception as e:
        print(f"❌ Error appending to file: {e}")

    # Reading again
    print("\n4. Reading file again to show appended content...")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("Updated file contents:\n" + content)
    except Exception as e:
        print(f"❌ Error reading file: {e}")

    # Demonstrating file not found
    print("\n5. Demonstrating file not found error handling...")
    try:
        with open("nonexistent.txt", 'r') as file:
            _ = file.read()
    except FileNotFoundError:
        print("✅ Handled FileNotFoundError: The file does not exist")
    except Exception as e:
        print(f"❌ Error: {e}")


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":
    print("="*60)
    print("TASK 4.1: STUDENT RECORDS FILE SYSTEM")
    print("="*60)

    student_records = {
        "S001": {"name": "Alice Johnson", "grade": "A", "major": "Computer Science"},
        "S002": {"name": "Bob Smith", "grade": "B+", "major": "Engineering"},
        "S003": {"name": "Charlie Brown", "grade": "A-", "major": "Mathematics"}
    }

    print("\nOriginal student records:")
    for sid, info in student_records.items():
        print(f"{sid}: {info['name']} - {info['grade']} - {info['major']}")

    print("\n" + "-"*60)
    fs = StudentFileSystem()
    fs.save_records(student_records)

    print("\n" + "-"*60)
    loaded_records = fs.load_records()

    if loaded_records:
        print("\nLoaded student records:")
        for sid, info in loaded_records.items():
            print(f"{sid}: {info['name']} - {info['grade']} - {info['major']}")

    print("\n" + "-"*60)
    fs.export_to_text(student_records)
    print("\nCheck 'students.txt' to see the readable export.")

    demonstrate_file_operations()

    print("\n" + "="*60)
    print("ALL TASKS COMPLETED!")
    print("="*60)
    print("\nFiles created:")
    print("  - students.pkl (pickle file)")
    print("  - students.txt (readable export)")
    print("  - sample.txt (file operations demo)")
