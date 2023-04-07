dolar = 0.00
colon = 0.00
bitcoin = 0.00
resultado = 0.00

monto = float(input("Ingrese el monto a convertir: "))

print("Que divisa desea convertir")
print("1- Dólar a Colon")
print("2- Colon a Dólar")
print("3- Dólar a Bitcoin")
opr = int(input("Seleccione una opción: "))

if opr == 1:
    dolar = 8.75
    resultado = monto * dolar
    print(str(monto) + " Dólares es igual ↔ ¢%.2f" % resultado + " Colones")
elif opr == 2:
    colon = 0.114286
    resultado = monto * colon
    print(str(monto) + " Colones es igual ↔ $%.2f" % resultado + " Dólares")
elif opr == 3:
    bitcoin = 28477
    resultado = monto / bitcoin
    print(str(monto) + " Dólares es igual ↔ ¤%.8f" % resultado +" Bitcoins")
    print("NOTA: TOMAR EN CUENTA QUE EN ESTA CONVERSIÓN SE UTILIZO UN VALOR FIJO, ANTES DE QUE EL VALOR DE ESTA DIVISA SE ACTULIZARA.")