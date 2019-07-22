# filename: atm.py

class Atm:
    def __init__(self, balance=0, transactions=[]):
        """initializes with default balance of zero and an empty transaction list"""
        self.b = balance
        self.t = transactions

    def check_balance(self):
        """returns current balance"""
        return self.b

    def deposit(self, amount):
        """adds specified amount to current balance / appends transaction statement"""
        self.b += amount
        self.t.append(f"user deposited ${amount}")

    def check_withdrawal(self, amount):
        """checks if the subtraction of the specified amount would place the balance in negative; if not, returns True"""
        if self.b - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        """subtracts specified amount from current balance / appends transaction statement"""
        self.b -= amount
        self.t.append(f"user withdrew ${amount}")

    def print_transactions(self):
        """prints a list of all transactions"""
        print(self.t)


# ***** TEST CASES *****
# atm = Atm()
# print(atm.check_balance())
# atm.deposit(50)
# atm.deposit(100)
# atm.withdraw(125)
# atm.deposit(175)
# atm.withdraw(150)
# print(atm.check_balance())
# atm.print_transactions()
