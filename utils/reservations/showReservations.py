def showReservations(reservations):
   for i, r in  enumerate(reservations.values()):
      customer = r['customer']
      reservation = r['reservation']

      print(f"\n{i+1}. {customer['name'].capitalize()} - {customer['idType']}: {customer['id']}")
      print(f"Reservación para vuelo {reservation['flight']} con destino a {reservation['flightDestiny']} - {reservation['seats']} asientos\n")
      
      if 'hotel' in reservation:
         print(f"Hotel: {reservation['hotel']}, {reservation['nightsInHotel']} noches")
         
      print(f"TOTAL: {reservation['totalPrice']} USD$")
      print("___________________________")