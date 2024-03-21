import json

#Ejercicio 1: Crea un programa que creé un archivo serializado en formato json con los datos nombre, apellido y edad

persona = {
    "nombre": "Jacinto",
    "apellido" : "Flores",
    "edad" : 45
}

objeto_json = json.dumps(persona, indent=2)
with open("persona.json", "w") as archivo_json:
    archivo_json.write(objeto_json)