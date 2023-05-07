def validar_email(email):
    if email.find("@") != -1:
        return True
    else:
        return False

def solicitar_email():
    email = input("Ingrese su dirección de correo electrónico: ")
    if validar_email(email):
        print("La dirección de correo electrónico ingresada es válida")
    else:
        print("La dirección de correo electrónico ingresada no es válida")

solicitar_email()