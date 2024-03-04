from accounts.account import Account
from accounts.saving_account import SavingAccount
from accounts.insufficientFundsException import InsufficientFundsException

harry_acc = SavingAccount(2000, 'Harry', 'Potter')
ron_acc = Account(1000, 'Ronald', 'Weasley')
print(ron_acc.__add__(harry_acc))

try:
    harry_acc.withdraw(1400)
    print(harry_acc)
    harry_acc.deposit(200)
    # harry_acc.withdraw(500)

    ron_acc.withdraw(1000)
    ron_acc.withdraw(-500)
    print(ron_acc)

except InsufficientFundsException as ex:
    print(f'\n{"!" * 50}\nWarning: exception has occurred.'
          f'\nYou have tried to breach minimum balance by ${ex.get_breach_amount()}')
finally:
    print(f"\nAs per requirement you must maintain a minimum balance of "
          f"${SavingAccount.min_balance} in savings account. There is no such"
          f"requirement for other accounts.\nThank you for banking with us!")


