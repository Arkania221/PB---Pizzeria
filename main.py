
comanda_completa = []
preparado = False

while True:
    print("1 - Seleccionar pedido / 2 - Visualizar preparacion / 3 - Gestionar Stock / 4 - Procesar Pago")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        while True:
            print("1 - Hamburguesa")
            print("2 - Pizza de glock")
            print("3 - Limon")
            print("4 - mas pizza")
            print("5 - Pizza de tierra")
            print("6 - Finalizar pedido")
            comanda = int(input("Seleccione su pedido: "))
            if comanda == 1:
                comanda_completa.append("Hamburguesa")
            elif comanda == 2:
                comanda_completa.append("Pizza de glock")
            elif comanda == 3:
                comanda_completa.append("Limon")
            elif comanda == 4:
                comanda_completa.append("mas Pizza")
            elif comanda == 5:
                comanda_completa.append("Pizza de tierra")
            elif comanda == 6:
                break
            else:
                print("No valido")
    if opcion == 2:
        if len(comanda_completa) == 0:
            print("Nada para preparar")
        else:
            preparado = True
            print("Haciendo la masa...")
            for i in range(100000000):
                None
            print("Añadiendo ingredientes al pan...")
            for i in range(100000000):
                None    
            print("Cosechando limones...")
            for i in range(100000000):
                None
            print("Encajando el pedido en caja...")
            for i in range(100000000):
                None
            print("Listo para la entrega...")
            for i in range(100000000):
                None
    if opcion == 3:
        print("Opcion 3")
        if preparado:
            print("Harina: " + str(50 - len(comanda_completa)) + "kg")
            print("Salchichon: " + "45" + "kg")
            print("Proteinas en polvo: " + str(23 - len(comanda_completa)) + "kg")
            print("Ingredientes variados: " + "98" + "kg")
        else:
            print("Harina: " + str(50) + "kg")
            print("Salchichon: " + "45" + "kg")
            print("Proteinas en polvo: " + str(23) + "kg")
            print("Ingredientes variados: " + "98" + "kg")
