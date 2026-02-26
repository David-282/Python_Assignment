class Course:
    def __init__(self,course_title:str):
        self.course_title = course_title
        # self.course_unit = course_unit

    @property
    def course_title(self):
        return self.__course_title

    @course_title.setter
    def course_title(self,course_title:str):
        if course_title is None or course_title.strip() == "":
            raise ValueError("Course Title cannot be empty")

        self.__course_title= course_title.strip()