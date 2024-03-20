#Personaliza un logger para evitar que se defina el logger como root, luego importa el modulo en un nuevo archivo llamado 'main.py'  

import logging

logger = logging.getLogger(__name__)
print(logger)

logger.warning("Log deadvertencia")