#Ejercicio 1: Crea 3 logs donde se imprima el nivel y el mensaje separado por un guión

"""
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

"""

#Ejercicio 2: Toma el ejericico anterior y agrega al formato la fecha en que se produce el error 

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")