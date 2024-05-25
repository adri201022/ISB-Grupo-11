# Informe de Laboratorio 8: Procesamiento de una señal EMG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Filtro de señal EMG](#id3)
4. [Segmentación de señal EMG](#id4)
5. [Extracción de características de señal EMG](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>
### Electromiografía
La electromiografía (EMG) se refiere a la señal eléctrica generada colectivamente por los músculos, la cual es controlada por el sistema nervioso y se produce durante la contracción muscular. Esta señal refleja las propiedades anatómicas y fisiológicas de los músculos. Específicamente, una señal EMG captura la actividad eléctrica de las unidades motoras de un músculo, que pueden ser registradas de dos maneras: EMG de superficie y EMG intramuscular. La EMG de superficie (sEMG) y la EMG intramuscular (iEMG) se obtienen mediante electrodos no invasivos y electrodos invasivos, respectivamente. Actualmente, se prefiere el uso de señales detectadas en la superficie para obtener información sobre el tiempo o la intensidad de la activación muscular superficial [1]. La señal EMG es una señal aleatoria no estacionaria que usualmente requiere la reducción de ruido y la amplificación de la señal para su adecuado análisis [2].

A continuación se presentan las principales etapas implicadas en la adquisición de la señal, preprocesamiento y extracción de características de señales EMG registradas a partir de una fibra muscular [3]:

<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/7191d6fc-8021-49a1-8340-25c3bfa453b3">
</p>
<p align="center"><b>Figura 1: Principales etapas implicadas en la adquisición de la señal, preprocesamiento y extracción de características de señales EMG [3].</b> </p>

### Procesamiento de señal EMG
El procesamiento de señales EMG es esencial para interpretar adecuadamente la actividad muscular registrada. Este proceso involucra varias etapas clave: adquisición, filtrado, rectificación, normalización, segmentación y extracción de características. A continuación, se describen cada una de estas etapas [4].

1. **Adquisión**: A pesar de la naturaleza no estacionaria de las señales sEMG, se pueden detectar con electrodos de superficie. Estos electrodos se clasifican según su tipo y densidad. Es crucial que el sensor sEMG cumpla con el teorema de Nyquist-Shannon, con una frecuencia de muestreo mayor a 1000 Hz para garantizar la precisión en la captura de señales [4].
2. **Filtrado**: Las señales EMG captadas suelen estar afectadas por ruido y artefactos originados por diversas fuentes, como el movimiento de los         electrodos, la actividad eléctrica de otros músculos (crosstalk) y la interferencia ambiental. Para mitigar estas interferencias y        mejorar la calidad de la señal, se recurre al filtrado. En algunos estudios, se emplearon tanto un filtro pasa banda como un filtro notch para extraer las señales sEMG, mientras que otros recomendaron el uso de un filtro Butterworth con parámetros específicos [4].
4. **Rectificación**

5. **Normalización**

6. **Segmentación**

7. **Extracción de características**

## **Objetivos** <a name="id2"></a>
<ul>
  <li>Detallar cada etapa involucrada en la captura y análisis de señales electromiográficas para comprender su funcionamiento y aplicación práctica.</li>
  <li>Analizar críticamente las técnicas empleadas en el preprocesamiento de señales EMG, evaluando su capacidad para reducir el ruido, mejorar la calidad de la señal y facilitar la extracción de información relevante.</li>
</ul>

## **Filtro de señal EMG** <a name="id3"></a>
### Metodología

### Resultados

## **Segmentación de señal EMG** <a name="id4"></a>
### Metodología

### Resultados

## **Extracción de características de señal EMG** <a name="id5"></a>
### Metodología

### Resultados

## **Discusión** <a name="id6"></a>

## **Archivos de códigos** <a name="id7"></a>

## **Referencias** <a name="id8"></a>
[1]R. Chowdhury, M. Reaz, M. Ali, A. Bakar, K. Chellappan, y T. Chang, «Surface Electromyography Signal Processing and Classification Techniques», Sensors, vol. 13, n.o 9, pp. 12431-12466, sep. 2013, doi: 10.3390/s130912431.

[2]Y. Wu, X. Hu, Z. Wang, J. Wen, J. Kan, y W. Li, «Exploration of Feature Extraction Methods and Dimension for sEMG Signal Classification», Applied Sciences, vol. 9, n.o 24, p. 5343, dic. 2019, doi: 10.3390/app9245343.

[3]J. J. G. Murillo, A. Ilzarbe, y S. Osuna, «Procesado de señales EMG en Trastornos Neuromusculares», 2013, doi: 10.13140/2.1.4902.9445.

[4]A. M. Moslhi, H. H. Aly, y M. ElMessiery, «The Impact of Feature Extraction on Classification Accuracy Examined by Employing a Signal Transformer to Classify Hand Gestures Using Surface Electromyography Signals», Sensors, vol. 24, n.o 4, p. 1259, feb. 2024, doi: 10.3390/s24041259.
