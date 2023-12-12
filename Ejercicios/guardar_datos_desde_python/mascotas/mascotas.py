import csv

"""
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
"""



"""
with open('datos_mascotas.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ['Nombre_mascota', 'Especie', 'Dueño']

    escritor_csv.writerow(encabezado)

    while True:
        nombre_m = input("Nombre de tu mascota: ")
        especie_m = input("Especie de tu mascota:")
        duenio = input("Tu nombre: ")

        escritor_csv.writerow([nombre_m,especie_m,duenio])

        print("se agrego una nueva lienea en datos_mascotas.csv")

        respuesta = input("¿Quieres agregar una nueva línea de datos? s/n:  ").lower()

        if respuesta != "s":
            break

    archivo_csv.close()

"""

#El código ahora permite al usuario asignar un nombre al archivo csv

nombre_archivo = input("Dale un nombre a tu archivo: ") #nueva línea

nombre_archivo = nombre_archivo + '.csv' #nueva línea

with open(nombre_archivo, "w", newline = '') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ["Nombre_mascota","Especie_mascota","Edad_mascota"]
    escritor_csv.writerow(encabezado)

    while True:
        n_mascota = input("¿Cuál es el nombre de tu mascota?: ")
        e_mascota = input("¿A qué especie pertenece tu mascota?: ")
        ed_mascota = input("¿Qué edad tiene tu mascota?: ")

        escritor_csv.writerow([n_mascota,e_mascota,ed_mascota])

        print("")
        iterador = input("¿Deseas agregar más datos? s/n: ").lower()

        if iterador != "s":
            break
            archivo_csv.close()