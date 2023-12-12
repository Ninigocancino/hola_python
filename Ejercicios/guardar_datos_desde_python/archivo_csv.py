#------------------------------------Guardar datos en CSV usando python----------------------------------

import csv #Importar la libreria CSV


"""
#Caso 01: Como convertir datos ingresados desde el usuario a través de input


with open("alumnos.csv", "w", newline="") as archivo_csv: #Usar 'with open' para abrir un archivo csv con permisos de escritura. Donde 'alumnos.csv' será el nombre del archivo, 'w' indica el permiso de escritura y 'newline=""' permnite crear una nueva linea en el archivo
    escritor_csv = csv.writer(archivo_csv) # Se asigna a la variable 'escritor_csv' los permisos para escribir valores en el archivo

    encabezados = ["Nombre", "Grupo", "Genero"] #Creamos la variable encabezados listar los nombres de los encabezados de las columnas, si es que el archivo debe contenerlo 
    escritor_csv.writerow(encabezados) #La variable 'escritor_csv' escribe en la primera fila del archivo el contenido de la variable 'encabezado' es decir; los encabezados de columna


    #Se crean variables para recibir los valores que se almacenaran en el archivo csv 
    nombre = input("Agrega tu nombre: ") 
    grupo = input("Agrega el grupo al que perteneces: ")
    genero = input("Agrega tu genero: ")

    escritor_csv.writerow([nombre, grupo, genero]) #Volvemos a usar el metodo '.writerow' en 'escritor_csv' para agregar los valores de las variables 'nombre', 'grupo' y 'genero' por debajo de la fila del encabezado

    archivo_csv.close() #Usamos el metodo '.close' para cerrar el programa después de que los datos se escriban

""" 


"""
#Caso 02: agregar más datos al archivo si es necesario



with open('alumnos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezados = ["Nombre", "Grupo", "Genero"]
    escritor_csv.writerow(encabezados)

    nombre_al = input("Nombre del alumno: ")
    grupo_al = input("Grupo del alumno: ")
    genero_al = input("Genero del alumno: ")

    escritor_csv.writerow([nombre_al,grupo_al, genero_al])

    print("Se agrego una nueva fila con datos al archivo")

    while True:
        p = input("¿Deseas agregar más datos? (si)/(no)")

        p = p.lower()

        if p == "si":
            nombre_al = input("Nombre del alumno: ")
            grupo_al = input("Grupo del alumno: ")
            genero_al = input("Genero del alumno: ")

            escritor_csv.writerow([nombre_al,grupo_al, genero_al])
            print("Se agrego una nueva fila con datos al archivo")
        else:
            break

"""

"""
#Caso 03: además de la lógica anterior;permitirle al usuario darle un nombre al archivo que guardará los datos que ingrese

nombre_archivo = input("Ingresa el nombre del archivo: ")

nombre_archivo = nombre_archivo + ".csv"

with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezados = ["Nombre", "Grupo", "Genero"]

    escritor_csv.writerow(encabezados)

    while True:
        nombre_al = input("Nombre del alumno: ")
        grupo_al = input("Grupo del alumno: ")
        genero_al = input("Genero del alumno: ")

        escritor_csv.writerow([nombre_al,grupo_al,genero_al])

        print("Se agrego una nueva línea de datos")

        eleccion = input("¿Deseas agregar más datos? s/n: ").lower()

        if eleccion != "s":
            break

    archivo_csv.close()

"""

#Caso 04: además de la lógica anterior; el programa debe ser capaz de guardar los archivos csv creados en una carpeta propia

import os

if not os.path.isdir("Datos_alumnos"):
    os.mkdir("Datos_alumnos")


nombre_archivo = input("Dale un nombre a la tabla: ")

nombre_archivo =nombre_archivo + ".csv"

os.path.join("Datos_alumnos", nombre_archivo)


with open(os.path.join("Datos_alumnos", nombre_archivo), 'a', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezados = ["Nombre", "Edad", "Grado"]
    escritor_csv.writerow(encabezados)

    while True:
        nombre = input("Nombre del alumno: ")
        edad = input("Ingresa la edad del alumno: ")
        grado = input("Agrega el grado al que pertenece el alumno: ")

        escritor_csv.writerow([nombre,edad,grado])

        print("Se agregaron nuevos datos")

        eleccion = input("¿Agregar más datos? s/n: ").lower()

        if eleccion != "s":
            print("No vemos pronto")
            break
    
    archivo_csv.close()







