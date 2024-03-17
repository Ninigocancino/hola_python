#Crea un archivo csv vacio

import csv

ruta = "csv_vacio.csv"

archivo_abierto = open(ruta, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()