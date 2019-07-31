class Atm:
    def __init__(self, balance = 0, transactions = []):
        self.balance = float(balance)
        self.transactions = transactions

    def check_balance(self):
        return (f'Current balance is ${self.balance}')
        
    def deposit(self, amount):
        self.balance += float(amount)
        self.transactions.append(f'User deposited ${amount}.')
        self.print_transactions()

    def check_withdrawal(self, amount):
        result = self.balance - float(amount)
        if result >= 0:
            return True
        return False

    def withdraw(self, amount):
        self.balance -= float(amount)
        # while self.check_withdrawal(True):
        self.transactions.append(f'User withdrew ${amount}.')

    def print_transactions(self):
        print(self.transactions[-1])


print(f'######## WELCOME TO YOUR ACCOUNT ON THE ATM ########\n')
print('Actions: ')
print(f'Check Balance')
print(f'Deposit')
print(f'Withdraw')
print(f'History')
print(f'Exit')

choice = input(f'\nWhat would you like to do? ').lower()

atm = Atm()
    
if choice == 'check balance':
    print(atm.check_balance())
elif choice == 'deposit':
    amount = float(input('How much would you like to deposit? '))
    atm.deposit(amount)   
elif choice == 'withdraw':
    amount = float(input('How much would you like to withdraw?'))
    print(atm.withdraw(amount))
elif choice == 'history':
    atm.print_transactions()

