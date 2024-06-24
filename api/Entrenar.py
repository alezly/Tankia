import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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
model.fit(X_train, y_train)

# Realizar predicciones
predictions = model.predict(X_test)

# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, predictions)
print('Error cuadrático medio:', mse)


# predicción ejemplo
distancia = 50
diametro = 100
altura = 90
litroxminuto = 5

prediction = model.predict([[distancia, diametro, altura, litroxminuto]])
print('Tiempo de llenado:', prediction)