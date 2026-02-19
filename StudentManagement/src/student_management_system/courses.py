
class Course:
    def __init__(self,course_title:str):
        self.__course_title = None
        self.set_course_title(course_title)




    def get_course_title(self):
        return self.__course_title

    def set_course_title(self,course_title:str):
        if course_title is None or course_title.strip() == "":
            raise ValueError("Course Title cannot be empty")

        self.__course_title = course_title.strip()