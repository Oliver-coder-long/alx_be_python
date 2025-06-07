FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celcius):
  return celcius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
temp = int(input("Enter the temperature to convert:"))
temp_version = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if temp_version == "C":
  convert_to_fahrenheit(temp)
elif temp_version == "F":
  convert_to_celcius(temp)
else:
  print("Enter a valid temperature unit from the two options.")
  
