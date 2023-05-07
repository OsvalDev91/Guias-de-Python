def aplicar_descuento(precio, descuento):
    precio_descuento = precio * (1 - descuento / 100)
    return precio_descuento

def aplicar_iva(precio, iva):
    precio_iva = precio * (1 + iva / 100)
    return precio_iva


def total_a_pagar(cesta, descuento, iva):
    total = 0
    for producto, precio in cesta.items():
        precio_descuento = aplicar_descuento(precio, descuento.get(producto, 0))
        precio_iva = aplicar_iva(precio_descuento, iva.get(producto, 0))
        total += precio_iva
    return total

# cesta = {"Manzanas": 100, "Plátanos": 50, "Peras": 75}
cesta = {"Manzanas": 10, "Plátanos": 20}
descuentos = {"Manzanas": 0.10, "Plátanos": 0.10}
ivas = {"Manzanas": 0.13, "Peras": 0.13}

# Llamado a la función para obtener el total a pagar
total = total_a_pagar(cesta, descuentos, ivas)
total = round(total,2)

print(f"El total a pagar de la cesta es : ${total}")