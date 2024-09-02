def showHotels(flightId, hotels):
   availableIds = []

   print("\n- HOTELES DISPONIBLES -\n")
   for hotelId, hotelData in hotels.items():
      if hotelData['flightId'] == flightId:
         print(f"{hotelId}: {hotelData['name']} - Precio por noche: {hotelData['pricePerNight']} USD$")
         availableIds.append(hotelId)
   
   return availableIds