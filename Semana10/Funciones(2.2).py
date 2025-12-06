#vamos a atender pedidos de pizza

#definiendo la funcion
def ordenar_pizza(size, masa, *ingredientes): #ahora con *args (recibe un conjunto de valores, como SI FUERA una lista)
    """vamos a imprimir su orden"""
    print(f"Usted a ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
         print(f"\t- {i}")  #el "\t-" sirve para crear esa tabulacion o listado con el -

#llamando la funcion
ordenar_pizza("grande", "gruesaaa", "peperoni", "queso", "chalchicha", "macarroni", "piña")
             #reconoce q el primer argumento es "size", el segundo de "masa" y los demas son args de ingredientes



