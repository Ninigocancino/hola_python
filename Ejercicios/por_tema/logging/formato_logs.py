#Ejercicio 1: Crea 3 logs donde se imprima el nivel y el mensaje separado por un guión


import logging

"""

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

"""

#Ejercicio 2: Toma el ejericico anterior y agrega al formato la fecha en que se produce el error 

"""

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

"""

#Ejercicio 3: Toma el ejericico anterior y cambia el formato en que se imprime la fecha del log para que se imprima la hora, minuto y segundos

"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%H:%M:%S"
)

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

"""

#Ejercicio 4: Toma el ejericico anterior y agrega un log de error que imprima el nombre de la persona que genera el error

"""

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%H:%M:%S"
)

nombre = "Juan"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

"""

#Ejercicio 5: Toma el ejercicio anterior y agregale una excepción que imprima un log error al dividir 2 entre 0

"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%H:%M:%S"
)

nombre = "Juan"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

try:
    division = 2 / 0
except:
    logging.error("Divisón entre 0")

"""


#Ejercicio 6: Toma el ejercicio anterior y ahora haz que la consola muestre más información sobre lo que ocurrer en el bloque de excepción

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%H:%M:%S"
)

nombre = "Juan"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

try:
    division = 2 / 0
except:
    logging.exception("Divisón entre 0")