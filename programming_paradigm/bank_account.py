class BankAccount:
  def __init__(self, account_balance, initial_balance = 0):
    self.account_balance = account_balance
    self.initial_balance = initial_balance
  def deposit(amount):
    return account_balance += amount
  def withdraw(amount):
    if amount >= account_balance:
      return account_balance -= amount
    else:
      return false
      print("You have insufficient funds")
  def display_balance():
    print (f"Current balance: ${amount}")
