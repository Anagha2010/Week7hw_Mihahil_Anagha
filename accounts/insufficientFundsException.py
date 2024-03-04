# User defined exception class inherits from built-in base class Exception

# class definition
class InsufficientFundsException(Exception):
    # constructor
    def __init__(self, breach_amount):
        self.breach_amount = breach_amount

    # getters and setters
    def get_breach_amount(self):
        return self.breach_amount

    def set_breach_amount(self, breach_amount):
        self.breach_amount = breach_amount
