"""""
datos = [1, 2, "tres",["lunes","martes","miercoles"]]
print(datos[2][1])  #extraigo doblemente: del dato 2 ("tres"), sacó el dato 1 (o sea, la "r") recordando 0,1,2,3...

#lista dentro de lista
print(datos[-1][-1][3]) #q era el -1??????

"""

numeros = ["uno", "dos", "tres"]
print(numeros)
numeros = numeros + ["cuatro", "cinco", "seis"]
print(numeros)
print(len(numeros))
 #y aparte podemos cambiar las listas
numeros[2] = "treis"
print(numeros)

numeros.append(input("Escriba el siguiente valor: "))
print(numeros)

numeros.insert(2, input("Enter number:"))
print(numeros)