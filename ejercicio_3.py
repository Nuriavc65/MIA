from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#datos
disparos = np.array([10,12,5,7]).reshape(-1,1)
posesion = np.array([55,60,45,50]).reshape(-1,1)
tiros_puerta = np.array([6,7,3,4]).reshape(-1,1)
X = np.hstack((disparos,posesion,tiros_puerta))
Y = np.array([3,2,1,1])

modelo = LinearRegression()
modelo.fit(X, Y)

x_pred = np.array([[12,55,6]])
y_pred = modelo.predict(x_pred)

#grafica ----->
plt.scatter(disparos, Y, color='blue', label='Datos de entrada')

#grafico para la predicion de fruta para 7 horas
plt.scatter(12, y_pred, color='blaCK', label='predicion de disparos, posesion y tiros a puerta')

#línea de regresión
plt.plot(X, modelo.predict(X), color='red', label='Línea de regresión')

plt.title('Regresión lineal: datps entrada vs goles')
plt.xlabel('X')
plt.ylabel('goles')
plt.legend()

#Mostrar el gráfico
plt.show()