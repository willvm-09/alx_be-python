FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHREINHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
     result = fahreinheit - 32 * FAHRENHEIT_TO_CELSIUS_FACTOR
     return result

def convert_to_fahreinheit(celsius):
     result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
     return result

temperature = float(input("Enter the temperature to convert: "))
symbol = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if symbol == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature} is {converted_temp}C")
elif symbol == "C":
    converted_temp = convert_to_fahreinheit(temperature)
    print(f"{temperature} is {converted_temp}F")
else:
     print("Invalid temperature. Please enter a numeric value.")

