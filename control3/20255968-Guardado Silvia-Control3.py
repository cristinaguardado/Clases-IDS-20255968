#Parte 1
agente = "encargado"
platillo = []
precios = []

#Parte 2
usuario  = input("Ingrese nombre del agente: ")
if usuario.lower() != agente:
    print("Agente no registrado")
    input("Favor ingrese el nombre del agente: ")

#Parte 3
aplicación = True
while aplicación:
    opcion = int(input("Elija la opción (1.Creación de platillos, 2. Consulta de platillos y precios, 3.Colocar un pedido, 4.Salir): "))
#Parte 4
    if opcion == 1:
        newplato = input("Ingrese el nombre del platillo a crear: ")
        newprecio = float(input("Ingrese el precio del platillo a crear: "))
        platillo.append(newplato)
        precios.append(newprecio)
#Parte 5
    elif opcion == 2:
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados")
        else:
            for i in range(len(platillo)):
                print(f"{platillo[i]}: {precios[i]:.2f}")
#Parte 6
    elif opcion == 3:
        pedido = input("Indique el nombre del platillo para su orden: ").lower()
        if pedido in platillo:
            x = platillo.index(pedido)
            print(f"Usted ha elegido {pedido} con un precio de ${precios[x]:.2f} ")
        else: 
            print("El platillo no existe")
#Parte 7
    elif opcion == 4:
        print("Bye bye!")
        aplicación == False
        break
        




