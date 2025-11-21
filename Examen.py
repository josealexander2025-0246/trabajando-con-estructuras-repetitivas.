numero_secreto = 5
Adivinar = False
oportunidades = 0

while oportunidades < 3 and not Adivinar:
    intento = int(input("Adivine el número entre 1 y 10: "))
    oportunidades = oportunidades + 1

    if intento == numero_secreto:
        print("Adivinaste")
        Adivinar = True
    elif intento < numero_secreto:
        print("El número es mayor que tu intento")
    else:
        print("El número es menor que tu intento")

if Adivinar:
    print("Ganaste el juego")
else:
    print("Agotaste tus intentos")
    print("El número era:", numero_secreto)
