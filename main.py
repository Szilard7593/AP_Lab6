from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student
from Repository.RepoLab import RepoLab
from Repository.RepoNota import RepoNota
from Repository.RepoStudent import RepoStudent
from Service.serviceLab import ServiceLab
from Service.serviceNota import serviceNota
from Service.serviceStudent import serviceStudent
from UI.UI import UI


def main():
    student_repo = RepoStudent()
    problema_repo = RepoLab()
    nota_repo = RepoNota()

    student_service = serviceStudent(student_repo)
    problema_service = ServiceLab(problema_repo)
    nota_service = serviceNota(nota_repo)

    s1 = Student(1, "Mihai", 321)
    s2 = Student(2, "Daria", 123)
    s3 = Student(3, "Ana", 456)
    s4 = Student(4, "Maria", 789)
    s5 = Student(5, "Iulian", 987)

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

    problema_repo.addLab(l1)
    problema_repo.addLab(l2)
    problema_repo.addLab(l3)
    problema_repo.addLab(l4)
    problema_repo.addLab(l5)

    console = UI(student_service, problema_service,nota_service)
    console.run()


main()
