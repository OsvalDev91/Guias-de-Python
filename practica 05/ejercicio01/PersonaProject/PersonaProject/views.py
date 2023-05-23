from django.shortcuts import render
from django.http import JsonResponse

# Ejercicio persona
def persona_detalle(request, nombre, edad):
    context = {
        'nombre': nombre,
        'edad': edad,
        }
    return render(request, 'persona_detalle.html', context)

# Ejercicio Calculadora
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

# Ejercicio Titulares de noticia.
titulares = [
    "Titular de noticia 1",
    "Titular de noticia 2",
    "Titular de noticia 3",
    "Titular de noticia 4",
    "Titular de noticia 5",
    "Titular de noticia 6",
    "Titular de noticia 7",
    "Titular de noticia 8",
    "Titular de noticia 9",
    "Titular de noticia 10",
    "Titular de noticia 11",
    "Titular de noticia 12",
    "Titular de noticia 13",
    "Titular de noticia 14",
    "Titular de noticia 15",
    "Titular de noticia 16",
    "Titular de noticia 17",
    "Titular de noticia 18",
    "Titular de noticia 19",
    "Titular de noticia 20"
]

def home(request):
    return render(request, 'home.html')

def resultados(request):
    palabra_clave = request.GET.get('palabra_clave', '')
    titulares_coincidentes = [titular for titular in titulares if palabra_clave.lower() in titular.lower()]

    context = {
        'palabra_clave': palabra_clave,
        'titulares_coincidentes': titulares_coincidentes,
    }

    return render(request, 'resultados.html', context)

# Ejercicio lista de usuarios
from django.shortcuts import render

usuarios = [   
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'María', 'edad': 30},
    {'nombre': 'Ana', 'edad': 28},
]

def lista_usuarios(request):
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'lista-usuarios.html', context)
