# Informe de Laboratorio 6: Filtrado de señales EMG, ECG y EEG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Filtros de señal EMG](#id3)
4. [Filtros de señal ECG](#id4)
5. [Filtros de señal EEG](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>
Los filtros digitales son un componente crucial en el procesamiento de señales biomédicas, ya que permiten eliminar el ruido, realzar características específicas y mejorar la calidad de las señales en diversas aplicaciones biomédicas como la electrocardiografía (ECG), la electromiografía (EMG) y la electroencefalografía (EEG) [1]. Los filtros se pueden clasificar de diversas maneras según sus características, como su comportamiento en el tiempo, su tipo de implementación (analógico o digital), y su respuesta al impulso (infinita o finita). Los filtros recursivos, también conocidos como IIR, utilizan conexiones de retroalimentación para lograr su función, mientras que los filtros FIR se basan en una respuesta al impulso de duración finita y no tienen retroalimentación. Estas diferencias en la estructura y el comportamiento hacen que cada tipo de filtro sea adecuado para diferentes aplicaciones [2].

### Filtros FIR
Esta sección se centra en los filtros de Respuesta Finita al Impulso (FIR). Un filtro FIR se construye con multiplicadores y sumadores, pudiendo ser implementado en hardware o software y ejecutarse en serie, paralelo o una combinación de ambos. Utiliza elementos de retardo, representados por registros con reloj, cruciales en el procesamiento de señales, y se denotan con el símbolo z1 en DSP debido a las propiedades matemáticas de la transformación Z. El número de "taps" o multiplicadores necesarios para calcular cada salida es un aspecto clave, coincidiendo en una implementación paralela con el número de taps, mientras que en serie, se utiliza un multiplicador secuencialmente para cada salida. La cantidad de taps puede variar según la complejidad del filtro, pudiendo alcanzar cientos en casos más complejos [3].

<div align="center";style="text-align:center;">
  <img width="400" height="400" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/156bcf55-a280-4bb2-904a-e1284ceb7b80">
  <br>
  <span style="font-style: italic;">Figura 1: Estrcutura de filtro de respuesta finita al impulso [3].</span>
</div>

#### Ventana Hanning

#### Ventana Hamming

#### Ventana Bartlett

#### Ventana Rectangular

#### Ventana Blackman

### Filtros IIR
Esta sección se centra en los filtros de Respuesta Infinita al Impulso (IIR), que son más complejos que los FIR. Mientras que un filtro FIR toma un flujo de datos de entrada y los multiplica por una serie de coeficientes para producir cada salida, un filtro IIR realiza este proceso y además retroalimenta el flujo de datos de salida a través de otra serie de multiplicadores y coeficientes. Esta retroalimentación elimina muchas de las propiedades lineales del filtro FIR, lo que hace que el filtro IIR sea mucho más difícil de analizar. Además, dependiendo de la elección de los coeficientes, puede generar comportamientos no deseados, como una respuesta al impulso de duración o magnitud infinita [*].

<div align="center";style="text-align:center;">
  <img width="400" height="400" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/82d4552f-adb3-4154-b023-9f24736867fc">
  <br>
  <span style="font-style: italic;">Figura : Estrcutura de filtro de respuesta infinita al impulso [*].</span>
</div>

#### Filtros Butterworth

#### Filtros Bessel 

#### Filtros Chebyshev

#### Filtros Elípticos

## **Objetivos** <a name="id2"></a>
<ul>
  <li>Filtrar las señales EMG para eliminar ruido y artefactos, y aislar la actividad muscular efectiva.</li>
  <li>Diseñar y aplicar filtros óptimos, tanto IIR como FIR, para eliminar las frecuencias altas correspondientes a ruido en las señales de ECG utilizando un dataset previamente creado.</li>
  <li>Preprocesar señales EEG para reducir el ruido y extraer características de interés como ondas
cerebrales específicas.</li>
</ul>

## **Filtros de señal EMG** <a name="id3"></a>

## **Filtros de señal ECG** <a name="id4"></a>

## **Filtros de señal EEG** <a name="id5"></a>

## **Discusión** <a name="id6"></a>

## **Archivos de códigos** <a name="id7"></a>

## **Referencias** <a name="id8"></a>
[1] P. Podder, Md. Mehedi Hasan, Md. Rafiqul Islam, and M. Sayeed, “Design and Implementation of Butterworth, Chebyshev-I and Elliptic Filter for Speech Signal Analysis,” International Journal of Computer Applications, vol. 98, no. 7, 2014, doi: 10.5120/17195-7390.

[2] “COMPARISON OF FIR AND IIR FILTERS USING ECG SIGNAL WITH DIFFERENT SAMPLING FREQUENCIES,” International Research Journal of Modernization in Engineering Technology and Science, 2023, doi: 10.56726/irjmets35977.

[3] M. Parker, “Finite Impulse Response (FIR) Filters,” in Digital Signal Processing 101, 2017. doi: 10.1016/b978-0-12-811453-7.00005-6.

[*] M. Parker, “Infinite Impulse Response (IIR) Filters,” in Digital Signal Processing 101, 2017. doi: 10.1016/b978-0-12-811453-7.00008-1.
