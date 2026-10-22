"""Lab 1 starter: complete every TODO."""


class InvalidMarksError(Exception):
    """Raised when a student's marks are outside the valid range."""


class Course:
    """A course that stores students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks

    def add_student(self, student, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student] = marks

    def average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        if not self.marks:
            return None
        return max(self.marks, key=self.marks.get)

    def __len__(self):
        return len(self.marks)

    def __str__(self):
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"
    def remove_student(self, name: str) -> None:
        """ remove a student, or raise KeyError if missing."""
        if name not in self.marks:
            raise KeyError(f"No student named {name}")
        del self.marks[name]

def load_course(name, filename):
    """Load students from a CSV-like marks file into a Course."""
    course = Course(name)

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                student, mark = line.split(",")
                student = student.strip()
                mark = mark.strip()

                try:
                    course.add_student(student, int(mark))
                except ValueError:
                    print(f"Skipping {student}: invalid mark '{mark}'")
                    continue
                except InvalidMarksError as exc:
                    print(exc)
                    continue
    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course
