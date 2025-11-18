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

    def lista_studenti_problema_alfabetic(self, numar_lab: int, numar_prob: int):
        """
        Returnează lista studenților și notele lor la o problemă dată, ordonată alfabetic
        """
        return self.__RepoNota.lista_studenti_problema_alfabetic(numar_lab, numar_prob)

    def lista_studenti_problema_dupa_nota(self, numar_lab: int, numar_prob: int):
        """
        Returnează lista studenților și notele lor la o problemă dată, ordonată după notă (descrescător)
        """
        return self.__RepoNota.lista_studenti_problema_dupa_nota(numar_lab, numar_prob)

    def studenti_media_sub_5(self):
        """
        Returnează toți studenții cu media notelor de laborator < 5
        """
        return self.__RepoNota.studenti_media_sub_5()








