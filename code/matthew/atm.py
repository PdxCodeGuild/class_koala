# filename: atm.py

class Atm:
    def __init__(self, balance=0):
        """initializes with default balance of zero"""
        self.b = balance

    def check_balance(self):
        """returns current balance"""
        return self.b

    def deposit(self, amount):
        """adds specified amount to current balance"""
        self.b += amount

    def check_withdrawal(self, amount):
        """checks if the subtraction of the specified amount would place the balance in negative; if not, returns True"""
        if self.b - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        """subtracts specified amount from current balance"""
        self.b -= amount

# ***** TEST CASES *****
# atm = Atm()
# print(atm.check_balance())
# atm.deposit(100)
# print(atm.check_balance())
# atm.deposit(100)
# print(atm.check_balance())
# print(atm.check_withdrawal(150))
# atm.withdraw(150)
# print(atm.check_balance())
# print(atm.check_withdrawal(150))
# atm.withdraw(150)
# print(atm.check_balance())
