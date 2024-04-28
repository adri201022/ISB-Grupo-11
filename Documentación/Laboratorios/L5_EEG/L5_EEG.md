# Informe de Laboratorio 4: Uso de BiTalino y Ultracortex para EEG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Materiales y equipos](#id3)
4. [Fotos de conexión usada](#id4)
5. [Videos de la señal](#id5)
6. [Ploteo de la señal en OpenSignals](#id6)
7. [Ploteo de la señal en python](#id7)
8. [Ploteo de la señal en OpenBCI GUI](#id8)
9. [Resumen y explicación de la señal ploteada](#id9)
10. [Archivo de los datos de la señal ploteada](#id10)
11. [Códido del ploteo de la señal en Python](#id11)
12. [Referencias](#id12)

## **Introducción** <a name="id1"></a>

### Una visión fisiológica
<p style="text-align: justify;">
  
El cerebro humano está compuesto por aproximadamente 85 mil millones de neuronas, las cuales son responsables de la mayor parte de la comunicación a través de las sinapsis, ubicadas al final de los axones. Cuando se transmite información, también se liberan neurotransmisores que provocan cambios en el voltaje en toda la membrana celular. Se genera un campo eléctrico de corta duración (potencial postsináptico) en apenas unos cientos de milisegundos. La neurona piramidal es el tipo celular más relevante para medir los campos eléctricos desde el cuero cabelludo, ya que su actividad es lo suficientemente intensa como para atravesar las distintas capas. Esto se debe a su orientación específica, perpendicular a la superficie cortical [1].

El cerebro está compuesto por cuatro áreas principales en su superficie: el lóbulo frontal (naranja), el temporal (verde), el parietal (azul) y el occipital (amarillo), como se muestra en la Figura 1, cada uno con funciones específicas. El lóbulo occipital, situado en la parte posterior del cráneo, se encarga del procesamiento visual. Por otro lado, el lóbulo temporal se dedica al procesamiento sensorial, la memoria a largo plazo, las memorias visuales, las emociones y el lenguaje. El lóbulo parietal integra información del entorno y su relación con nuestro cuerpo, como la coordinación al agarrar un objeto. Finalmente, el lóbulo frontal controla los movimientos voluntarios, las decisiones, el pensamiento, el procesamiento cognitivo, incluida la planificación y la atención, y se conoce como el centro de la personalidad [2].

</p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/ec6cdffa-bbf5-4561-a7fb-51fb9c4b4f82" width="400" height="300"> </p>
<p align="center"> <small>Figura 1: El cerebro y sus lóbulos superficiales con sus respectivas funciones (marcadas en rojo) [3].</small> </p>


### Adquisición de un EEG
<p style="text-align: justify;">
Cinco sub-bandas de frecuencia definen las frecuencias de la señal EEG que pueden medirse desde el cerebro, siendo la gamma la más rápida y la delta la más lenta.
</p>
<div align="center">
  
| **Tipo de onda** | **Ejemplo de señal** | **Frecuencia [Hz]** | **Ocurrencias** |
|:----------------:|:--------------------:|:-------------------:|:---------------:|
| Gamma | [![Gamma](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/711645fe-308f-4b50-a757-aebb16bd0496)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/711645fe-308f-4b50-a757-aebb16bd0496) | >25 | Concentración, resolver problemas |
| Beta | [![Beta](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/4a399e96-b010-4f05-b59a-1f9ce6d89211)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/4a399e96-b010-4f05-b59a-1f9ce6d89211) | 12-25 | Mente activa, ocupada |
| Alfa | [![Alpha](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/4b370e03-9e30-4903-a378-c61d746da04a)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/4b370e03-9e30-4903-a378-c61d746da04a) | 8-12 | Reflexiva, tranquila |
| Theta | [![Theta](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/76a6d69f-e0d6-4ae4-a0e5-baf8bf54df5b)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/76a6d69f-e0d6-4ae4-a0e5-baf8bf54df5b) | 4-12 | Somnolencia |
| Delta | [![Delta](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/45a9af16-12cd-4413-baa2-0a95c9d05dc3)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/45a9af16-12cd-4413-baa2-0a95c9d05dc3) | 0-4 | Dormir, soñando |

</div>
<p style="text-align: justify;">
  
Las oscilaciones en la **banda delta** se encuentran en un rango de frecuencias de 0 a 4 Hz y se observan en distintas fases del sueño, siendo su intensidad un indicador de la profundidad del mismo. Por otro lado, las frecuencias **theta**, que van desde los 4 hasta los 8 Hz, tienen su origen en el tálamo y muestran una mayor actividad en el lado derecho del cerebro. Estas ondas theta están asociadas con la región frontal del cerebro y están vinculadas a tareas mentales, mostrando mayor actividad conforme aumenta la dificultad de la tarea. Aunque son detectables en todas las áreas de la corteza cerebral, su importancia varía según la región cerebral. Ejemplos de pruebas que implican el uso de ondas theta son la prueba N-back, que evalúa la capacidad de memoria de trabajo, y la navegación en realidad virtual. En cuanto a las oscilaciones en la **banda alfa**, que tienen una frecuencia entre 8 y 12 Hz, reflejan funciones relacionadas con la memoria, el control motor y los sentidos. Se ha observado que la intensidad de la banda alfa aumenta durante estados de relajación despierta, como la meditación, y disminuye durante la actividad mental o física. Además de la meditación, otras áreas de estudio relacionadas con las ondas alfa incluyen la atención y el entrenamiento de biofeedback. Las ondas **beta**, que oscilan entre 12 y 25 Hz, se generan principalmente en las regiones frontal y posterior del cerebro y están asociadas con la actividad cognitiva y la concentración. Su frecuencia de oscilación aumenta con la intensidad del pensamiento y la concentración. Ejemplos de tareas que pueden emplear ondas beta son aquellas que implican el control motor fino y la alerta inducida por estímulos visuales o sonoros. Por último, la **banda gamma**, con frecuencias por encima de los 25 Hz, tiene un origen y función menos claros, aunque se ha sugerido su relación con movimientos oculares y se ha estudiado en investigaciones sobre microsacádicos [4].

Un método ampliamente reconocido a nivel internacional para describir las posiciones de los electrodos en el cuero cabelludo es el **sistema internacional 10-20**, ilustrado en la Figura 2. Este sistema establece que la distancia total entre el frente (nasion) y la parte posterior (inion), así como de derecha a izquierda, se define como el 100%, de ahí que los números 10 y 20 describan las distancias entre cada electrodo adyacente en términos de porcentaje. Cada posición incluye una letra y un número que indican la ubicación en el lóbulo (frontal, temporal, central, parietal y occipital) y en el hemisferio respectivamente. Es importante señalar que los números impares se refieren al hemisferio izquierdo (en rojo) y los números pares al hemisferio derecho (en azul), mientras que la línea media se identifica con la letra 'z' para cero (en negro). Para asegurar la correcta posición de los electrodos, se dispone de gorras de electrodos preensambladas que facilitan el proceso de posicionamiento óptimo. Estas gorras resultan especialmente prácticas cuando se necesita adquirir señales EEG de todo el cerebro. No obstante, preparar y ajustar la gorra y cada electrodo en el cuero cabelludo puede ser un proceso intensivo en tiempo, ya que implica la medición unipolar de señales y la fijación de electrodos en el cuero cabelludo mediante una pasta conductora [4-5].

</p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/c94909a0-8cd5-4814-b1d4-687551589be4" width="400" height="300"> </p>
<p align="center"> <small>Figura 2: Topografía de una cabeza con posicionamiento de electrodos según el sistema internacional 10-20. [3].</small> </p>

### Aplicaciones
<p style="text-align: justify;">

En el ámbito médico, el electroencefalograma (EEG) se emplea comúnmente para detectar trastornos o enfermedades cerebrales que generan irregularidades detectables en la señal EEG, como en casos de epilepsia o trastornos del sueño. Además, el EEG puede resultar beneficioso en conjunción con una interfaz cerebro-computadora (BCI), especialmente para pacientes con lesiones en la médula espinal, accidentes cerebrovasculares en el tronco encefálico o esclerosis lateral amiotrófica (ELA), quienes se encuentran "atrapados" en sus cuerpos sin capacidad de comunicación. Estos pacientes con discapacidades motoras graves requieren métodos alternativos de comunicación, y la BCI puede extraer "características" de las señales cerebrales para activar dispositivos externos, como interruptores, prótesis o computadoras [6].

</p>

## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de EEG.
- Hacer una correcta configuración de BiTalino
- Extraer la información de las señales EEG del software OpenSignals (r)evolution
- Extraer la información de las señales EEG del software OpenBCI GUI

## **Materiales y equipos** <a name="id3"></a>
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |
| Mark IV | Ultracortex | 1 |

</div>

## **Fotos de conexión usada** <a name="id4"></a>
<p style="text-align: justify;">

En la figura 3 se observa la colocación de los electrodos en el usuario de prueba que se realiza conforme a la Guía de Inicio BITalino (r)evolution en casa para Electroencefalografía (EEG), diseñada para familiarizarse con las bioseñales específicas de EEG [3]. En las siguientes imágenes se pueden observar las colocaciones electrodos-cuerpo para medir EEG en la posición FP1: pines de medición IN+/- (izquierda) y referencia (derecha) y las colocaciones BITalino-cables. En la figura 4 se observa la colocación del Ultracortex Mark IV en el usuario de prueba de acuerdo a lo indicado en sus instrucciones de uso [7].

</p>

<div align="center">

|  **Figura 3: Prueba con BITalino**  | **Figura 4: Prueba con Ultracortex** |
|:------------:|:---------------:|
|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/3ead35b7-7858-4e3b-bdb1-3955c5cfe5af" width="60%" height="60%"></p>|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/3bb20da0-a6af-4bb9-8937-844391850a27" width="60%" height="60%"></p>|

</div>

## **Videos de la señal** <a name="id5"></a>
<p style="text-align: justify;">
  
El procedimiento para la adquisición de señales EEG de acuerdo a la Guía de Inicio BITalino (r)evolution en casa para Electroencefalografía (EEG) es el siguiente:
1. Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal, sin movimientos oculares/ojos cerrados) durante 30 segundos.
2. Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos.
3. Registre otra fase de referencia de 30 segundos.
4. Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos y resuelve cada uno de ellos mentalmente enfocando tu mirada en un punto específico para evitar artefactos.
5. Detenga la grabación y guarde sus datos [4].

</p>

### **Prueba con BITalino**
<div align="center">

| **Fase de referencia** | **Ciclo Ojos abiertos-Ojos cerrados** | **Fase de ejercicios matemáticos** |
|:--------------------------------:|:---------------------------------:|:----------------------------:|
| <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/3cbe8832-91e8-47e6-9b09-bd43fb1abd32"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/c9640fea-7554-49af-a7eb-830ea7d28549"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/7fc7f436-a8d2-4472-862c-a85dba44f1c7"></video> |

</div>

### **Prueba con Ultracortex**
<div align="center">

| **Fase de referencia** | **Ciclo Ojos abiertos-Ojos cerrados** | **Fase de ejercicios matemáticos** |
|:--------------------------------:|:---------------------------------:|:----------------------------:|
| <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/2cc8ce80-f0ad-4faf-8ba9-dbc42f855989"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/5b6486f0-c345-4f29-bb59-5fd240f60d39"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/942fd7bf-19be-4ecd-af48-4d851a392a92"></video> |

</div>

## **Ploteo de la señal en OpenSignals** <a name="id6"></a>

En esta sección presentaremos los gráficos de los datos recopilados a una frecuencia de muestreo de 1 kHz mediante el uso de BITalino y el programa OpenSignals. Se mostrarán los gráficos durante el tiempo total de grabación y secciones de los datos con rangos cortos de tiempo para una mejor visualización.

* Referencia (reposo):

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/843efb64-d41c-45b1-a75f-916a882c1c9e"  width="700" height="350"> </p>
<p align="center"> <small>Figura 3: Ploteo de los datos en la fase de referencia con 32.3 segundos de duración.</small> </p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/97ca31f2-a628-4758-828c-17f8299a8230"  width="700" height="350"> </p>
<p align="center"> <small>Figura 4: Ploteo de los datos durante el rango de 6 a 16 segundos.</small> </p>

* Ciclo entre ojos abiertos y ojos cerrados:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/2a4102ec-bb01-486b-977d-cbfb471af36b"  width="700" height="350"> </p>
<p align="center"> <small>Figura 5: Ploteo de los datos en la fase de abrir y cerrar los ojos con 1 minuto y 16 segundos de duración.</small> </p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/aca03adf-d2f2-4058-87ac-a60157ec3fdf"  width="700" height="350"> </p>
<p align="center"> <small>Figura 6: Ploteo de los datos durante el rango de 15.2 a 25.1 segundos.</small> </p>


* Durante preguntas matemáticas:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/b6844cc9-e7d7-45b1-aa30-ffdd03645af1"  width="700" height="350"> </p>
<p align="center"> <small>Figura 7: Ploteo de los datos en la fase de preguntas con 1 minuto y 19 segundos de duración.</small> </p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/bdcebf02-205b-44c3-8da8-66c4941e8633"  width="700" height="350"> </p>
<p align="center"> <small>Figura 8: Ploteo de los datos durante el rango de 36.7 a 46.6 segundos de duración.</small> </p>

## **Ploteo de la señal en Python** <a name="id7"></a> 
A continuación mostraremos los ploteos en python que tienen un frecuencia de muestreo de 1000.
* Referencia (reposo):

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/1c5aa1c8-6231-43cb-a4ff-a9f22aacf47c"  width="700" height="350"> </p>

<p align="center"> <small>Figura 9: Ploteo de los datos en la fase de ojos cerrados.</small> </p>


* Ciclo entre ojos abiertos y ojos cerrados:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/d3574665-5991-45a5-bc42-874c653a6564"  width="700" height="350"> </p>

<p align="center"> <small>Figura 10: Ploteo de los datos en la fase de abrir y cerrar los ojos .</small> </p>

* repetición de reposo:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/6de06516-e48e-4638-b270-3bc5f096523e"  width="700" height="350"> </p>

<p align="center"> <small>Figura 11: Ploteo de los datos en la fase de ojos cerrados (repetición).</small> </p>

* Durante preguntas matemáticas:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/f0b7a8c1-bb6c-488d-85e0-fd64178327b2"  width="700" height="350"> </p>

<p align="center"> <small>Figura 12: Ploteo de los datos en la fase de preguntas.</small> </p>


## **Ploteo de la señal en OpenBCI GUI** <a name="id8"></a> 
* Referencia (reposo):

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/1baf2c63-3136-45f6-9f74-00b1c4f7bf9b"  width="700" height="350"> </p>


<p align="center"> <small>Figura 13: Ploteo de los datos en la fase de ojos cerrados.</small> </p>


* Ciclo entre ojos abiertos y ojos cerrados:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/79daadb9-3a59-43cb-ad37-6dc6695bfe34"  width="700" height="350"> </p>


<p align="center"> <small>Figura 14: Ploteo de los datos en la fase de abrir y cerrar los ojos .</small> </p>

* repetición de reposo:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/2ed05153-69b3-4789-aec1-cad986b236c3"  width="700" height="350"> </p>


<p align="center"> <small>Figura 15: Ploteo de los datos en la fase de ojos cerrados (repetición).</small> </p>

* Durante preguntas matemáticas:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/b2f04967-5a65-452d-885f-348134bf766d"  width="700" height="350"> </p>


<p align="center"> <small>Figura 16: Ploteo de los datos en la fase de preguntas.</small> </p>

A continuación presentaremos las gráficas de la densidad espectral de potencia de las FFT de los 4 tramos que tenemos, que en este caso son los 4 ejercicios que hicimos.

* Referencia (reposo):

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/da9e689a-b701-46fc-b1bb-ae08c4a21231"  width="700" height="350"> </p>


<p align="center"> <small>Figura 17: Ploteo de los datos en la fase de ojos cerrados.</small> </p>


* Ciclo entre ojos abiertos y ojos cerrados:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/3660912f-fc84-4fb0-848f-1199e4049134"  width="700" height="350"> </p>



<p align="center"> <small>Figura 18: Ploteo de los datos en la fase de abrir y cerrar los ojos .</small> </p>

* repetición de reposo:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/373cdf71-f4fb-4c99-a530-d72511f377aa"  width="700" height="350"> </p>



<p align="center"> <small>Figura 19: Ploteo de los datos en la fase de ojos cerrados (repetición).</small> </p>

* Durante preguntas matemáticas:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/8fdef3e9-79c1-457d-bb77-543f19a32062"  width="700" height="350"> </p>



<p align="center"> <small>Figura 20: Ploteo de los datos en la fase de preguntas.</small> </p>

## **Resumen y explicación de la señal ploteada** <a name="id9"></a>

## **Archivo de los datos de la señal ploteada** <a name="id10"></a>

* [Datos de las pruebas de EEG (.txt)](https://github.com/adri201022/ISB-Grupo-11/tree/main/Documentación/Laboratorios/L5_EEG/EEG_data/BITalino)

## **Códido del ploteo de la señal en Python** <a name="id11"></a>
- [Señal ploteada del open signal en python](https://github.com/adri201022/ISB-Grupo-11/blob/d5c2b668c479f883335dde8964ea4b5a51437736/Documentaci%C3%B3n/Laboratorios/L5_EEG/Ploteo_se%C3%B1ales%20de%20open%20signal.py)
- [Señal ploteada del OpenBCI GUI en python](https://github.com/adri201022/ISB-Grupo-11/blob/d5c2b668c479f883335dde8964ea4b5a51437736/Documentaci%C3%B3n/Laboratorios/L5_EEG/ploteo_se%C3%B1al.py)
- [Señal transformada a psd ploteada del OpenBCI GUI en python ](https://github.com/adri201022/ISB-Grupo-11/blob/d5c2b668c479f883335dde8964ea4b5a51437736/Documentaci%C3%B3n/Laboratorios/L5_EEG/fft_se%C3%B1an.py)
## **Referencias** <a name="id12"></a>
[1] Suzana Herculano-Houzel, “The human brain in numbers: a linearly scaled-up primate brain,” Frontiers in human neuroscience, vol. 3, Jan. 2009, doi: https://doi.org/10.3389/neuro.09.031.2009.

[2] Bansal, D., & Mahajan, R. (2019). EEG-Based Brain-Computer Interfaces: Cognitive Analysis and Control Applications. Academic Press.

[3] M. Proença and K. Mrotzeck, vol. 2021. BITalino (r)Evolution Lab Guide, Home Guide 2—EEG. Available at: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[4] Abhang, P. A., Gawali, B. W., & Mehrotra, S. C. (2016). Chapter 2 - Technological Basics of EEG Recording and Operation of Apparatus. In Introduction to EEG-and Speech-Based Emotion Recognition (pp. 19-50). Academic Press.

[5] Sazgar, M., & Young, M. G. (2019). Overview of EEG, electrode placement, and montages. In Absolute Epilepsy and EEG Rotation Review (pp. 117-125). Springer, Cham.

[6] Machado, S., et al. (2010). EEG-based brain-computer interfaces: an overview of basic concepts and clinical applications in neurorehabilitation. Reviews in the Neurosciences, 21(6), 451-468.

[7] “Ultracortex Mark IV | OpenBCI Documentation,” Openbci.com, Nov. 08, 2023. https://docs.openbci.com/AddOns/Headwear/MarkIV/#electrode-location-overview (accessed Apr. 27, 2024).
