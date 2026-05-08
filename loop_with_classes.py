class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student name:", self.name)

names = ["Ali", "Sara", "Ahmed"]

students = []


for n in names:
    students.append(Student(n))


for s in students:
    s.show()
    