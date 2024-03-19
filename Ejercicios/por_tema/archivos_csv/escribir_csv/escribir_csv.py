#Ejercicio 1: Usar open y close

import csv 

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco","Botero",26],
    ["Javier","Quiñonez",24],
    ["Emeilio","Tafur",25]
]

datos_dict = [
    {"nombre": "Paco", "apellido":"Botero", "edad" :26},
    {"nombre": "Javier", "apellido":"Tafur", "edad" :25},
    {"nombre": "Emilio", "apellido":"Quiñonez", "edad" :24},
]

"""
archivo = open("datos.csv", "w")
writer = csv.writer(archivo, delimiter=",")
archivo.close()
"""

#Ejercicio 2 crear un archivo csv usando with
"""
with open("datos_2.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(columnas)
    writer.writerow(dato)
"""

#Ejercicio 3 crear un archivo csv con mas de una fila de datos
"""
with open("datos_3.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(columnas)
    writer.writerows(datos_lista)
"""

#Ejercicio 4 crear un archivo csv a partir de datos contenidos en una lista de diccionarios
    
with open("datos_4.csv", "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict)