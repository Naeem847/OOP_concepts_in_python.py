class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def show_details(self):

        print(f"Name: {self.name}, Marks: {self.marks}") 

students=[
        student("ali", 85),
        student("ahmed", 90),
        student("sara", 95)
    ] 

     # for loop through objects
for student in students:
        student.show_details()