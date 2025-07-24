# Solicitar al usuario que ingrese las tres notas
try:
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
except ValueError:
    print("Entrada inválida. Por favor, ingrese números para las notas.")
else:
    # Calcular el promedio de las notas
    promedio = (nota1 + nota2 + nota3) / 3

    # Mostrar el promedio
    print(f"El promedio de las notas es: {promedio:.2f}")

    # Verificar si el alumno aprueba o reprueba
    if promedio >= 3.0:
        print("¡Felicidades! El alumno ganó la materia.")
    else:
        print("Lo siento, el alumno perdió la materia.")
