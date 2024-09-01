import re

allowedIdTypes = ['CC', 'CE', 'PEP']

def addCustomer(customers):
   readyToSave = False

   print("\n- AGREGAR CLIENTE -")

   while not readyToSave:
      error = False
      idType = input("\nTipo de documento de identificación(CC, CE, PEP): ")
      id = input(f"{idType.upper()} del cliente (sin puntos): ")
      name = input("Nombre completo del cliente: ")
      age = input("Edad del cliente: ")

      if idType.upper() not in allowedIdTypes:
         print(f"\n{idType} no es un tipo de ID admitido")
         error = True
      
      if re.search(r'[a-zA-Z]', id):
         print("\nQue ID tiene números?")
         error = True

      if 7 > len(id) or len(id) > 10:
         print("\nDebe ser un numero de documento valido ")
         error = True

      if re.search(r'[a-zA-Z]', age):
         print("\nEdad en números por favor :)")
         error = True

      if error:
         print("\nPor favor verifique que los datos ingresados coincidan con el formato solicitado.")
      else:
         readyToSave = True

   if id in customers.keys():
      print(f"\nERROR!: Ya existe un cliente registrado con ID {id}\n")
      showUser = input("¿Desea ver el nombre de éste cliente? (S/N)? ").upper() == 'S'
      if showUser:
         print(f"Cliente: {customers[id]['name'].upper()}")
      else:
         print("Bien")

   else:
      customers[id] = {
         "idType": idType,
         "id": id,
         "name": name,
         "age": int(age)
      }
      print("\nCliente agregado con éxito")

   return customers
