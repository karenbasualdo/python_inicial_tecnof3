import pickle
import sys
import os
import random

def generar_ticket():
    while True:
        print("Ingrese los datos para generar un nuevo ticket")
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese su sector: ")
        asunto = input("Ingrese asunto: ")
        mensaje = input("Ingrese mensaje: ")
        n_ticket = random.randrange(1000, 9999)

        ticket = {
            'nombre': nombre,
            'n_ticket': n_ticket,
            'sector': sector,
            'asunto': asunto,
            'mensaje': mensaje
        }

        with open(f"ticket_{n_ticket}.pkl", "wb") as f:
            pickle.dump(ticket, f)

        print("""
        ==================================== 
            Se generó el siguiente ticket
        ====================================
        """)
        print(f"Su nombre: {nombre}")
        print(f"N°Ticket: {n_ticket}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("Recordar su número de ticket")
        
        opcion = input("Desea generar un nuevo ticket? (s/n): ").lower()
        if opcion != 's':
            break

def leer_ticket():
    while True:
        n_ticket = input("Ingrese el número del ticket que desea leer: ")
        ruta = f"ticket_{n_ticket}.pkl"
        
        if os.path.isfile(ruta):
            with open(ruta, "rb") as f:
                ticket = pickle.load(f)
                print(f"""
                ==================================== 
                        Detalles del ticket
                ====================================
                """)
                print(f"Su nombre: {ticket['nombre']}")
                print(f"N°Ticket: {ticket['n_ticket']}")
                print(f"Sector: {ticket['sector']}")
                print(f"Asunto: {ticket['asunto']}")
                print(f"Mensaje: {ticket['mensaje']}")
        else:
            print(f"No se encontró un ticket con el número {n_ticket}.")

        opcion = input("Desea leer otro ticket? (s/n): ").lower()
        if opcion != 's':
            break

while True:
    print("Hola, bienvenido al sistema de tickets")
    print("1- Generar un nuevo ticket")
    print("2- Leer ticket")
    print("3- Salir")

    seleccione = int(input("Seleccione: "))

    if seleccione == 1:
        generar_ticket()
    elif seleccione == 2:
        leer_ticket()
    elif seleccione == 3:
        print("Saliendo del sistema. ¡Hasta luego!")
        sys.exit()
    else:
        print("Selección no válida, por favor intente nuevamente.")
