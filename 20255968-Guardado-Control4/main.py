#Hecho por: 20255968-Guardado-Control4
#El programa en sí
from libros import registrar_libros, mostrar_libros
from estudiantes import registrar_estudiante, mostrar_estudiantes
from prestamos import registrar_prestamo, mostrar_prestamos

# Listas principales del sistema
lista_libros = []
lista_estudiantes = []
lista_prestamos = []

def menu():
    while True:
        print("Bienvenido al sistema de la biblioteca: ")
        print("1. Registrar libro")
        print("2. Registrar estudiante")
        print("3. Registrar prestamo")
        print("4. Mostrar libros")
        print("5. Mostrar estudiantes")
        print("6. Mostrar prestamos")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_libros(lista_libros)
        elif opcion == "2":
            registrar_estudiante(lista_estudiantes)
        elif opcion == "3":
            registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos)
        elif opcion == "4":
            mostrar_libros(lista_libros)
        elif opcion == "5":
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == "6":
            mostrar_prestamos(lista_prestamos)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida")

menu()