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
Se procederá a presentar el análisis de las señales preprocesadas del OpenBCI, utilizando el ultracortex. Es importante destacar que el OpenBCI guarda los datos en microvoltios (uV), por lo cual se convirtieron a milivoltios (mV). Además, la frecuencia de muestreo utilizada fue de 125 Hz. Esta frecuencia se empleó para calcular el tiempo y se trabajó con 8 canales.

### Señales obtenida del ultracortex

| Estado          | Señal                                                                                      |
|--------------------|---------------------------------------------------------------------------------------------|
| Ojos Cerrados      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/5ff1d445-799f-4b8b-b015-3a5ea5aaa8d5" width="800" height="300"></p> |
| Ojos Abiertos      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/7ef22b8f-bc86-423e-a0eb-1319090423c6" width="800" height="300"></p> |
| Ojos Cerrados      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/1052106b-2cca-4082-ac5c-fb3b9d1b5803" width="800" height="300"></p> |
| Ejercicio Matemático | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/bfb3f410-ea9b-45a2-aaa9-b4c844b44a9b" width="800" height="300"></p> |

## **Filtro de señal EEG** <a name="id4"></a>
Para esta sección, se aplicó un filtro Butterworth pasa banda con el objetivo de eliminar ruidos innecesarios. El filtro se configuró para operar en el rango de frecuencias de 8 a 30 Hz. La decisión del filtro y las frecuencias de corte se basó en el análisis de un paper seleccionado previamente. Además, se utilizó un filtro Butterworth de orden 10 para proporcionar mayores tasas de caída entre la banda de paso y la banda de parada, lo cual puede ser necesario para alcanzar los niveles requeridos de atenuación en la banda de parada o para mejorar la nitidez del corte.[4]

| Estado          | Filtrado de Señal                                                                                      |
|--------------------|---------------------------------------------------------------------------------------------|
| Ojos Cerrados      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/c6f74026-a792-40e0-9159-444f066f05b9" width="800" height="300"></p> |
| Ojos Abiertos      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/2b3a6184-c38f-4c1e-9276-9cdba0b79577" width="800" height="300"></p> |
| Ojos Cerrados      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/a8053500-4b09-4991-98dd-620c01b4ce4b" width="800" height="300"></p> |
| Ejercicio Matemático | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/9948094d-9e5f-410e-8c49-c71a750ee063" width="800" height="300"></p> |


## **Extracción de características de señal EEG** <a name="id5"></a>
Para decidir las características del EEG a extraer, nos hemos guiado por el análisis detallado de un paper seleccionado. Este estudio estableció las bandas de frecuencia de interés y la generación de espectrogramas para el promedio de los canales como componentes clave de nuestro enfoque. Estas decisiones se basan en la necesidad de comprender y representar adecuadamente las diferentes bandas de frecuencia presentes en los datos del EEG, lo cual es crucial para nuestro análisis y posterior interpretación de los resultados.[4]

En primer lugar, se presentarán las bandas del EEG del promedio de los 8 canales.

* Canal General
  
| Estado          | Bandas                                                                                      |
|--------------------|---------------------------------------------------------------------------------------------|
| Ojos Cerrados      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/b432ab51-3c97-4546-9e81-699a02c28673" width="800" height="400"></p> |
| Ojos Abiertos      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/9cfbad07-9a10-4318-8444-f318dd2381af" width="800" height="400"></p> |
| Ojos Cerrados      | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/28b05cad-95a3-4a4c-9569-d7c2fd9c754d" width="800" height="400"></p> |
| Ejercicio Matemático | <p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/992e77f4-7753-4202-9409-c5eb66214404" width="800" height="400"></p> |

Ahora se presentarán el espectograma del EEG del promedio de los 8 canales.

* Ojos cerrados
<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/7b8b91c6-125a-4bbb-b377-e1bf707c022b" width="800" height="400"></p>
* Ojos abiertos-cerrados
<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/e5835c3a-923b-4f66-b7a8-a0429fa76d9a" width="800" height="400"></p>
* Ojos cerrados (post-ejercicio)
<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/167a157b-845e-46b9-a9ef-2c77e4b2daf0" width="800" height="400"></p>
* Ejercicios matemáticos
<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/452099d7-1b2a-4a85-b3ce-9742ff7f99cd" width="800" height="400"></p>


## **Discusión** <a name="id6"></a>



## **Archivos de códigos** <a name="id7"></a>
[Código_de_señal_EEG](https://github.com/adri201022/ISB-Grupo-11/blob/f38a8ff4ef55b3cae89caa654b8a17cc0c873700/Documentaci%C3%B3n/Laboratorios/L10_Procesamiento_EEG/Senal_EEG.ipynb)

## **Referencias** <a name="id8"></a>
  
    [1]C. S. Nayak y A. C. Anilkumar, «EEG Normal Waveforms», en StatPearls, Treasure Island (FL): StatPearls Publishing, 2024. Accedido: 18 de junio de 2024. [En línea]. Disponible en: http://www.ncbi.nlm.nih.gov/books/NBK539805/
  
    [2]P. A. Abhang, B. W. Gawali, y S. C. Mehrotra, «Chapter 2 - Technological Basics of EEG Recording and Operation of Apparatus», en Introduction to EEG- and Speech-Based Emotion Recognition, P. A. Abhang, B. W. Gawali, y S. C. Mehrotra, Eds., Academic Press, 2016, pp. 19-50. doi: 10.1016/B978-0-12-804490-2.00002-6.

    [3]A. Chaddad, Y. Wu, R. Kateb, y A. Bouridane, «Electroencephalography Signal Processing: A Comprehensive Review and Analysis of Methods and Techniques», Sensors (Basel), vol. 23, n.o 14, p. 6434, jul. 2023, doi: 10.3390/s23146434.
    [4] Goyal and A. Mehta, "Acquisition, pre-processing, and feature extraction of EEG," International Research Journal of Engineering and Technology (IRJET), vol. 8, no. 2, pp. 237-241, [Online]. Available: https://www.irjet.net/archives/V8/i2/IRJET-V8I237.pdf.
