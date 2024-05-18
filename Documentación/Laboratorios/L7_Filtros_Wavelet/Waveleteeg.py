import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pywt
from scipy import signal
from scipy.signal import firwin, lfilter, iirnotch
from statistics import median
import math

VCC = 3.3
n = 10

Fs = 1000
uploaded = files.upload()

# Leer el archivo
file_name = "referencia.txt"
datos = np.loadtxt(file_name)
print(datos)
datos = datos[:, 8]
print(datos)
datos = 1000*((((datos/(2**n)) - 0.5) * VCC)/1009)

frec_muestreo = Fs
tiempo = np.arange(len(datos)) / frec_muestreo

niveles = 4
coeficientes = pywt.wavedec(datos, 'db8', level=niveles)

plt.figure(figsize=(10, 10))
plt.subplot(niveles + 2, 1, 1)
plt.plot(datos)
plt.title('Señal Original')


for i, detalle in enumerate(coeficientes[1:]):
    plt.subplot(niveles + 2, 1, i + 2)
    plt.plot(detalle)
    plt.title(f'Detalle Nivel {i+1}')

plt.subplot(niveles + 2, 1, niveles + 2)
plt.plot(coeficientes[0])
plt.title(f'Aproximación Nivel {niveles}')

plt.tight_layout()
plt.show()

# Realizar la descomposición en wavelets
coeffs = pywt.wavedec(datos, 'db8', level=4)

# Establecer un umbral para el denoising
all_coeffs_flat = np.concatenate([c.flatten() for c in coeficientes])


desv = np.median(all_coeffs_flat)/0.6745
sq =  math.sqrt(math.log(len(datos)))
umbral = desv*sq
print(umbral)

Ts = 1/Fs
# Aplicar el umbral a los coeficientes
coeffs_umbral = [pywt.threshold(c, umbral, mode='soft') for c in coeffs]

# Reconstruir la señal denoised
senal_denoised = pywt.waverec(coeffs_umbral, 'db8')

plt.figure(figsize=(10, 4))
t_1 = np.arange(0, len(datos)*Ts, Ts)
plt.plot( tiempo,datos, label='Señal Original')
plt.title('Señal Original')



plt.tight_layout()
plt.show()
-0.0003424451968020734

plt.figure(figsize=(10, 4))
plt.plot( tiempo,senal_denoised, label='Señal Denoised')
plt.title('Señal filtrada (db8)')

plt.tight_layout()
plt.show()

coef_aproximacion = coeffs_umbral[0]

# Reconstruir la señal comprimida
senal_comprimida = pywt.waverec([coef_aproximacion], 'db8')

# Obtener el tiempo correspondiente a los datos
t_2 = np.linspace(0, len(datos)/1000, len(senal_denoised))  # Suponiendo que la frecuencia de muestreo es 1000 Hz

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(tiempo, datos, label='Señal Original')
plt.title('Señal Original')


plt.subplot(2, 1, 2)
plt.plot(t_2, senal_denoised, label='Señal Comprimida', color='red')
plt.title('Señal Comprimida')
plt.xlabel('Tiempo (s)')

plt.legend()
plt.grid(True)
plt.show()

uploaded2 = files.upload()
VCC = 3.3
n = 10

Fs = 1000
# Leer el archivo
file_name2 = "ojos_abiertos_cerrados.txt"
datos1 = np.loadtxt(file_name2)
print(datos1)
datos1 = datos1[:, 8]
print(datos1)
datos1 = 1000*((((datos1/(2**n)) - 0.5) * VCC)/1009)

frec_muestreo = Fs
tiempo = np.arange(len(datos1)) / frec_muestreo

niveles = 4
coeficientes = pywt.wavedec(datos1, 'db8', level=niveles)
print(len(coeficientes))
plt.figure(figsize=(10, 10))
plt.subplot(niveles + 2, 1, 1)
plt.plot(datos1)
plt.title('Señal Original')


for i, detalle in enumerate(coeficientes[1:]):
    plt.subplot(niveles + 2, 1, i + 2)
    plt.plot(detalle)
    plt.title(f'Detalle Nivel {i+1}')

plt.subplot(niveles + 2, 1, niveles + 2)
plt.plot(coeficientes[0])
plt.title(f'Aproximación Nivel {niveles}')

plt.tight_layout()
plt.show()
5

# Realizar la descomposición en wavelets
coeffs = pywt.wavedec(datos1, 'db8', level=4)

# Establecer un umbral para el denoising
all_coeffs_flat = np.concatenate([c.flatten() for c in coeficientes])


desv = np.median(all_coeffs_flat)/0.6745
sq =  math.sqrt(math.log(len(datos1)))
umbral = desv*sq
print(umbral)

Ts = 1/Fs
# Aplicar el umbral a los coeficientes
coeffs_umbral = [pywt.threshold(c, umbral, mode='soft') for c in coeffs]

# Reconstruir la señal denoised
senal_denoised = pywt.waverec(coeffs_umbral, 'db8')

plt.figure(figsize=(10, 4))
tiempo = np.arange(len(datos1)) / Fs
plt.plot( tiempo,datos1, label='Señal Original')
plt.title('Señal Original - Abrir y Cerrar')


plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot( tiempo,senal_denoised, label='Señal Denoised')
plt.title('Señal filtrada (db8)')
plt.tight_layout()
plt.show()

coef_aproximacion = coeffs_umbral[0]

# Reconstruir la señal comprimida
senal_comprimida = pywt.waverec([coef_aproximacion], 'db8')

# Obtener el tiempo correspondiente a los datos
t_2 = np.linspace(0, len(datos1)/1000, len(senal_denoised))  # Suponiendo que la frecuencia de muestreo es 1000 Hz

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(tiempo, datos1, label='Señal Original')
plt.xlim(1,4)
plt.title('Señal Original - Abrir y Cerrar')


plt.subplot(2, 1, 2)
plt.plot(t_2, senal_denoised, label='Señal Comprimida', color='red')
plt.xlim(1,4)
plt.title('Señal Comprimida')
plt.xlabel('Tiempo (s)')

plt.legend()
plt.grid(True)
plt.show()

uploaded2 = files.upload()
VCC = 3.3
n = 10

Fs = 1000
# Leer el archivo
file_name3 = "preguntas.txt"
datos2 = np.loadtxt(file_name3)
print(datos2)
datos2 = datos2[:, 8]
print(datos2)
datos2 = 1000*((((datos2/(2**n)) - 0.5) * VCC)/1009)

frec_muestreo = Fs
tiempo = np.arange(len(datos2)) / frec_muestreo

niveles = 4
coeficientes = pywt.wavedec(datos2, 'db8', level=niveles)
print(len(coeficientes))
plt.figure(figsize=(10, 10))
plt.subplot(niveles + 2, 1, 1)
plt.plot(datos2)
plt.title('Señal Original')


for i, detalle in enumerate(coeficientes[1:]):
    plt.subplot(niveles + 2, 1, i + 2)
    plt.plot(detalle)
    plt.title(f'Detalle Nivel {i+1}')

plt.subplot(niveles + 2, 1, niveles + 2)
plt.plot(coeficientes[0])
plt.title(f'Aproximación Nivel {niveles}')

plt.tight_layout()
plt.show()
5

# Realizar la descomposición en wavelets
coeffs = pywt.wavedec(datos2, 'db8', level=4)

# Establecer un umbral para el denoising
all_coeffs_flat = np.concatenate([c.flatten() for c in coeficientes])


desv = np.median(all_coeffs_flat)/0.6745
sq =  math.sqrt(math.log(len(datos2)))
umbral = desv*sq
print(umbral)

Ts = 1/Fs
# Aplicar el umbral a los coeficientes
coeffs_umbral = [pywt.threshold(c, umbral, mode='soft') for c in coeffs]

# Reconstruir la señal denoised
senal_denoised = pywt.waverec(coeffs_umbral, 'db8')

plt.figure(figsize=(10, 4))
tiempo = np.arange(len(datos2)) / Fs
plt.plot( tiempo,datos2, label='Señal Original')
plt.title('Señal Original - Preguntas')



plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 4))
plt.plot( tiempo,senal_denoised, label='Señal Denoised')
plt.title('Señal filtrada (db8)')
plt.tight_layout()
plt.show()

coef_aproximacion = coeffs_umbral[0]

# Reconstruir la señal comprimida
senal_comprimida = pywt.waverec([coef_aproximacion], 'db8')

# Obtener el tiempo correspondiente a los datos
t_2 = np.linspace(0, len(datos2)/1000, len(senal_denoised))  # Suponiendo que la frecuencia de muestreo es 1000 Hz

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(tiempo, datos2, label='Señal Original')
plt.xlim(1,4)
plt.title('Señal Original - Preguntas')


plt.subplot(2, 1, 2)
plt.plot(t_2, senal_denoised, label='Señal Comprimida', color='red')
plt.xlim(1,4)
plt.title('Señal Comprimida')
plt.xlabel('Tiempo (s)')

plt.legend()
plt.grid(True)
plt.show()