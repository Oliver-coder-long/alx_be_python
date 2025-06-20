class BankAccount:
    def __init__(self, account_balance, balance = 0):
        self.account_balance = account_balance
        self.balance = balance
    def deposit(self, amount):
        account_balance += amount
        print(f"Deposited: ${self.amount}")
    def withdraw(self, amount):
        if self.balance >= amount:
            account_balance -= amount
            print(f"Withdrew: ${self.amount}")
        else:
           print("Insufficient funds")
    def display_balance(self):
        print(f"[Current balance: ${balance}]")
