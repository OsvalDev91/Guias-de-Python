palabra = input("Ingrese una palabra: ")
palindromo = ""

i = len (palabra) - 1
while i >= 0:
    palindromo += palabra[i]
    i -= 1

if palabra == palindromo:
    print ("La palabra es un palindromo ")
    print ("Palabra ingresada: "+ palindromo)
else:
    print ("La palabra no es un palindromo")
    print ("Palabra ingresada: "+ palindromo)