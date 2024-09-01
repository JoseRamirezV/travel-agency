import re

def updateCustomer(customers):
   readyToSave = False
   error = False

   print("\n- ACTUALIZAR CLIENTE -")

   customerToUpdateId = input("\nIngrese ID de usuario a actualizar: ")

   while not readyToSave:
      name = input("Nombre completo del cliente: ")
      age = input("Edad del cliente: ")

      if re.search(r'[a-zA-Z]', age):
         print("\nEdad en números por favor :)")
         error = True

      if error:
         print("\nPor favor verifique que los datos ingresados coincidan con el formato solicitado.\n")
      else:
         readyToSave = True

   if customerToUpdateId in customers.keys():
      customers[customerToUpdateId]['name'] = name
      customers[customerToUpdateId]['age'] = int(age)

      print("\nUsuario actualizado con éxito")
   else:
      print(f"\nUsuario con ID {customerToUpdateId} no se encuentra registrado")

   return customers
