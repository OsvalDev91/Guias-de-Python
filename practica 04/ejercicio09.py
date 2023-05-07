def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Comprobar la relación entre los números dados
numeros = [(5, 10), (10, 5), (5, 5)]

for a, b in numeros:
    resultado = relacion(a, b)
    if resultado == 1:
        print(f"{a} es mayor que {b}")
    elif resultado == -1:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} es igual a {b}")