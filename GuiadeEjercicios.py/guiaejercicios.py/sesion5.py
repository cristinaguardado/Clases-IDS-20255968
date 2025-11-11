""""""
palabra = "Python"
print(palabra[0])
print(palabra[0:3])
print(palabra[0],palabra[-1]) #como hago para imprimir ultimas 2 letras??


frase = ("Aprender Python es divertido")
print(len(frase))
print(frase[9:15])



"""
palabra = input("Ingrese una palabra: ")
print(len(palabra))
print(palabra[0],[-1]) #como pedir la priemra y ultima letra?
#print(palabra[-1])
"""


nombre = "Juan Perez "
print(nombre[-6:]) #slicing

""""""

var1 = input("Ingrese su nombre: ")
var2 = input("Ingrese su edad: ")
var3 = input("Ingrese su cuidad: ")

print(f"¡Bienvenido {var1}!")
print(f"usted tiene {var2} años")
print(f"y es de la ciudad de {var3}")