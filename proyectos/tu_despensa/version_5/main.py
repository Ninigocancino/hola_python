#---------------------------------------CASO DE USO-------------------------------------------

# Ramón trabaja mucho y casi siempre anda distraido por lo que es común que al momento de ir al super mercado olvide comprar alguno que otro artículo que necesitará en su despensa semanal. Lo más sensato sería que Ramón hiciera una lista en una hoja de papel pero los boligrafos y el papel son el tipo de cosas que Ramón suele olvidar comprar.

# Desafío: Ayuda a Ramón a solucionar su problema. Crea un programa que le permita al usuario crear una lista donde pueda escribir las compras que necesita realizar en el super mercado.

# Además de las funcionalidades anteriores el programa ahora debe: 
# 1.- Evitar que el uso de minúsculas o mayúsculas, así como de tildes en el nombre de usuario generer un error y eviten el acceso al programa
# 2.- En caso de equivocación al ingresar por parte del usuario, indicarle donde se efectuo el error, en el nombre del usuario o en la contraseña

#________________________________________________________________________________________________________

#LÓGICA DEL PROGRAMA:

#importamos las librerias o modulos que se implementarán en el programa
from tabulate import tabulate
from utilidades import quitar_tildes


#Agregamos un poco de estilo al programa para que hacer más agradable lo que el usuario ve en su consola

print(" ") #Estás líneas de código generan un espacio vacio en la consola al momento de mostrar contenido al usuario

print((" " * 40),"TuListApp")

print(" ")

print((" " * 20),"¡Bienvenido a la mejor herramienta para crear listas de supermercado!")
print((" " * 5),"Vamos a crear tu lista del super, para hacerlo solo tienes que seguir las instrucciones")

print(" ")


#se imprime el mensaje de la siguiente línea de codigo, para indicar al usuario que debe hacer 
print("Ingresa tu nombre de usuario y contraseña para crear tu nueva lista")

print(" ")

user = "RAMON JAMON" #agregamos una variable que recibe el nombre de un usuario autorizado para usar el programa y establecemos un valor 

contrasenia = "puerquitovaliente" #Agregamos una variable que guarda una contraseña necesaria para ingresar al programa y establecemos un valor

user_name = input("Ingrese su nombre: ") #Solicitamos al usuario que ingrese un nombre de usuario que será comparado con el valor establecido (un usuario con acceso)

user_name = user_name.upper()#Convertimos las letras en mayuscúlas

user_name = quitar_tildes(user_name) #usamos la función 'quitar_tildes' para eliminar las tildes


user_contrasenia = input("Ingrese la contraseña: ") #Solicitamos al usuario que ingrese la contraseña que compararemos con el valor que se definio como contraseña


#Con respecto a la versión anterior del código; separamos la validación de nombre de usuario y contraseña en dos estructuras 'if'
if user_name == user: #la primera validación se realiza al nombre de usuario

    if contrasenia == user_contrasenia:#se anida dentro de la primera validación la estructura 'if' que valida la contraseña

        while True: #Usamos un ciclo 'while' en 'True' para envolver el código de la versión anterior. 'while True' indica que mientras el código en 'Try' sea cierto el ciclo se continuará ejecutando.
        
            try:
            
                #Mostramos en consola la pregunta '¿Qué desas hacer?' y le mostramos dos opciones posibles
                print("¿Qué deseas hacer?")
                print("")
                print("Ingresa el número 1 para crear una lista")
                print("Ingresa el número 2 para salir")

                print(" ")

                eleccion = int(input("Ingresa tu eleción: ")) #Solicitamos al usuario que elija una de las opciones dadas, después usamos el metodo 'int' para covertir la respuesta del usuario en un valor numerico que almacenamos en la variable 'eleccion'
            
                print(" ")

                #Usamos un 'if' para controlar el flujo del programa. "Si la variable elección es exactamente igual a 1 el programa debería ejecutar las siguientes instrucciones: "

                if eleccion == 1:
                    
                    productos = [] #Crear una lista vacia y almacenarla en la variable 'productos'

                    print(" ") #Imprimir un espacio vacio en consola

                    sig = input("¿Listo para ingresar tu primer item? (si), (no): ") #Solicitar el usuario que ingrese en formato string una de las opciones disponibles. (si) para ingresar el primer item, (no) para no realizar la acción mencionada y se almacena la respuesta del usuario en la variable 'sig'.

                    print(" ") #Imprimir un espacio vacio en consola

                    while sig == "si": #Ejecutar un ciclo 'while', donde mientras 'sig' sea exactamente igual a "si" el ciclo while se ejecutara como verdadero y se realizan a su vez las siguientes acciones:
                        

                        item = input("¿Qué necesitas comprar?: ") #Se pide al usuario que ingres el nombre del artículo o producto que desea ingresar a la lista, el cuál se almacena en la variable 'item'
                        productos.append([item]) #Usamos el metodo 'append' para agregar el valor almacenado en 'item' como un dato de tipo lista a la lista productos
                        print(" ")

                        print("Tu lista:")
                        print(productos) #imprimimos los valores contenidos en la lista 'productos'

                        print(tabulate(productos, headers=["Productos a comprar"], tablefmt="grid")) #Imprimimos en un formato tabular los items que vayan agregando los usuarios en cada iteración

                        print(" ")
                        sig = input("¿Ingresar nuevo item? (si), (no)?:  ") #Preguntamos al usuario si desea ingresar un nuevo artículo y asignamos este nuevo valor a la variable 'sig' para que sea evaluada de nueva cuenta por el 'while'


                        #Agregamos un nuevo 'if' que permite detener el ciclo si el último valor de 'sig' es exactamente igual a "no"
                        if sig == "no":
                            
                            print("Nos vemos en tu proxima lista")
                            exit()
                            break

                elif eleccion == 2: #En caso de que la variable 'eleccion' sea exactamente igual a 2, se ejecutan las siguientes acciones:
                    
                    print("Hasta luego, nos vemos en tu proxima lista") #Se imprime en consola un mensaje de despedida 
                    exit() #Se cierra el programa
                else:
                    
                    print("ingresa una opción valida") #Si en la primera ejecución de la variable 'eleccion' (que pregunta al usuario que desea hacer) se ingresa un valor numérico diferente a 1 o 2, el programa indica al usuario que necesita ingresar un valor valido y cierra el programa 

            #Usamos una excepción de error, que se ejecuta cuando el 'Try' es falso, en este caso; cuando el 'input' en 'eleccion' no es un numero entero o 'int'
            except ValueError:
                
                print("Por favor, ingrese un número válido.") #Se imprime un mensaje que indica al usuario que debe ingresar un número, y la ejecución regresa al 'Try' para recibir una nueva respuesta del usuario
    else:
        print("Lo siento tu contraseña es incorrecta. por favor ingresa una contraseña valida") #Si la validación de contraseña es incorrecta se imprime el mensaje de esta línea de código

else:
    print("Lo siento tu usuario es incorrecto. Por favor ingresa un nombre de usuario valido") #Si la validación de contraseña es incorrecta se imprime el mensaje de esta línea de código

#________________________________________________________________________________________________________

#MEJORAR EL PROGRAMA (Lista las siguientes mejoras que necesitan hacerse en el programa):

# Se necesita que el programa permita al usuario ingresar la catidad y la unidad de medida de cada item
# El programa debe permitir dar un nombre a la lista 
# El programa debe imprimir la fecha de creación de la lista