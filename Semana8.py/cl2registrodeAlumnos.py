#Registro de alumnos

#Configuración inicial
"""alumnos = 0
lista_alumnos = []
cantidad = int(input("Cuantos alumnos vamos a ingresar?: "))

for i in range(cantidad): #repite el num de veces ingresado en "cantidad"
    alumnos = input("Digite nombre del pajarito: ")
    lista_alumnos.append(alumnos)

print(lista_alumnos)"""



alumnos = 0
lista_alumnos = []
print("Bienvenido a nuestro sistema de control de Alumnos.")
menu_activo = True

while menu_activo:
    opcion = input("Elija la opción(1: Ingresar alumno, 2:Consultar, 3: Modificar, 4: Borrar, 5: Salir): ")
    if opcion == "5":
        menu_activo = False
    elif opcion == "1":
        alumnos = input("Nombre de alumno a agregar: ")
        lista_alumnos.append(alumnos)
    elif opcion == "2":
        print(lista_alumnos)
    elif opcion == "3":
        i = int(input("Ingrese la posicion del alumno a modificar:"))
        n = input("Ingrese el nuevo nombre:")
        lista_alumnos[i - 1] = n
    elif opcion == "4":
        borrado = lista_alumnos.pop(int(input("Ingrese el numero del alumno a popear (1-4): "))-1)   #el -1 
        print(f"Usted ha popeado a: {borrado}")
    else:
        print("La opcion no es válida")

print("Gracias por visitar nuestro sistema")