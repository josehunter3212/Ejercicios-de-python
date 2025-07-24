#Leer dos numeros enteros y determinar cual es el mayor

a = int(input("Ingresa un numero:"))
b = int(input("Ingresa otro numero:"))

if a == b:
    print("Los numeros son iguales")
else:
    if a > b:
        print(f"El numero mayor es:{a}")
    else:
        print(f"El numero mayor es:{b}")
        
