class BankAccount:
  def __init__(self, account_balance, balance = 0):
    self.account_balance = account_balance
    self.balance = balance
  def deposit(amount):
    self.balance += amount
    return self.balance
  def withdraw(amount):
    if amount >= account_balance:
      self.balance -= amount
      return self.balance
    else:
      return false
      print("You have insufficient funds")
  def display_balance(self):
        print(f"Current Balance: ${self.balance}")
