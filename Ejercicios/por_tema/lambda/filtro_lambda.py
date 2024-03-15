lista_numeros = [1,2,3,4,5,6,7,8,9,10]

lista_pares = list(filter(lambda numero: numero %2 == 0, lista_numeros))
print(lista_pares)