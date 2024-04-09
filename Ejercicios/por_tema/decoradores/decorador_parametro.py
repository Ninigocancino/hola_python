import time 

def medir_tiempo_ejecucion(funcion):

#Solución básica
    """
    def wrapper(rango):
        inicio = time.time()
        funcion(rango)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejercución: {tiempo_total}")
    """
#Solución optima

    def wrapper(*arg, **kwargs):
        inicio = time.time()
        funcion(*arg, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejercución: {tiempo_total}")

    return wrapper

@medir_tiempo_ejecucion
def recorrer_ciclo(rango):

    for i in range(rango):
        print(i)
        time.sleep(1)