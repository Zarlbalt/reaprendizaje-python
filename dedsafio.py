import random

def obtener_eleccion_jugador():
    eleccion = input("piedra, papel o tijera").lower()
    while eleccion not in ["piedra", "papel" , "tijera"]:
        print("entrada invalida")
        eleccion = input("elije priedra, papel o tijera").lower
    return eleccion

def obtener_eleccion_computador():
    opciones = ["piedra","papel","tijera"]
    eleccion = random.choice(opciones)