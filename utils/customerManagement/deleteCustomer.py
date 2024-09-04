def deleteCustomer(customers):
   print("\n- ELIMINAR CLIENTE -")

   customerToDeleteId = input("\nIngrese ID de usuario a eliminar (Sin puntos): ")
   
   if customerToDeleteId in customers.keys():
      customers.pop(customerToDeleteId)
      print("\nUsuario eliminado con éxito")
   else:
      print(f"\nUsuario con ID {customerToDeleteId} no se encuentra registrado")
   
   return customers