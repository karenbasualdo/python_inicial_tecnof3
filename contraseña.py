import secrets
import string
import sys
import random

def generador_contraseña_letr():
    while True:
        longitud = random.randint(8, 16)
        password = ''.join(secrets.choice(string.ascii_letters) for i in range(longitud))
        print(f"Contraseña generada: {password}")
        opcion = input("No te gusto y deseas generar una nueva contraseña solamente con letras? (s/n): ").lower()
        if opcion != 's':
            break

def generador_contraseña_num():
    while True:
        longitud = random.randint(8, 16)
        password = ''.join(secrets.choice(string.digits) for i in range(longitud))
        print(f"Contraseña generada: {password}")
        opcion = input("No te gusto y deseas generar una nueva contraseña solamente con numeros? (s/n): ").lower()
        if opcion != 's':
            break

def generador_contraseña_letrynum():
    while True:
        longitud = random.randint(8, 16)
        caracteres_posibles = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(caracteres_posibles) for i in range(longitud))
        print(f"Contraseña generada: {password}")
        opcion = input("No te gusto y deseas generar una nueva contraseña con letra y numeros? (s/n): ").lower()
        if opcion != 's':
            break

def generador_contraseña_alfanumerica():
    while True:
        longitud = random.randint(8, 16)
        caracteres_posibles = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(caracteres_posibles) for i in range(longitud))
        print(f"Contraseña generada: {password}")
        opcion = input("No te gusto y deseas generar una nueva contraseña con letras, numeros y caracteres? (s/n): ").lower()
        if opcion != 's':
            break

print("Seleccione una de las siguientes opciones")

while True:
    print("1- Generar contraseña solo de Letras")
    print("2- Generar contraseña solo de números")
    print("3- Generar contraseña de Letras y números")
    print("4- Generar contraseña de Letras, números y caracteres")
    print("0- Salir")

    generador = int(input("Escriba la opción seleccionada: "))

    if generador == 1:
        generador_contraseña_letr()
    elif generador == 2:
        generador_contraseña_num()
    elif generador == 3:
        generador_contraseña_letrynum()
    elif generador == 4:
        generador_contraseña_alfanumerica()
    elif generador == 0:
        print("Saliendo del sistema. ¡Hasta luego!")
        sys.exit()
    else:
        print("Selección no válida, por favor intente nuevamente.")
