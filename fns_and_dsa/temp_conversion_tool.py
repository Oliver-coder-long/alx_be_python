FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celcius):
  return celcius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
temp = int(input("enter the temperature:"))
temp_version = input("is it in celcius or fahrenheit?(Cel/fahr):")
if temp_version == "cel":
  convert_to_fahrenheit(temp)
elif temp_version == "fahr":
  convert_to_celcius(temp)
else:
  print("Enter a valid temperature unit from the two options.")
  
