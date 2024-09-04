def createTourPackage():
    destination = input("Ingrese el destino del paquete: ")
    hasFlight = input("¿Incluye vuelo?(S/N): ").upper() == "S"
    hasHotel = input("¿Incluye reserva de hotel?(S/N): ").upper() == "S"
    
    #Pedir un dato mayor a 0 y válido
    while True:
        try:    
            price = float(input("Ingrese el precio del paquete: "))
            if  price < 0:
                print("El precio no puede ser negativo")
            else:
                tourPackage = {
                    "destination": destination,
                    "hasFlight": hasFlight,
                    "hasHotel": hasHotel,
                    "price": price
                }
                return tourPackage
        
        except ValueError:
            print("El precio debe ser un valor numérico")

            
