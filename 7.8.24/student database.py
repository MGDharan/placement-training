class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grade):
        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        print(f"Added student: {name}")

    def update_student(self, student_id, name=None, age=None, grade=None):
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                print(f"Updated student ID {student_id}")
                return
        print(f"Student ID {student_id} not found")
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Deleted student ID {student_id}")
                return
        print(f"Student ID {student_id} not found")

    def display_students(self):
        if not self.students:
            print("No students found")
            return
        print("Student List:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
db = StudentDatabase()

