from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student
from Repository.FileRepository import FileRepository_Student, FileRepository_ProblemaLab, FileRepository_Nota
from Repository.RepoLab import RepoLab
from Repository.RepoNota import RepoNota
from Repository.RepoStudent import RepoStudent
from Service.serviceLab import ServiceLab
from Service.serviceNota import serviceNota
from Service.serviceStudent import serviceStudent
from UI.UI import UI


def main():
    student_repo = FileRepository_Student("student.txt")
    problema_repo = FileRepository_ProblemaLab("laboratoarea.txt")
    nota_repo = FileRepository_Nota("note.txt",student_repo,problema_repo)

    student_service = serviceStudent(student_repo)
    problema_service = ServiceLab(problema_repo)
    nota_service = serviceNota(nota_repo)
    '''
    s1 = Student(1, "Mihai", 321)
    s2 = Student(2, "Daria", 123)
    s3 = Student(3, "Ana", 456)
    s4 = Student(4, "Maria", 789)
    s5 = Student(5, "Iulian", 987)
    s6 = Student(6, "Mihai", 331)
    s7 = Student(7, "Daria", 113)
    s8 = Student(8, "Ana", 446)

    l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
    l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
    l3 = ProblemaLaborator(2, 3, "Problema 3", "13.11.2025")
    l4 = ProblemaLaborator(4, 4, "Problema 3", "14.10.2025")
    l5 = ProblemaLaborator(5, 5, "Problema 4", "15.12.2025")

    student_repo.addStudent(s1)
    student_repo.addStudent(s2)
    student_repo.addStudent(s3)
    student_repo.addStudent(s4)
    student_repo.addStudent(s5)
    student_repo.addStudent(s6)
    student_repo.addStudent(s7)
    student_repo.addStudent(s8)

    problema_repo.addLab(l1)
    problema_repo.addLab(l2)
    problema_repo.addLab(l3)
    problema_repo.addLab(l4)
    problema_repo.addLab(l5)

    n1 = Nota(s1,l1,4)
    n2 = Nota(s1,l2,3)
    n3 = Nota(s1,l3,2)
    n4 = Nota(s2,l4,10)
    n5 = Nota(s3,l5,5)

    nota_repo.addNote(n1)
    nota_repo.addNote(n2)
    nota_repo.addNote(n3)
    nota_repo.addNote(n4)
    nota_repo.addNote(n5)
    '''

    console = UI(student_service, problema_service,nota_service)
    console.run()


main()
