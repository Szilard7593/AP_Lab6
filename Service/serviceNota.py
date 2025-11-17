from Entitati.Nota import Nota  


class serviceNota:
    def __init__(self,RepoNota):
        self.__RepoNota = RepoNota

    def addNote(self,student_id,problema_numar,nota):
        n = Nota(student_id,problema_numar,nota)
        self.__RepoNota.addNote(n)
    
    def getAllNote(self):
        return self.__RepoNota.getall()

    def getNota(self):
        return self.__RepoNota.getNote()






