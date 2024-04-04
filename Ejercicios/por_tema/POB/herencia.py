class Persona:

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

    def agregar_documento_identidad(self,numero_documento):
        self.documento_identidad = numero_documento
        print("Documento guardado")

    def ejecutar_accion(self):
        print("Haciendo algo")

class Deportista(Persona):
    def __init__(self,nombre,apellido,edad,deporte):
        super().__init__(nombre,apellido,edad)
        self.deporte = deporte

    def ejecutar_acción(self):
        super().ejecutar_accion()
        print(f"practicando {self.deporte}")

juliana = Deportista("Juliana", "Cortes", 26, "volleyball")
juliana.agregar_documento_identidad(1234)
print(juliana.deporte)