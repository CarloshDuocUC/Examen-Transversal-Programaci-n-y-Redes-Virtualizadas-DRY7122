import math

# Coordenadas de las ciudades (latitud y longitud)
ciudades = {
    "Santiago, Chile": (-33.4489, -70.6693),
    "Buenos Aires, Argentina": (-34.6037, -58.3816),
    "Valparaíso, Chile": (-33.0472, -71.6127),
    "Mendoza, Argentina": (-32.8895, -68.8458)
    # Puedes añadir más ciudades aquí
}

def haversine(coord1, coord2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convertir coordenadas de grados a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Diferencias
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distancia en kilómetros
    distance_km = R * c
    # Distancia en millas
    distance_miles = distance_km * 0.621371

    return distance_km, distance_miles

def tiempo_viaje(distancia_km, transporte):
    # Velocidades promedio en km/h
    velocidades = {
        "auto": 80,
        "avión": 800,
        "bicicleta": 20,
        "a pie": 5
    }
    velocidad = velocidades.get(transporte, 80)
    tiempo_horas = distancia_km / velocidad
    return tiempo_horas

def narrativa_viaje(ciudad_origen, ciudad_destino, distancia_km, distancia_miles, tiempo_horas, transporte):
    narrativa = f"""
    Viaje desde {ciudad_origen} hasta {ciudad_destino}:
    - Distancia: {distancia_km:.2f} km ({distancia_miles:.2f} millas)
    - Medio de transporte: {transporte}
    - Duración estimada del viaje: {tiempo_horas:.2f} horas
    """
    return narrativa

while True:
    print("\nIngrese 's' para salir en cualquier momento.")
    ciudad_origen = input("Ingrese la Ciudad de Origen: ")
    if ciudad_origen.lower() == 's':
        break
    ciudad_destino = input("Ingrese la Ciudad de Destino: ")
    if ciudad_destino.lower() == 's':
        break

    if ciudad_origen in ciudades and ciudad_destino in ciudades:
        coord_origen = ciudades[ciudad_origen]
        coord_destino = ciudades[ciudad_destino]
        distancia_km, distancia_miles = haversine(coord_origen, coord_destino)

        print("Seleccione el medio de transporte:")
        print("1. Auto")
        print("2. Avión")
        print("3. Bicicleta")
        print("4. A pie")
        transporte_opcion = input("Opción: ")
        transportes = { "1": "auto", "2": "avión", "3": "bicicleta", "4": "a pie" }
        transporte = transportes.get(transporte_opcion, "auto")

        tiempo_horas = tiempo_viaje(distancia_km, transporte)
        narrativa = narrativa_viaje(ciudad_origen, ciudad_destino, distancia_km, distancia_miles, tiempo_horas, transporte)

        print(narrativa)
    else:
        print("Una o ambas ciudades no están en la lista. Intente nuevamente.")
