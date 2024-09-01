def mostrar_hoteles(vuelo_id):
    print("Hoteles disponibles:")
    for id_hotel, info in hoteles.items():
        if info['vuelo_id'] == vuelo_id:
            print(f"{id_hotel}: {info['nombre']} - Precio por noche: {info['precio_noche']}US$")