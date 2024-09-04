from utils.reservations.showFlights import showFLights
from utils.reservations.hotelReservation import hotelReservation

def flightReservation(flights, hotels):
   print("\n-- RESERVACIÓN DE VUELOS --")

   showFLights(flights)
   flightID = input("\nSelecciona el ID del vuelo que deseas reservar: ")
   
   if flightID in flights:
      flight = flights[flightID]
      seats = int(input("\n¿Cuántos puestos desea reservar? "))
      flightPrice = flight['price'] * seats

      flights[flightID]['seatsAvailable'] -= seats
      print(f"Has reservado {seats} puesto(s) de {flight['origin']} a {flight['destiny']} por un total de {flightPrice} USD$.")

      reservation = {
         'flight': flightID,
         'flightDestiny': flight['destiny'],
         'totalPrice': flight['price'],
         'seats': seats
      }

      bookHotel = input('\nDesea reservar un hotel? (S/N) ').upper() == 'S'
      if bookHotel:
         flightInfo = {
            'price': flightPrice,
            'seats': seats
         }
         newReservation = hotelReservation(flightID, hotels, flightInfo)
         if newReservation:
            print(newReservation)
            reservation.update(newReservation)
      
      print("\nReservación completada con éxito!")

      return reservation
   else:
      print("\nID de vuelo no válido.")