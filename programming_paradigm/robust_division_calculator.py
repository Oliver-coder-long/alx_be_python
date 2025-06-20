def safe_divide(numerator,denomenator):
  numerator = float(numerator)
  denomenator = float(denomenator)
  return numerator/denomenator
  try:
    if "denomenator" == 0:
      raise ZeroDivisionError("Cannot divide by zero")
    else:
      return numerator/denomenator
  except:
    print("Cannot divide a number by zero.")
  try:
    if denomenator or numerator not int or float:
      raise ValueError("Please enter numeric values only.")
