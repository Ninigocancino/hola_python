#------------------------------------Guardar datos en CSV usando python----------------------------------

#Ejemplo 01: Como convertir datos ingresados desde el usuario a través de input

import csv #Importar la libreria CSV

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
    


