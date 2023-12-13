#Crea una función que calcule una regla de tres

#Supongamos que 2 litros de pintura cuestan $10. Si queremos saber cuánto costarán 5 litros, podemos usar la regla de tres directa.

def regla_tres(a,b,c):
    x = a / b

    respuesta = c * x

    print(respuesta)


cantidad_conocida = 2
suma_conocida = 10
suma_a_saber = 5

regla_tres(suma_conocida, cantidad_conocida,suma_a_saber)