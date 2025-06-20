def safe_divide(numerator,denomenator):
  numerator = float(numerator)
  denomenator = float(denomenator)
  try:
    if denomenator == 0:
      raise ZeroDivisionError("Cannot divide by zero")
    else:
      return("The result of the division is", numerator/denomenator)
  except:
    print("Cannot divide a number by zero.")
  try:
    if denomenator or numerator not int or float:
      raise ValueError("Please enter numeric values only.")
