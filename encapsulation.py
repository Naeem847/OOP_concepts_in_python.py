class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #this ia a private variable

    def deposit(self,amount):
        self.__balance+=amount
        print("you deposited:",amount)
        
        
    def show_balance(self):
        print("your balance is:",self.__balance)

account=BankAccount(1000)
account.deposit(500)
account.show_balance()

