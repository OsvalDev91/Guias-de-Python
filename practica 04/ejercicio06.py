agenda = {}

while True:
    nombre = input("Ingresa un nombre o 'salir' para terminar: ")
    
    if nombre == "salir":
        break
    
    if nombre in agenda:
        print("El número de teléfono de", nombre, "es:", agenda[nombre])
        
        respuesta = input("¿Quieres modificar el número de teléfono? (s/n): ")
        
        if respuesta.lower() == "s":
            telefono = input("Ingresa el nuevo número de teléfono para " + nombre + ": ")
            agenda[nombre] = telefono
    else:
        if nombre == "*":
            break
        
        telefono = input("Ingresa el número de teléfono para " + nombre + ": ")
        agenda[nombre] = telefono
        
print("Agenda actualizada:")
print(agenda)