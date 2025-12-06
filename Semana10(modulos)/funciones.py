#Este modulo contendrá funciones

def ordenar_pizza(size, masa, *ingredientes): #ahora con *args (recibe un conjunto de valores, como SI FUERA una lista)
    """vamos a imprimir su orden"""
    print(f"Usted a ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
         print(f"\t- {i}")  #el "\t-" sirve para crear esa tabulacion o listado con el -


def registro_profesores(nombre, apellido, **materias): #es kwargs al utilizar **
    """Crear un registro de profesor, utilizando kwargs"""
    #args crea listas
    #kwargs crea diccionarios
    print(f"El profesor {nombre} {apellido} imparte las materias:  ")
    for ciclo, materias in materias.items():
        print(f"\t- {ciclo}: \t {materias}")


def saludar_usuarios(nombresitos):
    """Saludara al usuario"""
    for nombre in nombresitos: #haremos una interacion en la lista
     print(f"hola, {nombre.title()}")




