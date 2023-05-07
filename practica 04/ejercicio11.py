def titulo(cadena):
    palabras = cadena.split()
    resultado = []
    for palabra in palabras:
        resultado.append(palabra[0].upper() + palabra[1:].lower())
    return " ".join(resultado)

cadena = input("Ingrese una cadena de texto: ")
cadena_convertida = titulo(cadena)

print(cadena_convertida)