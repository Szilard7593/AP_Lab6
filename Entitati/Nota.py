from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student


class Nota:
    def __init__(self, student: Student, problema_lab: ProblemaLaborator, nota: int):
        self.__Student = student
        self.__ProblemaLaborator = problema_lab
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"Nota(student={self.__Student}, problemaLab={self.__ProblemaLaborator}, nota={self.__nota})"

    def __repr__(self):
        return self.__str__()

    def get_student(self):
        return self.__Student

    def get_problema_lab(self):
        return self.__ProblemaLaborator

    def set_student(self,student):
        self.__Student = student

    def set_problema_lab(self,problema_lab):
        self.__ProblemaLaborator = problema_lab

    def get_student_id(self):
        return self.__Student.get_student_id()

    def get_nume(self):
        return self.__Student.get_nume()

    def get_grupa(self):
        return self.__Student.get_grupa()

