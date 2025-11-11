"""""
#capturar articulos producidos
enero = int(input("Introduzca cantidades enero: "))
febrero = int(input("Introduzca cantidades febrero: "))
marzo = int(input("Introduzca cantidades marzo: "))

costo_total = (enero*1.25 + febrero*1.38 + marzo*1.14) #multiplicado por el costo de cada uno

print(costo_total)
print(f"Las cantidades de enero, febrero y marzo son: ")
print(f"{enero}, {febrero} y {marzo} con un costo")
print(f"de ${costo_total:.2f}")

"""
"""
#1
#dias de la semana

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
lu = int(input("Lunes: "))
dias[0]=lu
print(dias)

ma = int(input("Martes: "))
dias[1]=ma
print(dias)

mi = int(input("Miercoles: "))
dias[2]=mi
print(dias)

ju = int(input("Jueves: "))
dias[3]=ju
print(dias)

vi = int(input("Viernes: "))
dias[4]=vi
print(dias)

print(f"La producción de la semana fue {lu+ma+mi+ju+vi}")

"""
"""""
#2
#poner nosotros el numero para saber que niño es segun el orden
alumnos = ("chistian", "joe mimido", "campozzzsura","andy","gracee","myonly")
ninio = int(input("Ingrese el orden del niño que desea saber (1-7): "))
print(f"El alumno que ingresó como numero {ninio} es {alumnos[ninio-1]}")

"""
"""
#5
nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su apellido: ")

print(f"{nombre.lower()}{apellido.lower()}@ISND.com")

"""
"""
#6
salario = input("Ingrese su salario con $: ")
print(salario[0])
print(salario[0]=="$")

print(salario.count("$"))
print(salario.count("$")==1)

"""

#7

contra = "DFGUPCCBJKAJ"
print(contra[: :2])
