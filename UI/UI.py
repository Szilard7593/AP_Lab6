class UI:
    def __init__(self,serviceStudent,serviceLab,serviceNota):
        self.serviceStudent = serviceStudent
        self.serviceLab = serviceLab
        self.serviceNota = serviceNota


    @staticmethod
    def meniu():
       print("1.Adauga un student")
       print("2.Adauga un laborator")
       print("3.Arata toti studentii")
       print("4.Arata toate laboratoarele")
       print("5.Sterge un student")
       print("6.Sterge un laborator")
       print("7.Update student")
       print("8.Update laborator")
       print("9.Cauta un student")
       print("10.Cauta o problema de laborator")
       print("20.Noteaza un student: ")
       print("21.Arata toate notele studentilor:")

       print("11.Toti studentii cu media notelor de la lab mai mica de 5")
       print("12.Lista de studenți și notele lor la o problema de laborator data, ordonata: alfabetic după nume, după notă.")
       print("13.Exit")

    def run(self):
        while True:
            self.meniu()

            optiune = int(input(("Introduceti optiunea dorita: ")))
            
            match optiune:
                case 1:
                    self.AdaugaunStudent()
                case 2:
                    self.AdaugaunLaborator()
                case 3:
                    self.AfiseazaStudenti()
                case 4:
                    self.AfiseazaLaboratori()
                case 5:
                    self.StergeunStudent()
                case 6:
                    self.stergeunLaborator()
                case 7:
                    self.updateStudent()
                case 8:
                    self.updateLaborator()
                case 9:
                    self.CautaunStudent()
                case 10:
                    self.CautaunLaborator()
                case 11:
                    self.AdaugaNotare()
                case 12:
                    self.studentiInOrdineAlfa()
                case 13:
                    exit(0)
                case 21:
                    self.print_all_note()
                case 20:
                    self.AdaugaNotare()
                case _:
                    print("Optiune inexistenta!")
                    continue


    def AdaugaunStudent(self):
        id = int(input("ID Student:  "))
        nume = input("Nume student: ")
        grupa = input("Grupa student: ")
        student = self.serviceStudent.adauga_student(id,nume,grupa)
        print("Studentul a fost adaugat cu succes!")

    def AdaugaunLaborator(self):
        id_lab = int(input("ID Laborator:  "))
        problema_lab = int(input("Problema laborator: "))
        descriere = input("Descriere laborator: ")
        deadline = input("Deadline laborator: ")
        laborator = self.serviceLab.adauga_problema(id_lab,problema_lab,descriere ,deadline)
        print("Laboratorul a fost adaugat cu succes!")

    def AfiseazaStudenti(self):
        studenti = self.serviceStudent.get_toti_studentii()
        for student in studenti:
            print(student)

    def AfiseazaLaboratori(self):
        laboratori = self.serviceLab.get_toate_problemele()
        for laborator in laboratori:
            print(laborator)

    def StergeunStudent(self):
        id = int(input("ID Student:  "))
        student = self.serviceStudent.sterge_student(id)
        print("Studentul a fost sterget cu succes!")

    def stergeunLaborator(self):
        numar_laborator = int(input("Numar Laborator:  "))
        laborator = self.serviceLab.sterge_problema(numar_laborator)
        print("Laboratorul a fost sterget cu succes!")

    def updateStudent(self):
        id = int(input("ID Student:  "))
        nume = input("Nume student: ")
        grupa = int(input("Grupa student: "))
        student = self.serviceStudent.update_student(id,nume,grupa)
        print("Studentul a fost update cu succes!")

    def updateLaborator(self):
        numar_lab = int(input("Numar Laborator:  "))
        numar_problema = int(input("Numar problema de laborator: "))
        descriere = input("Descriere laborator: ")
        deadline = input("Deadline laborator: ")
        laborator = self.serviceLab.update_problema(numar_lab,numar_problema,descriere,deadline)
        print("Laboratorul a fost update cu succes!")

    def CautaunStudent(self):
        id_student = int(input("ID Student:  "))
        student = self.serviceStudent.cauta_student(id_student)
        print(student)

    def CautaunLaborator(self):
        id_laborator = int(input("Numar laborator:  "))
        laborator = self.serviceLab.cauta_problema(id_laborator)

    def AdaugaNotare(self):
        id = int(input("Introduceti id-ul studentului: "))
        student_found = self.serviceStudent.cauta_student(id)
        numar_lab = int(input("Introduceti numarul laboratorului: "))
        lab_found = self.serviceLab.cauta_problema(numar_lab)
        nota = int(input("Introduceti nota studentului: "))
        self.serviceNota.addNote(student_found,lab_found,nota)

    def print_all_note(self):
        all_notes = self.serviceNota.getAllNote()
        for note in all_notes:
            print(note)
        
