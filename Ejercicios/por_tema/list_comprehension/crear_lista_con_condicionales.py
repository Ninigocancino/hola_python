"""
lista = [expresion(elemento) for elemento in objeto_iterable if condicion]
lista = [expresion(condicion) for elemento in objeto_iterable]
"""
#Ejercicio 1: Crea una expresión list comprehension donde se guarden los cuadrados de una lista dada y luego crea una list comprhension con una condición que imprima solo aquellos que cudadros cuyo numero original sea para
def calcular_cuadrado(numero):
    return numero**2

def es_par(numero):
    return numero % 2 == 0

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = [calcular_cuadrado(num) for num in lista_num]
print(lista_cuadrados)

lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print(lista_cuadrados_pares)

#Ejercicio 2:

lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print(lista_resultados)