#Crea una calculadora simple que pueda realizar operaciones básicas como suma, resta, multiplicación y división. 

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicación(a,b):
    return a * b 

def division(a,b):
    return a / b



def calculadora():

    operacion = int(input("¿Qué operación quieres realizar? 1) suma, 2) resta, 3) multiplicación, 4) división:"))

    if operacion in (1,2,3,4):
        value_1 = int(input("Ingresa el primer valor: "))
        value_2 = int(input("Ingresa el segundo valor: "))

        if operacion == 1:
            resultado = suma(value_1,value_2)
            print(resultado)

        elif operacion == 2:
            resultado = resta(value_1, value_2)
            print(resultado)
        
        elif operacion == 3:
            resultado = multiplicacion(value_1,value_2)
            print(resultado)

        elif operacion == 4:
            resultado = division(value_1,value_2)
            print(resultado)


    else:
        print("Operación no valida, por favor ingres 1,2 o 3")

if __name__ == "__main__":
    calculadora()