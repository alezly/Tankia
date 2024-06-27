import pandas as pd
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.externals import joblib

class Distance(BaseModel):
    data: int

DistanceData = {"data":0}

app  = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.1.133:8080","http://localhost:8080"],  # Origen permitido para las peticiones (puedes usar '*' para permitir cualquier origen)
    # allow_origins=["http://localhost:8080"],  # Origen permitido para las peticiones (puedes usar '*' para permitir cualquier origen)
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

# Lee el archivo CSV y almacena su contenido en un DataFrame
data = pd.read_csv('dataset.csv')

class SensorData(BaseModel):
    distance: float

@app.get("/")
async def root():
    return {"message": "hello Fastapi"}

@app.post("/api/")
# Endpoint de ejemplo
@app.get("/getMax")
async def getMinMax():
    max_distance_cm = data['distance'].max()
    max_distance_m = max_distance_cm / 100
    return {"max": round(max_distance_m, 2)}

@app.get("/api/getDistance")
async def getDistance():
    return DistanceData

@app.post("/api/setDistance")
async def setDistance(distance:Distance):
    DistanceData["data"] = distance.data
    return "All Ok!"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
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
