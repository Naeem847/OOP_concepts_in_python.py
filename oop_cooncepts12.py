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