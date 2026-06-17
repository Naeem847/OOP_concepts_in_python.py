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
    

# 3. Text Information Processor (Data Handling)
text=input("paste your text here: ")

words=text.split()

print(f"total words: {len(words)}")

search_word=input("enter a word to search for: ")

if search_word in text:

    print(f"found  the word '{search_word}' appears  {text.count(search_word)} times in the text.")
else:
    
    print("word not found in the text:")

# 3. Smart Task Checklist (Basic Automation)    
todo_list=[]
while True:
    action=input("\nchoose [add] task,[view] tasks, or [exit] to quit: ").lower()
    if action=="add":
        task=input("enter a task to add: ")
        todo_list.append(task)
        print(f"task '{task}' added to the list.")
    elif action=="view":
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    elif action=="exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose [add], [view], or [exit].")

        # You can add a while loop and if-else statement to make the program interactive and allow users to add tasks, view the list, or exit the program.

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying")

# Create object
s = Student("Ali")

while True:
    print("\n1. Display Name")
    print("2. Study")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.display()

    elif choice == 2:
        s.study()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid choice! Please try again.")        

# This code demonstrates several Object-Oriented Programming (OOP) concepts in Python using a for loop and an if-else statement.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 50:
            print(self.name, "has Passed")
        else:
            print(self.name, "has Failed")


# Create objects
students = [
    Student("Ali", 75),
    Student("Sara", 45),
    Student("Ahmed", 60)
]

# for loop
for s in students:
    s.result()
# This code defines a `BankAccount` class with a private variable `__balance` and a method `check_balance()` to check the balance. It then creates a list of `BankAccount` objects with different balances and uses a for loop to call the `check_balance()` method for each account, demonstrating encapsulation and data hiding in OOP.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def check_balance(self):
        if self.__balance > 0:
            print("Balance:", self.__balance)
        else:
            print("No balance available")

accounts = [BankAccount(5000), BankAccount(0), BankAccount(2500)]

for account in accounts:
    account.check_balance()
# This code defines an `Employee` class with a private variable `__salary` and a method `check_salary()` to check if the salary is high or low. It then creates a list of `Employee` objects with different salaries and uses a for loop to call the `check_salary()` method for each employee, demonstrating encapsulation and data hiding in OOP.
    
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # Private variable

    def check_salary(self):
        if self.__salary >= 50000:
            print(self.name, "has a High Salary")
        else:
            print(self.name, "has a Low Salary")

# Create objects
employees = [
    Employee("Ali", 60000),
    Employee("Sara", 40000),
    Employee("Ahmed", 55000)
]

# Loop through all employees
for emp in employees:
    emp.check_salary()
