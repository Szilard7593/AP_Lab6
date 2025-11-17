class RepoNota:
    def __init__(self):
        self.__note = []

    def addNote(self, note):
        self.__note.append(note)

    def getNote(self):
        return list(self.__note)

    def getNoteById(self, note):
        for note in self.__note:
            if note.note == note:
                return note

    def delete(self,id):
        for note in self.__note:
            if note.student_id == id:
                self.__note.remove(note)
                return True
            
    def getall(self):
        return list(self.__note)
        