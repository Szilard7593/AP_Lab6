from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student
from Repository.RepoLab import RepoLab
from Repository.RepoNota import RepoNota
from Repository.RepoStudent import RepoStudent


class FileRepository_Student(RepoStudent):
    def __init__(self, fisier: str):
        super().__init__()
        self.__fisier = fisier
        self.load()

    def load(self):
        try:
            with open(self.__fisier) as f:
                for line in f:
                    array = line.split(",")
                    student = Student(int(array[0]), array[1], int(array[2]))
                    super().addStudent(student)
        except FileNotFoundError:
            with open(self.__fisier) as f:
                pass

    def save(self, student):
        with open(self.__fisier, "a") as f:
            f.write( str(student.get_student_id()) + "," + str(student.get_nume()) + "," + str(student.get_grupa())+ "\n")
            f.close()

    def file_overwrite(self):
        with open(self.__fisier, "w") as f:
            students = super().getAllStudents()
            for student in students:
                line = f"{student.get_student_id()},{student.get_nume()},{student.get_grupa()}\n"
                f.write(line)

    def addStudent(self, student):
        super().addStudent(student)
        self.save(student)

    def deleteStudent(self, id):
        super().deleteStudent(id)
        self.file_overwrite()

    def getAllStudents(self):
        return super().getAllStudents()

    def getStudentById(self, id):
        return super().getStudentById(id)


    def updateStudent(self,id: int,nume,grupa):
        super().updateStudent(id,nume,grupa)
        self.file_overwrite()



class FileRepository_ProblemaLab(RepoLab):
    def __init__(self,fisier: str):
        super().__init__()
        self.__fisier = fisier
        self.load()

    def load(self):
        try:
            with open(self.__fisier) as f:
                for line in f:
                    array = line.split(",")
                    problema = ProblemaLaborator(int(array[0]),int(array[1]),array[2],array[3])
                    super().addLab(problema)
        except FileNotFoundError:
            with open(self.__fisier,"w") as f:
                pass
        f.close()

    def save(self,problema):
        with open(self.__fisier,"a") as f:
            f.write(str(problema.get_numar_laborator()) + "," + str(problema.get_numar_problema()) + "," + str(problema.get_descriere()) + "," + str(problema.get_deadline())+ "\n")
        f.close()

    def overwrite(self):
        with open(self.__fisier, "w") as f:
            labs = super().getLabs()
            for lab in labs:
                line = f"{lab.get_numar_lab()},{lab.get_numar_problema()},{lab.get_descriere()},{lab.get_deadline()}\n"
                f.write(line)


    def addLab(self,lab):
        super().addLab(lab)
        self.save(lab)

    def getLabs(self):
        return super().getLabs()

    #TODO unexpected output
    def deleteLab(self, numar_laborator: int ):
        super().deleteLab(numar_laborator)
        self.overwrite()

    def updateLab(self, numar_laborator: int , numar_problema: int, description: str, deadline: str):
        super().updateLab(numar_laborator,numar_problema,description,deadline)
        self.overwrite()

    def find_by_id(self,numar_laborator: int):
        return super().find_by_id(numar_laborator)


class FileRepository_Nota(RepoNota):
    def __init__(self, fisier: str, repo_student, repo_lab):
        super().__init__()
        self.__fisier = fisier
        self.__repo_student = repo_student
        self.__repo_lab = repo_lab
        self.load()

    #TODO O medota in care putem converti string-ul din fisierul text in entitatea Nota
    #initial avem nevoie sa convertim in Student si ProblemaLab ca sa cream entitatea corect
    def load(self):
        pass

    def save(self, nota):
        with open(self.__fisier, "a") as f:
            s_id = nota.get_student()
            l_nr = nota.get_problema_lab()
            val = nota.get_nota()

            f.write(f"{s_id}~{l_nr}~{val}\n")

    def __file_overwrite(self):
        with open(self.__fisier, "w") as f:
            all_notes = super().getNote()
            for nota in all_notes:
                s_id = nota.get_student()
                l_nr = nota.get_problema_lab()
                val = nota.get_nota()
                f.write(f"{s_id},{l_nr},{val}\n")

    def addNote(self, nota):
        super().addNote(nota)
        self.save(nota)

    def getNote(self):
        return super().getNote()

    def getall(self):
        return super().getall()

    def lista_studenti_problema_alfabetic(self, numar_lab: int, numar_prob: int):
        return super().lista_studenti_problema_alfabetic(numar_lab,numar_prob)

    def lista_studenti_problema_dupa_nota(self, numar_lab: int, numar_prob: int):
        return super().lista_studenti_problema_dupa_nota(numar_lab, numar_prob)

    def studenti_media_sub_5(self):
        return super().studenti_media_sub_5()




