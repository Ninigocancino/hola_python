#---------------------------------------------CASO DE USO------------------------------------------------

#Supon que debes listar nombres de frutas, verduras y dulces ¿cómo guardarias los datos ingresados por el usuario en un archivo CSV? 

import csv

with open('frutas_verduras_dulces.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ["Frutas","Verduras","Dulces"]
    escritor_csv.writerow(encabezado)

    frutas = input("Agrega el nombre de una fruta: ")
    verduras = input("Agrega el nombre de una verdura: ")
    dulces = input("Agrega el nombre de un dulce: ")

    escritor_csv.writerow([frutas,verduras,dulces])

    archivo_csv.close()