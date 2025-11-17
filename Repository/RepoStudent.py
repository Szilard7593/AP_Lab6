class RepoStudent:
    def __init__(self):
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def getStudents(self):
        return self.__students

    def getAllStudents(self):
        return list(self.__students)

    def getStudentById(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                return student
        return None

    def getStudentByName(self, name):
        for student in self.__students:
            if student.name == name:
                return student
        return None

    def deleteStudent(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                self.__students.remove(student)
        return False





