from src.student_management_system.courses import Course
from src.student_management_system.managment import StudentManagementSystem
from src.student_management_system.student_creation import Student

student_management_system = StudentManagementSystem()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Assign Grade")
    print("5. View Student Courses")
    print("6. View Student Grade")
    print("7. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone number (11 digits): ")
            gender = input("Enter gender (Male/Female): ")
            email = input("Enter email: ")

            student = Student(name, age, phone, gender, email)
            student_management_system.add_student(student)

            print("Student added successfully!")

        case "2":
            title = input("Enter course title: ")
            course = Course(title)
            student_management_system.add_course(course)

            print("Course added successfully!")

        case "3":

            print("\nStudents:")
            for index, student in enumerate(student_management_system.students):
                print(index, "-", student.get_name())

            print("\nCourses:")
            for index, course in enumerate(student_management_system.courses):
                print(index, "-", course.course_title)

            student_index = int(input("Select student index: "))
            course_index = int(input("Select course index: "))

            student = student_management_system.students[student_index]
            course = student_management_system.courses[course_index]

            student_management_system.enroll_student(student, course)

            print("Student enrolled successfully!")

        case "4":

            print("\nStudents:")
            for index, student in enumerate(student_management_system.students):
                print(index, "-", student.get_name())

            print("\nCourses:")
            for index, course in enumerate(student_management_system.courses):
                print(index, "-", course.course_title)

            student_index = int(input("Select student index: "))
            course_index = int(input("Select course index: "))
            grade = float(input("Enter grade (0-100): "))

            student = student_management_system.students[student_index]
            course = student_management_system.courses[course_index]

            student_management_system.assign_grade(student, course, grade)

            print("Grade assigned successfully!")

        case "5":
            print("\nStudents:")
            for index, student in enumerate(student_management_system.students):
                print(index, "-", student.get_name())

            student_index = int(input("Select student index: "))
            student = student_management_system.students[student_index]

            courses = student_management_system.get_student_courses(student)

            if not courses:
                print("Student is not enrolled in any course.")
            else:
                print("Courses:")
                for course in courses:
                    print("-", course.course_title)

        case "6":

            print("\nStudents:")
            for index, student in enumerate(student_management_system.students):
                print(index, "-", student.get_name())

            print("\nCourses:")
            for index, course in enumerate(student_management_system.courses):
                print(index, "-", course.course_title)

            student_index = int(input("Select student index: "))
            course_index = int(input("Select course index: "))

            student = student_management_system.students[student_index]
            course = student_management_system.courses[course_index]

            grade = student_management_system.get_student_grade(student, course)

            if grade is None:
                print("No grade assigned or student not enrolled.")
            else:
                print("Grade:", grade)

        case "7":
            print("Exiting system...")
            break
        case _:
            print("Invalid choice. Try again.")