#--------------------------------------------- CASO DE USO -------------------------------------------

#Supon que debes llenar una hoja de registro para un tramite

import csv 

with open('datos_personales.csv', 'w', newline='')as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    encabezado = ['Nombre','Edad', 'DNI']
    escritor_csv.writerow(encabezado)

    nombre= input('Ingresa tu nombre: ')
    edad = input('ingresa tu edad: ')
    dni = input('ingresa tu DNI: ')

    escritor_csv.writerow([nombre,edad, dni])

    archivo_csv.close()