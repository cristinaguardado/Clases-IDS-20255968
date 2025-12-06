#Aqui vamos a construir las funciones del sistema

#importamos el modulo datos
import modulo_datos as dat

def registrar_estudiante():
    """Validará y registrará estudiantes""" #la funcion le pide a uno valor de carnet, nombre y empleado 
    while True: #ponemos ahora el while para que no deje pasar a la siguiente fase hasta que el codigo este bien
        carnet_i = input("Digite el numero del carnet:")   #carnet que recibimos por medio del input
        largo_carnet = len(carnet_i)

        #verificaremos que el estudiante no exista
        existe = False
        for estu in dat.estudiantes:
            if estu["carnet"] == carnet_i:
                existe = True #solo si encontró una coincidenciaa 

        if largo_carnet >= 6 and largo_carnet <= 10 and existe == False: #verificamos que las 2 condiciones sean ciertas de una
            break #para seguir con la otra parte si se cumplen las 3 condiciones
        else:
            print("El carnet no tiene el largo requerido o ya existe")
            #aqui no ponemos el int pq es un numero que queremos que funcione como texto
    while True: #QUE SE REPITA HASTA QUE UNA CONDICION SE CUMPLAAA
            nombre_i = input("Digite el nombre:")
            if len(nombre_i) > 1:
                break
            else:
                print("El nombre no tiene el largo requerido")
    while True:
        apellido_i = input("Digite el apellido:")
        if len(apellido_i)>1:
            break
        else:
            print("El largo del apellido no es permitido.")

    dat.estudiantes.append({
        "carnet": carnet_i,
        "nombre": nombre_i,
        "apellido": apellido_i
    })
    print(dat.estudiantes)


#Parte 2: incribir en un cursooo
def inscribir_en_curso():
    while True:
        carnet_i = input("Ingrese el carnet:")
        if carnet_i.lower() == "salir":
            continue 
        existe = False
        for estu in dat.estudiantes:
            if estu("carnet") == carnet_i:
                existe = True
        if existe == False:
            break
        else: 
         print("El codigo del estudiante ya existe")




           
        
   
    

