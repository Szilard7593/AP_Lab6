class RepoNota:
    def __init__(self):
        self.__note = []

    def addNote(self, note):
        self.__note.append(note)

    def getNote(self):
        return self.__note

    def getall(self):
        return self.__note

    def lista_studenti_problema_alfabetic(self, numar_lab: int, numar_prob: int):

        note_problema = [
            n for n in self.__note
            if n.get_problema_lab().get_numar_laborator() == numar_lab and n.get_problema_lab().get_numar_problema() == numar_prob
        ]

        note_sortate = sorted(note_problema, key=lambda n: n.get_nume())

        rezultat = []
        for nota in note_sortate:
            rezultat.append({
                'nume': nota.get_nume(),
                'nota': nota.get_nota()
            })

        return rezultat

    def lista_studenti_problema_dupa_nota(self, numar_lab: int, numar_prob: int):

        note_problema = [
            n for n in self.__note
            if n.get_problema_lab().get_numar_laborator() == numar_lab
               and n.get_problema_lab().get_numar_problema() == numar_prob
        ]

        note_sortate = sorted(note_problema, key=lambda n: n.get_nota(), reverse=True)

        rezultat = []
        for nota in note_sortate:
            rezultat.append({
                'nume': nota.get_nume(),
                'nota': nota.get_nota()
            })

        return rezultat

    def studenti_media_sub_5(self):

        note_pe_student = {}

        for nota in self.__note:
            student_id = nota.get_student_id()
            if student_id not in note_pe_student:
                note_pe_student[student_id] = {
                    'nume': nota.get_nume(),
                    'note': []
                }
            note_pe_student[student_id]['note'].append(nota.get_nota())

        rezultat = []
        for student_id, data in note_pe_student.items():
            media = sum(data['note']) / len(data['note'])
            if media < 5:
                rezultat.append({
                    'nume': data['nume'],
                    'media': round(media, 2),
                    'note': data['note']
                })

        rezultat = sorted(rezultat, key=lambda x: x['nume'])

        return rezultat
