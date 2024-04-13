import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo de texto, omitiendo las primeras 8 líneas de texto
data = np.loadtxt('rodrigo_opensignals_98d341fd4f0d_2024-04-12_12-07-25.txt', skiprows=6, usecols=5)

# Calcula el tiempo transcurrido entre cada muestra (asumiendo una frecuencia de muestreo de 1000 Hz)
# Usando np.linspace()
frecuencia_muestreo = 1000  # Hz
num_muestras = len(data)
tiempo_final = (num_muestras - 1) / frecuencia_muestreo  # Tiempo total de la señal
tiempo = np.linspace(0, tiempo_final, num_muestras)

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo, data)

plt.xlabel('Tiempo (s)')
plt.ylabel('EMG (mV)')
plt.title('Señal con oposición')
plt.grid(True)
plt.show()

