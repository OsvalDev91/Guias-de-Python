precioHora = 10.00
horasExtras = 0
salario = 0.00

nombre = (input("Digite el nombre de la persona: "))
dui = (input("Digite el DUI de la persona: "))
horasTrabajadas = int(input("Digite la cantidad de horas trabajadas: "))

if horasTrabajadas <= 40:
    salario = precioHora * horasTrabajadas
else:
    horasExtras = horasTrabajadas - 40
    salario = precioHora * 40 + (horasExtras * precioHora) * 2.0

print("")
print("► Nombre de la persona:",nombre," ► DUI de la persona:",dui)
print("► Cantidad de horas trabajadas: ",horasTrabajadas," ► Sueldo a remunerar $%.2f: "%salario)