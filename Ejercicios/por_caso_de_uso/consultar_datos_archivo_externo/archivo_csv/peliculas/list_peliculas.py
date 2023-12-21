import csv

pelicula = "avatar"

with open("lista_peliculas.csv", "r") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    next(lector_csv)
    ubicar = False
    for i in lector_csv:
        movie = i[0]
        if movie == pelicula:
            print(f"El titulo {pelicula} está en la lista")
            ubicar = True
            break

if not ubicar:
    print(f"El titulo {pelicula} no se encuentra en el registro")
        


