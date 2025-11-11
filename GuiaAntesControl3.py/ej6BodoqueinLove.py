n = int(input())
nombre = []
for i in range(n):
    apodo = input()
    nombre.append(apodo)
    if len(apodo) <= 6:
        print("No vale la pena")
    elif len(apodo) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    else:
        print("Dios no creo aguantar esta vez")


