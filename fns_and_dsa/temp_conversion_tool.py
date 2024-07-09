FAHRENHEIT_TO_CELSIUS_FACTOR = 0.56
CELSIUS_TO_FAHRENHEIT_FACTOR = 1.8

def convert_to_celsius(fahrenheit):
     result = (fahreinheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahreinheit(celsius):
     result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert: "))
symbol = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature == True and symbol == "F":
    convert_to_celsius(temperature)
    print(f"{temperature} is {result}°C")
elif temperature == True and symbol == "C":
    convert_to_fahreinheit(temperature)
    print(f"{temperature} is {result}°F")
else:
     print("Invalid temperature. Please enter a numeric value.")

