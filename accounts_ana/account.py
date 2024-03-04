# imports an exception class
from accounts_ana.insufficientFundsException import InsufficientFundsException

# Class definition
class Account:

    # CONSTRUCTOR
    def __init__(self, initial_amount, firstname, lastname):
        self._balance = initial_amount
        self.first_name = firstname
        self.__last_name = lastname

    # method
    def deposit(self, amount):
        self._balance += amount

    # method
    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >= 0:
            self._balance -= amount
        else:
            breach_amount = self._balance - amount
            raise InsufficientFundsException(breach_amount)

    # getters and setters
    def get_balance(self):
        return self._balance

    def get_firstname(self):
        return self.first_name

    def set_firstname(self, firstname):
        self.first_name = firstname

    def get_lastname(self):
        return self.__last_name.upper()

    # overriding a built-in method to display object in readable form
    def __str__(self):
        return f"\nAccount\nFirstname: {self.get_firstname()}\nLastname: {self.get_lastname()}" \
               f"\nBalance: ${self.get_balance()}\n{'*'*30}"

    # method to do operator overloading of add for objects
    def __add__(self, other):
        return self._balance + other.get_balance()
