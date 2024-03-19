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
    {"nombre": "Paco", "Apellido":"Botero", "Edad" :26},
    {"nombre": "Javier", "Apellido":"Tafur", "Edad" :25},
    {"nombre": "Emilio", "Apellido":"Quiñonez", "Edad" :24},
]

archivo = open("datos.csv", "w")
writer = csv.writer(archivo, delimiter=",")
archivo.close()