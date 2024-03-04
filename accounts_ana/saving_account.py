# importing base class and used class for exception
from accounts_ana.account import Account
from accounts_ana.insufficientFundsException import InsufficientFundsException

# Class definition
class SavingAccount(Account):
    # class variable
    min_balance = 500

    # Class constructor
    def __init__(self, amount, firstname, lastname, rate=0.05):
        # calling base class constructor
        super().__init__(amount, firstname, lastname)
        self.int_rate = rate
        self.interest = 0

    #     Add getters and setters here

    # methods

    # withdraw method overrides the same method of base class
    def withdraw(self, amount):
        if amount > 0 and self._balance - amount > SavingAccount.min_balance:
            self._balance -= amount
        else:
            breach_amount = SavingAccount.min_balance - (self._balance - amount)
            raise InsufficientFundsException(breach_amount)

    # method to calculate yearly interest
    def calculate_interest(self):
        self.interest = (super().get_balance()*self.int_rate*1)     # P*R*T
        return f"\nInterest Earned by {self.get_lastname()} in one year: Galleons {self.interest}"


