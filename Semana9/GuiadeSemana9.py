""""
nombre = []
codigo = []
correo = []
telefono = []
lista1 = {nombre, codigo, correo, telefono}
for i in lista1:
    nom = input("Inserte su nombre: ")
    cod = input("Inserte su codigo: ")
    cor = input("Inserte su correo: ")
    tel= input("Inserte su telefono:")
    nombre.append(nom)
    codigo.append(cod)
    correo.append(cor)
    telefono.append(tel)
print(lista1)

aplicacion = True
while aplicacion:
    opcion = int(input(Elija la opcion(1.Mostrar productos
2.	Agregar producto
3.	Registrar nuevo cliente
4.	Mostrar clientes
5.	Registrar pedido
6.	Mostrar pedidos del día
7.	Mostrar categorías disponibles
8.	Salir)))
    if opcion == 8:
        aplicacion = False
        break
    elif opcion == 2:
        codigo1 = []
        producto = []
   """
        
