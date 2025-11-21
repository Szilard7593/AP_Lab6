from Entitati.Student import Student


class serviceStudent:
    def __init__(self,RepoStudent):
        self.__RepoStudent = RepoStudent

    def adauga_student(self, student_id, nume, grupa):
        student = Student(student_id, nume, grupa)
        self.__RepoStudent.addStudent(student)

    def sterge_student(self, student_id):
        self.__RepoStudent.deleteStudent(student_id)

    def cauta_student(self, student_id):
        student = self.__RepoStudent.getStudentById(student_id)
        return student

    def get_toti_studentii(self):
        return self.__RepoStudent.getAllStudents()

    def get_student_id(self, student_id):
        return self.__RepoStudent.getStudentById(student_id)

    def update_student(self, student_id, nume, grupa):
        self.__RepoStudent.updateStudent(student_id,nume,grupa)