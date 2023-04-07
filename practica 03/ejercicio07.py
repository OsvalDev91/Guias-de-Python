montoTotal = 0.00
descuento = 0.00
obsequio = 0

cantDocenas = int(input("Digite la cantidad de docenas a comprar de x producto: "))
precioDocenas = int(input("Digite el precio por docena del x producto: "))

if cantDocenas > 3:
    obsequio = cantDocenas - 3
    montoTotal = cantDocenas * precioDocenas
    descuento = montoTotal * 0.15
    montoTotal -= descuento
else:
    obsequio = 0
    montoTotal = cantDocenas * precioDocenas
    descuento = montoTotal * 0.10
    montoTotal -= descuento

print("")
print("► Cantidad de docenas compradas:",cantDocenas)
print("► Precio por docena: $%.2f"%precioDocenas)
print("► Monto de descuento: $%.2f"%descuento)
print("► Total a pagar: $%.2f"%montoTotal)
print("► Catidad de unidades de obsequio:",obsequio)