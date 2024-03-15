numeros = [4,8,10,20,22,23,14,1,5,15]

lista_pares = list(filter(lambda numero: numero %2 == 0, numeros))

mapa = list(map(lambda numero:numero*10, lista_pares))
print(mapa)