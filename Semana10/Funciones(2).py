#otro modilo para comprender

def describir_mascota(nombre_mascota: str, tipo_animal: str = "perro"): #definir parametro con un valor POR DEFECTO
    """Esta funcion describe una mascota, por defecto = perro"""
    print(f"""mi mascota es un/a {tipo_animal.lower()}
    y se llama {nombre_mascota.capitalize()}""")

#llamamos la funcion
#describir_mascota(nombre_mascota = "dameluu") #el tipo de animal sera "perro" por defecto
#describir_mascota(nombre_mascota ="ñaña", tipo_animal = "jirafa")


def registro_usuarios(nombre, apellido, inicial = " ", edad = 0): #si la edad la defino como string, la riego
    """Construye nombre a partir de sus componentes """
    if edad:
        nombre_completo = f"La persona {nombre} {inicial} {apellido} de {edad} años"    
    else:
        nombre_completo = f"La persona {nombre} {inicial} {apellido}"
    return nombre_completo

#print(registro_usuarios( nombre = "Daniel", inicial = "A", apellido = "Loundres"))


#definimos una funcion que es usada por una lista
def saludar_usuarios(nombresitos):
    """Saludara al usuario"""
    for nombre in nombresitos: #haremos una interacion en la lista
     print(f"hola, {nombre.title()}")

usuarios = ["ana", "luis", "muscra"]
saludar_usuarios(usuarios) #imprime 3 lineas saludando a cada usuario




