#--------------------------------------------- CASO DE USO -------------------------------------------

#Supon que debes llenar una hoja de registro para un tramite

import csv 
import os

"""
with open('datos_personales.csv', 'w', newline='')as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ['Nombre','Edad', 'DNI']
    escritor_csv.writerow(encabezado)

    nombre= input('Ingresa tu nombre: ')
    edad = input('ingresa tu edad: ')
    dni = input('ingresa tu DNI: ')

    escritor_csv.writerow([nombre,edad, dni])

    archivo_csv.close()
"""

"""
with open('data_personal.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    header = ["Nombre", "Estado_civil", "Ciudad de residencia"]
    escritor_csv.writerow(header)

    while True: 
        nombre = input("Agrega tu nombre: ")
        est_civil = input("Agrega tu estado civil: ")
        ciudad_natal = input("Agrega la ciudad donde naciste: ")

        escritor_csv.writerow([nombre,est_civil,ciudad_natal])

        print("Se agrego una nueva fila de datos al archivo 'data_personal.csv' ")

        respuesta = input("¿Quieres agregar una nueva fila de datos? s/n: ").lower()

        if respuesta != "s":
            break

    archivo_csv.close()
"""



nombre_archivo = input("¿Con qué nombre deseas guardar este archivo?: ")

nombre_archivo = nombre_archivo + ".csv"

with open(nombre_archivo, "w", newline='') as archivo_csv:
    archivo_csv = csv.writer(archivo_csv)

    encabezados = ["Nombre", "Edad", "Promedio"]
    archivo_csv.writerow(encabezados)

    while True:

        nombre = input("Escribe tu nombre: ")
        edad = input("Escribe tu edad: ")
        promedio = input("¿Cuál es tu promedio actual?: ")

        archivo_csv.writerow([nombre,edad,promedio])

        print("")
        iterador = input("¿Deseas guardar más datos? s/n: ")

        if iterador != "s":
            break

            archivo_csv.close()