from unittest import TestCase

from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student

#TODO Sa folosim assert-urile din unittest, nu cele antice
class TestNota(TestCase):
    def setUp(self):
        self.s = Student(1, "Mihai", 321)
        self.s3 = Student(3, "Ana", 456)
        self.p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        self.q = ProblemaLaborator(1, 2, "Problema 2", "12.12.1015")
        self.nota = Nota(self.s, self.p, 1)

    def test_get_nota(self):
        self.assertEqual(self.nota.get_nota(), 1)

    def test_set_nota(self):
        self.nota.set_nota(2)
        self.assertEqual(self.nota.get_nota(), 2)

    def test_get_student(self):
        self.assertEqual(self.nota.get_student(), self.s)
        self.assertEqual(self.nota.get_student_id(), 1)
        self.assertEqual(self.nota.get_nume(), "Mihai")

    def test_get_problema_lab(self):
        self.assertEqual(self.nota.get_problema_lab(), self.p)

    def test_set_student(self):
        self.nota.set_student(self.s3)
        self.assertEqual(self.nota.get_student(), self.s3)

    def test_set_problema_lab(self):
        self.nota.set_problema_lab(self.q)
        self.assertEqual(self.nota.get_problema_lab(), self.q)

    def test_get_student_id(self):
        self.assertEqual(self.nota.get_student_id(), 1)

    def test_get_nume(self):
        self.assertEqual(self.nota.get_nume(), "Mihai")

    def test_get_grupa(self):
        self.assertEqual(self.nota.get_grupa(), 321)

    def testExceptiiIdNegativ(self):
        with self.assertRaises(ValueError):
            s = Student(-1, "Mihai", 321)

    def testExceptiiSetariNegativ(self):
        with self.assertRaises(ValueError):
            s = Student(1, "Mihai", 321)
            s.set_student_id(-1)