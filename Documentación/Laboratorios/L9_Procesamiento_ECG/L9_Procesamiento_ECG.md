# Informe de Laboratorio 9: Procesamiento de una señal ECG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Filtro de señal ECG](#id3)
4. [Picos de la onda R](#id4)
5. [HRV](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>

El electrocardiograma (ECG) es una señal que registra la actividad eléctrica del corazón.
Su adquisición se suele hacer de forma digital o mediante un papel milimitrado de dimensión 1 mm x 1 mm,
con líneas gruesas de 5 mm (cada mm representa la amplitud de las ondas ECG medidas en mV; 10 mm =1
mV)
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/42382650/d1bc3440-643f-46a6-aa1d-3156429f651f">
</p>
<p align="center"><b>Figura 1: Componentes de la señales ECG [3].</b> </p>

Onda P: La despolarización de las
aurículas antes de la contracción
provoca una pequeña deflexión
de bajo voltaje, seguida con un
retraso.

Complejo QRS: La
despolarización de los ventrículos
antes de la contracción provoca
una gran deflexión de voltaje. Es
la sección con mayor amplitud de
ECG.

Onda T: Repolarización
ventricular, es la última sección y
más complicada de visualizar.

<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/42382650/b8ea7da0-bb34-4660-b3fd-17f23dcc4223">
</p>
<p align="center"><b>Figura 1: Componentes de la señales ECG [3].</b> </p>

##### Onda P: 
Suele tener una duración menor de 120 mseg (< 3 cuadrados) y una
amplitud inferior a 0.25 mV (2.5 mm equivalente a 2 1/2 cuadrados). Fuera de estos límites suele
denominarse hipertrofia auricular.

##### Complejo QRS: 
Compuesto por tres ondas trifásicas: dos ondas negativas Q y S y una onda positiva R. La
duración del complejo QRS va entre 60 a 120 mseg. Los parámetros como duración, amplitud y
morfología son útiles para el diagnóstico de arritmias cardiacas, anormalidades de la conducción,
hipertrofia ventricular, infarto agudo de miocardio, desequilibrio electrolíticos y entre otros.

##### Onda Q: 
Suele ser 1/3 mayor que la onda R o mayores que 0.4 mseg en duración.

##### Onda T: 
Representa la repolarización ventricular, suele tener una duración de 160 mseg y ser uniforme.

## **Objetivos** <a name="id2"></a>

<ul>
  <li>Detallar cada etapa involucrada en la captura y análisis de señales electrocardiacas para comprender su funcionamiento y aplicación práctica.</li>
  <li>Analizar el estrés, la vitalidad y variabilidad del ritmo cardiaco</li>

  <li>Hallar los picos de la onda R y graficarlos (alternativa: usar la función punking)</li>

 <li>Hallar el HRV (basándose en un artículo base) </li>

 <li>Analizar críticamente las técnicas empleadas en el preprocesamiento de señales ECG, evaluando su capacidad para reducir el ruido, mejorar la calidad de la señal y facilitar la extracción de información relevante.</li>
</ul>

## **Filtro de señal ECG** <a name="id3"></a>

En el caso del filtrado de las señales, primero hemos utilizado un filtro notch para poder eliminar el ruido ambiental que aparece a menúdo en estos tipos de tomas. El segundo filtro que hemos usado es un filtro pasa baja bessel de tercer órden que tiene una frecuencia de corte de 30 Hz. Estamos usando este filtro ya que la bibliografía encontrada nos la recomienda para minimizar el efecto de ruido en altas frecuencias y artefactos en la detección de picos R [G2].

### Señal en reposo
|                   | Señal cruda                          | Filtro Notch                          | Filtro Bessel                        |
|-------------------|--------------------------------------|---------------------------------------|--------------------------------------|
| Señal en reposo   | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/95c74016-64c6-4eba-a2e3-749bd6e51998" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/9ce09ca1-0489-4a25-92ea-8bf37ebd5d69" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/e5452472-3d28-4e90-a1fa-a24890f2d2b3" width="550" height="250"> |

### Señal en respiraciones rápidas
|                           | Señal cruda                          | Filtro Notch                          | Filtro Bessel                        |
|---------------------------|--------------------------------------|---------------------------------------|--------------------------------------|
| Señal en respiraciones rápidas  | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/151615a4-5692-4e0d-9358-9f96c15afee5" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/0fcfc928-bc34-4d07-ac5e-bdff7ecc383d" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/d513ed52-b307-44d4-9c64-6846a1c760d5" width="550" height="250"> |

### Señal durante actividad
|                     | Señal cruda                          | Filtro Notch                          | Filtro Bessel                        |
|---------------------|--------------------------------------|---------------------------------------|--------------------------------------|
| Señal durante actividad | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/72d0fa70-1499-4781-8ae3-04499caa4147" width="450" height="300"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/f6adc0aa-898f-49a7-810d-9ddd77e3ab36" width="450" height="300"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/121294e7-3047-4f63-b310-40ad5827762e" width="450" height="300"> |


## **Picos de la onda R** <a name="id4"></a>
### Señal en reposo
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/1374a815-ce17-4b16-add7-4d67328f2b36" width="500" height="350">
</p>

### Señal en respiraciones rápidas
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/77455889-150d-4326-ada3-63f450c6635e" width="500" height="350">
</p>

### Señal durante actividad
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/992b9f80-dddc-4443-959f-39f1300c4f82" width="500" height="350">
</p>

## **HRV** <a name="id5"></a>

Para esta parte hemos obtenido los datos importantes que destaca la bibliografía encontrada, las cuales son SDNN, rMSSD, SD1 y SD2 [G2].

### Señal en reposo
#### Resultados HRV
- **SDNN**: 33.85 ms
- **rMSSD**: 19.33 ms
- **SD1**: 0.09 s
- **SD2**: 0.04 s

### Señal en respiraciones rápidas
#### Resultados HRV
- **SDNN**: 122.54 ms
- **rMSSD**: 171.79 ms
- **SD1**: 0.29 s
- **SD2**: 0.12 s

### Señal durante actividad
#### Resultados HRV
- **SDNN**: 117.89 ms
- **rMSSD**: 172.71 ms
- **SD1**: 0.29 s
- **SD2**: 0.11 s
## **Discusión** <a name="id6"></a>
Durante esta sección se discutirán los resultados para el SDNN, rMSSD, SD1 y SD2.

#### SDNN
Se trata de la desviación estándar de todos los intervalos entre latidos R-R. Tomando en cuenta los valores de referencia y el nivel de riesgo que brinda un estudio hecho por De la Cruz (2008) tenemos que, en reposo un valor de SDRR de 33.85 ms indica una variabilidad moderada, lo que demuestra un buen equilibrio entre los sistemas simpático y parasimpático, pero señalaría un nivel de riesgo alto para la salud cardiovascular ya que tiene un valor menor a 50 ms. Pero cuando se realizan respiraciones rápidas, el SDNN sube a 122.54 ms, demostrando la capacidad de adaptación debido a la activación del sistema parasimpático durante la respiración controlada, además que al ser mayor a 100 ms indicaría un nivel de riesgo bajo, lo que evidencia una buena salud. Finalmente, durante la actividad física el SDNN es de 117.89 ms, lo cual es menor en comparación con las respiraciones rápidas, pero sigue siendo un valor alto. Además, indica un bajo nivel de riesgo y muestra que tanto el corazón como el sistema nervioso se adaptan bien al esfuerzo físico. [G1] 

#### rMSSD

Respecto a los resultados de la raiz cuadrática media de diferencias sucesivas (rMSSD), tenemos que identificar que esta métrica o parámetro es un indicador de la actividad parasimpática del sistema nervioso autónomo, y se suele usar bastante para evaluar la variabilidad de frecuencia cardíaca (HRV) en estudios de salud y deporte. En nuestros resultados vemos un incremento significativo  del rMSSD del valor inicial de la señal en resposo de 19.33ms de la señal en reposo a los dos casos señal en respiraciones rápidas (171.79 ms) y señal durante actividad (172.71 ms). Esto nos sugiere una mayor activación parasimpática en ambas condiciones. Este comportamiento es consistente con estudios previos que asocian el aumento del rMSSD con estados de alta demanda física y respiratoria [R1].

#### SD1

Representa la desviación estándar de las distancias perpendiculares al eje de identidad en el gráfico de Poincaré. [G2] En reposo, el valor de SD1 es de 0.09 segundos, lo que significa que la frecuencia cardíaca es constante, debido a que, en reposo, el cuerpo humano no se encuentra bajo mucho estrés. Mientras que, durante las respiraciones rápidas y la actividad física, el valor de SD1 aumenta a 0.29 segundos. Esto indica que la frecuencia cardíaca presenta una mayor variación durante estas actividades, ya que los cambios en la respiración afectan la señal del ECG, haciendo que los intervalos entre latidos sean más irregulares. Lo mismo ocurre durante la actividad física, donde el esfuerzo causa alteraciones en la frecuencia cardíaca.

#### SD2

Respecto a los resultados de SD2, es fundamental comprender que esta métrica evalúa tanto la variabilidad de largo como de corto plazo en la variabilidad de frecuencia cardíaca (HRV). SD2 se obtiene de los gráficos de Poincaré y es utilizada para evaluar la dinámica autonómica a lo largo del tiempo [R2]. En nuestros resultados, observamos un incremento en los valores de SD2 durante las respiraciones rápidas (0.12 s) y la actividad física (0.11 s) en comparación con el reposo (0.04 s). Este incremento sugiere una mayor complejidad y variabilidad en las condiciones de mayor demanda fisiológica; a diferencia, del SD2 de las condiciones iniciales (0.04 s), estos resultados son consistentes con investigaciones previas que asocian altos valores de SD2 con una mayor variabilidad autonómica y adaptabilidad [R2].

## **Archivos de códigos** <a name="id7"></a>

[Tratamiento de señal  ECG en colab](https://github.com/adri201022/ISB-Grupo-11/blob/4b4ce18e4fabbbc0655e8162bcf6cdbd4163f358/Documentaci%C3%B3n/Laboratorios/L9_Procesamiento_ECG/Tratamiento%20de%20ECG.ipynb)

## **Referencias** <a name="id8"></a>

[G1] B. De La Cruz Torres, C. L. Lopez, and J. N. Orellana, “Analysis of heart rate variability at rest and during aerobic exercise: a study in healthy people and cardiac patients,” British Journal of Sports Medicine, vol. 42, no. 9, pp. 715–720, May 2008, doi: 10.1136/bjsm.2007.043646. Available: https://pubmed.ncbi.nlm.nih.gov/18199627/

[R1] A. Natarajan. “Frontiers | Heart rate variability during mindful breathing meditation”. Frontiers. Accedido el 7 de junio de 2024. [En línea]. Disponible: https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.1017350/full

[G2] “Effect of Different ECG Leads on Estimated R-R Intervals and Heart Rate Variability Parameters - PubMed”. PubMed. Accedido el 7 de junio de 2024. [En línea]. Disponible: https://pubmed.ncbi.nlm.nih.gov/31946698/

[R2] S. Lee. “Stochastic vagus nerve stimulation affects acute heart rate dynamics in rats”. Home - PLOS. Accedido el 7 de junio de 2024. [En línea]. Disponible: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194910
