import time 

def medir_tiempo_ejecucion(funcion):

    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejercución: {tiempo_total}")

    return wrapper

def decorador_puntos(funcion):

    def wrapper(*args, **kwargs):
        print(".............")
        funcion(*args, **kwargs)
        print(".............")

    return wrapper

@decorador_puntos
@medir_tiempo_ejecucion
def recorrer_ciclo(rango):

    for i in range(rango):
        print(i)
        time.sleep(1)