nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate python
este curso contempla todos los detalles
que se necesitan para aprender para encontrar
un trabajo como programador.
"""

print(len(nombre_curso))  # nos permite encontrar la longitud de un string
# los argumentos son los valores que le pasamos a una funcion en este caso nombre_curso

print(nombre_curso[0])
# los indices empiezan desde 0 no desde 1

print(nombre_curso[0:8])
# entonces el primero dice desde donde empieza el segundo dice hasta donde como un rango

print(nombre_curso[9:])
# si no se pone el segundo numero se tomara el final del strig

print(nombre_curso[:8])
# cuando no se pone el primero el valor por defecto es 0

print(nombre_curso[:])
# asume los dos valores por defecto el de la izq y derecha dando toda la variable
