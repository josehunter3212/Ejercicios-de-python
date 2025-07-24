def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): El peso de la persona en kilogramos.
        altura (float): La altura de la persona en metros.

    Returns:
        float: El valor del IMC calculado.
    """
    return peso / (altura * altura)

def nivel_de_peso(imc):
    """
    Clasifica el nivel de peso de una persona según su IMC.

    Args:
        imc (float): El valor del Índice de Masa Corporal.

    Returns:
        str: La clasificación del nivel de peso (ej. "bajo peso", "normal").
    """
    if imc < 18.5:
        return "bajo peso"
    elif 18.5 <= imc < 25:
        return "normal"
    elif 25 <= imc < 30:
        return "sobrepeso"
    else:
        return "obesidad"

# Solicitar al usuario que ingrese su peso y altura
try:
    peso_usuario = float(input("Ingresa tu peso en kilogramos: "))
    altura_usuario = float(input("Ingresa tu altura en metros: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa números para el peso y la altura.")
else:
    # Calcular el IMC
    imc_calculado = calcular_imc(peso_usuario, altura_usuario)

    # Obtener el nivel de peso
    clasificacion_peso = nivel_de_peso(imc_calculado)

    # Imprimir el resultado
    print(f"Su IMC es: {imc_calculado:.2f}") # Se formatea a 2 decimales para una mejor lectura
    print(f"Su nivel de peso es: {clasificacion_peso}")
