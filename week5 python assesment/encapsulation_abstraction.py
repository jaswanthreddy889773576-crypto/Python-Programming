from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    # Method to access private balance
    def get_balance(self):
        return self.__balance


# Child class
class SavingsAccount(BankAccount):

    def account_type(self):
        print("Account Type: Savings Account")


# Creating an object
account = SavingsAccount("Rahul", 5000)

print("Account Holder:", account.account_holder)

# Demonstrating abstraction
account.account_type()

# Demonstrating encapsulation
print("Initial Balance:", account.get_balance())

account.deposit(2000)
print("Balance after deposit:", account.get_balance())

account.withdraw(1000)
print("Balance after withdrawal:", account.get_balance())
