from utils.customerManagement.addCustomer import addCustomer
from utils.customerManagement.updateCustomer import updateCustomer
from utils.customerManagement.listCustomers import listCustomers
from utils.customerManagement.deleteCustomer import deleteCustomer
import re

def customersMenu(customers):

   options = ["Listar clientes", "Agregar cliente", "Actualizar cliente", "Eliminar cliente", "Salir"]

   print("\n-- GESTIóN DE CLIENTES --")

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
            if customers:
               listCustomers(customers)
            else:
               print("\nNo hay clientes registrados aun")
            
         if(selectedOption == 2):
            updatedCustomers = addCustomer(customers)
            
            customers = updatedCustomers

         if(selectedOption == 3):
            updatedCustomers = updateCustomer(customers)

            customers = updatedCustomers

         if(selectedOption == 4):
            updatedCustomers = deleteCustomer(customers)

            customers = updatedCustomers
               
         if(selectedOption == 5):
            stopExecution = True

   return customers