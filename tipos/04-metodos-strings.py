animal = "   chanCHito feliz   "
# el nombre tecnico para las "funciones" como upper seria "Metodos"
# metodos es una funcion que se encuentra dentro de un objeto
print(animal.upper())  # convierte el string en letras mayusculas
print(animal.lower())  # convierte el string en letras minusculas
print(
    animal.capitalize()
)  # convierte el primer caracter en mayusculas y los demas en minusculas

print(
    animal.title()
)  # convierte la primera letra de cada palabra en mayuscula y las demas en minusculas

print(animal.strip())  # remueve todos los espacios de la izq y de la derecha

print(animal.strip().capitalize())  # podemos contatenar metodos


print(animal.lstrip())  # quita los espacios del lado izq
print(animal.rstrip())  # quita los espacios del lado derecho

print(animal.find("CH"))  # nos devuelve el indice
# en caso de que en la terminal salga -1 significa que no lo encontro

print(
    animal.replace("CH", "j")
)  # esta busca lo que introduscas en el primer espacio y  en el segundo es con lo que lo remplaza

print("nCH" in animal)  # devuelve un boolean si se encuentra en el string
print("nCH" not in animal)  # busca si la cadena no se encuentra en el string
