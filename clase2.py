# Voy a iniciar una variable en True
ejecucion = True
while ejecucion: #mientras lo que esté aqui sea un "True" se siga ejecutando
    opcion = input("Estamos ejecutando el menu? Y/N: ")
    if opcion.lower() == "n":
        ejecucion = False
    elif opcion.lower() == "y":
        ejecucion == True
    else:
        print("La opcion elegida no es valida.")

print("Gracias por utilizar nuestro sistema!!!")