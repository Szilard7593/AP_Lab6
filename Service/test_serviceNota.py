from unittest import TestCase

from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student
from Repository.RepoNota import RepoNota
from Service.serviceNota import serviceNota


class TestserviceNota(TestCase):

    def test_add_note_and_get_all_note(self):
        repo = RepoNota()
        service = serviceNota(repo)
        student = Student(1, "Mihai", 321)
        problema = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        service.addNote(student, problema, 1)
        m = repo.getNote()
        self.assertEqual(m[0].get_nota(), 1)

    def test_get_nota(self):
        nota = Nota(Student(1, 'd', 1), ProblemaLaborator(1, 1, 'd', 'd'), 1)
        self.assertEqual(nota.get_nota(), 1)