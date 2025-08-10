import random

# Uso de diccionarios para datos más claros y legibles
lista_de_dinosaurios = [
    {
        "nombre_comun": "spinosaurus",
        "especie": "Spinosaurus",
        "dieta": "carnivoro",
        "periodo": "cretacico",
        "temperamento": "hostil"
    },
    {
        "nombre_comun": "triceraptor",
        "especie": "Prorsus",
        "dieta": "herbivoro",
        "periodo": "cretacico",
        "temperamento": "hostil"
    },
    {
        "nombre_comun": "velociraptor",
        "especie": "Raptor",
        "dieta": "carnivoro",
        "periodo": "cretacico",
        "temperamento": "hostil"
    },
    {
        "nombre_comun": "stegosaurus",
        "especie": "Armatus",
        "dieta": "herbivoro",
        "periodo": "jurasico",
        "temperamento": "pacifico"
    },
    {
        "nombre_comun": "mosasaurus",
        "especie": "Mosasaurus",
        "dieta": "carnivoro",
        "periodo": "cretacico",
        "temperamento": "hostil"
    }
]

def buscar_dinosaurio(lista, campo, valor):
    """Función genérica para buscar dinosaurios por un campo y valor específicos."""
    return [dino for dino in lista if dino.get(campo) == valor]

def buscar_por_nombre(lista_de_dinosaurios):
    nombre = input("Introduzca el nombre del dinosaurio: ").lower()
    
    for dino in lista_de_dinosaurios:
        if dino["nombre_comun"] == nombre:
            print("\n--- Dinosaurio Encontrado ---")
            print(f"Nombre: {dino['nombre_comun'].capitalize()}, Especie: {dino['especie']}, Dieta: {dino['dieta']}, Periodo: {dino['periodo']}, Temperamento: {dino['temperamento']}")
            return dino
    
    print("\nEl dinosaurio no se encuentra en la lista.")
    return None

def buscar_y_mostrar(lista_de_dinosaurios, campo, titulo):
    """Función para manejar la entrada del usuario, la búsqueda y la impresión."""
    
    opciones_validas = sorted(list(set(dino[campo] for dino in lista_de_dinosaurios)))
    
    entrada = None
    while entrada not in opciones_validas:
        entrada = input(f"Introduzca el {campo} ({', '.join(opciones_validas)}): ").lower()
    
    dinosaurios_encontrados = buscar_dinosaurio(lista_de_dinosaurios, campo, entrada)
    
    if dinosaurios_encontrados:
        print(f"\n--- Dinosaurios {titulo.capitalize()}s ---")
        for dino in dinosaurios_encontrados:
            print(f"Nombre: {dino['nombre_comun'].capitalize()}, Especie: {dino['especie']}, Dieta: {dino['dieta']}, Periodo: {dino['periodo']}, Temperamento: {dino['temperamento']}")
    else:
        print(f"\nNo se encontraron dinosaurios con ese {campo}.")

def simular_encuentro(dinosaurio):
    if dinosaurio:
        print(f"\n¡Has encontrado un {dinosaurio['nombre_comun'].capitalize()}!")
        if dinosaurio['temperamento'] == "hostil":
            print(f"¡Cuidado! El {dinosaurio['nombre_comun'].capitalize()} es hostil y te ataca.")
            print("Fin del encuentro.")
        else:
            print(f"El {dinosaurio['nombre_comun'].capitalize()} es pacífico y se aleja. Todo está bien.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Buscar por nombre y simular encuentro")
        print("2. Buscar por dieta")
        print("3. Buscar por periodo")
        print("4. Buscar por temperamento")
        print("5. Salir")
        
        try:
            user_option = int(input("Seleccione una opción: "))
            
            if user_option == 1:
                dino_encontrado = buscar_por_nombre(lista_de_dinosaurios)
                if dino_encontrado:
                    simular_encuentro(dino_encontrado)
            elif user_option == 2:
                buscar_y_mostrar(lista_de_dinosaurios, "dieta", "Dieta")
            elif user_option == 3:
                buscar_y_mostrar(lista_de_dinosaurios, "periodo", "Periodo")
            elif user_option == 4:
                buscar_y_mostrar(lista_de_dinosaurios, "temperamento", "Temperamento")
            elif user_option == 5:
                print("Saliendo del programa. ¡Adiós!")
                break
            else:
                print("Opción no válida. Por favor, elija un número del 1 al 5.")
        
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número.")

if __name__ == "__main__":
    menu_principal()
