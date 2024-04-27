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
  
El cerebro humano está compuesto por aproximadamente 85 mil millones de neuronas, las cuales son responsables de la mayor parte de la comunicación a través de las sinapsis, ubicadas al final de los axones. Cuando se transmite información, también se liberan neurotransmisores que provocan cambios en el voltaje en toda la membrana celular. Se genera un campo eléctrico de corta duración (potencial postsináptico) en apenas unos cientos de milisegundos. La neurona piramidal es el tipo celular más relevante para medir los campos eléctricos desde el cuero cabelludo, ya que su actividad es lo suficientemente intensa como para atravesar las distintas capas. Esto se debe a su orientación específica, perpendicular a la superficie cortical [1][2].

El cerebro está compuesto por cuatro áreas principales en su superficie: el lóbulo frontal (naranja), el temporal (verde), el parietal (azul) y el occipital (amarillo), como se muestra en la Figura 1, cada uno con funciones específicas. El lóbulo occipital, situado en la parte posterior del cráneo, se encarga del procesamiento visual. Por otro lado, el lóbulo temporal se dedica al procesamiento sensorial, la memoria a largo plazo, las memorias visuales, las emociones y el lenguaje. El lóbulo parietal integra información del entorno y su relación con nuestro cuerpo, como la coordinación al agarrar un objeto. Finalmente, el lóbulo frontal controla los movimientos voluntarios, las decisiones, el pensamiento, el procesamiento cognitivo, incluida la planificación y la atención, y se conoce como el centro de la personalidad [2][3].

</p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/ec6cdffa-bbf5-4561-a7fb-51fb9c4b4f82" width="400" height="300"> </p>
<p align="center"> <small>Figura 1: El cerebro y sus lóbulos superficiales con sus respectivas funciones (marcadas en rojo) [guia].</small> </p>


### Adquisición de un EEG
<p style="text-align: justify;">
Cinco sub-bandas de frecuencia definen las frecuencias de la señal EEG que pueden medirse desde el cerebro, siendo la gamma la más rápida y la delta la más lenta.
</p>

| **Tipo de onda** | **Ejemplo de señal** | **Frecuencia [Hz]** | **Ocurrencias** | 
|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| Gamma | ![image-removebg-preview](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/711645fe-308f-4b50-a757-aebb16bd0496) | >25 | Concentración, resolver problemas | 
| Beta | ![beta_onda](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/4a399e96-b010-4f05-b59a-1f9ce6d89211)
| 12-25 | Menta activa, ocupada | 
| Alpha | ![image-removebg-preview (1)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/4b370e03-9e30-4903-a378-c61d746da04a)
| 8-12 | Reflexiva, tranquila | 
| Theta | ![theta_onda](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/76a6d69f-e0d6-4ae4-a0e5-baf8bf54df5b)
| 4-12 | Somnolencia |
| Delta | ![image-removebg-preview (2)](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/45a9af16-12cd-4413-baa2-0a95c9d05dc3)
| 0-4 | Dormir, soñando |


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

En la figura 1 se observa la colocación de los electrodos en el usuario de prueba que se realiza conforme a la Guía de Inicio BITalino (r)evolution en casa para Electroencefalografía (EEG), diseñada para familiarizarse con las bioseñales específicas de EEG [guia]. En las siguientes imágenes se pueden observar las colocaciones electrodos-cuerpo para medir EEG en la posición FP1: pines de medición IN+/- (izquierda) y referencia (derecha) y las colocaciones BITalino-cables. En la figura 2 se observa la colocación del Ultracortex Mark IV en el usuario de prueba de acuerdo a lo indicado en sus instrucciones de uso [ultra].

</p>

<div align="center">

|  **Figura 1: Prueba con BITalino**  | **Figura 2: Prueba con Ultracortex** 
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
5. Detenga la grabación y guarde sus datos [guia].

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

## **Ploteo de la señal en Python** <a name="id7"></a> 

## **Ploteo de la señal en OpenBCI GUI** <a name="id8"></a> 

## **Resumen y explicación de la señal ploteada** <a name="id9"></a>

## **Archivo de los datos de la señal ploteada** <a name="id10"></a>

## **Códido del ploteo de la señal en Python** <a name="id11"></a>

## **Referencias** <a name="id12"></a>
[1] M. Proença and K. Mrotzeck, vol. 2021. BITalino (r)Evolution Lab Guide, Home Guide 2—EEG. Available at: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[2] “Ultracortex Mark IV | OpenBCI Documentation,” Openbci.com, Nov. 08, 2023. https://docs.openbci.com/AddOns/Headwear/MarkIV/#electrode-location-overview (accessed Apr. 27, 2024).
