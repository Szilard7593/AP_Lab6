from Entitati.ProblemaLaborator import ProblemaLaborator


class ServiceLab:
    def __init__(self,RepoLab):
        self.__RepoLab = RepoLab

    def adauga_problema(self, numar_lab,numar_problema, descriere, deadline):
        problema = ProblemaLaborator(numar_lab,numar_problema, descriere, deadline)
        self.__RepoLab.addLab(problema)

    def sterge_problema(self, numar_lab):
        self.__RepoLab.deleteLab(numar_lab)

    def get_toate_problemele(self):
        return self.__RepoLab.getLabs()

    def cauta_problema(self, numar_lab:int):
        problema = self.__RepoLab.find_by_id(numar_lab)
        return problema

    def update_problema(self, numar_lab, numar_problema ,descriere, deadline):
        self.__RepoLab.updateLab(numar_lab,numar_problema, descriere, deadline)

    def cauta_id(self, numar_lab):
         self.__RepoLab.find_id(numar_lab)