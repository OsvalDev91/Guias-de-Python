from django.shortcuts import render
from django.http import JsonResponse

def persona_detalle(request, nombre, edad):
    context = {
        'nombre': nombre,
        'edad': edad,
        }
    return render(request, 'persona_detalle.html', context)


def math(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        operacion = request.POST.get('operacion')

        if operacion == 'sumar':
            resultado = num1 + num2
        elif operacion == 'restar':
            resultado = num1 - num2
        elif operacion == 'multiplicar':
            resultado = num1 * num2
        elif operacion == 'dividir':
            resultado = num1 / num2

        context = {
            'resultado': resultado,
        }
        return render(request, 'calc.html', context)

    return render(request, 'calc.html')

# def math(request):
#     if request.method == 'POST':
#         num1 = int(request.POST.get('num1'))
#         num2 = int(request.POST.get('num2'))
#         operacion = request.POST.get('operacion')

#         if operacion == 'sumar':
#             resultado = num1 + num2
#         elif operacion == 'restar':
#             resultado = num1 - num2
#         elif operacion == 'multiplicar':
#             resultado = num1 * num2
#         elif operacion == 'dividir':
#             resultado = num1 / num2

#         return JsonResponse({'resultado': resultado})

#     return JsonResponse({'error': 'No se recibieron datos válidos'})