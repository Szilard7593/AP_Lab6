from unittest import TestCase

from Entitati.Student import Student
from Repository.RepoStudent import RepoStudent


class TestRepoStudent(TestCase):
    def test_add_student(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        repo.addStudent(student)
        list = repo.getAllStudents()
        assert len(list) == 1

    def test_get_all_students(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        student2 = Student(2, "Daria", 123)

        repo.addStudent(student)
        repo.addStudent(student2)
        list = repo.getAllStudents()
        assert len(list) == 2

    def test_get_student_by_id(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        student2 = Student(2, "Daria", 123)

        repo.addStudent(student)
        repo.addStudent(student2)
        student_id = repo.getStudentById(1)
        assert student_id == student

    def test_delete_student(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        student2 = Student(2, "Daria", 123)

        repo.addStudent(student)
        repo.addStudent(student2)
        repo.deleteStudent(1)
        self.assertEqual(repo.getAllStudents(), [student2])

    #TODO Teste la exceptii folosind unit test
    def test_exceptie(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        student2 = Student(1, "Daria", 123)
        repo.addStudent(student)
        #Deci mai pe scurt verifica daca repo.addStudent(student), cand este
        #apelat din nou, returneaza un valueerror
        with self.assertRaises(ValueError):
            repo.addStudent(student)

    def test_delete_student_exceptie(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        student2 = Student(2, "Daria", 123)
        repo.addStudent(student)
        repo.addStudent(student2)
        with self.assertRaises(ValueError):
            repo.deleteStudent(3)

    def test_update_exceptie(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        repo.addStudent(student)
        with self.assertRaises(ValueError):
            repo.updateStudent(3, "Ana", 2)

    def test_get_student_by_id_exceptie(self):
        repo = RepoStudent()
        student = Student(1, "Mihai", 321)
        repo.addStudent(student)
        with self.assertRaises(ValueError):
            repo.getStudentById(3)


