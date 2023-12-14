"""

#------------------------------Ejercicio 01

#Define una función llamada sumar que tome dos números como parámetros y devuelva su suma.

def sumar(a,b):
    print(a + b)

sumar(3,2)

"""


"""

#------------------------------Ejercicio 02

#Crea una función llamada saludar que tome un nombre como parámetro y devuelva un saludo personalizado.

def saludar(n):
    print(f"Hola {n}, bienvenido a las funciones con Python")

saludar("Goku")

"""


"""

#------------------------------Ejercicio 03

#Escribe una función llamada cuadrado que tome un número como parámetro y devuelva su valor al cuadrado.

def cuadrado(num):
    print(num ** 2)

cuadrado(2)

"""


#------------------------------Ejercicio 04

#Crea una función llamada par_o_impar que tome un número como parámetro e imprima si es par o impar.

numero = int(input("Ingresa un número: "))

def par_o_impar(p):

    if p != 0 and p % 2 == 0:
        return "Es par"
    else:
        return "Es impar"


resultado = par_o_impar(numero)
print(resultado)
