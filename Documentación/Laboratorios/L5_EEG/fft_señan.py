import numpy as np
import matplotlib.pyplot as plt


# Listas para almacenar los datos de cada canal
canales = [[] for _ in range(16)]

# Variable para controlar si hemos pasado las líneas de metadatos
pasadas_lineas_metadatos = False

with open("OpenBCI-RAW-2024-04-26_12-22-01.txt", "r") as archivo:
    # Iterar sobre cada línea del archivo
    for linea in archivo:
        # Si todavía no hemos pasado las líneas de metadatos, verificamos si la línea contiene información de los canales
        if not pasadas_lineas_metadatos:
            # Verificar si la línea contiene información de los canales
            if "Sample Index" in linea:
                pasadas_lineas_metadatos = True
            continue  # Pasar a la siguiente línea si aún estamos en las líneas de metadatos
        # Si hemos pasado las líneas de metadatos, procesamos la línea como datos de los canales
        # Dividir la línea en columnas utilizando la coma como separador
        columnas = linea.strip().split(", ")
        # Verificar si la línea tiene al menos 17 columnas (16 canales más una columna adicional)
        if len(columnas) >= 17:
            # Almacenar los datos de cada canal en la lista correspondiente
            for i in range(16):
                canales[i].append(float(columnas[i+1]))

# Convertir de uV a mV (Etapa de Conversión)
canales = np.array(canales) * 1000

# Definir los tramos de tiempo
tramos_tiempo = [(0, 30), (30, 80), (80, 110), (110, 180)]
titulos = ["Ojos cerrados (primer tramo)", "Ojos abiertos-cerrados (segundo tramo)", "Ojos cerrados (tercer tramo)", "Ejercicios matemáticos (cuarto tramo)"]

for i, (inicio, fin) in enumerate(tramos_tiempo, start=1):
    plt.figure(figsize=(10, 6))
    for canal in canales:
        # Seleccionar los datos del canal dentro del tramo de tiempo actual
        datos_tramo = canal[inicio*125:fin*125]  # Multiplicar por 125 para convertir segundos a muestras (a 125 Hz)
        # Calcular el PSD utilizando la FFT
        psd, freq = plt.psd(datos_tramo, NFFT=512, Fs=160, label='Canal')
        # Agregar un valor pequeño a los valores iguales a cero para evitar el logaritmo de cero
        psd = np.where(psd > 0, psd, 1e-16)
        # Graficar el PSD en dB/Hz
        plt.plot(freq, 10 * np.log10(psd), label='Canal')
    plt.title(titulos[i-1])
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('PSD (dB/Hz)')
    plt.legend(loc='upper right')
    plt.savefig(f'eeg_multichannel_CASCO_psd{i}.png')
    plt.show()





