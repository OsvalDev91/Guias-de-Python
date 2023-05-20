from django.shortcuts import render

def persona_detalle(request, nombre, edad):
    context = {
        'nombre': nombre,
        'edad': edad,
        }
    return render(request, 'persona_detalle.html', context)