import opciones as op
        
        
while True:
    print("1 - Seleccionar pedido / 2 - Visualizar preparacion / 3 - Gestionar Stock / 4 - Procesar Pago")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        op.opcion1()
    if opcion == 2:
        op.opcion2()
    if opcion == 3:
        op.opcion3()
    if opcion == 4:
        op.opcion4()
