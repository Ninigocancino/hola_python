#Ejercicio 1: Empaqueta con zip dos listas

nombres = ["Juan", "Maria","Pablo", "Luis"]
apellidos = ["Gomez", "Luna", "Vaca"]

nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)

#Ejercicio 2: Desempaqueta los elementos del ejercicio anterior

nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

