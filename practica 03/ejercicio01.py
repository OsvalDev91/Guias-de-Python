# Solicitar el año por teclado
year = int(input("Introduce un año: "))

# Comprobar si el año es bisiesto
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} es un año bisiesto".format(year))
        else:
            print("{0} no es un año bisiesto".format(year))
    else:
        print("{0} es un año bisiesto".format(year))
else:
    print("{0} no es un año bisiesto".format(year))
