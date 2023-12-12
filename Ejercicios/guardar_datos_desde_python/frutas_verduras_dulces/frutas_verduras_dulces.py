#---------------------------------------------CASO DE USO------------------------------------------------

#Supon que debes listar nombres de frutas, verduras y dulces ¿cómo guardarias los datos ingresados por el usuario en un archivo CSV? 

import csv
import os

"""
with open('frutas_verduras_dulces.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ["Frutas","Verduras","Dulces"]
    escritor_csv.writerow(encabezado)

    frutas = input("Agrega el nombre de una fruta: ")
    verduras = input("Agrega el nombre de una verdura: ")
    dulces = input("Agrega el nombre de un dulce: ")

    escritor_csv.writerow([frutas,verduras,dulces])

    archivo_csv.close()

    """


"""
#En la primera version de este código solo podías ingresar una nueva línea de datos justo al momento de crear el archivo '.csv'. El código siguiente estabasado en el anterior pero ahora utiliza un ciclo 'while' para iterar el código las veces que el usuario necesite para ingresar tantos datos quiera.


with open('frut_verd_dulc.csv', 'w',newline='') as archivo_csv:

    escritor_csv= csv.writer(archivo_csv)

    encabezados=["Fruta","Verdura","Dulce"]
    escritor_csv.writerow(encabezados)

    while True:
        fruta = input("Agrega una fruta: ")
        verdura= input("Agrega una verdura: ")
        dulce = input("Agrega un dulce: ")

        escritor_csv.writerow([fruta,verdura,dulce])

        print("Se agrego una nueva línea de datos")

        respuesta = input("¿Quieres agregar más datos? s/n : ").lower()

        if respuesta!= "s":
            break
            archivo_csv.close()

"""


"""

#El código ahora permite al usuario asignar un nombre al archivo csv

nombre_archivo = input("Dale un nombre a tu archivo: ") #nueva línea en código

nombre_archivo = nombre_archivo + ".csv" #nueva línea en código

with open(nombre_archivo, "a", newline= '') as archivo_csv:
    archivo_csv = csv.writer(archivo_csv)

    encabezados = ["Fruta", "Verdura", "Dulce"]
    archivo_csv.writerow(encabezados)

    while True:
        fruta= input("Agrega una fruta: ")
        verdura= input("Agrega una verdura: ")
        dulce= input("Agrega un dulce: ")

        archivo_csv.writerow([fruta,verdura,dulce])

        iterador = input("¿Deseas agregar más datos? s/n: ").lower()

        if iterador != "s":
            break
            archivo_csv.close()

"""

#El código ahora permite guardar los archivos csv creados por el usuario en un nuevo directorio llamado 'datos_fvd'

if not os.path.isdir("datos_fvd"): #Nueva línea
    os.mkdir("datos_fvd") #Nueva línea

nombre_archivo = input("Agrega un nombre para tu archivo: ")

nombre_archivo = nombre_archivo + ".csv"

os.path.join("datos_fvd", nombre_archivo) #Nueva línea

with open(os.path.join("datos_fvd",nombre_archivo),"a", newline='') as archivo_csv: #Línea modificada
    escritor_csv = csv.writer(archivo_csv)

    encabezados = ["Fruta","Verdura","Dulce"]
    escritor_csv.writerow(encabezados)

    while True:
        fruta = input("Agrega una fruta: ")
        verdura = input("agrega una verdure: ")
        dulce = input("agrega un dulce: ")

        escritor_csv.writerow([fruta,verdura, dulce])

        iterador = input("¿Deseas agregar más datos? s/n: ").lower()

        if iterador != "s":
            break
            archivo_csv.close()