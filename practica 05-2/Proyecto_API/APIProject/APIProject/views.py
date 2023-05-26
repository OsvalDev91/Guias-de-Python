import requests
from django.shortcuts import render

# Ejercicio numero 1
def tabla_usuarios(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    usuarios = response.json()

    campos = ['ID', 'NAME', 'USERNAME', 'EMAIL', 'PHONE']
    datos = []

    for usuario in usuarios:
        usuario_data = {
            'ID': usuario['id'],
            'NAME': usuario['name'],
            'USERNAME': usuario['username'],
            'EMAIL': usuario['email'],
            'PHONE': usuario['phone'],
        }
        datos.append(usuario_data)

    return render(request, 'ejercicio01.html', {'campos': campos, 'datos': datos})

# Ejercicio numero 2
def mostrar_formulario(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    post = response.json()

    return render(request, 'ejercicio02.html', {'post': post})