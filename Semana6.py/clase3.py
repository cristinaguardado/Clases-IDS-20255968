tipo = (input("Ingrese el tipo (local/internacional): "))
monto = float(input("Digite el monto: "))


if tipo.lower() == "local": #se pone "tipo.lower()" pq se pasa a minusculas lo ingresado y eso debe ser igual a "local"
  if monto > 100:
    print("7%")
  elif monto > 75:
    print("5%")
  else: 
    print("0%")
else:
  if monto > 100:
    print("12%")
  elif monto > 75:
    print("9%")
  else:
    print("0%")


