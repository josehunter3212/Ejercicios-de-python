
# metro_completo_jr.py
# Simulador del Metro de Caracas (Nivel Junior) con todas las estaciones del mapa

import collections

# --- 1. EL MAPA DEL METRO (ESTRUCTURA DE DATOS) ---
# Cada estación es una llave, y su valor es una lista de conexiones.
# Cada conexión es una tupla: (estación_vecina, tiempo_de_viaje, nombre_de_la_linea)
# Se incluye una penalización de 5 minutos para simular un cambio de línea.
metro_caracas = {
    # Línea 1 (Roja)
    "Propatria": [("Perez Bonalde", 2, "linea1")],
    "Perez Bonalde": [("Propatria", 2, "linea1"), ("Plaza Sucre", 2, "linea1")],
    "Plaza Sucre": [("Perez Bonalde", 2, "linea1"), ("Gato Negro", 2, "linea1")],
    "Gato Negro": [("Plaza Sucre", 2, "linea1"), ("Agua Salud", 2, "linea1")],
    "Agua Salud": [("Gato Negro", 2, "linea1"), ("Caño Amarillo", 2, "linea1")],
    "Caño Amarillo": [("Agua Salud", 2, "linea1"), ("Capitolio", 2, "linea1")],
    "Capitolio": [("Caño Amarillo", 2, "linea1"), ("El Silencio", 2, "linea1")], # Conexión con Línea 2 y 4
    "El Silencio": [("Capitolio", 2, "linea1"), ("La Hoyada", 2, "linea1"), ("Capuchinos", 2, "linea2"), ("Teatros", 2, "linea4")], # Estación de Transferencia
    "La Hoyada": [("El Silencio", 2, "linea1"), ("Parque Carabobo", 2, "linea1")],
    "Parque Carabobo": [("La Hoyada", 2, "linea1"), ("Bellas Artes", 2, "linea1")],
    "Bellas Artes": [("Parque Carabobo", 2, "linea1"), ("Colegio de Ingenieros", 2, "linea1")],
    "Colegio de Ingenieros": [("Bellas Artes", 2, "linea1"), ("Plaza Venezuela", 2, "linea1")],
    "Plaza Venezuela": [("Colegio de Ingenieros", 2, "linea1"), ("Sabana Grande", 2, "linea1"), ("Ciudad Universitaria", 2, "linea3"), ("Zona Rental", 2, "linea4")], # Estación de Transferencia
    "Sabana Grande": [("Plaza Venezuela", 2, "linea1"), ("Chacaito", 2, "linea1")],
    "Chacaito": [("Sabana Grande", 2, "linea1"), ("Chacao", 2, "linea1")],
    "Chacao": [("Chacaito", 2, "linea1"), ("Altamira", 2, "linea1")],
    "Altamira": [("Chacao", 2, "linea1"), ("Miranda", 2, "linea1")],
    "Miranda": [("Altamira", 2, "linea1"), ("Los Dos Caminos", 2, "linea1")],
    "Los Dos Caminos": [("Miranda", 2, "linea1"), ("Los Cortijos", 2, "linea1"), ("Boleita", 2, "linea5")], # Conexión con Línea 5 (proyectada)
    "Los Cortijos": [("Los Dos Caminos", 2, "linea1"), ("La California", 2, "linea1")],
    "La California": [("Los Cortijos", 2, "linea1"), ("Petare", 2, "linea1"), ("Warairarepano", 2, "linea5")], # Conexión con Línea 5 (proyectada)
    "Petare": [("La California", 2, "linea1"), ("Palo Verde", 2, "linea1"), ("Mariches", 5, "metrocable")], # Conexión con Metrocable
    "Palo Verde": [("Petare", 2, "linea1")],

    # Línea 2 (Verde)
    "Capuchinos": [("El Silencio", 2, "linea2"), ("Maternidad", 2, "linea2")],
    "Maternidad": [("Capuchinos", 2, "linea2"), ("Artigas", 2, "linea2")],
    "Artigas": [("Maternidad", 2, "linea2"), ("La Paz", 2, "linea2")],
    "La Paz": [("Artigas", 2, "linea2"), ("La Yaguara", 2, "linea2"), ("Ruiz Pineda", 2, "linea2")], # Conexión con la rama Las Adjuntas
    "La Yaguara": [("La Paz", 2, "linea2"), ("Carapita", 2, "linea2")],
    "Carapita": [("La Yaguara", 2, "linea2"), ("Antímano", 2, "linea2")],
    "Antímano": [("Carapita", 2, "linea2"), ("Mamera", 2, "linea2")],
    "Mamera": [("Antímano", 2, "linea2"), ("Caricuao", 2, "linea2")],
    "Caricuao": [("Mamera", 2, "linea2"), ("Zoológico", 2, "linea2")],
    "Zoológico": [("Caricuao", 2, "linea2")],
    "Ruiz Pineda": [("La Paz", 2, "linea2"), ("Las Adjuntas", 2, "linea2")], # Rama de la Línea 2
    "Las Adjuntas": [("Ruiz Pineda", 2, "linea2")],

    # Línea 3 (Amarilla)
    "Ciudad Universitaria": [("Plaza Venezuela", 2, "linea3"), ("Los Símbolos", 2, "linea3")],
    "Los Símbolos": [("Ciudad Universitaria", 2, "linea3"), ("La Bandera", 2, "linea3")],
    "La Bandera": [("Los Símbolos", 2, "linea3"), ("El Valle", 2, "linea3")],
    "El Valle": [("La Bandera", 2, "linea3"), ("Los Jardines", 2, "linea3")],
    "Los Jardines": [("El Valle", 2, "linea3"), ("Coche", 2, "linea3")],
    "Coche": [("Los Jardines", 2, "linea3"), ("Mercado", 2, "linea3")],
    "Mercado": [("Coche", 2, "linea3"), ("La Rinconada", 2, "linea3")],
    "La Rinconada": [("Mercado", 2, "linea3")],
    
    # Línea 4 (Azul)
    "Zona Rental": [("Plaza Venezuela", 2, "linea4"), ("Parque Central", 2, "linea4"), ("Bello Monte", 2, "linea5")], # Conexión con Línea 5 (proyectada)
    "Parque Central": [("Zona Rental", 2, "linea4"), ("Teatros", 2, "linea4")],
    "Teatros": [("Parque Central", 2, "linea4"), ("El Silencio", 2, "linea4"), ("Nueva Circo", 5, "buscaracas")], # Conexión con BusCaracas

    # Línea 5 (Morada - en proyecto)
    "Bello Monte": [("Zona Rental", 2, "linea5"), ("Las Mercedes", 2, "linea5")],
    "Las Mercedes": [("Bello Monte", 2, "linea5"), ("Tamanaco", 2, "linea5")],
    "Tamanaco": [("Las Mercedes", 2, "linea5"), ("Chuao", 2, "linea5")],
    "Chuao": [("Tamanaco", 2, "linea5"), ("Bello Campo", 2, "linea5")],
    "Bello Campo": [("Chuao", 2, "linea5"), ("Parque del Este II", 2, "linea5")],
    "Parque del Este II": [("Bello Campo", 2, "linea5"), ("Parque del Este", 2, "linea1")], # Conexión con Línea 1
    "Boleita": [("Los Dos Caminos", 2, "linea5"), ("El Marques", 2, "linea5")],
    "El Marques": [("Boleita", 2, "linea5"), ("La California", 2, "linea5")],
    "Warairarepano": [("La California", 2, "linea5")],

    # Conexiones adicionales (Metrocable, BusCaracas)
    "Mariches": [("Petare", 5, "metrocable")],
    "Nueva Circo": [("Teatros", 5, "buscaracas")],
}

# --- 2. EL BUSCADOR DE RUTAS (ALGORITMO BFS) ---
# (La lógica de esta función sigue siendo la misma y funciona perfectamente)
def planificar_ruta(origen, destino):
    """
    Busca la ruta más corta en estaciones usando el algoritmo BFS.
    """
    if origen not in metro_caracas or destino not in metro_caracas:
        return None
    if origen == destino:
        return {"ruta": [origen], "tiempo": 0, "estaciones": 1, "cambios": []}

    cola = collections.deque([(origen, [origen], 0, None)])
    visitadas = {origen}

    while cola:
        estacion_actual, ruta_actual, tiempo_total, linea_actual = cola.popleft()

        if estacion_actual == destino:
            cambios = []
            linea_anterior = None
            for i in range(len(ruta_actual)):
                estacion = ruta_actual[i]
                lineas_posibles = [linea for _, _, linea in metro_caracas.get(estacion, []) if metro_caracas.get(estacion)]
                if not lineas_posibles:
                    continue
                linea_proxima = lineas_posibles[0]
                if linea_anterior is not None and linea_proxima != linea_anterior:
                    cambios.append(f"Cambia en {estacion} a la línea {linea_proxima.replace('linea', '')}")
                linea_anterior = linea_proxima

            return {
                "ruta": ruta_actual,
                "tiempo": tiempo_total,
                "estaciones": len(ruta_actual),
                "cambios": list(set(cambios))
            }

        for estacion_siguiente, tiempo_viaje, linea_proxima in metro_caracas.get(estacion_actual, []):
            if estacion_siguiente not in visitadas:
                visitadas.add(estacion_siguiente)
                nueva_ruta = ruta_actual + [estacion_siguiente]
                nuevo_tiempo = tiempo_total + tiempo_viaje
                if linea_actual is not None and linea_proxima != linea_actual:
                    nuevo_tiempo += 5  # Penalización por cambio de línea
                cola.append((estacion_siguiente, nueva_ruta, nuevo_tiempo, linea_proxima))

    return None

def obtener_nombres_estaciones():
    return sorted(list(metro_caracas.keys()))


# --- 3. INTERFAZ DE USUARIO ---
def main():
    print("--- Simulador de Viajes en el Metro de Caracas ---")
    print("      (Incluye todas las líneas del mapa, incluso las proyectadas)")
    estaciones_disponibles = obtener_nombres_estaciones()

    while True:
        print("\nEstaciones disponibles:")
        print(", ".join(estaciones_disponibles))
        print("--------------------------------------------------")

        origen_input = input("Ingresa tu estación de origen: ").strip().title()
        destino_input = input("Ingresa tu estación de destino: ").strip().title()

        if origen_input not in estaciones_disponibles or destino_input not in estaciones_disponibles:
            print("¡Error! Una o ambas estaciones no son válidas. Intenta de nuevo.")
            continue

        resultado = planificar_ruta(origen_input, destino_input)

        if resultado:
            print("\n¡Ruta encontrada!")
            print(f"Origen: {origen_input}")
            print(f"Destino: {destino_input}")
            print(f"Ruta a seguir: {' -> '.join(resultado['ruta'])}")
            print(f"Estaciones a recorrer: {resultado['estaciones']}")
            print(f"Tiempo total estimado: {resultado['tiempo']} minutos")

            if resultado['cambios']:
                print("\nNecesitas hacer los siguientes cambios de línea:")
                for cambio in resultado['cambios']:
                    print(f"- {cambio}")
            else:
                print("\n¡No necesitas hacer cambios de línea!")
        else:
            print("\nNo se pudo encontrar una ruta entre esas estaciones. Intenta con otras.")

        otra_vez = input("\n¿Quieres planificar otro viaje? (s/n): ").lower()
        if otra_vez != 's':
            print("¡Gracias por usar el simulador! ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
