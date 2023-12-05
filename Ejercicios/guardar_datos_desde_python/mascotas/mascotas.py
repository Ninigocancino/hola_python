import csv

with open('mascotas.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezados=['nombre_mascota','especie','dueño']
    escritor_csv.writerow(encabezados)

    n_mascota = input("¿Cuál es el nombre de tu mascota?: ")
    especie_m = input("¿A qué especie pertenece tu mascota?: ")
    duenio_m = input("¿Cuál es tu nombre?: ")

    escritor_csv.writerow([n_mascota,especie_m,duenio_m])

    print("se creo un archivo CSV")

    archivo_csv.close()