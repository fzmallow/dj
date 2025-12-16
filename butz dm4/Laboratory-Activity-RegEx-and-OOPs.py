import re

# ==================================================
# PART 1 – REGULAR EXPRESSION UTILITIES
# ==================================================

STUDENT_PATTERN = re.compile(
    r"""
    ID:\s*(?P<id>\d{4}-\d{3})\s*\|\s*
    Name:\s*(?P<name>[A-Za-z\s]+)\s*\|\s*
    Email:\s*(?P<email>[^\s|]+)\s*\|\s*
    Age:\s*(?P<age>\d+)
    """,
    re.VERBOSE
)

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

ID_PATTERN = re.compile(r'^\d{4}-\d{3}$')
NAME_PATTERN = re.compile(r'^[A-Za-z\s]+$')


def extract_student_data(data: str) -> dict | None:
    """Extract student data using named regex groups."""
    match = STUDENT_PATTERN.search(data)
    return match.groupdict() if match else None


def validate_email(email: str) -> bool:
    """Validate email format."""
    return EMAIL_PATTERN.fullmatch(email) is not None


def validate_student_id(student_id: str) -> bool:
    """Validate student ID format (YYYY-XXX)."""
    return ID_PATTERN.fullmatch(student_id) is not None


def validate_name(name: str) -> bool:
    """Validate name (letters and spaces only)."""
    return NAME_PATTERN.fullmatch(name.strip()) is not None


def mask_email(email: str) -> str:
    """Mask email username while keeping domain."""
    return re.sub(r'^[^@]+', '*****', email)


def find_all_words(text: str) -> list:
    """Find all words using regex."""
    return re.findall(r'[A-Za-z]+', text)


# ==================================================
# PART 2 – OBJECT-ORIENTED PROGRAMMING
# ==================================================

class Student:
    """Represents a student."""

    def __init__(self, student_id: str, name: str, email: str, age: int):
        if not validate_student_id(student_id):
            raise ValueError("Invalid student ID format")
        if not validate_name(name):
            raise ValueError("Invalid name format")
        if not validate_email(email):
            raise ValueError("Invalid email format")
        if age <= 0:
            raise ValueError("Invalid age")

        self.student_id = student_id
        self.name = name
        self._email = email
        self._age = age

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not validate_email(value):
            raise ValueError("Invalid email format")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Invalid age")
        self._age = value

    def display_info(self):
        """Display student information."""
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Age        : {self.age}")


class Scholar(Student):
    """Represents a scholar student."""

    def __init__(self, student_id, name, email, age, scholarship_type):
        super().__init__(student_id, name, email, age)
        self.scholarship_type = scholarship_type

    def display_info(self):
        super().display_info()
        print(f"Scholarship: {self.scholarship_type}")


# ==================================================
# PART 3 – INTEGRATION & PROCESSING
# ==================================================

def process_students(students_raw: list) -> list:
    """Convert raw text entries into Student / Scholar objects."""
    students = []

    for entry in students_raw:
        data = extract_student_data(entry)

        if not data:
            print(f"❌ Failed to parse entry:\n{entry}\n")
            continue

        student_id = data['id']
        name = data['name'].strip()
        email = data['email']
        age = int(data['age'])

        scholarship_match = re.search(r'Scholarship:\s*(\w+)', entry)

        try:
            if scholarship_match:
                student = Scholar(
                    student_id, name, email, age,
                    scholarship_match.group(1)
                )
            else:
                student = Student(student_id, name, email, age)

            students.append(student)

        except ValueError as error:
            print(f"❌ Error processing student: {error}")

    return students


# ==================================================
# MAIN PROGRAM – DEMONSTRATION
# ==================================================

if __name__ == "__main__":

    print("=" * 70)
    print("STUDENT INFORMATION PROCESSING SYSTEM")
    print("=" * 70, "\n")

    students_raw = [
        "ID: 2025-001 | Name: Juan Dela Cruz | Email: juan.cruz@example.com | Age: 20",
        "ID: 2025-002 | Name: Maria Santos | Email: maria.santos@school.edu | Age: 21 | Scholarship: Academic",
        "ID: 2025-003 | Name: Pedro Reyes | Email: pedro.reyes@university.ph | Age: 22",
        "ID: 2025-004 | Name: Ana Gonzales | Email: ana.gonzales@school.edu | Age: 19 | Scholarship: Athletic"
    ]

    students = process_students(students_raw)

    print(f"\nSuccessfully processed {len(students)} student(s)\n")
    print("=" * 70)

    for i, student in enumerate(students, 1):
        student.display_info()
        if i < len(students):
            print("-" * 70)

    print("\n" + "=" * 70)
    print("EXTRA TASK DEMONSTRATIONS")
    print("=" * 70, "\n")

    print("Email Masking Example:")
    email = "juan.cruz@example.com"
    print(f"Original: {email}")
    print(f"Masked  : {mask_email(email)}\n")

    print("Find Words in Name:")
    name = "Juan Dela Cruz"
    print(f"Words: {find_all_words(name)}\n")

    print("Email Validation via Property:")
    student = students[0]
    print(f"Old Email: {student.email}")
    student.email = "updated.email@valid.com"
    print(f"New Email: {student.email}")

    print("\n" + "=" * 70)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("=" * 70)
