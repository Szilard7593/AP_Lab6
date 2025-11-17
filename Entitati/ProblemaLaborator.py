class ProblemaLaborator:
    def __init__(self,numar_laborator: int,numar_problema: int,descriere: str,deadline: str):
        self.__numar_laborator = numar_laborator
        self.__numar_problema = numar_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_numar_laborator(self):
        return self.__numar_laborator

    def get_numar_problema(self):
        return self.__numar_problema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_numar_laborator(self,numar_laborator):
        self.__numar_laborator = numar_laborator

    def set_numar_problema(self,numar_problema):
        self.__numar_problema = numar_problema

    def set_descriere(self,descriere):
        self.__descriere = descriere

    def set_deadline(self,deadline):
        self.__deadline = deadline

    def __str__(self):
        return f"LAB(Numar laborator: {self.__numar_laborator} , Numar problema: {self.__numar_problema} , Descriere: {self.__descriere} , Deadline: {self.__deadline})"