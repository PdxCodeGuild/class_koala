class ATM:
    def __init__(self, name):
        self.balance = 0
        self.name = name
        self.check = False
        
        self.transactions_list = []

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        
        self.transactions_list.append(f"{self.name} deposited ${amount}")
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.check = True
            return(self.check)
           
    def withdrawal(self, amount):
        if self.check_withdrawal(amount) == True:
            self.balance -= amount
            self.transactions_list.append(f"{self.name} withdrew ${amount}")
            return self.balance
        else:
            print( " not enough sorry ")

    def print_transactions(self):
        for each in self.transactions_list:
            print(each)

    def repl(self):
        while True:
            x = input("What would you like to do? \ndeposit, withdrawal, check balance, history, or finished => ")
            if x == "deposit":
                amount = int(input("how much would you like to deposit? => "))
                self.deposit(amount)
            elif x == "withdrawal":
                amount = int(input("how much would you like to withdrawal? => "))
                self.withdrawal(amount)
            elif x == "check balance":
                self.check_balance()
            elif x == "history":
                self.print_transactions()
            elif x == "finished":
                break
            else:
                print("Please try again")

account_name = input("enter your acount name => ")
a1 = ATM(account_name)
a1.repl() 