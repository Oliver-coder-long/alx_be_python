class BankAccount:
  def __init__(self, account_balance, balance = 0):
    self.account_balance = balance
  def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
  def withdraw(self, amount):
    if amount >= account_balance:
      self.__account_balance -= amount
      return self.__account_balance
    else:
      return false
      print("You have insufficient funds")
  def display_balance(self):
        print(f"Current Balance: ${self.balance}")
