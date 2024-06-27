import joblib
import math as mt
import pandas as pd

modelo = joblib.load('modelo_entrenado.pkl')

#predicción ejemplo
distance = [71]
diametro = [95]
altura = [142]
litroxminuto = [4]
radio = [47.5]
volumen = [(mt.pi*((diametro[0]/2)**2)*altura[0])/1000]
volumen_agua = [(mt.pi*((diametro[0]/2)**2)*distance[0])/1000]
tiempoTanque = [volumen[0] / litroxminuto[0]]
tiempoAgua = volumen_agua[0] / litroxminuto[0]
tiempo_final = (volumen[0]-volumen_agua[0])/litroxminuto[0]
print(tiempoTanque, tiempo_final, tiempoAgua)


datos_prueba = pd.DataFrame({'distance':distance, 'diametro':diametro,
                             'altura':altura, 'volumen_tanque':volumen, 'tiempo_tanque':tiempoTanque
                             })

prediction = modelo.predict(datos_prueba)

print('prediccion', prediction)