"""
nombre = "Antonio"
repetidos = nombre.lower().count("o")
print(repetidos)
#busca las "o" minusculas
"""


"""nombres = ["Ana", "Antonio", "Ana", "Jose", "Carlos"]


repetidos_a = 0 
print(nombres.count("Ana")) #genera un proceso algoritmico y busca la cantidad de "ana" en la lista
repetidos_a = repetidos_a + nombres[0].lower().count("a") #repeticiones de a + las que existan en la palabra 1
repetidos_a = repetidos_a + nombres[1].lower().count("a")
repetidos_a = repetidos_a + nombres[2].lower().count("a")
repetidos_a = repetidos_a + nombres[3].lower().count("a")
print(repetidos_a)

print(nombres.index("Ana", nombres.index("Ana")+1))""" #hace busqueda en la coleccion de una coleccion



nombres = ["Ana", "Antonio", "Ana", "Jose", "Carlos"]
"""nombres.append("Aby") #al listado agregar al final el "aby"
print(nombres)
nombres.insert(2, "Jorge") #al listado insertar Jorge en la posicion 2 y lo que estaba ahi se hace para atras (en la 3, 3 en 4 y asi,,,)
print(nombres)

nombres.insert(int(input("Posicion:")), input("Nombre nuevo: "))
print(nombres)


#para sustituir el valor por otro
posicion = int(input("Posicion sustituir: "))
nombres[posicion] = input("Nombre nuevo sustituir: ")
print(nombres)

#para borrar
nombres.remove("Carlos")
print(nombres)

#
valor_borrado = nombres.pop(3)
print(f"Nombre borrado: {valor_borrado}")
print(nombres)

#invertir el orden de los componentes
nombres.reverse()
print(nombres)"""
