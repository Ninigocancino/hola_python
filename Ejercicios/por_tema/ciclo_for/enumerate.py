"""
enumerate(iterable, start=0)
"""

#Ejercicio 1: Muestra los indices de una lista de elementos

nombres = ["Saul", "Alejandro", "Ana", "Emiliano"]
nombres_enumerados = enumerate(nombres, start=5)
print(nombres_enumerados)
print(list(nombres_enumerados))