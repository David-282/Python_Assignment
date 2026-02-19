from unittest import TestCase

from src.student_management_system.courses import Course
from src.student_management_system.student_creation import Student


class StudentTest(TestCase):

    def setUp(self):
        self._student =  Student("Afolabi David",13,"09071151567","MALe", "afolabi@gmail.com")


    def test_student_is_craeted_with_all_the_right_credentials(self):

        self.assertEqual("Afolabi David",self._student.get_name())
        self.assertEqual(13, self._student.get_age())
        self.assertEqual("09071151567",self._student.get_phone_number())
        self.assertEqual("male",self._student.get_gender())
        self.assertEqual("afolabi@gmail.com",self._student.get_email())


    def test_after_student_creation_the_student_is_increases (self):

        self.assertEqual(0o01, self._student.get_student_id())
        self._student =  Student("Olidi Dave",13,"08071151567","MALE", "afolabi@123gmail.com")
        self.assertEqual(0o02, self._student.get_student_id())


    def test_that_empty_name_will_throw_error_and_not_create_student(self):
        self._student2 = None

        with self.assertRaises(ValueError):
            self._student2 = Student("", 13, "08071151567", "MALE", "afolabi@123gmail.com")

        self.assertIsNone(self._student2)

    def test_that_gender_is_either_male_or_female(self):

        self._student2= None

        with self.assertRaises(ValueError):
            self._student2 = Student("Olidi Dave",13,"08071151567","man", "afolabi@123gmail.com")

        self.assertIsNone(self._student2)

    def test_that_student_age_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            self._student.set_age(-1)


    def test_course_can_be_created_with_the_right_credentials(self):

        self._course = Course("Biology")

        self.assertEqual("Biology",self._course.get_course_title())


    def test_that_course_can_not_cannot_be_created_with_wrong_input(self):
        self._course = Course("Biology")

        with self.assertRaises(ValueError):
            self._course.set_course_title("  ")