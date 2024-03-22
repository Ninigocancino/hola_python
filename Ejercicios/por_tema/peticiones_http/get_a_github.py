import requests

#Ejercicio 1: haz una etición GET a la API de GitHub e imprime el código de  estado de la petición 
response = requests.get("https://api.github.com")
print(response)

#Ejercicio 2: Trae los headers de la petición 

print(response.headers)