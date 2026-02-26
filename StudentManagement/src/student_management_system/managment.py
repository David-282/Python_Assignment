# 4
from src.student_management_system.courses import Course
from src.student_management_system.enrollment import Enrollment
from src.student_management_system.student_creation import Student


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []


    def add_student(self, student: Student):
        self.students.append(student)


    def add_course(self, course: Course):
        self.courses.append(course)

    def enroll_student(self, student: Student, course: Course):
        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)
        return enrollment

    def assign_grade(self, student: Student, course: Course, grade: float):
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                enrollment.assign_grade(grade)
                return
        raise ValueError("Student is not enrolled in the course")


    def get_student_courses(self, student: Student):
        student_courses = []

        for enrollment in self.enrollments:
            if enrollment.student == student:
                student_courses.append(enrollment.course)

        return student_courses


    def get_student_grade(self, student: Student, course: Course):

        for enrollment in self.enrollments:

            if enrollment.student == student and enrollment.course == course:
                return enrollment.grade

        return None