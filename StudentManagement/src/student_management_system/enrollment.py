# 1
from src.student_management_system.courses import Course
from src.student_management_system.student_creation import Student


class Enrollment:
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
        self.grade = None

    # 2
    def assign_grade(self, grade: float):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grade = grade

    # 3
    def get_grade(self):
        return self.grade