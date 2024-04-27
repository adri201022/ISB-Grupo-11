import numpy as np
import matplotlib.pyplot as plt

# Cargo is archivos
data1 = np.loadtxt('eeg_punto1.txt',skiprows=5, usecols=5)
data2 = np.loadtxt('eeg_punto2.txt',skiprows=5, usecols=5)
data3 = np.loadtxt('eeg_punto3_denuevo.txt',skiprows=5, usecols=5)
data4 = np.loadtxt('eeg_preguntas.txt',skiprows=5, usecols=5)

# calculo el tiempo entre muestra (mi frecuencia de muestreo es de 1000)
tiempo1 = np.arange(len(data1)) / 1000
tiempo2 = np.arange(len(data2)) / 1000
tiempo3 = np.arange(len(data3)) / 1000
tiempo4 = np.arange(len(data4)) / 1000

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo1, data1)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG ojos cerrados por 30 segundos')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo2, data2)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG intervalo ojos abierto-cerrado')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo3, data3)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG ojos cerrados por 30 segundos')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo4, data4)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG ejercicios')


# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

