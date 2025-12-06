#Hecho por: 20255968-Guardado-Control4
#Parte 2: Registro del estudiante
def registrar_estudiante(lista_estudiantes):
    """Permite registrar al estudiante"""
    nombre = input("Ingrese el nombre del estudiante: ")
    carnet = f"S00{len(lista_estudiantes) + 1}"

    estudiante = {"carnet": carnet,"nombre": nombre}

    lista_estudiantes.append(estudiante)
    print("Estudiante registrado")

#Parte 5: Funcion para mostrar los estudiantes
def mostrar_estudiantes(lista_estudiantes):
    """Muestra un listado de los estudiantes registrados"""
    print("Lista de estudiantes:")
    if not lista_estudiantes:
        print("No se han registrado alumnos")
        return
    for estudiante in lista_estudiantes:
        print(f"""{estudiante['carnet']},
               {estudiante['nombre']}""")