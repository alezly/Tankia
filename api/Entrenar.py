import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.externals import joblib

# Cargar el archivo CSV
data = pd.read_csv('dataset_tiempo.csv')

# Seleccionar las características y la variable objetivo
X = data[['distancia', 'diametro', 'altura', 'litro_x_minuto']]
y = data['tiempo_llenado']

# Dividir el conjunto de datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train.values, y_train.values)

# Realizar predicciones
predictions = model.predict(X_test.values)

# Cálculo de R^2 y R^2 ajustado en data de prueba
r2_test = r2_score(y_test, model.predict(X_test))

n_test, n_vars = X_test.shape
r2_test_ajustado = 1 - (1 - r2_test)*(n_test-1)/(n_test-n_vars-1)

print("R2          en prueba = {:.5f}".format(r2_test))
print("R2 ajustado en prueba = {:.5f}".format(r2_test_ajustado))

#Guardar el modelo entrenado
joblib.dump(model, 'modelo_entrenado.pkl')

# predicción ejemplo
# distancia = 50
# diametro = 100
# altura = 90
# litroxminuto = 5

# prediction = model.predict([[distancia, diametro, altura, litroxminuto]])
# print('Tiempo de llenado:', prediction)