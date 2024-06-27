import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Cargar el archivo CSV
data = pd.read_csv('dataset_tiempo.csv')

# Seleccionar las características y la variable objetivo
X = data[["distance", "diametro","altura","volumen_tanque", "tiempo_tanque"]]
y = data['tiempo']

# Dividir el conjunto de datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Tamaño de Entrenamiento = {}".format(X_train.shape))
print("Tamaño de Test          = {}".format(X_test.shape))

# Inicializar el modelo de regresión lineal
model = LinearRegression()

# Entrenar el model
model.fit(X_train, y_train)

# Cálculo de R^2 y R^2 ajustado en data de prueba
r2_test = r2_score(y_train, modelo.predict(X_train))

n_train, n_vars = X_train.shape

r2_test_ajustado = 1 - (1 - r2_test)*(n_train-1)/(n_train-n_vars-1)
r2_test_ajustado

print("R2          en prueba = {:.5f}".format(r2_test))
print("R2 ajustado en prueba = {:.5f}".format(r2_test_ajustado))
 