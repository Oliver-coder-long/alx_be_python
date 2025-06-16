class BankAccount:
  def __init__(self, account_balance, balance = 0):
    self.account_balance = account_balance
    self.balance = balance
  def deposit(amount):
    account_balance += amount
    return account_balance
  def withdraw(amount):
    if amount >= account_balance:
      account_balance -= amount
      return account_balance
    else:
      return false
      print("You have insufficient funds")
  def display_balance(self):
        print(f"Current Balance: ${self.balance}")
