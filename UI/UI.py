

class UI:
    def __init__(self,serviceStudent,serviceLab,serviceNota):
        self.__serviceStudent = serviceStudent
        self.__serviceLab = serviceLab
        self.__serviceNota = serviceNota


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
       print("24.Lista de studenți și notele lor la o problema de laborator data, ordonata: alfabetic după nume, după notă.")
       print("13.Exit")

    def run(self):
        while True:
            self.meniu()
            opțiune = int(input("Introduceti optiunea dorita: "))
            
            match opțiune:
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
                case 13:
                    exit(0)
                case 21:
                    self.print_all_note()
                case 20:
                    self.AdaugaNotare()
                case 24:
                    self.afiseaza_studenti_problema_alfabetic()
                    self.afiseaza_studenti_problema_dupa_nota()
                    self.afiseaza_studenti_media_sub_5()
                case _:
                    print("Optiune inexistenta!")
                    continue


    def AdaugaunStudent(self):
        id = int(input("ID Student:  "))
        nume = input("Nume student: ")
        grupa = input("Grupa student: ")
        self.__serviceStudent.adauga_student(id,nume,grupa)
        print("Studentul a fost adaugat cu succes!")

    def AdaugaunLaborator(self):
        id_lab = int(input("ID Laborator:  "))
        problema_lab = int(input("Problema laborator: "))
        descriere = input("Descriere laborator: ")
        deadline = input("Deadline laborator: ")
        self.__serviceLab.adauga_problema(id_lab,problema_lab,descriere ,deadline)
        print("Laboratorul a fost adaugat cu succes!")

    def AfiseazaStudenti(self):
        studenti = self.__serviceStudent.get_toti_studentii()
        for student in studenti:
            print(student)

    def AfiseazaLaboratori(self):
        laboratori = self.__serviceLab.get_toate_problemele()
        for laborator in laboratori:
            print(laborator)

    def StergeunStudent(self):
        id = int(input("ID Student:  "))
        self.__serviceStudent.sterge_student(id)
        print("Studentul a fost sterget cu succes!")

    def stergeunLaborator(self):
        numar_problema = int(input("Numar problema:  "))
        self.__serviceLab.sterge_problema(numar_problema)
        print("Laboratorul a fost sterget cu succes!")

    def updateStudent(self):
        id = int(input("ID Student:  "))
        nume = input("Nume student: ")
        grupa = int(input("Grupa student: "))
        self.__serviceStudent.update_student(id,nume,grupa)
        print("Studentul a fost update cu succes!")

    def updateLaborator(self):
        numar_lab = int(input("Numar Laborator:  "))
        numar_problema = int(input("Numar problema de laborator: "))
        descriere = input("Descriere laborator: ")
        deadline = input("Deadline laborator: ")
        laborator = self.__serviceLab.update_problema(numar_lab,numar_problema,descriere,deadline)
        print("Laboratorul a fost update cu succes!")

    def CautaunStudent(self):
        id_student = int(input("ID Student:  "))
        student = self.__serviceStudent.cauta_student(id_student)
        print(student)

    def CautaunLaborator(self):
        id_laborator = int(input("Numar laborator:  "))
        laborator = self.__serviceLab.cauta_problema(id_laborator)
        print(laborator)

    def AdaugaNotare(self):
        id = int(input("Introduceti id-ul studentului: "))
        student_found = self.__serviceStudent.cauta_student(id)
        numar_lab = int(input("Introduceti numarul laboratorului: "))
        lab_found = self.__serviceLab.cauta_problema(numar_lab)
        nota = int(input("Introduceti nota studentului: "))
        self.__serviceNota.addNote(student_found,lab_found,nota)

    def print_all_note(self):
        all_notes = self.__serviceNota.getAllNote()
        for note in all_notes:
            print(note)

    def afiseaza_studenti_problema_alfabetic(self):
        try:
            numar_lab = int(input("Introduceți numărul laboratorului: "))
            numar_prob = int(input("Introduceți numărul problemei: "))

            rezultat = self.__serviceNota.lista_studenti_problema_alfabetic(numar_lab, numar_prob)

            print(f"\n Studenți la Laborator {numar_lab}, Problema {numar_prob} (Alfabetic) ")
            if not rezultat:
                print("Nu există note pentru această problemă.")
            else:
                for item in rezultat:
                    print(f"{item['nume']}: {item['nota']}")
        except ValueError:
            print("Eroare: Introduceți numere valide!")

    def afiseaza_studenti_problema_dupa_nota(self):
        try:
            numar_lab = int(input("Introduceți numărul laboratorului: "))
            numar_prob = int(input("Introduceți numărul problemei: "))

            rezultat = self.__serviceNota.lista_studenti_problema_dupa_nota(numar_lab, numar_prob)

            print(f"\n Studenți la Laborator {numar_lab}, Problema {numar_prob} (După notă) ")
            if not rezultat:
                print("Nu există note pentru această problemă.")
            else:
                for item in rezultat:
                    print(f"{item['nume']}: {item['nota']}")
        except ValueError:
            print("Eroare: Introduceți numere valide!")

    def afiseaza_studenti_media_sub_5(self):
        rezultat = self.__serviceNota.studenti_media_sub_5()

        print("\n Studenți cu media notelor < 5 ")
        if not rezultat:
            print("Nu există studenți cu media sub 5.")
        else:
            for item in rezultat:
                print(f"{item['nume']}: Media = {item['media']}")
                print(f"  Note: {item['note']}")