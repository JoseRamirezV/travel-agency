import re

allowedIdTypes = ['CC', 'CE', 'PEP']

def addCustomer(customers):
   readyToSave = False
   error = False

   print("\n- AGREGAR CLIENTE -\n")

   while not readyToSave:
      idType = input("Tipo de documento de identificación(CC, CE, PEP): ")
      id = input(f"{idType.upper()} del cliente (sin puntos): ")
      name = input("Nombre completo del cliente: ")
      age = input("Edad del cliente: ")

      if idType.upper() not in allowedIdTypes:
         print(f"\n{idType} no es un tipo de ID admitido")
         error = True
      
      if re.search(r'[a-zA-Z]', id):
         print("\nQue ID tiene números?")
         error = True

      if 8 > len(id) or len(id) > 10:
         print("\nEl numero de documento debe tener mínimo 8 números ")
         error = True

      if re.search(r'[a-zA-Z]', age):
         print("\nEdad en números por favor :)")
         error = True

      if error:
         print("\nPor favor verifique que los datos ingresados coincidan con el formato solicitado.")
      else:
         readyToSave = True

   if id in customers.keys():
      print("\nERROR!: Este cliente ya existe")
   else:
      customers[id] = {
         "idType": idType,
         "id": id,
         "name": name,
         "age": int(age)
      }
      print("\nCliente agregado con éxito")

   return customers
