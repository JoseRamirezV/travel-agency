from utils.reservations.showHotels import showHotels

def hotelReservation(flightID, hotels, flightInfo):
   availableHotelIds = showHotels(flightID, hotels)
   hotelId = input("\nSelecciona el ID del hotel que deseas reservar: ")

   if hotelId in availableHotelIds and hotels[hotelId]['flightId'] == flightID:
      nights = int(input("¿Cuántas noches deseas reservar? "))
      hotel = hotels[hotelId]
      totalPrice = (hotel['pricePerNight'] * nights) + flightInfo['price']

      reservation = {
         'nightsInHotel': nights,
         'hotel': hotel['name'],
         'totalPrice': totalPrice,
      }

      print(f"\nBIEN! Has reservado {nights} noches en {hotel['name']} y {flightInfo['seats']} puesto(s) en el vuelo por un total de {totalPrice} USD$.")

      return reservation
   else:
      print("\nID de hotel no válido o el hotel no está disponible para este vuelo.")