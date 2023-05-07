numeros = input("Ingresa los números separados por comas: ")

lista_numeros = [int(num) for num in numeros.split(",")]

def elimina_duplicados(lista):
    conjunto = set(lista)
    lista_sin_duplicados = list(conjunto)
    return lista_sin_duplicados

# Llamamos a la función elimina_duplicados para eliminar los elementos duplicados
lista_sin_duplicados = elimina_duplicados(lista_numeros)

print("Lista sin duplicados:", lista_sin_duplicados)