def safe_divide(numerator,denomenator):
  if denominator == 0:
        return "Error: Cannot divide by zero"
    return numerator / denominator
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
