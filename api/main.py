import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import math as mt
import random
class Distance(BaseModel):
    data: int

DistanceData = {"data":2}

app  = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Origen permitido para las peticiones (puedes usar '*' para permitir cualquier origen)
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

@app.get("/")
async def root():
    return {"message": "hello Fastapi"}

@app.get("/api/getDistance")
async def getDistance():
    #leyendo el modelo
    modelo = joblib.load('modelo_entrenado.pkl')
    #datos para la prediccion
    diametro = [95]
    altura = [142]
    litroxminuto = [random.uniform(3.8, 4.4)]
    volumen = [(mt.pi*((diametro[0]/2)**2)*altura[0])/1000]
    tiempoTanque = [volumen[0] / litroxminuto[0]]
    datos_prueba = pd.DataFrame({'distance':[DistanceData['data']], 'diametro':diametro,
                                'altura':altura, 'volumen_tanque':volumen, 'tiempo_tanque':tiempoTanque})

    prediction = modelo.predict(datos_prueba)

    return {'tiempo': prediction[0], 'distancia':DistanceData['data'], 'litroxminuto':litroxminuto[0]}

@app.post("/api/setDistance")
async def setDistance(distance:Distance):
    DistanceData["data"] = distance.data
    return "All Ok!"

# @app.get("/prediction")
# async def cargarModelo():
#     modelo = joblib.load('modelo_entrenado.pkl')

#     #predicción ejemplo
#     distancia = 50
#     diametro = 100
#     altura = 90
#     litroxminuto = 5

#     prediction = model.predict([[distancia, diametro, altura, litroxminuto]])

#     print('prediccion', prediction)