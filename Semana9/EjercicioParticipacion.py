def dui_validacion(dui):
    cantidad_cond = 0
    if len(dui) == 10:
        cantidad_cond += 1
    else: 
        cantidad_cond = 0
    if dui.count("-") == 1:
        cantidad_cond += 1
    else: 
        cantidad_cond = 0
    if dui[-1] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
        cantidad_cond += 1
    else: 
        cantidad_cond = 0

    print(f"Cumple {cantidad_cond} condiciones")
dui_validacion(input("Ingrese su correo: "))