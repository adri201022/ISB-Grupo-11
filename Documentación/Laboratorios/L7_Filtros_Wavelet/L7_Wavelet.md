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
### Transformada Wavelet
La transformada wavelet se ha convertido en una herramienta esencial para el análisis de señales, destacándose por su capacidad para trabajar tanto en el dominio del tiempo como en el de la frecuencia. Esto es especialmente útil para el análisis de señales no estacionarias, como las obtenidas en electrocardiografía (ECG), electromiografía (EMG) y electroencefalografía (EEG). La transformada wavelet es un método matemático que descompone una señal en componentes de diversas frecuencias y duraciones. Esto se realiza utilizando una función denominada wavelet madre, que es una pequeña onda de duración limitada con características matemáticas específicas, como tener una media de cero y estar normalizada. La wavelet madre se escala (mediante el factor de escala (a)) y se desplaza (mediante el factor de traslación (b) para crear una familia de wavelets utilizadas en el análisis de la señal.

### Transformada Wavelet Continua
La CWT proporciona una representación redundante y detallada de la señal, aunque a costa de un mayor requerimiento de almacenamiento y computación. Matemáticamente, la CWT de una señal f(t) se define como la convolución de f(t) con la wavelet madre escalada y trasladada, generando un espectro tiempo-frecuencia continuo donde cada par de parámetros (a,b) ofrece información sobre la presencia de la wavelet en esa escala y posición.

### Transformada Wavelet Discreta
La DWT es más eficiente computacionalmente y se usa ampliamente en aplicaciones prácticas como la compresión de imágenes. Utiliza un conjunto discreto de escalas y posiciones, típicamente en potencias de dos (escalas diádicas). La DWT descompone la señal en diferentes niveles de resolución mediante un proceso iterativo de filtrado y submuestreo, utilizando filtros de paso alto y paso bajo derivados de la wavelet madre.

### Filtros Wavelet
Los filtros wavelet son cruciales para implementar la transformada wavelet discreta (DWT) y desempeñan un papel esencial en la descomposición y reconstrucción de señales en el dominio wavelet. Estos filtros incluyen filtros de paso bajo y paso alto, que se utilizan para separar una señal en sus componentes de baja y alta frecuencia, respectivamente.

#### Filtros de un Nivel

**Filtro de Paso Bajo (Low-Pass Filter):**
- Retiene las componentes de baja frecuencia de la señal.
- Produce las aproximaciones (coeficientes de baja frecuencia).

**Filtro de Paso Alto (High-Pass Filter):**
- Retiene las componentes de alta frecuencia de la señal.
- Produce los detalles (coeficientes de alta frecuencia).

#### Descomposición Multinivel
Para realizar una descomposición multinivel, el proceso de filtrado se itera, aplicando los mismos filtros a las señales resultantes de cada etapa sucesiva. Este proceso continúa hasta alcanzar el nivel de precisión deseado. La descomposición multinivel, también conocida como árbol de descomposición wavelet, divide la señal original en diferentes bandas de frecuencia a múltiples niveles.

#### Determinación del Número de Niveles
Teóricamente, este proceso podría repetirse indefinidamente. Sin embargo, en la práctica, se detiene cuando un intervalo o nivel contiene solo una muestra (o píxel en el análisis de imágenes bidimensionales). Se recomienda seleccionar el número de niveles de descomposición en función de la naturaleza de la señal estudiada o utilizando métodos de optimización, como la entropía.

#### Reconstrucción Wavelet
La reconstrucción wavelet, o transformada inversa de wavelet, permite recuperar la señal original a partir de los coeficientes de descomposición. Este proceso inverso implica interpolar los coeficientes de aproximación y detalle, convolucionar con los filtros inversos de paso bajo y alto, y sumar las componentes resultantes para obtener la señal en el siguiente nivel superior.

### Tipos de Filtros Wavelet
Los distintos tipos de filtros wavelet presentan características específicas que los hacen adecuados para diferentes aplicaciones. El Haar wavelet es simple y fácil de implementar, aunque no muy suave. Las wavelets Daubechies están diseñadas para maximizar la suavidad para una longitud dada, ofreciendo mejor localización en frecuencia y mayor suavidad que el Haar. Los Symlets, similares a las Daubechies pero con mejor simetría, combinan simetría y suavidad, mejorando las propiedades de reconstrucción. Los Coiflets, diseñados con momentos de la primera derivada nulos, proporcionan una mejor representación de señales polinomiales. Finalmente, las Meyer wavelets, aunque no son compactamente soportadas, son infinitamente diferenciables y ofrecen una buena localización en frecuencia.

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

