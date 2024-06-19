# Informe de Laboratorio 10: Procesamiento de una señal EEG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Preprocesamiento de señal EEG](#id3)
4. [Filtrado de señal EEG](#id4)
5. [Extracción de características de señal EEG](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>
La actividad del EEG refleja la suma temporal de la actividad sincrónica de millones de neuronas corticales que están alineadas espacialmente. El EEG normal presenta una gran diversidad y una amplia variabilidad fisiológica. Las formas de onda del EEG se pueden caracterizar según su ubicación, amplitud, frecuencia, morfología, continuidad (rítmica, intermitente o continua), sincronía, simetría y reactividad. No obstante, el método más común para clasificar las formas de onda del EEG es por su frecuencia, de manera que las ondas del EEG se nombran de acuerdo a su rango de frecuencia utilizando numerales griegos. Las formas de onda más estudiadas incluyen delta (0.5 a 4Hz); theta (4 a 7Hz); alfa (8 a 12Hz); sigma (12 a 16Hz) y beta (13 a 30Hz). Además, existen otras formas de onda como las oscilaciones infralentas (ISO) (menos de 0.5Hz) y las oscilaciones de alta frecuencia (HFOs) (más de 30Hz), que están fuera del rango convencional del EEG clínico pero que han ganado importancia clínica con el desarrollo del procesamiento digital de señales [1].
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/bf1db342-f359-443d-99f9-ee0e08b3b558" width="400"><br> 
<p align="center"><b>Figura 1: Muestras de ondas cerebrales con frecuencias dominantes pertenecientes a las bandas beta, alfa, theta y delta, así como ondas gamma [2].</b> <br> 

Las señales EEG obtenidas de los electrodos colocados en el cuero cabelludo a menudo están contaminadas por varios tipos de ruido y artefactos, como movimientos oculares, actividad muscular e interferencias eléctricas externas [3]. Por lo tanto, la preprocesamiento y filtrado son pasos cruciales en el análisis de datos de EEG para mejorar la calidad de la señal y extraer información significativa. El preprocesamiento de señales EEG incluye pasos como la re-referencia, eliminación de artefactos e interpolación de canales defectuosos. Luego, se aplica filtrado para eliminar frecuencias no deseadas, utilizando técnicas como filtrado de paso de banda, de muesca y de paso alto o bajo. Posteriormente, se extraen características de los datos EEG, analizando propiedades espectrales, temporales y de conectividad funcional mediante métodos como el análisis de Fourier y de wavelets [3]. Estas técnicas permiten capturar patrones y dinámicas subyacentes, útiles en aplicaciones como interfaces cerebro-computadora, monitoreo cognitivo y diagnóstico de trastornos neurológicos.

<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/14c111cb-5f71-459a-8f61-266c9bc21ee7" width="400"><br> 
<p align="center"><b>Figura 2: El proceso de cuatro pasos para el análisis de señales EEG. El análisis de señales EEG implica cuatro etapas: adquisición, eliminación de ruido, ingeniería de características y clasificación. [3]</b> <br> 

## **Objetivos** <a name="id2"></a>
<ul>
  <li>Comprender el proceso de preprocesamiento de señales EEG, ya que es fundamental para garantizar la calidad de los datos</li>
  <li>Analizar la importancia y aplicaciones del procesamiento de señales EEG, lo que proporciona contexto sobre su relevancia en la investigación y la práctica clínica</li>
</ul>

## **Preprocesamiento de señal EEG** <a name="id3"></a>

## **Filtro de señal EEG** <a name="id4"></a>

## **Extracción de características de señal EEG** <a name="id5"></a>

## **Discusión** <a name="id6"></a>


## **Archivos de códigos** <a name="id7"></a>


## **Referencias** <a name="id8"></a>
  
    [1]C. S. Nayak y A. C. Anilkumar, «EEG Normal Waveforms», en StatPearls, Treasure Island (FL): StatPearls Publishing, 2024. Accedido: 18 de junio de 2024. [En línea]. Disponible en: http://www.ncbi.nlm.nih.gov/books/NBK539805/
  
    [2]P. A. Abhang, B. W. Gawali, y S. C. Mehrotra, «Chapter 2 - Technological Basics of EEG Recording and Operation of Apparatus», en Introduction to EEG- and Speech-Based Emotion Recognition, P. A. Abhang, B. W. Gawali, y S. C. Mehrotra, Eds., Academic Press, 2016, pp. 19-50. doi: 10.1016/B978-0-12-804490-2.00002-6.

    [3]A. Chaddad, Y. Wu, R. Kateb, y A. Bouridane, «Electroencephalography Signal Processing: A Comprehensive Review and Analysis of Methods and Techniques», Sensors (Basel), vol. 23, n.o 14, p. 6434, jul. 2023, doi: 10.3390/s23146434.
