from sklearn.externals import joblib

modelo = joblib.load('modelo_entrenado.pkl')

#predicción ejemplo
distancia = 50
diametro = 100
altura = 90
litroxminuto = 5

prediction = model.predict([[distancia, diametro, altura, litroxminuto]])

print('prediccion', prediction)