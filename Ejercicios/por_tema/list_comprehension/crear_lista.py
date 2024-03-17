#Crea listas usando el ciclo for y luego crea la misma lista usando List Comprehension

"""
#Estructura de list comprehension:
lista = [expresion(elemento) for elemento in objeto_iterable]
"""
"""
lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = num ** 2
    lista_cuadrados.append(cuadrado)

print("Ciclo for", lista_cuadrados)


list_comprehension = [num**2 for num in lista_num]
print("list comprehension", list_comprehension)

"""

#Ejercicio 2: Toma como base el ejercicio anterior, pero ahora crea una función que sustituya en la expresion 'list comprehension' la instrucción de elevar al cuadrado los números de la lista inicial

def elevar_cuadrado(num):
    return num**2

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = num ** 2
    lista_cuadrados.append(cuadrado)

print("Ciclo for", lista_cuadrados)


list_comprehension = [elevar_cuadrado(num) for num in lista_num]
print("list comprehension", list_comprehension)