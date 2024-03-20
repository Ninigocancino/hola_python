#Crea un archivo que guarde los registros de logs en sus diferentes niveles de seguridad

import logging

logging.basicConfig(level=logging.DEBUG, filename="Ejemplo_logs.log",filemode="w")

logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")