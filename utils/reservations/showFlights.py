def showFLights(flights):
   print("\n- VUELOS DISPONIBLES -\n")
   for flightId, flightData in flights.items():
      print(f"{flightId}: {flightData['origin']} a {flightData['destiny']} - Precio: {flightData['price']} USD$ - Asientos disponibles: {flightData['seatsAvailable']}")