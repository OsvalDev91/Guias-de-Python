sueldoNeto = float(input("Ingrese salario neto: "))

isss = 0.03
afp = 0.0725
sueldoGravable = 0.00
isr = 0.00
descuento1 = 0.00
descuento2 = 0.00

if sueldoNeto >= 1000:
    isss = 30.00
else:
    descuento1 = isss * sueldoNeto

descuento2 = sueldoNeto * afp
sueldoGravable = sueldoNeto - (descuento1 + descuento2)

if 0.01 <= sueldoGravable <= 472:
    isr = 0.00
elif 472.01 <= sueldoGravable <= 895.24:
    isr = (sueldoGravable - 472.00) * 0.10 + 17.67
elif 895.25 <= sueldoGravable <= 2038.10:
    isr = (sueldoGravable - 895.24) * 0.20 + 60.00
elif sueldoGravable >= 2038.11:
    isr = (sueldoGravable - 2038.10) * 0.30 + 288.57

print("sueldo total con descuento de ISSS y AFP: $%.2f" % sueldoGravable)
print("impuesto sobre la renta: $%.2f" % isr)
