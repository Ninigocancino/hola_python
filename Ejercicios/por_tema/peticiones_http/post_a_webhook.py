import requests

#Ejercicio 1: Crea una petición que solicite datos al servidor
url = "https://webhook.site/6dbbc723-ac21-4c6b-bf0b-1b01d1e2a8aa"

"""
payload = {"plato":"pasta","cantidad":2}
response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)
"""

#Ejercicio 2: Envia query params al servidor 

payload = {"plato":"pasta","cantidad":2}
query_params = {"nombre":"Florencio"}
response = requests.post(url, data=payload, params=query_params)
