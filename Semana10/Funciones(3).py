#crearemos una funcion usando kwargs

def registro_profesores(nombre, apellido, **materias): #es kwargs al utilizar **
    """Crear un registro de profesor, utilizando kwargs"""
    #args crea listas
    #kwargs crea diccionarios
    print(f"El profesor {nombre} {apellido} imparte las materias:  ")
    for ciclo, materias in materias.items():
        print(f"\t- {ciclo}: \t {materias}")

registro_profesores(
    "Alvin",
    "Portillo",
    Ciclo1 = ["BD1", "IIJ", "IDN"],
    Ciclo2 = ["BT2", "PYTHON", "CANVA"],
    Ciclo3 = ["hambre", "hambuerguesa", "papas"]
)
