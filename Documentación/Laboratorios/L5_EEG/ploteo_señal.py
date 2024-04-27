import numpy as np
import matplotlib.pyplot as plt

# Listas para almacenar los datos de cada canal
canales = [[] for _ in range(16)]

with open("OpenBCI-RAW-2024-04-26_12-22-01.txt", "r") as archivo:
    # Saltar las primeras líneas que contienen comentarios y metadatos
    for _ in range(6):
        archivo.readline()
    # Iterar sobre cada línea del archivo
    for linea in archivo:
        # Dividir la línea en columnas utilizando la coma como separador
        columnas = linea.strip().split(", ")
        # Almacenar los datos de cada canal en la lista correspondiente
        for i in range(16):
            canales[i].append(float(columnas[i+1]))

# Convertir a mV
canales = np.array(canales) * 1000

# Crear un array de tiempo en segundos
tiempo = np.arange(len(canales[0])) / 160

# Definir los límites de tiempo para cada gráfico y sus títulos
limites_tiempo = [(0, 30, 'Ojos Cerrados'),
                  (30, 80, 'Ojos Abiertos-Cerrados'),
                  (80, 110, 'Ojos Cerrados'),
                  (110, 180, 'Ejercicios Matemáticos')]

# Ploteo manual de cada segmento de tiempo uno por uno
# Ojos Cerrados
plt.figure(figsize=(14, 10))
plt.plot(tiempo[:30*160], canales[0][:30*160], label='Canal 1')
plt.plot(tiempo[:30*160], canales[1][:30*160], label='Canal 2')
plt.plot(tiempo[:30*160], canales[2][:30*160], label='Canal 3')
plt.plot(tiempo[:30*160], canales[3][:30*160], label='Canal 4')
plt.plot(tiempo[:30*160], canales[4][:30*160], label='Canal 5')
plt.plot(tiempo[:30*160], canales[5][:30*160], label='Canal 6')
plt.plot(tiempo[:30*160], canales[6][:30*160], label='Canal 7')
plt.plot(tiempo[:30*160], canales[7][:30*160], label='Canal 8')
plt.title('Ojos Cerrados')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend(loc='upper right')
plt.show()
plt.close()

# Ojos Abiertos-Cerrados
plt.figure(figsize=(14, 10))
plt.plot(tiempo[30*160:80*160], canales[0][30*160:80*160], label='Canal 1')
plt.plot(tiempo[30*160:80*160], canales[1][30*160:80*160], label='Canal 2')
plt.plot(tiempo[30*160:80*160], canales[2][30*160:80*160], label='Canal 3')
plt.plot(tiempo[30*160:80*160], canales[3][30*160:80*160], label='Canal 4')
plt.plot(tiempo[30*160:80*160], canales[4][30*160:80*160], label='Canal 5')
plt.plot(tiempo[30*160:80*160], canales[5][30*160:80*160], label='Canal 6')
plt.plot(tiempo[30*160:80*160], canales[6][30*160:80*160], label='Canal 7')
plt.plot(tiempo[30*160:80*160], canales[7][30*160:80*160], label='Canal 8')
plt.title('Ojos Abiertos-Cerrados')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend(loc='upper right')
plt.show()
plt.close()

# Ojos Cerrados
plt.figure(figsize=(14, 10))
plt.plot(tiempo[80*160:110*160], canales[0][80*160:110*160], label='Canal 1')
plt.plot(tiempo[80*160:110*160], canales[1][80*160:110*160], label='Canal 2')
plt.plot(tiempo[80*160:110*160], canales[2][80*160:110*160], label='Canal 3')
plt.plot(tiempo[80*160:110*160], canales[3][80*160:110*160], label='Canal 4')
plt.plot(tiempo[80*160:110*160], canales[4][80*160:110*160], label='Canal 5')
plt.plot(tiempo[80*160:110*160], canales[5][80*160:110*160], label='Canal 6')
plt.plot(tiempo[80*160:110*160], canales[6][80*160:110*160], label='Canal 7')
plt.plot(tiempo[80*160:110*160], canales[7][80*160:110*160], label='Canal 8')
plt.title('Ojos Cerrados')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend(loc='upper right')
plt.show()
plt.close()

# Ejercicios Matemáticos
plt.figure(figsize=(14, 10))
plt.plot(tiempo[110*160:180*160], canales[0][110*160:180*160], label='Canal 1')
plt.plot(tiempo[110*160:180*160], canales[1][110*160:180*160], label='Canal 2')
plt.plot(tiempo[110*160:180*160], canales[2][110*160:180*160], label='Canal 3')
plt.plot(tiempo[110*160:180*160], canales[3][110*160:180*160], label='Canal 4')
plt.plot(tiempo[110*160:180*160], canales[4][110*160:180*160], label='Canal 5')
plt.plot(tiempo[110*160:180*160], canales[5][110*160:180*160], label='Canal 6')
plt.plot(tiempo[110*160:180*160], canales[6][110*160:180*160], label='Canal 7')
plt.plot(tiempo[110*160:180*160], canales[7][110*160:180*160], label='Canal 8')
plt.title('Ejercicios Matemáticos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend(loc='upper right')
plt.show()
plt.close()




