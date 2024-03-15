def calcular_perimetro(*args):
    perimetro = 0
    for lado in args: 
        perimetro+= lado
    return perimetro

perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)

triangulo = calcular_perimetro(4,5,6)
print(triangulo)