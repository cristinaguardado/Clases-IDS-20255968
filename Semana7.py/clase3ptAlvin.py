monto = float(input("Ingrese el monto: "))
tipo = input("Tipo(Local/Interno): ")

if tipo.lower() == "local":
    if monto > 100 :
        impuesto = 0.07
    else:
        if monto > 75:
            impuesto = 0.05
        else:
            impuesto = 0
elif tipo.lower() == "internacional":
    if monto > 100: 
        impuesto = 0.12
    elif monto > 75:
        impuesto = 0.09
    else:
        impuesto = 0
else:   #El recomienda primero hacer todo lo de las variables e imprimir todo al final
    print("ese tipo no existe")

print(f"El tipo {tipo} con monto {monto:,.2f}") #la coma se utiliza para dar formato de separar cada miles (ej: 103,549.04)
print(f"para un impuesto de {monto*impuesto:,.2f}")




