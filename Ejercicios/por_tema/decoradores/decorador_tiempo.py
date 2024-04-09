import time


def medir_tiempo_ejecucion(funcion):
    
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"Tiempo total de ejecución: {fin-inicio}")
    return wrapper



@medir_tiempo_ejecucion
def recorrer_ciclo():

    for i in range(5):
        print(i)
        time.sleep(1)

recorrer_ciclo()