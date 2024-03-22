#Ejercicio 1: crea un archivo pdb
def calcular_area_cuadrado(lado):

    area = lado*lado
    return area

lado_cuadrados = [1,3,4]
area_cuadrados = []
for lado in lado_cuadrados:
    area = calcular_area_cuadrado(lado)
    area_cuadrados.append(area)