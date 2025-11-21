from unittest import TestCase

from Entitati.ProblemaLaborator import ProblemaLaborator


class TestProblemaLaborator(TestCase):

    def setUp(self):
        self.l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")

    def test_get_numar_laborator(self):
        self.assertEqual(self.l1.get_numar_laborator(), 1  )

    def test_get_numar_problema(self):
        self.assertEqual(self.l1.get_numar_problema(), 1)

    def test_get_descriere(self):
        self.assertEqual(self.l1.get_descriere(), "Introducere")

    def test_get_deadline(self):
        self.assertEqual(self.l1.get_deadline(), "11.10.2025")

    def test_set_numar_laborator(self):
        self.l1.set_numar_laborator(2)
        self.assertEqual(self.l1.get_numar_laborator(), 2
                         )
    def test_set_numar_problema(self):
        self.l1.set_numar_problema(2)
        self.assertEqual(self.l1.get_numar_problema(), 2)

    def test_set_descriere(self):
        self.l1.set_descriere("Problema 2")
        self.assertEqual(self.l1.get_descriere(), "Problema 2")

    def test_set_deadline(self):
        self.l1.set_deadline("12.12.1015")
        self.assertEqual(self.l1.get_deadline(), "12.12.1015")

    def testExceptiiConsttructor(self):
        with self.assertRaises(ValueError):
            l1 = ProblemaLaborator(-1, 1, "Introducere", "11.10.2025")

    def testExceptiiSetari(self):
        with self.assertRaises(ValueError):
            l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
            l1.set_numar_laborator(-1)

    def testExceptiiSetari2(self):
        with self.assertRaises(ValueError):
            l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
            l1.set_numar_problema(-99)