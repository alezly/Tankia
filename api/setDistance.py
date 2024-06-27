import requests
import json

url = 'http://localhost:8000/api/setDistance'
data = {'data': 30}

# Convertir el diccionario de datos a una cadena JSON
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

# Imprimir la respuesta
print(response.json())
