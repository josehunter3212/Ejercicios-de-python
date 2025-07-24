# Solicitar al usuario que ingrese la temperatura en grados Celsius
try:
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número.")
else:
    # Convertir Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Convertir Celsius a Kelvin
    kelvin = celsius + 273.15

    # Imprimir los resultados
    print(f"{celsius}°C es igual a {fahrenheit}°F")
    print(f"{celsius}°C es igual a {kelvin}K")
