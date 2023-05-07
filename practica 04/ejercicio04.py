
dia = int(input("Ingresa el día (1-31): "))
mes = int(input("Ingresa el mes (1-12): "))
anio = int(input("Ingresa el año: "))

# Pedimos la cantidad de días a sumar
dias_a_sumar = int(input("Ingresa la cantidad de días a sumar: "))

# Creamos una lista con el número de días de cada mes
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Utilizar esta validación si el mes de febrero es en un año bisiesto
"""if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    dias_por_mes[1] = 29"""

# Sumamos los días a la fecha inicial
dia += dias_a_sumar
while dia > dias_por_mes[mes - 1]:
    dia -= dias_por_mes[mes - 1]
    mes += 1
    if mes > 12:
        mes = 1
        anio += 1

# Imprimimos la fecha resultante en pantalla
print("La fecha resultante es:", "{:02d}/{:02d}/{:04d}".format(dia, mes, anio))

