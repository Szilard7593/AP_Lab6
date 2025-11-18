from Entitati.ProblemaLaborator import ProblemaLaborator


class RepoLab:
    def __init__(self):
        self.__labs = []

    def addLab(self, lab):
        self.__labs.append(lab)

    def getLabs(self):
        return list(self.__labs)

    def deleteLab(self, numar_laborator: int ):
        for lab in self.__labs:
            if lab.get_numar_problema() == numar_laborator:
                self.__labs.remove(lab)
        return False

    def updateLab(self, numar_laborator: int , numar_problema: int, description: str, deadline: str):
        for lab in self.__labs:
            if lab.get_numar_laborator() == numar_laborator and lab.get_numar_problema() == numar_problema:
                self.__labs.remove(lab)
                l = ProblemaLaborator(numar_laborator, numar_problema, description, deadline)
                self.__labs.append(l)

    def find_by_id(self,numar_laborator: int):
        for lab in self.__labs:
            if lab.get_numar_problema() == numar_laborator:
                return (lab)
        return None

    def find_id(self,numar_laborator: int):
        for lab in self.__labs:
            if lab.numar_laborator == numar_laborator:
                return lab.numar_laborator
        return None
