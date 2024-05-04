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

### Filtros IIR

#### Filtros Butterworth

#### Filtros Bessel 

#### Filtros Chebyshev

#### Filtros Elípticos

### Filtros FIR

#### Ventana Hanning

#### Ventana Hamming

#### Ventana Bartlett

#### Ventana Rectangular

#### Ventana Blackman

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
