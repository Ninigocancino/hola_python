import csv
import os

with open('datos_raza.csv', 'a', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ["Nombre_raza","Talla","Tamaño_cm","País_origen"]
    escritor_csv.writerow(encabezado)

    while True: 
        n_raza = input("Agrega la raza del perro: ").lower()
        talla = input("Agrega la talla del perro g(grande)/m(Mediana),p(Pequeña),b(Miniatura): ").lower()
        tamanio_max = input("Agrega el tamaño máximo de la raza en cm: ")
        tamanio_min = input("Agregra el minimo de la raza en cm: ")
        peso_min = input("Agrega el peso minimo de la raza en kg: ")
        peso_max = input("Agrega el peso maximo de la raza en kg: ")
        pais = input("Agrega el país de origen de la raza: ").lower()

        escritor_csv.writerow([n_raza,talla,tamanio_max,tamanio_min, peso_min,peso_max,pais])

        agregador = input("Deseas agregar otra raza al registro? s/n: ")

        if agregador != "s":
            break
            archivo_csv.close()