#Este modulo va a contener funciones

#Una funcion tiene 2 tiempos: una definicion y una llamada

#1:definiremos la funcion
def mi_funcion(): #lo de adentro del () es un parámetro 
    """Esta funcion imprime un saludo"""
    print("Hola mundo")
    print("amigo usuario")
    print("gracias por usar nuestro sistema")

#2:utilizaremos la funcion
#mi_funcion() #Lo del () es un argumento

#vamos a recibir informacion desde afuera de la funcion
def capturar_nombre():
    """Esta funcion recibe valores por medio de input"""
    nombre = input("Ingrese su nombre:")
    apellido = input("Digite su apellido: ")
    nombre_completo = nombre.capitalize() + " " + apellido.capitalize()
    print(f"Bienvenid@ {nombre_completo}")

def capturar_usuario(nombre, edad):
    """Esta funcion recibe valores por medio de argumentos"""
    nombre_usuario = nombre  # o input("ingresar nombre")
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad} años de edad"
    print(texto)


#capturar_usuario("ranarene", 16) #no olvidar las "" para el usuario
#capturar_usuario(input("Ingrese nombre: "), int(input("Ingrese edad: "))) #el input puede estar aquiiii

def calculo_impuesto(ventas):
    """Esta funcion calcula el valor del impuesto"""
    if ventas < 500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto * ventas #aqui le estamos diciendo que solo calcule

ventas = 500
#aqui vamos a llamar a la funcion
tasa_calculada = calculo_impuesto(ventas)
monto_impuesto = calculo_impuesto(ventas)*ventas
print(f"""El valor de la venta fue de {ventas:,.2f}
      la tasa de impuesto es {tasa_calculada:,.2f}
      y el monto por tanto es ${monto_impuesto:,.2f}""") #y hasta aqui lo imprimimos






