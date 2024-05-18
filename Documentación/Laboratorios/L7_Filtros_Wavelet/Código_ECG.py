import numpy as np
import pywt
import matplotlib.pyplot as plt
from numpy import array, linspace
# Lectura de documento txt con tabulación (\t) como delimitador
datos = np.genfromtxt("REPOSO.txt", delimiter="\t")

# Nos quedamos con los datos del sensor (asumiendo que están en unidades arbitrarias)
ecg_datos = datos[:, -2]

# Convertir los datos de señal a milivoltios (mV)
ecg_datos_mV = (((array(ecg_datos) / 1024) - 0.5) * 3000) / 1000

# Definir el tramo de la señal que deseas analizar
start = 0  # Índice de inicio del tramo
end = 20000    # Índice de fin del tramo
ecg_tramo_mV = ecg_datos_mV[start:end]

# Aplicar la transformada wavelet
wavelet = 'db4'
level = 5
coeffs = pywt.wavedec(ecg_tramo_mV, wavelet, level=level)

# Calcular el nivel de ruido y el nivel de la señal sobre la magnitud absoluta de la señal
noise_level = np.std(ecg_datos_mV) # Estimación del nivel de ruido
n_samples = len(ecg_tramo_mV)  # Estimación del nivel de la señal

# Manejo de excepciones para evitar RuntimeWarning si la señal no tiene variabilidad
threshold = noise_level * np.sqrt(2 * np.log(n_samples))


# Filtrar los coeficientes con el umbral calculado
filtered_coeffs = [pywt.threshold(coeff, threshold, mode='soft') for coeff in coeffs]

# Reconstruir la señal filtrada
filtered_signal_mV = pywt.waverec(filtered_coeffs, wavelet)

# Graficar el tramo original y el tramo filtrado
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(ecg_tramo_mV)
plt.title('Tramo de la Señal de ECG en reposo')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.subplot(2, 1, 2)
plt.plot(filtered_signal_mV)
plt.title('Tramo de la Señal de ECG en reposo Filtrada')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.tight_layout()
plt.show()
plt.close()


#AHORA para la señal en respiraciones rápidas
datos_respiraciones_Rapidas = np.genfromtxt("respiraciones_rapidas.txt", delimiter="\t")

# Nos quedamos con los datos del sensor (asumiendo que están en unidades arbitrarias)
ecg_datos_respiraciones = datos_respiraciones_Rapidas[:, -2]

# Convertir los datos de señal a milivoltios (mV)
ecg_datos_mV_respiraciones = (((array(ecg_datos_respiraciones) / 1024) - 0.5) * 3000) / 1000

# Definir el tramo de la señal que deseas analizar
start = 0  # Índice de inicio del tramo
end = 10000    # Índice de fin del tramo
ecg_tramo_mV_respiraciones = ecg_datos_mV_respiraciones[start:end]

# Aplicar la transformada wavelet
wavelet = 'db4'
level = 5
coeffs1 = pywt.wavedec(ecg_tramo_mV_respiraciones, wavelet, level=level)

# Calcular el nivel de ruido y el nivel de la señal sobre la magnitud absoluta de la señal
noise_level1 = np.std(ecg_datos_mV_respiraciones) # Estimación del nivel de ruido
n_samples1 = len(ecg_tramo_mV_respiraciones)  # Estimación del nivel de la señal

# Manejo de excepciones para evitar RuntimeWarning si la señal no tiene variabilidad
threshold = noise_level1 * np.sqrt(2 * np.log(n_samples1))


# Filtrar los coeficientes con el umbral calculado
filtered_coeffs1 = [pywt.threshold(coeff, threshold, mode='soft') for coeff in coeffs1]

# Reconstruir la señal filtrada
filtered_signal_mV_respiraciones = pywt.waverec(filtered_coeffs1, wavelet)

# Graficar el tramo original y el tramo filtrado
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(ecg_tramo_mV_respiraciones)
plt.title('Tramo de la Señal de ECG en respiraciones rápidas')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.subplot(2, 1, 2)
plt.plot(filtered_signal_mV_respiraciones)
plt.title('Tramo de la Señal de ECG en respiraciones rápidas Filtrada')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.tight_layout()
plt.show()
plt.close()

#AHORA para la señal en actividadd

datos_actividad = np.genfromtxt("durante actividad.txt", delimiter="\t")

# Nos quedamos con los datos del sensor (asumiendo que están en unidades arbitrarias)
ecg_datos_actividad = datos_actividad[:, -2]

# Convertir los datos de señal a milivoltios (mV)
ecg_datos_mV_actividad = (((array(ecg_datos_actividad) / 1024) - 0.5) * 3000) / 1000

# Definir el tramo de la señal que deseas analizar
start = 0  # Índice de inicio del tramo
end = 10000    # Índice de fin del tramo
ecg_tramo_mV_actividad = ecg_datos_mV_actividad[start:end]

# Aplicar la transformada wavelet
wavelet = 'db4'
level = 5
coeffs2 = pywt.wavedec(ecg_tramo_mV_actividad, wavelet, level=level)

# Calcular el nivel de ruido y el nivel de la señal sobre la magnitud absoluta de la señal
noise_level2 = np.std(ecg_datos_mV_actividad) # Estimación del nivel de ruido
n_samples2 = len(ecg_tramo_mV_actividad)  # Estimación del nivel de la señal

# Manejo de excepciones para evitar RuntimeWarning si la señal no tiene variabilidad
threshold = noise_level2 * np.sqrt(2 * np.log(n_samples2))


# Filtrar los coeficientes con el umbral calculado
filtered_coeffs2 = [pywt.threshold(coeff, threshold, mode='soft') for coeff in coeffs2]

# Reconstruir la señal filtrada
filtered_signal_mV_actividad = pywt.waverec(filtered_coeffs2, wavelet)

# Graficar el tramo original y el tramo filtrado
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(ecg_tramo_mV_actividad)
plt.title('Tramo de la Señal de ECG en actividad ')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.subplot(2, 1, 2)
plt.plot(filtered_signal_mV_actividad)
plt.title('Tramo de la Señal de ECG en actividad Filtrada')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.tight_layout()
plt.show()
plt.close()