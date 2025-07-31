# Ejercicios-de-python
Ejercicios de python
"""Programa que valide si una contraseña especificada por el usuario es segura.
Una contraseña segura:
-> Tiene mas de 8 caracteres
-> Tiene al menos una letra mayúscula
-> Tiene al menos un número"""

def comprobarContraseña(password):
    Largo = False
    mayus = False
    numer = False

    # Verificar si la contraseña tiene más de 8 caracteres
    if len(password) > 8: # Corregido: Debe ser > 8, no > 0
        Largo = True

    # Iterar sobre cada caracter de la contraseña para verificar mayúsculas y números
    for caracter in password: # Uso de 'caracter' para mayor claridad
        if caracter.isupper():
            mayus = True
        if caracter.isnumeric():
            numer = True
    
    # Evaluar si todas las condiciones se cumplen
    if Largo and mayus and numer:
        return True
    else:
        return False

# Solicitar al usuario que ingrese una contraseña
password = input("Ingrese una contraseña:")

# Llamar a la función para verificar la contraseña
verificacion = comprobarContraseña(password)


# Imprimir el resultado de la verificación
if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")

"""
1
1 2
1 2 3
1 2 3 4
"""
lineas = int(input("Cuantas lineas tendra el traingulo?"))
for i in range(lineas):
    print("*" * (i+1))

print("Ingrese un numero")
num = int(input())
fact=1
for i in range(1, num+1):
    fact*=i
print("El factorial de",num,"es:",fact)

import random

def jugar_piedra_papel_tijera():
    lista = ['Piedra', 'Papel', 'Tijera']

    while True:
        computadora = random.choice(lista)
        jugador = None

        while jugador not in [item.lower() for item in lista]: # Convert lista items to lowercase for comparison
            jugador_raw = input('roca, papel o tijera?: ').lower()
            if jugador_raw in ['roca', 'piedra']: # Handle 'roca' as an alias for 'Piedra'
                jugador = 'piedra'
            elif jugador_raw in ['papel']:
                jugador = 'papel'
            elif jugador_raw in ['tijera']:
                jugador = 'tijera'
            else:
                print("Entrada inválida. Por favor, elige roca, papel o tijera.")

        print('Computadora:', computadora)
        print('Jugador:', jugador.capitalize()) # Capitalize for consistent output

        if jugador == computadora.lower(): # Compare lowercase versions for consistency
            print('Empate!')
        elif (jugador == 'piedra' and computadora.lower() == 'tijera') or \
             (jugador == 'papel' and computadora.lower() == 'piedra') or \
             (jugador == 'tijera' and computadora.lower() == 'papel'):
            print('Ganaste!')
        else:
            print('Perdiste!')

        jugar_de_nuevo = input('Quieres jugar de nuevo? (si/no): ').lower()
        if jugar_de_nuevo != 'si':
            break

# Call the function to start the game
jugar_piedra_papel_tijera()

import random
aleatorio = random.randint(1,100)

while True:
    num = int(input("Ingrese un numero entre 1 y 100"))
    if num == aleatorio:
        print("Felicidades adivinaste el numero!")
    elif num < aleatorio:
        print("El numero es mayor, Intenta nuevamente")
    else:
        print("El numero es menor, Intenta nuevamente")
print("Fin del juego!")
    
        

frase=input("Ingrese la frase a utilizar:")
contador=0
for i in frase:
    if i in "aeiou":
        contador=contador+1
        print("La cantidad de vocales son:",contador)
