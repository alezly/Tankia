import pandas as pd
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

containerData = {"data":""}

app  = FastAPI()
connected_sockets: List[WebSocket] = []

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

@app.post("/api/data")
async def receive_data(data: SensorData):
    print(f"Recibido data: {data}")
    containerData["data"] = data
    notify_all_clients({"message": "Datos recibidos correctamente"})
    return {"message": "Datos recibidos correctamente"}

@app.get("/api/getDistance")
async def get_distance(data: SensorData):
    print(f"Recibido data: {data}")
    return containerData

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_sockets.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Aquí puedes procesar los datos recibidos del ESP32
            print(f"Recibido Daniel: {data}")
            # Notificar a todos los clientes conectados
            notify_all_clients({"message": "Datos recibidos correctamente"})
    except WebSocketDisconnect:
        connected_sockets.remove(websocket)

def notify_all_clients(message):
    print("notify_all_clients")
    for socket in connected_sockets:
        print("Viendo Socket",socket.state)
        if socket.state:
            try:
                print(str(message))

                socket.send_text(str(message))
            except Exception as e:
                print(f"Error sending message: {e}")
                connected_sockets.remove(socket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
