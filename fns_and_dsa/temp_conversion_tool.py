FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input('Enter the temperature to convert: '))
Celsius_or_Fahrenheit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

if Celsius_or_Fahrenheit == 'F':
    convert_to_celsius(temperature)
elif Celsius_or_Fahrenheit == 'C':
    convert_to_fahrenheit(temperature)
else:
    print('Error: Please enter "C" for Celsius or "F" for Fahrenheit.')