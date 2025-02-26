from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


horas_sol = np.array([4, 6, 8, 10]).reshape(-1, 1)  
litros_agua = np.array([1000, 2000, 3000, 4000]).reshape(-1, 1) 
X = np.hstack((horas_sol,litros_agua))
Y = np.array([10, 15, 20, 25])   #Kg de producción de manzanas
'''
jstack junta ambas matrcies en una sola con una columna con horas_sol y otra columna al lado con litros_agua -->
4 1000
6 2000
8 3000
20 4000
con vstack hace los mismo pero en vertical -->
4    6     8    20
1000 2000 3000 4000

'''
modelo = LinearRegression()
modelo.fit(X, Y)

#pendiente y interseccion
m1 = modelo.coef_[0] #pendiente (m)
m2 = modelo.coef_[1] #pendiente (m) 
b =  modelo.intercept_  #interseccion (b)

#predicion de fruta para 7 horas Y 2500 litros
x_pred = np.array([[7,2500]])
y_pred = modelo.predict(x_pred)

#grafico con los datos
plt.scatter(X, Y, color='blue', label='Datos de entrada')

#grafico para la predicion de fruta para 7 horas
plt.scatter(x_pred, y_pred, color='blaCK', label='predicion para 7 horas')

#línea de regresión
plt.plot(X, modelo.predict(X), color='red', label='Línea de regresión')

plt.title('Regresión lineal: Producción de manzanas vs Horas de sol')
plt.xlabel('Horas de sol (h)')
plt.ylabel('Producción de manzanas (kg)')
plt.legend()

#Mostrar el gráfico
plt.show()