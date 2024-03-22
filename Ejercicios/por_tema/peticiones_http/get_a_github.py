import requests

#Ejercicio 1: haz una etición GET a la API de GitHub e imprime el código de  estado de la petición 
"""
response = requests.get("https://api.github.com")
"""

"""
print(response)
"""

#Ejercicio 2: Trae los headers de la petición 

"""
print(response.headers)
"""

#Ejercicio 3: Muestra el código d eestado de la petición

"""
print(response.status_code)
"""

#Ejercicio 4: accede al cuerpo de la petición 

"""
#Forma 1:
print(response.content)
"""

"""
#Forma 2:
print(response.text)
"""
"""
#Forma 3:
print(response.json()["current_user_url"])
"""

#Ejercicio 5: Usa un endpoint de github para filtrar información de la petición

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q":"python"}
)

#print(response.status_code)

#Ejercicio 6: accede al cuero de la consulta en formato json y almacena el resultado en una variable

#print(response.json())

data = response.json()
print(data.keys())