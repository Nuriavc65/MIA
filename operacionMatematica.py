from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt 

tiros_puerta = np.array([8,5,4,6]).reshape(-1,1)
goles_anotados = np.array([3,3,1,2])

modelo = LinearRegression()
modelo.fit(tiros_puerta,goles_anotados)

plt.scatter(tiros_puerta,goles_anotados,color='red', label="Datos iniciales")

plt.plot(tiros_puerta,modelo.predict(goles_anotados),color='blue', label=" linear Regression")

plt.show()


m = modelo.coef_[0]
b = modelo.intercept_
print(f"peniente {m} intersecion {b}")
X = np.array([[3]])
pred = modelo.predict(X)
print(f"Para 3 tiros a puerta {pred}")

