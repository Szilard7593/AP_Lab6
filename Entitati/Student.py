from Entitati.BaseEntity import BaseEntity


class Student(BaseEntity):
    def __init__(self,student_id:int , nume: str ,grupa: int):
        if int(student_id) < 0:
            raise ValueError("Student ID invalid!")

        super().__init__(student_id)
        self.__nume = nume
        self.__grupa = grupa

    def get_student_id(self):
        return super().getID()

    def get_nume(self):
        return self.__nume

    def get_grupa(self):
        return self.__grupa

    def set_student_id(self,student_id):
        if student_id < 0:
            raise ValueError("Student ID invalid!")
        super().setID(student_id)


    def set_nume(self,nume):
        self.__nume = nume

    def set_grupa(self,grupa):
        self.__grupa = grupa

    def __str__(self):
        return f"Student( ID: {super().__str__()} , Nume: {self.__nume} , Grupa: {self.__grupa})"

    def __repr__(self):
        return f"Student(student_id={super().__str__()}, nume={self.__nume}, grupa={self.__grupa})"
