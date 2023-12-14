#Convertiremos funciones de expresión convencinal a expresiones lambdas

def suma(x,y):
    print(x + y)

suma(8,9)



print("versión lamda")

suma_lambda = lambda x,y: x + y

resultado = suma_lambda(4,3)

print(resultado)

