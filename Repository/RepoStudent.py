class RepoStudent:
    def __init__(self):
        self.__students = []

    def addStudent(self, student):
        if student.get_student_id() < 0:
            raise ValueError("Student ID cannot be negative")
        for stud in self.__students:
            if stud.get_student_id() == student.get_student_id():
                raise ValueError("Student ID already exists")
        self.__students.append(student)

    def getAllStudents(self):
        return list(self.__students)

    def getStudentById(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                return student
        raise ValueError("Nu sa gasit studentuk")

    #TODO De implementat in Java ca sa ved daca putem elimina
    #in timp ce o interam
    def deleteStudent(self, id):
        for student in self.__students:
            if student.get_student_id() == id:
                self.__students.remove(student)
        raise ValueError("Nu sa gasit syudentul")





