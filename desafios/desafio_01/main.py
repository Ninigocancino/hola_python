"""
Luis y Luisa están planeando su boda, ellos consideran que no es necesario gastar tanto en una gran fiesta y desean ahorrar lo más posible. Mientras realizaban la planeación se dieron cuenta que podían ahorrarse mucho si el numero de invitados era lo más cercano posible al número de asistentes finales.

Desafío:

Crea un programa que muestre a los invitados un mensaje de invitación a la boda de Luis y Luisa con la información necesaria sobre la boda y después le pida confirmar si asistirán a la boda y que registre sus datos para agregarlos a la lista de invitados.

Al final Luis y Luisa deben contar con la lista de invitados que confirmaron su asistencia.

Genera 10 registros para confirmar que el programa funciona.
"""

print("                                NOS CASAMOS                                ")
print("")
print("                                Luis & Luisa                               ")
print("")
print("")
print("              Y queremos que seas parte de nuestro enlace nupcial          ")
print("             para nosotros no hay nada más importante que compartir        ")
print("               con aquellos que son especiales para nosotros este          ")
print("                maravilloso momento de nuestra vida como pareja            ")
print("")
print("               Por lo cuál queremos invitarte a nuestra ceremonia          ")
print("")
print("                     La cita es el 05 de febrero de 2024                   ")
print("             En la capilla del Sagrado Corazón en el parque central        ")
print("                                A las 11:00 am                             ")


print("                 Para que todo sea perfecto durante la cermonia            ")
print("                te pedímos que por favor confirmes tu asistencia           ")
print("")
print("                     ¿Deseas confirmar tu asistencia ahora?                ")
print("                Para confirmar la asistencia ahora ingresar [1]            ")
print("                         Para hacerlo después ingresa [2]                  ")
print("")

eleccion = int(input("¿Qué deseas hacer?: "))

if eleccion == 1:
    registro= []

    invitado = input("Por favor ingresa tu nombre completo: ")
    confirmacion = input("¿Confirmas tu asistencia? para sí [s], para no [n]")
    if confirmacion == "s":
        print("Gracias por confirmar tu aistencia")
        registro.append(invitado)
        print(registro)
else:
    print("Esperamos tu confirmación para reservar tu lugar :) ")