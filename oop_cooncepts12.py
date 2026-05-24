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

    

    # Class Car with attributes and method
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_car(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


# Objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("BMW", "X5")

# Store objects
cars = [car1, car2, car3]

# Loop through objects
for car in cars:
    car.show_car()


    # cunter class with method to increment count
class Counter:
    def __init__(self):
        self.count=0
    def show_count(self):
        print(f"Count: {self.count}")

        while self.count<5:
            print("count,",self.count)

            self.count += 1

    # object
object= Counter()

# calling method
object.show_count()

    # def increment(self):
    #     self.count += 1
    # practise fastapi concepts


from fastapi import FastAPI
 
import uvicorn

app= FastAPI(
    title="My FastAPI Application",
    description="this is a simple FastAPI application",
    version="1.0.0"

)
@app.get("/")   # this handle get request to the root endpoint("/")
def read_root():
    
    return {"message": "Welcome to my FastAPI application!"}
@app.get("/hello/{name}")  # this handle get request to the "/hello/{name}" endpoint

def read_item(name: str):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    # start the server using uvicorn
    uvicorn.run("my_firstproject:app", host="127.0.0.1", port=8000, reload=True)
