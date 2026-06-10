class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass


d = Dog()
d.speak()

# # Parent Class
class Person:
    def introduce(self):
        print("I am a Person")

# Child Class
class Student(Person):
    pass

# Create a list of students
students = [Student(), Student(), Student()]

# Use loop
for s in students:
    s.introduce()
    