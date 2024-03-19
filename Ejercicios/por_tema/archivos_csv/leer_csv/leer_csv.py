import csv


#Ejercicio 1: Lee un archivo csv y muestralo en formato de lista en la consola
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    next(reader) #esta instrucción evita que la primer fila del archivo se lea 
    for fila in reader:
        print(fila)