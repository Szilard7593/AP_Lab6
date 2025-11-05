from Entitati.Nota import Nota  


class serviceNota:
    def __init__(self,RepoNota):
        self.RepoNota = RepoNota

    def addNote(self,student_id,problema_numar,nota):
        n = Nota(student_id,problema_numar,nota)
        self.RepoNota.addNote(n)
    
    def getAllNote(self):
        return self.RepoNota.getall()

