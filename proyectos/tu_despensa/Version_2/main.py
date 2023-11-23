#---------------------------------------CASO DE USO-------------------------------------------

# Ramón trabaja mucho y casi siempre anda distraido por lo que es común que al momento de ir al super mercado olvide comprar alguno que otro artículo que necesitará en su despensa semanal. Lo más sensato sería que Ramón hiciera una lista en una hoja de papel pero los boligrafos y el papel son el tipo de cosas que Ramón suele olvidar comprar.

# Desafío: Ayuda a Ramón a solucionar su problema. Crea un programa que le permita al usuario crear una lista donde pueda escribir las compras que necesita realizar en el super mercado.

# Además de las funcionalidades anteriores el programa ahora debe: 
# -Permitir al usuario elegir la acción que desea realizar
# -Ingresar más de un elemento a la lista de productos

#________________________________________________________________________________________________________

#LÓGICA DEL PROGRAMA:

#Agregamos un poco de estilo al programa para que hacer más agradable lo que el usuario ve en su consola


print(" ")

print((" " * 40),"TuListApp")

print(" ")

print((" " * 20),"¡Bienvenido a la mejor herramienta para crear listas de supermercado!")
print((" " * 5),"Vamos a crear tu lista del super, para hacerlo solo tienes que seguir las instrucciones")

print("")

print("¿Qué deseas hacer?")
print("")
print("Ingresa el número 1 para crear una lista")
print("Ingresa el número 2 para salir")

print(" ")

eleccion = int(input("Ingresa tu eleción: "))

print(" ")


if eleccion == 1:
    
    productos = []

    print(" ")

    sig = input("¿Listo para ingresar tu primer item? (si), (no): ")

    print(" ")

    while sig == "si":
        item = input("¿Qué necesitas comprar?: ")
        productos.append(item)
        print(" ")

        print("Tu lista:")
        print(productos)

        print(" ")
        sig = input("¿Ingresar nuevo item? (si), (no)?:  ")
elif eleccion == 2:
    print("Hasta luego, vuelve pronto")
    exit()
else:
    print("ingresa una opción valida")