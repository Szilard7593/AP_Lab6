from unittest import TestCase

from Repository.RepoStudent import RepoStudent
from Service.serviceStudent import serviceStudent


class TestserviceStudent(TestCase):
    def test_adauga_student(self):
        repo = RepoStudent()
        s2erviceStudent = serviceStudent(repo)
        s2erviceStudent.adauga_student(1,"Mihai",1)
        toti = s2erviceStudent.get_toti_studentii()
        self.assertEqual(len(toti),1)

    def test_sterge_student(self):

        #Incercam sa stergem ceva inexistent
        repo = RepoStudent()
        s2erviceStud = serviceStudent(repo)
        with self.assertRaises(ValueError):
            s2erviceStud.sterge_student(3)

    def test_cauta_student(self):
        repo = RepoStudent()
        s2erviceStudent = serviceStudent(repo)
        s2erviceStudent.adauga_student(1, "Mihai", 1)
        student2 = s2erviceStudent.cauta_student(1)
        self.assertEqual(student2.get_student_id(), 1)
        self.assertEqual(student2.get_nume(), "Mihai")
        self.assertEqual(student2.get_grupa(), 1)

    def test_update_student(self):
        repo = RepoStudent()
        s2erviceStudent = serviceStudent(repo)
        s2erviceStudent.adauga_student(1, "Mihai", 1)
        s2erviceStudent.update_student(1, "Ana", 2)
        student2 = s2erviceStudent.cauta_student(1)
        self.assertEqual(student2.get_student_id(), 1)
        self.assertEqual(student2.get_nume(), "Ana")
        self.assertEqual(student2.get_grupa(), 2)
