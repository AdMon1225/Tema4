# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import random

# Variables aleatorias son C y Z
vaC = stats.norm(5, np.sqrt(0.2)) # Gaussiana
vaZ = stats.uniform(0, np.pi/2) # "uniformemente distribuida" 

# Omega constante en el punto a, con lo cual se escoge un valor dentro del rango
vcO = random.uniform(2*np.pi*59.1, 2*np.pi*60.1) 


# Creación del vector de tiempo
T = 200			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 20
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (C y Z independientes), son las realizaciones
for i in range(N):
	C = vaC.rvs()
	Z = vaZ.rvs()
	x_t = C * np.cos(vcO*t + Z) 
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
Prom = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, Prom, lw=6, label='Promedio de las N realizaciones') #lw from linewidth

# Se grafica el promedio teórico
E = 10/np.pi * (np.cos(vcO*t) - np.sin(vcO*t)) #Esto viene de la solución a mano, teórica
plt.plot(t, E, '-.', lw=4, label='Resultado teórico del promedio')


# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.legend()
plt.show()
