#Este es un docstring
#vamos a crear vaarias funciones

def saludar():
    """Es una función que va a saludar"""
    nombre = input("Digite el nombre: ")
    apellido = input("Digite el apellido: ")
    nombre_completo = f"{nombre.title()} {apellido.title()}"
    print(f"Hola {nombre_completo}!")

#saludar()

def saludar_con_param(nombre, apellido): #definira una funcion que se llama saludar con param y ahora se define el param. "nombre"
    """Es una función que va a saludar"""

    print(f"Hola {nombre.title()} {apellido.title()}")

#saludar_con_param("Alvin", "Albino") #El "Alvin" es el argumento, ya no es parámetro

def describir_mascota(animal, nombre_mascota):
    """Vamos a describir mascotas"""
    print(f"Tengo un {animal.title()} y su nombre es {nombre_mascota.title()}")

describir_mascota(nombre_mascota = "chamuc", animal = "chumpe")
describir_mascota("pollo", "damil")
describir_mascota(    
    input("Digite el tipo de animal: "),
    input("Digite el nombre de la mascota: ") #OJOOO: es necesario poner la "," entre inputs
)

    





