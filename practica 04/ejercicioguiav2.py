empleados = []

def menu():
    while True:
        print('------- MENU -------')
        print('1 - Agregar Empleado')
        print('2 - Imprimir Empleados')
        print('3 - Salir')

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            imprimir_empleado()
        elif opcion == "3":
            print("HASTA LUEGO!!!!...")
            break
        else:
            print("Opción incorrecta")

def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))

    empleado = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo": sueldo
    }

    empleados.append(empleado)
    print("Empleado agregado")

def imprimir_empleado():
    if len(empleados) == 0:
        print("No hay empleados registrados")
    else:
        print("LISTA DE EMPLEADOS")
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Sueldo: {empleado['sueldo']}")

menu()