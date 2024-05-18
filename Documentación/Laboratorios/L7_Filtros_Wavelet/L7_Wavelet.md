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
La transformada wavelet se ha convertido en una herramienta esencial para el análisis de señales, destacándose por su capacidad para trabajar tanto en el dominio del tiempo como en el de la frecuencia. Esto es especialmente útil para el análisis de señales no estacionarias, como las obtenidas en electrocardiografía (ECG), electromiografía (EMG) y electroencefalografía (EEG). La transformada wavelet es un método matemático que descompone una señal en componentes de diversas frecuencias y duraciones [1]. 

<div align="center";style="text-align:center;">
  <img width="400" height="100" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/0576b869-7ba0-4630-916b-ce740c519dec">
  <br>
  <span style="font-style: italic;">Figura 1: Esquema de la Transformada Wavelet [2].</span>
</div>

Esto se realiza utilizando una función denominada wavelet madre, que es una pequeña onda de duración limitada con características matemáticas específicas, como tener una media de cero y estar normalizada. La wavelet madre se escala (mediante el factor de escala (a) y se desplaza (mediante el factor de traslación (b) para crear una familia de wavelets utilizadas en el análisis de la señal [1].

<div align="center";style="text-align:center;">
  <img width="200" height="50" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/fb8f2e6f-5706-4de9-9184-1dc6999edb80">
  <br>
  <span style="font-style: italic;">Figura 2: Ecuación que define la función wavelet madre [1].</span>
</div>

### Transformada Wavelet Continua
La CWT proporciona una representación redundante y detallada de la señal, aunque a costa de un mayor requerimiento de almacenamiento y computación. Matemáticamente, la CWT de una señal f(t) se define como la convolución de f(t) con la wavelet madre escalada y trasladada, generando un espectro tiempo-frecuencia continuo donde cada par de parámetros (a,b) ofrece información sobre la presencia de la wavelet en esa escala y posición [1].

<div align="center";style="text-align:center;">
  <img width="200" height="50" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/d59141ae-4333-49bd-8e2b-9c98cf42272d">
  <br>
  <span style="font-style: italic;">Figura 3: Ecuación que define la transformada wavelet continua [3].</span>
</div>

### Transformada Wavelet Discreta
La DWT es más eficiente computacionalmente y se usa ampliamente en aplicaciones prácticas como la compresión de imágenes. Utiliza un conjunto discreto de escalas y posiciones, típicamente en potencias de dos (escalas diádicas). La DWT descompone la señal en diferentes niveles de resolución mediante un proceso iterativo de filtrado y submuestreo, utilizando filtros de paso alto y paso bajo derivados de la wavelet madre [1].

<div align="center";style="text-align:center;">
  <img width="200" height="50" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/ff9295d5-ddc2-4b68-81bb-dc3c5bf0adb8">
  <br>
  <span style="font-style: italic;">Figura 4: Ecuación que define la transformada wavelet discreta [3].</span>
</div>

### Filtros Wavelet
Los filtros wavelet son cruciales para implementar la transformada wavelet discreta (DWT) y desempeñan un papel esencial en la descomposición y reconstrucción de señales en el dominio wavelet.

#### Filtros de un Nivel

<div align="center";style="text-align:center;">
  <img width="400" height="200" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/fd71421b-b92e-4775-87c0-140a4a5799e3">
  <br>
  <span style="font-style: italic;">Figura 5: Diagrama de descomposición de filtros de un nivel [2].</span>
</div>

#### Descomposición Multinivel
Para realizar una descomposición multinivel, el proceso de filtrado se itera, aplicando los mismos filtros a las señales resultantes de cada etapa sucesiva. Este proceso continúa hasta alcanzar el nivel de precisión deseado. La descomposición multinivel, también conocida como árbol de descomposición wavelet, divide la señal original en diferentes bandas de frecuencia a múltiples niveles [4].

<div align="center";style="text-align:center;">
  <img width="400" height="200" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/802a55b4-c968-4fa5-bd01-56cdf91d8912">
  <br>
  <span style="font-style: italic;">Figura 6: Árbol de descomposición wavelet [2].</span>
</div>

#### Determinación del Número de Niveles
Teóricamente, este proceso podría repetirse indefinidamente. Sin embargo, en la práctica, se detiene cuando un intervalo o nivel contiene solo una muestra (o píxel en el análisis de imágenes bidimensionales). Se recomienda seleccionar el número de niveles de descomposición en función de la naturaleza de la señal estudiada o utilizando métodos de optimización, como la entropía [4].

#### Reconstrucción Wavelet
La reconstrucción wavelet, o transformada inversa de wavelet, permite recuperar la señal original a partir de los coeficientes de descomposición. Este proceso inverso implica interpolar los coeficientes de aproximación y detalle, convolucionar con los filtros inversos de paso bajo y alto, y sumar las componentes resultantes para obtener la señal en el siguiente nivel superior [4].

### Tipos de Filtros Wavelet
Los distintos tipos de filtros wavelet presentan características específicas que los hacen adecuados para diferentes aplicaciones. El Haar wavelet es simple y fácil de implementar, aunque no muy suave. Las wavelets Daubechies están diseñadas para maximizar la suavidad para una longitud dada, ofreciendo mejor localización en frecuencia y mayor suavidad que el Haar. Los Symlets, similares a las Daubechies pero con mejor simetría, combinan simetría y suavidad, mejorando las propiedades de reconstrucción. Los Coiflets, diseñados con momentos de la primera derivada nulos, proporcionan una mejor representación de señales polinomiales. Finalmente, las Meyer wavelets, aunque no son compactamente soportadas, son infinitamente diferenciables y ofrecen una buena localización en frecuencia [1].

<div align="center";style="text-align:center;">
  <img width="450" height="400" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/75ca92d4-94fb-4111-92d9-4d7da4cb7258">
  <br>
  <span style="font-style: italic;">Figura 8: Distintas familias wavelet [5].</span>
</div>

## **Objetivos** <a name="id2"></a>
<ul>
  <li>Desarrollar filtros wavelet para el procesamiento y mejora de la calidad de las señales electrocardiográficas (ECG), electromiográficas (EMG) y electroencefalográficas (EEG).</li>
  <li>Analizar la efectividad de los filtros wavelet en la reducción de ruido y la extracción de características clave en las señales ECG, EMG y EEG.</li>
</ul>

## **Filtro de señal ECG** <a name="id3"></a>
### Metodología
Las señales de ECG se pasaron a mV, para eso utilizamos la fórmula que nos proporciona el Bitalino, el cual relaciona el ADC que es la señal, el vcc que es 300 mV, Gecg que es 1000, y la resolución de 1024. 

Posteriormente a eso realizamos nuestro filtrado con la transformada de Wavelet. Para esta parte hemos utilizado un journal el cual nos indica que para el caso de ECG utilizaron un nivel de 5 y un Daubechies wavelet (db4), y para el caso del umbral el mismo journal nos proporciona la fórmula para calcular este umbral.[6]

<p align="center"> <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/adf62692-08b4-4475-a381-625ef277b10a">
<p align="center"> <small>Figura extraida de [6].</small> </p>


### Resultados

|                   | Señal cruda | Señal filtrada con wavelet |  
|-------------------|--------------------------|----------------------|
| Reposo    | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/61a444d5-e960-427b-9a69-093bf6bafe0e" width="350" height="200"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/ea1409ee-a1d5-468a-87cf-776910d18521" width="350" height="200"> | 
| Respiraciones rápidas  | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/708368f7-47bf-46ed-ab72-27a2d9ea9ac9" width="350" height="200"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/faf7df34-b2f0-4097-982c-f79620ced73d" width="350" height="200"> |
| Actividad    | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/63a9e5e4-9ff5-45e2-b387-1a518741e32a" width="350" height="200"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/dd379093-293c-41b6-ab2b-c3c96ee4dc38" width="350" height="200"> |

## **Filtro de señal EMG** <a name="id4"></a>
### Metodología

### Resultados
|                   | Señal cruda | Señal filtrada con wavelet |  
|-------------------|--------------------------|----------------------|
| Reposo    |![Reposo_original](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/374da051-bfe5-4c33-9e16-48d6135762e9)|![Reposo_filtrada](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/8e9ae4ae-acc5-41bb-b3de-903cf46b1b7b)| 
| Sin oposición    |![SinOposicion_original](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/6361b873-86f2-4439-852f-19778fc0b784)|![SinOposicion_filtrada](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/63f6e494-1d79-4943-af7d-886dc1185e12)|
| Con oposición    |![ConOposicion_original](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/07141158-f89a-4a74-bbb9-537867d94da7)|![ConOposicion_filtrada](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/274aa6ce-dc24-4d1a-a683-26b01902be16)|

## **Filtro de señal EEG** <a name="id5"></a>
### Metodología
#### Datos y técnicas de adquisición
Para el experimento se tomaron 3 señales correspondientes a las ondas cerebrales durante 3 estímuloss distintos: Una de referencia o reposo, una abriendo y cerrando los ojos y una respondiendo preguntas. Para esto las señales EEG registradas se muestrearon a una frecuencia de 1000 Hz, utilizando al bitalino y también utilizando el sistema de electrodos 10 20; esto aplicando un método monopolar con dos electrodos posicionados en una región cerebral específica más un electrodo de referencia. Para la conversión de las señales a milivoltios, se utilizó una ecuación que considera un voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits, permitiendo una cuantificación precisa de la señal EEG. 

#### Eliminación del ruido
Una vez adquiridas las señales toca mejorar la calidad de estas, para ello vamos a eliminar los ruidos no deseados, implementando filtros digitales. Se aplicará directamente el filtro wavelet para seguir un poco la idea de trabajo del artículo "Effectiveness of Wavelet Denoising on Electroencephalogram Signals" [R1] esto porque según se mencionó en clase podemos preprocesar la señal aplicando los filtros FIR e IIR antes de aplicar el filtro wavelet con el fin de mejorar la calidad del análisis wavelet.
Dentro del artículo se determina un umbral para las señales EEG sin procesar que se aplica a los coeficientes wavelet (dmey, db8, db6, db4) el dmey es (discrete meyer) y es para un tipo de wavelet en este caso discreta [R1] Para nuestro caso, solo plotearemos a 8 decibeles esto para no hacer demasiado extenso el análisis en este inciso.

### Resultados

|                   | Señal cruda | Señal filtrada con wavelet |  
|-------------------|----------------------------|------------------------|
| Referencia    | ![Waveletseñalcrudareferencia](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/75e681b4-1b2a-4a44-bd2e-c634170bc2cf) | ![Waveletseñalfiltradareferencia](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/3ab64f9d-2b91-4ae5-a6bc-664045c74363) | 
| Ojos abiertos y cerrados    | ![Waveletseñalcrudaojosabiertoscerrados](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/c0f5dd3d-20c1-4970-8970-ed1612001f87)| ![Waveletseñalfiltradaojosabiertoscerrados](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/601f01b2-99fb-413a-9ded-4b3d682fa847)|
| Preguntas    | ![Waveletseñalpreguntas](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/78894c96-beee-4e85-8394-3ac4f2aa496b) | ![Waveletseñalfiltradapreguntas](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/5bab9619-23da-4a98-b97c-d965367e11e8) | 

## **Discusión** <a name="id6"></a>
### Señal ECG
Para el caso de la señal de ECG en reposo, se puede observar que el filtrado de la señal con la transformada de wavelet fue relativamente correcta ya que no se observa ruido, sin embargo se puede observar que la amplitud de la señal ha disminiudo considerablemente y que en ciertos sectores ha perdido su forma como en la parte de curvas, ya no es asi sino que es es recto en la señal filtrada.

Para el caso de la señal de ECG en respiraciones rápidas, se puede observar tambien que el filtrado de la señal fue relativamente correcta, pero también tiene el mimsmo problema que en la señal de reposo, el cual es que la amplitud de la señal disminuyo y en ciertos punto perdio su forma.

En el caso de la señal de ECG  en actividad , se logra ver que hubo un filtrado excesivo, ya que su amplitud ha disminuido considerablemente y al forma de la onda si bien en ciertas partes se parece a la señal sin filtrar hay otras partes que no.

La disminución de la señal y la perdida de la forma en ciertos sectores de la seañ filtrada, se pueden deber a los parametros escogidos, ya que los parametros del estudios fueron escogidos en base a la señal de ECG que ellos teniam y en nuestro caso como nuestra señal no es la misma puede que es estos parametros hagan que haya un filtrafo excesivo.
### Señal EMG

### Señal EEG
Para el caso de la señal EEG en reposo, se puede observar que no se ha obtenido casi ninguna diferencia entre la señal original y la señal filtrada con la transformada wavelet db8. Esto sugiere que el filtrado no fue tan efectivo como se esperaba, probablemente debido a la falta de pretratamiento de la señal. La ausencia de una etapa previa de filtrado FIR o IIR podría haber disminuido la eficacia del filtro wavelet en la eliminación de ruido [R1].

En la señal EEG obtenida durante la actividad de abrir y cerrar los ojos, la situación es similar. El filtrado con wavelet db8 no mostró una mejora significativa en la calidad de la señal, con mínimas diferencias observables entre la señal cruda y la señal filtrada. Esto refuerza la idea de que un pretratamiento adecuado es crucial para maximizar la efectividad del filtrado wavelet. La implementación de filtros digitales FIR o IIR antes de aplicar el wavelet podría haber mejorado considerablemente los resultados tan como lo menciona el artículo "Effectiveness of Wavelet Denoising on Electroencephalogram Signals" [R1].

En el caso de la señal EEG durante la actividad de responder preguntas, el filtrado nuevamente no logró una mejora considerable. La señal filtrada con wavelet no difiere significativamente de la señal original, indicando una eliminación de ruido ineficaz. Esto puede deberse a que los parámetros del filtro wavelet no fueron optimizados para estas condiciones específicas (fs=1000 Hz), y la falta de un pretratamiento adecuado de la señal influyó negativamente en el desempeño del filtrado wavelet [R1].

La reducción en la eficacia del filtrado wavelet y la falta de diferencias notables entre las señales originales y filtradas podrían estar relacionadas con la ausencia de pretratamiento de las señales EEG. Como se ha señalado en estudios previos, no existe un método de eliminación de ruido que combine alta precisión con eficiencia algorítmica en todas las situaciones [R2]. Los métodos basados en wavelets, aunque precisos, requieren una adecuada preparación de las señales para ser realmente efectivos. La implementación de un pretratamiento mediante filtros FIR o IIR antes del filtrado wavelet es crucial para asegurar una eliminación de ruido más eficaz y mantener la integridad de la señal original.

## **Archivos de códigos** <a name="id7"></a>
[Señal filtrada de ECG con transformada wavelet](https://github.com/adri201022/ISB-Grupo-11/blob/7caa18f4cc3dd7cca9a34894013ee3a05a5de28a/Documentaci%C3%B3n/Laboratorios/L7_Filtros_Wavelet/C%C3%B3digo_ECG.py)

## **Referencias** <a name="id8"></a>

[1] A. N. Akansu and R. A. Haddad, “Chapter 6 - Wavelet Transform,” in Multiresolution Signal Decomposition (Second Edition), A. N. Akansu and R. A. Haddad, Eds., San Diego: Academic Press, 2001, pp. 391–442. doi: 10.1016/B978-012047141-6/50006-9.

[2] S. Kouro and R. Musalem, “Tutorial introductorio a la Teoría de Wavelet.” Accessed: May 17, 2024. [Online]. Available: http://www2.elo.utfsm.cl/~elo377/documentos/Wavelet.pdf

[3] S. Talebi, “The Wavelet Transform - Towards Data Science” Medium. Accessed: May 17, 2024. [Online]. Available: https://towardsdatascience.com/the-wavelet-transform-e9cfa85d7b34
  
[4] P. S. Addison, The Illustrated Wavelet Transform Handbook: Introductory Theory and Applications in Science, Engineering, Medicine and Finance, SECOND EDITION. 2017. doi: 10.1201/9781315372556.

[5] J. Castanedo, "Aplicación de la transformada wavelet en la caracterización de señales eléctricas". Accessed May 17, 2024. [Online]. Available: https://addi.ehu.es/bitstream/handle/10810/29202/Memoria.pdf
[6] M.Alfaouri y K.Daqrouq,"ECG Signal Denoising by Wavelet Transform Thresholding",American Journal of Applied Sciences,vol. 5, no. 3,pp. 276-281, 2008

[R1] M.Al-kadi (2013, 2 de febrero). Effectiveness of Wavelet Denoising on Electroencephalogram Signals. Science Direct. https://www.sciencedirect.com/science/article/pii/S1665642313715244

[R2] Grobbelaar, M. (2022, 22 de julio). A Survey on Denoising Techniques of Electroencephalogram Signals Using Wavelet Transform. MDPI. https://www.mdpi.com/2624-6120/3/3/35
‌
