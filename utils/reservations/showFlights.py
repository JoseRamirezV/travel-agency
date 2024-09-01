def mostrar_vuelos():
    print("Vuelos disponibles:")
    for id_vuelo, info in vuelos.items():
        print(f"{id_vuelo}: {info['origen']} a {info['destino']} - Precio: {info['precio']}US$")