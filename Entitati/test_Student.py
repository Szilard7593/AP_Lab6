from unittest import TestCase

from Entitati.Student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student(1, "Mihai", 321)

    def test_get_student_id(self):
        self.assertEqual(self.student.get_student_id(), 1)

    def test_get_nume(self):
        self.assertEqual(self.student.get_nume(), "Mihai")


    def test_get_grupa(self):
        self.assertEqual(self.student.get_grupa(), 321)

    def test_set_student_id(self):
        self.student.set_student_id(2)
        self.assertEqual(self.student.get_student_id(),2)

    def test_set_nume(self):
        self.student.set_nume("Ana")
        self.assertEqual(self.student.get_nume(), "Ana")

    def test_set_grupa(self):
        self.student.set_grupa(456)
        self.assertTrue(self.student.get_grupa() == 456)

    def testExceptie(self):
        with self.assertRaises(ValueError):
            s = Student(-1, "Mihai", 321)

    def testExceptie2(self):
        with self.assertRaises(ValueError):
            s = Student(1, "Mihai", 1)
            s.set_student_id(-1)

    def testMedotaAntica(self):
        try:
            s = Student(-1, "Mihai", 321)
            assert(False)
        except ValueError:
            assert(True)

