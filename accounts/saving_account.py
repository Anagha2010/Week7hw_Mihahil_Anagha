from accounts.account import Account
from accounts.insufficientFundsException import InsufficientFundsException

class SavingAccount(Account):
    min_balance = 500

    def __init__(self, amount, firstname, lastname):
        super().__init__(amount, firstname, lastname)

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount > SavingAccount.min_balance:
            self._balance -= amount
        else:
            breach_amount = SavingAccount.min_balance - (self._balance - amount)
            raise InsufficientFundsException(breach_amount)

