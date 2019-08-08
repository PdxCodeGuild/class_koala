# filename: atm.py

class Atm:
    def __init__(self, balance=0, transactions=[]):
        """initializes with default balance of zero and an empty transaction list"""
        self.b = balance
        self.t = transactions

    def check_balance(self):
        """returns current balance with two decimal places"""
        return "\nCurrent balance: ${:.2f}".format(self.b)

    def deposit(self, amount):
        """adds specified amount to current balance / appends transaction statement"""
        self.b += amount
        self.t.append("user deposited ${:.2f}".format(amount))

    def check_withdrawal(self, amount):
        """checks if the subtraction of the specified amount would place the balance in negative; if not, returns True"""
        if self.b - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        """subtracts specified amount from current balance / appends transaction statement"""
        self.b -= round(amount, 2)
        self.t.append("user withdrew ${:.2f}".format(amount))

    def print_transactions(self):
        """prints a list of all transactions"""
        print(f"\n{self.t}")


atm = Atm()
while True:
    action = input("\n(Select from: 'deposit', 'withdraw', 'check balance', 'history')\nWhich transaction would you like to perform today? ").lower()

    if action.startswith("d"):
        amount = float(input("\nHow much would you like to deposit? "))
        atm.deposit(amount)
    elif action.startswith("w"):
        amount = float(input("\nHow much would you like to withdraw? "))
        atm.withdraw(amount)
    elif action.startswith("c"):
        print(atm.check_balance())
    elif action.startswith("h"):
        atm.print_transactions()
    else:
        print("\nValid transaction type not received... please try again.")
        continue

    again = input("\nWould you like to perform another transaction? (y or n) ").lower()
    if again.startswith("n"):
        print("\nTransaction(s) complete. Please visit again soon.\n")
        quit()
