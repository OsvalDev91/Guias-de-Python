montoFijo = 30.00
km = 0.00
montoAdicional = 0.00
montoTotal = 0.00

km = float(input("Digite los Kilometros recorridos por el vehiculos: "))

if km <= 300:
    montoTotal = montoFijo
elif km > 300 and km <= 1000:
    montoAdicional = (km - 300)* 0.25
    montoTotal = montoFijo + montoAdicional
else:
    montoAdicional = (km - 1000)* 0.50
    montoTotal = montoFijo + montoAdicional

print("")
print("► Monto incluido por los Kilometros extra recorridos: $%.2f"%montoAdicional)
print("► Kilometros recorridos por el vehiculo:",km,"Km")
print("► Monto total a pagar por el alquiler del vehiculo: $%.2f"%montoTotal)