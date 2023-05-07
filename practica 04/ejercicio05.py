def contar_palabras():
    cadena = input("Introduce una cadena: ")

    # Convertimos todas las palabras a minúsculas para evitar contar palabras duplicadas con diferente capitalización
    cadena = cadena.lower()

    # Separamos la cadena en palabras individuales utilizando el método split()
    palabras = cadena.split()

    # Creamos un diccionario vacío para almacenar las palabras y su cantidad de apariciones
    contador = {}

    # Recorremos la lista de palabras y contamos la cantidad de veces que aparece cada una
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador

resultado = contar_palabras()
print(resultado)