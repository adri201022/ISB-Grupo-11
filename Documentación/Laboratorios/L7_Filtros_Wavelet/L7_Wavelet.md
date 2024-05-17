# Informe de Laboratorio 7: Filtrado Wavelet de señales EMG, ECG y EEG 

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Filtro de señal ECG](#id3)
4. [Filtro de señal EMG](#id4)
5. [Filtro de señal EEG](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>


## **Objetivos** <a name="id2"></a>
<ul>
  <li>Desarrollar filtros wavelet para el procesamiento y mejora de la calidad de las señales electrocardiográficas (ECG), electromiográficas (EMG) y electroencefalográficas (EEG).</li>
  <li>Analizar la efectividad de los filtros wavelet en la reducción de ruido y la extracción de características clave en las señales ECG, EMG y EEG.</li>
</ul>

## **Filtro de señal ECG** <a name="id3"></a>
### Metodología

### Resultados

## **Filtro de señal EMG** <a name="id4"></a>
### Metodología

### Resultados

## **Filtro de señal EEG** <a name="id5"></a>
### Metodología
#### Datos y técnicas de adquisición
Para el experimento se tomaron 3 señales correspondientes a las ondas cerebrales durante 3 estímuloss distintos: Una de referencia o reposo, una abriendo y cerrando los ojos y una respondiendo preguntas. Para esto las señales EEG registradas se muestrearon a una frecuencia de 1000 Hz, utilizando al bitalino y también utilizando el sistema de electrodos 10 20; esto aplicando un método monopolar con dos electrodos posicionados en una región cerebral específica más un electrodo de referencia. Para la conversión de las señales a milivoltios, se utilizó una ecuación que considera un voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits, permitiendo una cuantificación precisa de la señal EEG. 

#### Eliminación del ruido
Una vez adquiridas las señales toca mejorar la calidad de estas, para ello vamos a eliminar los ruidos no deseados, implementando filtros digitales. Se aplicará directamente el filtro wavelet para seguir un poco la idea de trabajo del artículo "Effectiveness of Wavelet Denoising on Electroencephalogram Signals" [R1] esto porque según se mencionó en clase podemos preprocesar la señal aplicando los filtros FIR e IIR antes de aplicar el filtro wavelet con el fin de mejorar la calidad del análisis wavelet.
Dentro del artículo se determina un umbral para las señales EEG sin procesar que se aplica a los coeficientes wavelet (dmey, db8, db6, db4) el dmey es (discrete meyer) y es para un tipo de wavelet en este caso discreta [R1] Para nuestro caso, solo plotearemos a 8 decibeles esto para no hacer demasiado extenso el análisis en este inciso.
### Resultados

## **Discusión** <a name="id6"></a>
### Señal ECG

### Señal EMG

### Señal EEG

## **Archivos de códigos** <a name="id7"></a>


## **Referencias** <a name="id8"></a>

