from utils.customerManagement.customersMenu import customersMenu
from utils.reservations.flightReservation import flightReservation
from utils.reservations.showReservations import showReservations

import re


customers = {
   '123123123': {
         "idType": 'CC',
         "id": '123123123',
         "name": 'Jose',
         "age": 25
      }
}
customerReservations = {}
flights = {
   "1": {"origin": "Cali(Colombia)", "destiny": "Barcelona(España)", "price": 857, "seatsAvailable": 100},
   "2": {"origin": "Cali(Colombia)", "destiny": "Cancun(Mexico)", "price": 343, "seatsAvailable": 100},
   "3": {"origin": "Cali(Colombia)", "destiny": "Londres(Inglaterra)", "price": 1100, "seatsAvailable": 100},
}
hotels = {
   "1": {"name": "Hotel Plaza", "pricePerNight": 150, "flightId": "1"},
   "2": {"name": "Hotel Sol", "pricePerNight": 100, "flightId": "1"},
   "3": {"name": "Hotel Mar", "pricePerNight": 200, "flightId": "1"},
   "4": {"name": "Hotel Barcelona Center", "pricePerNight": 180, "flightId": "1"},

   "5": {"name": "Hotel Cancun Beach", "pricePerNight": 120, "flightId": "2"},
   "6": {"name": "Hotel Caribe", "pricePerNight": 140, "flightId": "2"},
   "7": {"name": "Hotel Solymar", "pricePerNight": 130, "flightId": "2"},
   "8": {"name": "Hotel Selina", "pricePerNight": 75, "flightId": "2"},

   "9": {"name": "Hotel London Eye", "pricePerNight": 250, "flightId": "3"},
   "10": {"name": "Hotel Big Ben", "pricePerNight": 260, "flightId": "3"},
   "11": {"name": "Hotel Westminster", "pricePerNight": 240, "flightId": "3"},
   "12": {"name": "Hotel Park Plaza", "pricePerNight": 245, "flightId": "3"},
}


options = ["Crear paquetes turísticos", "Buscar paquetes turísticos", "Reservas de vuelos", "Ver reservas","Gestión de clientes", "Salir"]

print("\n--- ¡Bienvenido a IDKAirlines! ---")

stopExecution = False

while not stopExecution:
   print("")
   for i in range(len(options)):
      print(f"{i+1}. {options[i]}")
   
   optionInput = input("\nPor favor seleccione una opción: ")

   if re.search(r'[a-zA-Z]', optionInput) or 1 < int(optionInput) > len(options):
      print(f"\n{optionInput} no es una de las opciones disponibles, por favor ingrese un valor del 1 al {len(options)}")
   else:
      selectedOption = int(optionInput)

      if(selectedOption == 1):
         print(options[selectedOption-1])

      if(selectedOption == 2):
         print(options[selectedOption-1])

      if(selectedOption == 3):
         customerId = input("\nID de cliente: ")
         if customerId in customerReservations.keys():
            print('\nLo sentimos, solo se admite una reservación por cliente')
         else:
            if customers and customerId in customers.keys():
               reservation = flightReservation(flights, hotels)
               
               customerReservations[customerId] = {
                  "customer": {
                     'idType': customers[customerId]['idType'],
                     'id': customers[customerId]['id'],
                     'name': customers[customerId]['name']
                  },
                  "reservation": reservation,
               }
            else:
               print("\nERROR!: El cliente debe estar registrado para poder reservar un vuelo")

      if(selectedOption == 4):
         showReservations(customerReservations)

      if(selectedOption == 5):
         updatedCustomers = customersMenu(customers)
         
         customers = updatedCustomers
         
      if(selectedOption == 6):
         stopExecution = True