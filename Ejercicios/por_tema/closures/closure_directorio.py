#Este código utiliza un closure que permite agregar datos de una persona a un diccionario

def agregar_persona_directorio():
    directorio = {}
    def agregar(nombre,edad,ciudad):
        directorio[nombre] = {"edad": edad,"ciudad": ciudad}
        return directorio
    return agregar

almacenar = agregar_persona_directorio()
directorio = almacenar("Paco", 27, "Villahermosa")
directorio = almacenar("Javier", 26, "Merida")
print(directorio)