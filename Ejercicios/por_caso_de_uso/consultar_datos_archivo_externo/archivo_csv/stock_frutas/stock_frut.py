import csv

fruta = "Melon"

with open('muestra_frut.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    next(lector_csv)

    ubicar = False
    for i in lector_csv:
        frut = i[0]
        if frut == fruta:
            print(f"Tenemos disponible {fruta} en una de nuestras sucursales")
            ubicar = True
            break

if not ubicar:
    print(f"No contamos con {fruta} en ninguna de nuestras ubicaciones")




