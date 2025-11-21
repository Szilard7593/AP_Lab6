from Entitati.ProblemaLaborator import ProblemaLaborator


class RepoLab:
    def __init__(self):
        self.__labs = []

    def addLab(self, lab):
        if lab.get_numar_laborator() < 0 and lab.get_numar_problema() < 0:
            raise ValueError("Entitate invalida")
        self.__labs.append(lab)

    def getLabs(self):
        return self.__labs

    def deleteLab(self, numar_laborator: int ):
        l = self.find_by_id(numar_laborator)
        if l:
            self.__labs.remove(l)
            return
        raise ValueError("Nu esxista lab-ul")

    def updateLab(self, numar_laborator: int , numar_problema: int, description: str, deadline: str):
        for lab in self.__labs:
            if lab.get_numar_laborator() == numar_laborator and lab.get_numar_problema() == numar_problema:
                self.__labs.remove(lab)
                l = ProblemaLaborator(numar_laborator, numar_problema, description, deadline)
                self.__labs.append(l)
                return
        raise ValueError("Nu exista lab-ul")

    def find_by_id(self,numar_laborator: int):
        for lab in self.__labs:
            if lab.get_numar_laborator() == numar_laborator:
                return lab
        raise ValueError("Nu sa gasit")


