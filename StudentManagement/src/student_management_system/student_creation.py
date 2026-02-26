from src.student_management_system.courses import Course


class Student:
    __no_of_student = 0
    def __init__(self,name: str,age: int,phone_number: str,gender: str, email:str):

        self.__email = None
        self.set_email(email)

        Student.__no_of_student += 1
        self.__student_id = 000 +(self.__no_of_student)

        self.__age = None
        self.set_age(age)

        self.__phone_number = None
        self.set_phone_number(phone_number)

        self.__name = name
        self.set_name(name)

        self.__gender = None
        self.set_gender(gender)



    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_gender(self):
        return self.__gender

    def get_student_id(self):
        return self.__student_id

    def set_name(self,name):
        if name.strip() == "":
            raise ValueError("Student name cannot be empty")

        self.__name = name.strip()

    def set_age(self,age):
        if age <= 0:
            raise ValueError("Age must be greater than 0")

        self.__age = age

    def set_gender(self,gender):
        if gender is None or gender == "":
            raise ValueError("Gender cannot be Empty")

        if gender.strip().lower() not in ["male", "female"]:
            raise ValueError("Gender must be either Male or Female. ")

        self.__gender = gender.strip().lower()



    def set_phone_number(self,phone_number):
        if len(phone_number) != 11 or not phone_number.isdigit():
            raise ValueError("Phone number must be 11 digits")

        self.__phone_number = phone_number

    def set_email(self, email: str) -> None:
        if "@" not in email or not email.strip():
            raise ValueError("Invalid email address")
        self.__email = email
