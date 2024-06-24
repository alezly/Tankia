import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Origen permitido para las peticiones (puedes usar '*' para permitir cualquier origen)
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

# Lee el archivo CSV y almacena su contenido en un DataFrame
data = pd.read_csv('dataset.csv')

@app.get("/")
async def root():
    return {"message": "hello Fastapi"}

# Endpoint de ejemplo
@app.get("/getMax")
async def getMinMax():
    max_distance_cm = data['distance'].max()
    max_distance_m = max_distance_cm / 100
    return {"max": round(max_distance_m, 2)}