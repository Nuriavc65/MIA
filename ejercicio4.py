from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

x1 = np.array ([11,27,34,43,58]).reshape(-1,1)
x2 = np.array([1200,2800,3500,4400,5900]).reshape(-1,1)

x= np.hstack((x1,x2))
y = np.array([14,29,36,45,60])

x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(x, y, test_size=0.2, random_state= 0)

modelo = LinearRegression()
modelo.fit(x_entrenamiento,y_entrenamiento)
y_prediccion = modelo.predict(x_entrenamiento)

mse = mean_squared_error(y_prueba,y_entrenamiento)
r2 = r2_score(y_prueba,y_entrenamiento) 
mae = mean_absolute_error(y_prueba,y_entrenamiento)

print(f"mse: {mse} ,r2: {r2}, mae: {mae}")