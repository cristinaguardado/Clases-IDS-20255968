#Hecho por: 20255968-Guardado-Control4
#Parte 1: Funcion para registrar los libros 
def registrar_libros(lista_libros):
    """Permite registrar un libro con titulo, autor y le genera el codigo"""
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    codigo = f"L00{len(lista_libros)+1}"

    libro = {"codigo": codigo, "titulo": titulo, "autor": autor, "disponible": True}

    lista_libros.append(libro)
    print("Libro registrado")

#Parte 4: Funcion que sirve para mostrar los libros
def mostrar_libros(lista_libros):
    """Muestra los libros disponibles"""
    print("Lista de libros:")
    if not lista_libros:
        print("No se han registrado libros.")
        return
    for libro in lista_libros:
        estado = "Disponible" if libro["disponible"] else "Prestado" 
        print(f"""Código: {libro['codigo']},
              Titulo: {libro['titulo']},
               Autor: {libro['autor']},
                Estado: {libro[estado]} """)







