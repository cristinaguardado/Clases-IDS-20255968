"""



M = int(input())
S = int(input())
A = input()
B = input()
var = "_Alvin"

pt1 = (A[ : : S])
pt2 = B * M

texto = (pt1 + var + pt2)
print(texto)
"""

"""{Ejercicio1 pendienteeee

correo = input()

con1 = correo.count("@")>=1
con2 = (len(correo[:correo.index("@")])>=3) and (len(correo[correo.index("@"):])>=3)
con3 = (correo.count(".")>=1)
con4 = (correo.count(" ")==0)
con5 = (correo[0]!= ".") and (correo[-1]!= ".")

print(con1 and con2 and con3 and con4 and con5 )

condiciones = con1, con2 ,con3 , con4, con5
print(condiciones)
"""

"""{Ejercicio2

cadena = input()
print(cadena.count("z"))

"""

"""{Ejercicio3
 
x = int(input())
p1 = input()
p2 = input()

pt1 = len(p1)//x
pt2 = len(p2)// x

print(f"{p1[:pt1]}{p2[ -pt2:]}")
"""

"""Ejercicio4"""


Ejercicio5

Ejercicio6

Ejercicio7
 


Ejercicio8
 




Ejercicio9
 
tup1 = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
tup2 = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")
p1 = int(input())
p2 = int(input())
plato = tup1[p1-1]
complemento = tup2[p2-1]

print(f"El pedido de Alvin es: {plato} con {complemento}")



Ejercicio10
 
n = int(input())
sum = n * (n+1) // 2
print(sum)

"""