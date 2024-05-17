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
La transformada wavelet se ha convertido en una herramienta esencial para el análisis de señales, destacándose por su capacidad para trabajar tanto en el dominio del tiempo como en el de la frecuencia. Esto es especialmente útil para el análisis de señales no estacionarias, como las obtenidas en electrocardiografía (ECG), electromiografía (EMG) y electroencefalografía (EEG). La transformada wavelet es un método matemático que descompone una señal en componentes de diversas frecuencias y duraciones. 

<div align="center";style="text-align:center;">
  <img width="400" height="100" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/0576b869-7ba0-4630-916b-ce740c519dec">
  <br>
  <span style="font-style: italic;">Figura 1: Esquema de la Transformada Wavelet .</span>
</div>

Esto se realiza utilizando una función denominada wavelet madre, que es una pequeña onda de duración limitada con características matemáticas específicas, como tener una media de cero y estar normalizada. La wavelet madre se escala (mediante el factor de escala (a) y se desplaza (mediante el factor de traslación (b) para crear una familia de wavelets utilizadas en el análisis de la señal.

<div align="center";style="text-align:center;">
  <img width="200" height="50" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/fb8f2e6f-5706-4de9-9184-1dc6999edb80">
  <br>
  <span style="font-style: italic;">Figura 2: Ecuación que define la función wavelet madre .</span>
</div>

### Transformada Wavelet Continua
La CWT proporciona una representación redundante y detallada de la señal, aunque a costa de un mayor requerimiento de almacenamiento y computación. Matemáticamente, la CWT de una señal f(t) se define como la convolución de f(t) con la wavelet madre escalada y trasladada, generando un espectro tiempo-frecuencia continuo donde cada par de parámetros (a,b) ofrece información sobre la presencia de la wavelet en esa escala y posición.

<div align="center";style="text-align:center;">
  <img width="200" height="50" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/d59141ae-4333-49bd-8e2b-9c98cf42272d">
  <br>
  <span style="font-style: italic;">Figura 3: Ecuación que define la transformada wavelet continua .</span>
</div>

### Transformada Wavelet Discreta
La DWT es más eficiente computacionalmente y se usa ampliamente en aplicaciones prácticas como la compresión de imágenes. Utiliza un conjunto discreto de escalas y posiciones, típicamente en potencias de dos (escalas diádicas). La DWT descompone la señal en diferentes niveles de resolución mediante un proceso iterativo de filtrado y submuestreo, utilizando filtros de paso alto y paso bajo derivados de la wavelet madre.

<div align="center";style="text-align:center;">
  <img width="200" height="50" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/ff9295d5-ddc2-4b68-81bb-dc3c5bf0adb8">
  <br>
  <span style="font-style: italic;">Figura 4: Ecuación que define la transformada wavelet discreta .</span>
</div>

### Filtros Wavelet
Los filtros wavelet son cruciales para implementar la transformada wavelet discreta (DWT) y desempeñan un papel esencial en la descomposición y reconstrucción de señales en el dominio wavelet.

#### Filtros de un Nivel

<div align="center";style="text-align:center;">
  <img width="400" height="200" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/fd71421b-b92e-4775-87c0-140a4a5799e3">
  <br>
  <span style="font-style: italic;">Figura 5: Diagrama de descomposición de filtros de un nivel .</span>
</div>

#### Descomposición Multinivel
Para realizar una descomposición multinivel, el proceso de filtrado se itera, aplicando los mismos filtros a las señales resultantes de cada etapa sucesiva. Este proceso continúa hasta alcanzar el nivel de precisión deseado. La descomposición multinivel, también conocida como árbol de descomposición wavelet, divide la señal original en diferentes bandas de frecuencia a múltiples niveles.

<div align="center";style="text-align:center;">
  <img width="400" height="200" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/802a55b4-c968-4fa5-bd01-56cdf91d8912">
  <br>
  <span style="font-style: italic;">Figura 6: Árbol de descomposición wavelet .</span>
</div>

#### Determinación del Número de Niveles
Teóricamente, este proceso podría repetirse indefinidamente. Sin embargo, en la práctica, se detiene cuando un intervalo o nivel contiene solo una muestra (o píxel en el análisis de imágenes bidimensionales). Se recomienda seleccionar el número de niveles de descomposición en función de la naturaleza de la señal estudiada o utilizando métodos de optimización, como la entropía.

#### Reconstrucción Wavelet
La reconstrucción wavelet, o transformada inversa de wavelet, permite recuperar la señal original a partir de los coeficientes de descomposición. Este proceso inverso implica interpolar los coeficientes de aproximación y detalle, convolucionar con los filtros inversos de paso bajo y alto, y sumar las componentes resultantes para obtener la señal en el siguiente nivel superior.

### Tipos de Filtros Wavelet
Los distintos tipos de filtros wavelet presentan características específicas que los hacen adecuados para diferentes aplicaciones. El Haar wavelet es simple y fácil de implementar, aunque no muy suave. Las wavelets Daubechies están diseñadas para maximizar la suavidad para una longitud dada, ofreciendo mejor localización en frecuencia y mayor suavidad que el Haar. Los Symlets, similares a las Daubechies pero con mejor simetría, combinan simetría y suavidad, mejorando las propiedades de reconstrucción. Los Coiflets, diseñados con momentos de la primera derivada nulos, proporcionan una mejor representación de señales polinomiales. Finalmente, las Meyer wavelets, aunque no son compactamente soportadas, son infinitamente diferenciables y ofrecen una buena localización en frecuencia.

<div align="center";style="text-align:center;">
  <img width="450" height="400" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/75ca92d4-94fb-4111-92d9-4d7da4cb7258">
  <br>
  <span style="font-style: italic;">Figura 8: Distintas familias wavelet .</span>
</div>

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

|                   | Señal cruda | Señal filtrada con wavelet |  
|-------------------|--------------------------|----------------------|
| Referencia    | ![Waveletseñalcrudareferencia](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/75e681b4-1b2a-4a44-bd2e-c634170bc2cf) | ![Waveletseñalfiltradareferencia](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/3ab64f9d-2b91-4ae5-a6bc-664045c74363) | 
| Ojos abiertos y cerrados    | ![Waveletseñalcrudaojosabiertoscerrados](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/c0f5dd3d-20c1-4970-8970-ed1612001f87)| ![Waveletseñalfiltradaojosabiertoscerrados](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/601f01b2-99fb-413a-9ded-4b3d682fa847)|
| Preguntas    | ![Waveletseñalpreguntas](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/78894c96-beee-4e85-8394-3ac4f2aa496b) | ![Waveletseñalfiltradapreguntas](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/5bab9619-23da-4a98-b97c-d965367e11e8) | 

## **Discusión** <a name="id6"></a>
### Señal ECG

### Señal EMG

### Señal EEG

## **Archivos de códigos** <a name="id7"></a>


## **Referencias** <a name="id8"></a>

