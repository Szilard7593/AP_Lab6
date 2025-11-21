from unittest import TestCase

from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student
from Repository.RepoNota import RepoNota


class TestRepoNota(TestCase):
    def test_add_note_and_get_note(self):
        repo = RepoNota()
        student = Student(1,"Mihai",1)
        problema = ProblemaLaborator(1,1,"Nimic","Oricand")
        nota = Nota(student,problema,1)
        repo.addNote(nota)
        m = repo.getNote()
        self.assertEqual(m[0],nota)

    def test_getall(self):
        repo = RepoNota()
        student = Student(1, "Mihai", 1)
        problema = ProblemaLaborator(1, 1, "Nimic", "Oricand")
        nota = Nota(student, problema, 1)
        repo.addNote(nota)
        m = repo.getall()
        self.assertEqual(m[0], nota)

