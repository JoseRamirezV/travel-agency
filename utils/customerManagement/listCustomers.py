def listCustomers(customers):
   print("\n- LISTADO DE CLIENTES -\n")
   for i, customer in enumerate(customers.values()):
      print(f"{i+1}. {customer['idType'].upper()}: {customer['id']} - {customer['name'].upper()}, Edad: {customer['age']}")
   
   print("\n- FIN LISTA -")