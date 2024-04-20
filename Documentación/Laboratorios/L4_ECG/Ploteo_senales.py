import numpy as np
import matplotlib.pyplot as plt

# Función para cargar y plotear un archivo
def plot_ecg(file_name, title):
    # Cargar el archivo de texto y omitir las primeras 8 líneas
    data = np.loadtxt(file_name, skiprows=5, usecols=5)
    # Calcular el tiempo transcurrido entre cada muestra
    tiempo = np.arange(len(data)) / 1000
    # Plotear los datos
    plt.plot(tiempo, data)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('ECG (mV)')
    plt.title(title)
    plt.grid(True)
    plt.savefig(f'{title}.png')
    plt.show()
    plt.close()

# Plotear cada archivo
plot_ecg('REPOSO.txt', 'Reposo')
plot_ecg('respiraciones_rapidas.txt', 'Respiraciones rápidad')
plot_ecg('durante actividad.txt', 'Durante actividad')
plot_ecg('luego de actividad fisica intensa.txt', 'Despues de actividad')
