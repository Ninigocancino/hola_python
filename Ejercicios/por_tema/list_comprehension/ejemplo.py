#List comprehension básico

"""

#Ejemplo: Trabajar con listas que contienen caracteres

ciudades_mx = ["Ciudad de México", "Monterrey", "Villahermosa","Guadalajara", "Merida", "Veracruz"]

mayusculas = [i.upper() for i in ciudades_mx]

print(mayusculas)

"""


#Ejemplo: Trabajar con listas que contienen valores númericos 

cifras = [23,45,98, 102,48, 12, 22, 12, 9, 89, 120, 406, 1002]

numeros = [ i for i in cifras if i > 800]

print(numeros)