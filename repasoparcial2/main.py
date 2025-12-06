#Este modulo será el inicio de mi sistema


#importar los módulos necesarios
import modulo_funciones as md  #cuando yo mencione mf es modulo funciones


while True:
    print("""
    Bienvenido a nuestro sistema.
    1. Registrar estudiante
    2. Inscribir en curso
    3. Generar reportes
    4. Salir
     """)
    opcion = input("Elija una opcion 1-4:")
    if opcion == "1":
        md.registrar_estudiante()
    elif opcion == "2":
        print("Ha elegido la opcion 2.")
    elif opcion == "3":
        print("Ha elegido la opcion 3.")
    elif opcion == "4":
        print("Gracias por visitarnos.")
        break
    else:
        print("La opcion elegida no es valida.")

        