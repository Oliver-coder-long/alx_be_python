num1 = input ("Enter the first number: ")
num2 = input ("Enter the second number: ")
operation = input ("Choose the operation (+, -, *, /): ")
match operation:
  case "+":
    print ("The result is {num1 + num2}")
  case "-":
    print ("The result is {num1 - num2}")
  case "*":
    print ("The result is {num1 * num2}")
  case "/":
    print ("The result is {num1/num2}" if num2 > 0)
