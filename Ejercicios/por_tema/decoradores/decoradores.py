def funcion_decorador(funcion):

    def funcion_wrapper():

        print("Dentro de la funcion wrapper")
        funcion()

    return funcion_wrapper

def funcion_prueba():
    print("Función de prueba")

#Añadir el decorador como instancia

funcion_prueba = funcion_decorador(funcion_prueba)
funcion_prueba()

# # Añadir el decorador como instancia
#funcion_prueba = funcion_decorador(funcion_prueba)
#funcion_prueba()

# # añadir el decorador de manera pythonica
@funcion_decorador 
def funcion_prueba():
    print("Función de prueba")

funcion_prueba()