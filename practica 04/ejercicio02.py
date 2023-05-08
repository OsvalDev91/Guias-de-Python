numero = int(input("Ingrese el número: "))
exponente = int(input("Ingrese el exponente: "))

resultado = 1

if exponente >= 0:
    for i in range(int(exponente)):
        resultado *= numero
        print(numero, "elevado a la", exponente, "es igual a %.2f"% resultado)

elif numero or exponente <0:
    resultado = -(1/numero)**exponente
    print(numero, "elevado a la", exponente, "es igual a %.0f"% resultado)

