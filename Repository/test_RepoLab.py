from unittest import TestCase

from Entitati.ProblemaLaborator import ProblemaLaborator
from Repository.RepoLab import RepoLab


class TestRepoLab(TestCase):
    def test_add_lab(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        repo = RepoLab()
        repo.addLab(l1)
        assert len(repo.getLabs()) == 1

    def test_get_labs(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        repo = RepoLab()
        repo.addLab(l1)
        m = repo.getLabs()
        assert len(m) == 1

    def test_delete_lab(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
        repo = RepoLab()
        repo.addLab(l1)
        repo.addLab(l2)
        repo.deleteLab(1)
        repo.deleteLab(2)
        assert len(repo.getLabs()) == 0

    def test_update_lab(self):
        pass

    def test_find_by_id(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
        repo = RepoLab()
        repo.addLab(l1)
        repo.addLab(l2)
        l = repo.find_by_id(1)
        assert l.get_numar_laborator() == 1

    def test_find_id(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l2 = ProblemaLaborator(2, 2, "Problema 2", "12.12.1015")
        repo = RepoLab()
        repo.addLab(l1)
        repo.addLab(l2)

