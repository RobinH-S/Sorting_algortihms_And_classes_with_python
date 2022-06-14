class BankAccount:


    def __init__(self, number):
        self.number = number
        self.balance = 0

    def set_balance(self, new_b):
        self.balance = new_b

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print('Balance for the account', self.number)
        print('is ', self.balance, 'NOK')

my_account = BankAccount(45000932)
my_account.deposit(5000)
my_account.withdraw(1400)
my_account.print_balance()