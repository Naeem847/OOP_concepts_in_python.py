class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 21)

print(s1.name)
print(s1.age)
# oop concepts12
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

account = BankAccount(1000)

account.deposit(500)
account.show_balance()
# oop concepts123
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts with key")

c = Car()
c.start()
# oop concepts1234
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# list of objects
students = [
    Student("Ali", 85),
    Student("Ahmed", 90),
    Student("Sara", 95)
]

# loop through objects
for student in students:
    student.show_details()