FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9, 9/5

def convert_to_celsius(fahrenheit):
    to_celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{temperature}°F is {to_celsius}°C')

def convert_to_fahrenheit(celsius):
    to_fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f'{temperature}°C is {to_fahrenheit}°F')

temperature = float(input('Enter the temperature to convert: '))
Celsius_or_Fahrenheit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')

if Celsius_or_Fahrenheit == 'F':
    convert_to_celsius(temperature)
elif Celsius_or_Fahrenheit == 'C':
    convert_to_fahrenheit(temperature)
else:
    print('erroe')