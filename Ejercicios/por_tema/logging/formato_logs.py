#Ejercicio 1: Crea 3 logs donde se imprima el nivel y el mensaje separado por un guión

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")