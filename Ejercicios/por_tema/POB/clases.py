class Persona:
    tipo = "humano"

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

    def agregar_documento(self, documento_identidad):
        self.documento_identidad = documento_identidad
        print("Documento guardado")


paco = Persona("Paco", "Botero", 27)
print(paco.nombre)
paco.agregar_documento(1234)