import csv

nombre_usuario = "ramon_jamon"

with open('muestra.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    next(lector_csv)

    encontrado = False
    for fila in lector_csv:
        nombre = fila[0]
        if nombre == nombre_usuario:
            print(f"El dato {nombre_usuario} existe en el registro")
            encontrado = True
            break

if not encontrado:
    print(f"Este dato: {nombre_usuario} no se está en el registro")

