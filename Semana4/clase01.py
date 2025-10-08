usuario = "Javier"
cantidad_alumnos = 79
media_edad = 18.342523
monto_hope = 145324343.675
inversion_evento = -574342.74364

print(f"El usuario es {usuario}")
print(f"y en su aula con {cantidad_alumnos - 4} pajaritos")
print(f"con edad promedio de {media_edad:.1f} años")
print(f"colectaron {monto_hope:,.2f} como un donativo")
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f} dolares")

print(type(usuario) is str)

esta_lloviendo = False
print(type(esta_lloviendo) is not bool)
print(type(monto_hope) is not bool)

nombre = "Alvin"
apellido = "Portillo" 
nombre_completo = nombre + " " + apellido
print(nombre_completo)