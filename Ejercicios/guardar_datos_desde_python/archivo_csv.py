import csv

with open("alumnos.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezados = ["Nombre", "Grupo", "Genero"]
    escritor_csv.writerow(encabezados)

    nombre = input("Agrega tu nombre: ")
    grupo = input("Agrega el grupo al que perteneces: ")
    genero = input("Agrega tu genero: ")

    escritor_csv.writerow([nombre, grupo, genero])

    archivo_csv.close()