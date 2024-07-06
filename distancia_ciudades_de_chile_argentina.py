import math

# Coordenadas de las ciudades (latitud y longitud)
# Ejemplo: Santiago, Chile y Buenos Aires, Argentina
ciudades = {
    "Santiago, Chile": (-33.4489, -70.6693),
    "Buenos Aires, Argentina": (-34.6037, -58.3816)
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
    distance = R * c

    return distance

# Coordenadas de las ciudades de interés
ciudad_chile = "Santiago, Chile"
ciudad_argentina = "Buenos Aires, Argentina"

coord_chile = ciudades[ciudad_chile]
coord_argentina = ciudades[ciudad_argentina]

# Calcular la distancia
distancia = haversine(coord_chile, coord_argentina)

print(f"La distancia entre {ciudad_chile} y {ciudad_argentina} es de {distancia:.2f} km.")

