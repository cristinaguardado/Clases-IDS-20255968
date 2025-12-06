#Hecho por: 20255968-Guardado-Control4
#Parte 3: funcion para registrar un préstamo
def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    print("Registrar prestamo")
    carnet = input("Ingrese el carnet del estudiante: ")

    #para verificar al estudiante
    estudiante = next((e for e in lista_estudiantes if e["carnet"] == carnet), None)
    if not estudiante:
        print("El estudiante no existe.")
        return

    codigo = input("Ingrese el código del libro: ")

    #verificar el libro
    libro = next((l for l in lista_libros if l["codigo"] == codigo), None)
    if not libro:
        print("El libro no existe.")
        return

    #verificando la disponibilidad
    if not libro["disponible"]:
        print("El libro NO está disponible.")
        return

    fecha = input("Fecha del préstamo (YYYY-MM-DD): ")

    prestamo = {"carnet_estudiante": carnet, "codigo_libro": codigo,"fecha": fecha}

    lista_prestamos.append(prestamo)
    libro["disponible"] = False  

    print("Prestamo registrado.")


#Parte 6: mostrar los prestamos realizados
def mostrar_prestamos(lista_prestamos):
    """Ayuda a mostrar los prestamos realizados"""
    print("Lista de prestamos")
    if not lista_prestamos:
        print("No hay prestamos registrados")
        return

    for i in lista_prestamos:
        print(f"""{i['carnet_estudiante']},
               {i['codigo_libro']}, 
               {i['fecha']}""")