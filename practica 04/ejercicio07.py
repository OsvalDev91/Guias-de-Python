n = int(input("Ingrese la cantidad de números que desea ingresar: "))

# Creamos una lista vacía para guardar los números
numeros = []

# Pedimos al usuario que ingrese cada uno de los números
for i in range(n):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Ordenamos los números de menor a mayor utilizando el método de selección
for i in range(len(numeros)):
    min_idx = i
    for j in range(i+1, len(numeros)):
        if numeros[j] < numeros[min_idx]:
            min_idx = j
    numeros[i], numeros[min_idx] = numeros[min_idx], numeros[i]

print(f"El número mayor es: {numeros[-1]}")
print(f"El número menor es: {numeros[0]}")
print(f"La sumatoria de los números es: {sum(numeros)}")
print(f"El promedio de los números es: {sum(numeros) / len(numeros)}")