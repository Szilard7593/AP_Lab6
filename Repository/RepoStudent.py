class RepoStudent:
    def __init__(self):
        self.__students = []

    def addStudent(self, student):
        for stud in self.__students:
            if stud.get_student_id() == student.get_student_id():
                raise ValueError("Student ID already exists")
        self.__students.append(student)





    def getAllStudents(self):
        return self.__students

    def getStudentById(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                return student
        raise ValueError("Nu sa gasit studentuk")

    #TODO De implementat in Java ca sa ved daca putem elimina
    #in timp ce o interam
    def deleteStudent(self, id):
        for student in self.__students[:]:
            if student.get_student_id() == id:
                self.__students.remove(student)
                return
        raise ValueError(f"Nu există student cu ID-ul {id}!")

    def updateStudent(self,id: int,nume,grupa):
        for student in self.__students:
            if student.get_student_id() == id:
                student.set_nume(nume)
                student.set_grupa(grupa)
                return
        raise ValueError("Studentul nu exista")






