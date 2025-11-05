class ProblemaLaborator:
    def __init__(self,numar_laborator: int,numar_problema: int,descriere: str,deadline: str):
        self.numar_laborator = numar_laborator
        self.numar_problema = numar_problema
        self.descriere = descriere
        self.deadline = deadline

    def get_numar_laborator(self):
        return self.numar_laborator

    def get_numar_problema(self):
        return self.numar_problema

    def get_descriere(self):
        return self.descriere

    def get_deadline(self):
        return self.deadline

    def set_numar_laborator(self,numar_laborator):
        self.numar_laborator = numar_laborator

    def set_numar_problema(self,numar_problema):
        self.numar_problema = numar_problema

    def set_descriere(self,descriere):
        self.descriere = descriere

    def set_deadline(self,deadline):
        self.deadline = deadline

    def __str__(self):
        return f"LAB(Numar laborator: {self.numar_laborator} , Numar problema: {self.numar_problema} , Descriere: {self.descriere} , Deadline: {self.deadline})"