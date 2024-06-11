import random

def obtener_eleccion_jugador():
<<<<<<< HEAD
    eleccion = input("piedra, papel o tijera").lower()
    while eleccion not in ["piedra", "papel" , "tijera"]:
        print("entrada invalida")
        eleccion = input("elije priedra, papel o tijera").lower
    return eleccion

def obtener_eleccion_computador():
    opciones = ["piedra","papel","tijera"]
    eleccion = random.choice(opciones)
=======
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        print("Entrada inválida, por favor elige nuevamente.")
        eleccion = input("Elige piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    eleccion = random.choice(opciones)
    return eleccion

>>>>>>> origin/main
