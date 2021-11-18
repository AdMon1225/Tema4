# Base para la solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatoria C
vaC = stats.norm(5, np.sqrt(0.2))
omega = 3 #Ahora tanto Omega como Theta son constantes, se escogen valores arbitrarios.
theta = 1

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t)
# Nótese que ya que tenemos otro proceso aleatorio X(t) disitnto, hay que repetir
# los mismos pasos que se siguieron en la parte A pero para el nuevo proceso aleatorio.
for i in range(N):
	C = vaC.rvs()
	x_t = C * np.cos(omega*t + theta)
	X_t[i,:] = x_t
    
# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de t
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
# Aquí se cambia la ecuación de Rxx por la dada en el problema 4.
Rxx = 25.2*np.cos(omega*t+theta)*np.cos(omega*(t+taus)+theta)

# Gráficas de correlación para cada realización y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{WW}(\tau)$')
plt.legend()
plt.show()