# importing all classes
from accounts.account import Account
from accounts.saving_account import SavingAccount
from accounts.insufficientFundsException import InsufficientFundsException

# instantiating class SavingAccount with two objects
harry_acc = SavingAccount(2000, 'Harry', 'Potter')
ron_acc = Account(1000, 'Ronald', 'Weasley')

# Calling SavingAccount method on its object
print(harry_acc.calculate_interest())

# Adding the two objects and printing
print(f"\nAdding two accounts to see combined funds..."
      f"\nTotal amount available in Galleons: {ron_acc.__add__(harry_acc)}")

# try and catch block for exception handling - withdraw method potentially throws exception
try:
    harry_acc.withdraw(1400)
    print(harry_acc)
    harry_acc.deposit(200)
    # harry_acc.withdraw(500)

    ron_acc.withdraw(1000)
    ron_acc.withdraw(-500)
    print(ron_acc)

# following block will be executed to catch exception for insufficient funds should it occur
except InsufficientFundsException as ex:
    print(f'\n{"!" * 50}\nWarning: exception has occurred.'
          f'\nYou have tried to breach minimum balance by ${ex.get_breach_amount()}')

# finally block is always executed
finally:
    print(f"\nUnlike other account types, there is a requirement for minimum balance of "
          f"${SavingAccount.min_balance} in savings account.\nThank you for banking with us!")


