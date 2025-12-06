from Entitati.BaseEntity import BaseEntity


class ProblemaLaborator(BaseEntity):
    def __init__(self,numar_laborator: int,numar_problema: int,descriere: str,deadline: str):
        if int(numar_laborator) < 0 or int(numar_problema) < 0:
            raise ValueError("Numar invalid!")

        super().__init__(numar_laborator)
        self.__numar_problema = numar_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_numar_laborator(self):
        return super().getID()

    def get_numar_problema(self):
        return self.__numar_problema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_numar_laborator(self,numar_laborator: int):
        if numar_laborator < 0:
            raise ValueError("Numar laborator invalid!")
        super().setID(numar_laborator)

    def set_numar_problema(self,numar_problema: int):
        if numar_problema < 0:
            raise ValueError("Numar problema invalid!")
        self.__numar_problema = numar_problema

    def set_descriere(self,descriere: str):
        self.__descriere = descriere

    def set_deadline(self,deadline: str):
        self.__deadline = deadline

    def __str__(self):
        return f"LAB(Numar laborator: {super().__str__()} , Numar problema: {self.__numar_problema} , Descriere: {self.__descriere} , Deadline: {self.__deadline})"
