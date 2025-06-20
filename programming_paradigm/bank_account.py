class BankAccount:
    def __init__(self, account_balance, balance = 0):
        self.account_balance = account_balance
        self.balance = balance
    def deposit(self, amount):
        self.__account_balance() += amount
        print(f"Deposited: ${self.amount}")
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.__account_balance() -= amount
            print(f"Withdrew: ${self.amount}")
            return True
        else:
           print("Insufficient funds")
           return False
    def display_balance(self):
        print(f"[Current Balance: ${self.account_balance}]")
