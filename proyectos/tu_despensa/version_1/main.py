#---------------------------------------CASO DE USO-------------------------------------------

# Ramón trabaja mucho y casi siempre anda distraido por lo que es común que al momento de ir al super mercado olvide comprar alguno que otro artículo que necesitará en su despensa semanal. Lo más sensato sería que Ramón hiciera una lista en una hoja de papel pero los boligrafos y el papel son el tipo de cosas que Ramón suele olvidar comprar.

# Desafío: Ayuda a Ramón a solucionar su problema. Crea un programa que le permita al usuario crear una lista donde pueda escribir las compras que necesita realizar en el super mercado.

# El programa debe: 
# -Brindar instrucciones básicas al ususario sobre como usar el programa.
# -Ser capaz de interactuar con el usuario y permitirle ingresar datos (al menos un artículo).
# -Permitir al usuario saber si se ha realizado una acción correctamente.

#________________________________________________________________________________________________________

#LÓGICA DEL PROGRAMA:

#Agregamos un poco de estilo al programa para que hacer más agradable lo que el usuario ve en su consola

print(" ")

print((" " * 40),"")

print(" ")

print((" " * 20),"¡Bienvenido a la mejor herramienta para crear listas de supermercado!")
print((" " * 5),"Vamos a crear tu lista del super, para hacerlo solo tienes que seguir las instrucciones")

print("")

#Solicitamos al usuario que ingrese un dato, en este caso el nombre de algún enser que necesite comprar

item = input("Escribe el artículo que necesitas en tu despensa:  ")

#Creamos una lista vacia, donde guradaremos el dato ingresado por el usuario 
productos = []

#Usamos la estructura de control condicional 'if' para validar que el usuario haya ingresado un dato. De haberse ingresado el dato, este se agrega a la lista 'productos' usando el metodo 'append'
if item:
    producto = item
    productos.append(producto)

print(" ") #Está línea unicamente separa en consola el mensaje inicial que solicita un input, del mensaje de salida

print(f"Haz agregado '{item}' a tu lista de productos") #Está línea utiliza interpolación e imprime un mensaje de salida que indica al usuario que se ha agregado un producto o artículo a la lista

#Reforzamos el feedback del usuario monstrando el contenido de la lista
print("")
print("Tu lista:")
print(productos)

#________________________________________________________________________________________________________

#MEJORAR EL PROGRAMA (Lista las siguientes mejoras que necesitan hacerse en el programa):

# 1.- El programa actual solo permite agregar un artículo a la lista, lo optimo sería que el usuario pudiera ingresar cuantos artículos necesite.
# 2.- La interacción con el usuario podría ser más amigable.