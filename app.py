from utils.customerManagement.customersMenu import customersMenu
import re


customers = {}
options = ["Crear paquetes turísticos", "Buscar paquetes turísticos", "Reservas de vuelos", "Reservas de hoteles","Gestión de clientes", "Salir"]

print("\n--- ¡Bienvenido a IDKAirlines! :) ---")

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
         print(options[selectedOption])

      if(selectedOption == 2):
         print(options[selectedOption])

      if(selectedOption == 3):
         print(options[selectedOption])

      if(selectedOption == 4):
         print(options[selectedOption])

      if(selectedOption == 5):
         updatedCustomers = customersMenu(customers)
         
         customers = updatedCustomers
         
      if(selectedOption == 6):
         stopExecution = True