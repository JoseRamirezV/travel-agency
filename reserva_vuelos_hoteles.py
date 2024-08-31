#reserva_vuelos_hoteles
vuelos = {
    "1": {"origen": "Cali(Colombia)", "destino": "Barcelona(españa)", "precio": 857},
    "2": {"origen": "Cali(Colombia)", "destino": "cancun(mexico)", "precio": 343},
    "3": {"origen": "Cali(Colombia)", "destino": "Londres(inglaterra)", "precio": 1100},
}

hoteles = {

    "1": {"nombre": "Hotel Plaza", "precio_noche": 150, "vuelo_id": "1"},
    "2": {"nombre": "Hotel Sol", "precio_noche": 100, "vuelo_id": "1"},
    "3": {"nombre": "Hotel Mar", "precio_noche": 200, "vuelo_id": "1"},
    "4": {"nombre": "Hotel Barcelona Center", "precio_noche": 180, "vuelo_id": "1"},

    "5": {"nombre": "Hotel Cancun Beach", "precio_noche": 120, "vuelo_id": "2"},
    "6": {"nombre": "Hotel Caribe", "precio_noche": 140, "vuelo_id": "2"},
    "7": {"nombre": "Hotel Solymar", "precio_noche": 130, "vuelo_id": "2"},
    "8": {"nombre": "Hotel Selina", "precio_noche": 75, "vuelo_id": "2"},

    "9": {"nombre": "Hotel London Eye", "precio_noche": 250, "vuelo_id": "3"},
    "10": {"nombre": "Hotel Big Ben", "precio_noche": 260, "vuelo_id": "3"},
    "11": {"nombre": "Hotel Westminster", "precio_noche": 240, "vuelo_id": "3"},
    "12": {"nombre": "Hotel Park Plaza", "precio_noche": 245, "vuelo_id": "3"},
}
def mostrar_vuelos():
    print("Vuelos disponibles:")
    for id_vuelo, info in vuelos.items():
        print(f"{id_vuelo}: {info['origen']} a {info['destino']} - Precio: {info['precio']}US$")

def mostrar_hoteles(vuelo_id):
    print("Hoteles disponibles:")
    for id_hotel, info in hoteles.items():
        if info['vuelo_id'] == vuelo_id:
            print(f"{id_hotel}: {info['nombre']} - Precio por noche: {info['precio_noche']}US$")

def reservar():
    mostrar_vuelos()
    vuelo_id = input("Selecciona el ID del vuelo que deseas reservar: ")

    if vuelo_id in vuelos:
        vuelo = vuelos[vuelo_id]
        puestos = int(input("¿Cuántos puestos deseas reservar? "))
        costo_vuelo = vuelo['precio'] * puestos
        print(f"Has reservado {puestos} puesto(s) de {vuelo['origen']} a {vuelo['destino']} por un total de {costo_vuelo}US$.")
    else:
        print("ID de vuelo no válido.")
        return

    mostrar_hoteles(vuelo_id)
    hotel_id = input("Selecciona el ID del hotel que deseas reservar: ")

    if hotel_id in hoteles and hoteles[hotel_id]['vuelo_id'] == vuelo_id:
        noches = int(input("¿Cuántas noches deseas reservar? "))
        hotel = hoteles[hotel_id]
        costo_total = hotel['precio_noche'] * noches
        costo_total += costo_vuelo
        print(f"Has reservado {noches} noches en {hotel['nombre']} y {puestos} puesto(s) en el vuelo por un total de {costo_total}US$.")
    else:
        print("ID de hotel no válido o el hotel no está disponible para este vuelo.")

reservar()