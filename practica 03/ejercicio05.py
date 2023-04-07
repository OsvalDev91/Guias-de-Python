t = int(input("Ingrese la hora actual del reloj (en formato de 24 horas): "))
h = int(input("Ingrese el número de horas a partir de ahora: "))

nueva_hora = (t + h) % 24

if nueva_hora == 0:
    nueva_hora = 12
    sufijo = "AM"
elif nueva_hora < 12:
    sufijo = "AM"
else:
    nueva_hora -= 12
    sufijo = "PM"

print("En", h, "horas, el reloj marcará las", nueva_hora, sufijo)