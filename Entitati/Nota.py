from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student


class Nota:
    def __init__(self, student: Student, problema_lab: ProblemaLaborator, nota: int):
        self.Student = student
        self.ProblemaLaborator = problema_lab
        self.nota = nota

    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota

    def __str__(self):
        return f"Nota(student={self.Student}, problemaLab={self.ProblemaLaborator}, nota={self.nota})"

    def __repr__(self):
        return self.__str__()