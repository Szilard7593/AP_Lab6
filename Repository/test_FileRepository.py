import os.path
from unittest import TestCase

from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student
from Repository.FileRepository import FileRepository_Student, FileRepository_ProblemaLab, FileRepository_Nota
from Service.serviceStudent import serviceStudent


#TODO TESTE
class TestFileRepository_Student(TestCase):
    def setUp(self):
        self.fisier = "test_student.txt"

        with open(self.fisier, "w") as f:
            pass

        self.repo = FileRepository_Student(self.fisier)

        self.s1 = Student(1,"Mihai",321)
        self.s2 = Student(2,"Maria",323)
        self.s3 = Student(3,"MM",111)

    def tearDown(self):
        if os.path.exists(self.fisier):
            os.remove(self.fisier)

    def test_load(self):
        pass

    def test_save(self):

        self.repo.addStudent(self.s1)

        with open(self.fisier, "r") as f:
            content = f.read()

        self.assertIn("Mihai", content)
        self.assertIn("321", content)

    def test_add_student(self):
        self.repo.addStudent(self.s1)
        all_students = self.repo.getAllStudents()

        self.assertEqual(len(all_students), 1)
        self.assertEqual(all_students[0].get_nume(), "Mihai")

        # Test adding a second one
        self.repo.addStudent(self.s2)
        self.assertEqual(len(self.repo.getAllStudents()), 2)

    def test_delete_student(self):
        self.repo.addStudent(self.s1)
        self.repo.addStudent(self.s2)

        self.repo.deleteStudent(1)

        students = self.repo.getAllStudents()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].get_student_id(), 2)
        with self.assertRaises(ValueError):
            self.repo.deleteStudent(99)

    def test_get_all_students(self):
        self.assertEqual(len(self.repo.getAllStudents()),0)
        self.repo.addStudent(self.s1)
        self.repo.addStudent(self.s2)
        self.assertEqual(len(self.repo.getAllStudents()),2)

    def test_get_student_by_id(self):
        self.repo.addStudent(self.s1)
        self.assertEqual(self.repo.getStudentById(1),self.s1)
        with self.assertRaises(ValueError):
            self.repo.getStudentById(111)

    def test_update_student(self):
        self.repo.addStudent(self.s1)

        self.repo.updateStudent(1,"Mihai Updated",322)

        result = self.repo.getStudentById(1)
        self.assertEqual(result.get_nume(), "Mihai Updated")
        with self.assertRaises(ValueError):
            self.repo.updateStudent(1000,"da",21)




class TestFileRepository_ProblemaLab(TestCase):
    def setUp(self):
        self.fisier = "test_lab.txt"

        with open(self.fisier, "w") as f:
            pass

        self.repo = FileRepository_ProblemaLab(self.fisier)
        self.l1 = ProblemaLaborator(1,1,"ceva","11.01.2025")
        self.l2 = ProblemaLaborator(2,1,"Altceva","07.12.2025")

    def tearDown(self):
        if os.path.exists(self.fisier):
            os.remove(self.fisier)

class TestFileRepository_Nota(TestCase):
    def setUp(self):
        self.fisier = "test_nota.txt"
        self.fisierStud = "test_stud.txt"
        self.fisierLab = "test_lab.txt"

        with open(self.fisier,"w") as f:
            pass

        with open(self.fisierLab, "w") as f:
            pass

        with open(self.fisierStud,"w") as f:
            pass

        self.repoStud = FileRepository_Student(self.fisierStud)
        self.repoLab = FileRepository_ProblemaLab(self.fisierLab)
        self.repo = FileRepository_Nota(self.fisier,self.repoStud,self.repoLab)

    def tearDown(self):
        if os.path.exists(self.fisier):
            os.remove(self.fisier)
            os.remove(self.fisierLab)
            os.remove(self.fisierStud)

