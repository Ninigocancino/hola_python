
import unicodedata

def quitar_tildes(input_str):

    #Elimina las tildes deuna cadena de caracteres utiliza la función unicodedata.normalize para convertir el string a su forma de composición canónica (NFKD), y luego utiliza una comprensión de lista para filtrar los caracteres que son marcadores de combinación (diacríticos)

    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])