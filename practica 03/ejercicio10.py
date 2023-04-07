totalHoras = 0
totalMinutos = 0
costo = 0.00

horas = int(input("Ingrese las horas de estacionamiento: "))
minutos = int(input("Ingrese los minutos de estacionamiento: "))

totalMinutos = (horas * 60) + minutos

if totalMinutos % 60 > 0:
    totalHoras = (totalMinutos // 60) + 1
else:    
    totalHoras = (totalMinutos//60)

costo = totalHoras * 1.50

print("")
print("► Tiempo registrado de estacionamiento es de →",horas,"Horas",minutos,"Minutos")
print("► Monto a pagar por el tiempo de estacionamiento es de: $%.2f"%costo)