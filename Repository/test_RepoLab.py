from unittest import TestCase

from Entitati.ProblemaLaborator import ProblemaLaborator
from Repository.RepoLab import RepoLab


class TestRepoLab(TestCase):
    def test_add_lab(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        repo = RepoLab()
        repo.addLab(l1)
        self.assertEqual(len(repo.getLabs()), 1)

    def test_get_labs(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        repo = RepoLab()
        repo.addLab(l1)
        self.assertEqual(repo.getLabs()[0], l1)

    def test_delete_lab(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
        repo = RepoLab()
        repo.addLab(l1)
        repo.addLab(l2)
        repo.deleteLab(1)
        repo.deleteLab(2)
        self.assertEqual(len(repo.getLabs()), 0)

    def test_update_lab(self):
        pass

    def test_find_by_id(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
        repo = RepoLab()
        repo.addLab(l1)
        repo.addLab(l2)
        l = repo.find_by_id(1)
        self.assertEqual(l.get_numar_laborator(), 1)
        self.assertEqual(l.get_numar_problema(), 1)
        self.assertEqual(l.get_descriere(), "Introducere")
        self.assertEqual(l.get_deadline(), "11.10.2025")

    def test_find_id(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
        repo = RepoLab()
        repo.addLab(l1)
        repo.addLab(l2)

        self.assertEqual(repo.find_by_id(1),l1)

    def test_add_exceptie(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        repo = RepoLab()
        repo.addLab(l1)
        with self.assertRaises(ValueError):
            repo.addLab(l1)

    def test_delete_exceptie(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        repo = RepoLab()
        with self.assertRaises(ValueError):
            repo.deleteLab(1)

    def test_update_exceptie(self):
        repo = RepoLab()
        with self.assertRaises(ValueError):
            repo.updateLab(1,1,"fa", "11.10.2025")

    def test_find_by_id_exceptie(self):
        repo = RepoLab()
        with self.assertRaises(ValueError):
            repo.find_by_id(1)