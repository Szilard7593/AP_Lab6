from unittest import TestCase

from Entitati.Student import Student


class TestStudent(TestCase):
    def test_get_student_id(self):
        student = Student(1, "Mihai", 321)
        assert student.get_student_id() == 1

    def test_get_nume(self):
        student = Student(1, "Mihai", 321)
        assert student.get_nume() == "Mihai"


    def test_get_grupa(self):
        student = Student(1, "Mihai", 321)
        assert student.get_grupa() == 321

    def test_set_student_id(self):
        student = Student(1, "Mihai", 321)
        student.set_student_id(2)
        self.assertEqual(student.get_student_id(),2)

    def test_set_nume(self):
        student = Student(1, "Mihai", 321)
        student.set_nume("Ana")
        self.assertEqual(student.get_nume(), "Ana")

    def test_set_grupa(self):
        student = Student(1, "Mihai", 321)
        student.set_grupa(456)
        self.assertTrue(student.get_grupa() == 456)

    def testExceptie(self):
        with self.assertRaises(ValueError):
            s = Student(-1, "Mihai", 321)
            s.set_student_id(2)
            s.set_student_id(-1)



