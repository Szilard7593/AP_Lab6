class RepoStudent:
    def __init__(self):
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def getAllStudents(self):
        return list(self.__students)

    def getStudentById(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                return student
        return None


    def deleteStudent(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                self.__students.remove(student)
        return False





