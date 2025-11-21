class RepoLab:
    def __init__(self):
        self.__labs = []

    def addLab(self, lab):
        for labs in self.__labs:
            if labs.get_numar_laborator() == lab.get_numar_laborator() and labs.get_numar_problema() == lab.get_numar_problema():
                raise ValueError("Lab-ul exista deja")
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
                lab.set_descriere(description)
                lab.set_deadline(deadline)
                return
        raise ValueError("Nu exista lab-ul")

    def find_by_id(self,numar_laborator: int):
        for lab in self.__labs:
            if lab.get_numar_laborator() == numar_laborator:
                return lab
        raise ValueError("Nu sa gasit")


