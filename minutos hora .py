# Solicitar al usuario que ingrese el tiempo en segundos
try:
    segundos_totales = int(input("Dime el tiempo en segundos: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
else:
    # Calcular los minutos totales
    minutos_totales = segundos_totales // 60

    # Calcular los segundos restantes
    segundos_resto = segundos_totales % 60

    # Calcular las horas
    horas = minutos_totales // 60

    # Calcular los minutos restantes
    minutos_resto = minutos_totales % 60

    # Imprimir el resultado
    print(f"{horas} horas, {minutos_resto} minutos, {segundos_resto} segundos")
