# Informe de Laboratorio 4: Uso de BiTalino para ECG

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
8. [Resumen y explicación de la señal ploteada](#id8)
9. [Archivo de los datos de la señal ploteada](#id9)
10. [Códido del ploteo de la señal en Python](#id10)
11. [Referencias](#id11)

## **Introducción** <a name="id1"></a>

### Una visión fisiológica del corazón
<p style="text-align: justify;">
  
El corazón realiza dos funciones principales: bombea sangre rica en oxígeno desde la aurícula izquierda hasta la aorta y el resto del cuerpo, y bombea sangre pobre en oxígeno desde la aurícula derecha hacia los pulmones. Estas acciones se deben a las contracciones regulares y repetitivas del músculo cardíaco, que son generadas por señales eléctricas conocidas como potenciales de acción. La actividad eléctrica del corazón comienza en el nódulo sinoauricular (SA), ubicado en la aurícula derecha, también llamado marcapasos del corazón. Desde aquí, las señales se propagan al nódulo atrioventricular (AV) y luego a través de las ramas del haz de His y las fibras de Purkinje, lo que permite la activación coordinada de las células ventriculares para bombear sangre eficientemente [1]. 

</p>

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/00483b35-750f-4cef-a4b2-3d545925a5cf" width="400" height="300"> </p>
<p align="center"> <small>Figura 1: Ciclo cardíaco: Zonas del corazón [2].</small> </p>

<p style="text-align: justify;">
  
El ciclo cardíaco incluye dos fases principales: la diástole, en la que las cámaras cardíacas se llenan de sangre, y la sístole, durante la cual se contraen las cámaras cardíacas para bombear la sangre fuera del corazón. Durante este proceso, se generan cambios eléctricos que pueden ser detectados en la superficie de la piel mediante un electrocardiograma (ECG). Cada parte del corazón tiene tiempos específicos para la excitación y propagación de las señales eléctricas, lo que influye en los patrones observados en el ECG [3].
  
</p>

### Adquisición de un ECG
Cuando una onda de despolarización se desplaza hacia un electrodo, se registra como una elevación positiva, mientras que cuando se aleja, se registra como una deflexión negativa. La amplitud de una onda se refiere a la magnitud de esta deflexión, medida en milímetros. Un electrocardiograma (ECG) básico incluye seis derivaciones primarias, obtenidas con electrodos en los brazos y las piernas. Las derivaciones cardíacas registran la diferencia de potencial eléctrico entre dos puntos, ya sea entre dos electrodos (derivaciones bipolares) o entre un punto virtual y un electrodo (derivaciones monopolares). Las derivaciones bipolares incluyen I(brazo derecho–brazo izquierdo), II(brazo derecho–pierna izquierda) y III(pierna izquierda–brazo izquierdo), que forman el triángulo de Einthoven. Según la Ley de Einthoven, la suma de las derivaciones II y III es igual a la derivación I. Las derivaciones unipolares incluyen aVR(brazo derecho), aVL(brazo izquierdo) y aVF(pierna izquierda), que parten de un electrodo positivo central hacia los extremos. Estas derivaciones amplifican el voltaje de las extremidades. Finalmente, las derivaciones precordiales incluyen V1 a V6, ubicadas en puntos específicos del tórax para registrar la actividad eléctrica del corazón desde diferentes ángulos [4].

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/f09c100a-3ac1-47a6-ab35-cef6be7e55ce" width="400" height="300"> </p>
<p align="center"> <small>Figura 2: Los sitios de colocación estándar para las derivaciones precordiales [4].</small> </p>

### Aplicaciones
<p style="text-align: justify;">
  
En el contexto de las aplicaciones médicas, la señal del electrocardiograma (ECG) juega un papel crucial en la identificación de anomalías, como la elevación del segmento ST, donde la señal no regresa a su línea base después del complejo QRS. Esta observación nos proporciona indicios sobre posibles obstrucciones en el suministro de oxígeno a los tejidos del corazón, lo que podría desencadenar un ataque cardíaco. Otro factor relevante es la variabilidad de la frecuencia cardíaca (VFC), ya que puede ofrecer información sobre la salud general del corazón y puede evaluarse mediante el análisis de los intervalos entre los picos R [2].

</p>

## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino
- Extraer la información de las señales ECG del software OpenSignals (r)evolution

## **Materiales y equipos** <a name="id3"></a>
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |
| Fluke Biomedical ProSim 4 | Vital Signs Simulator | 1 |

</div>

## **Fotos de conexión usada** <a name="id4"></a>
<p style="text-align: justify;">
  
La colocación de los electrodos en el usuario de prueba se realiza conforme a la Guía de Inicio BITalino (r)evolution en casa para Electrocardiografía (ECG), diseñada para familiarizarse con las bioseñales específicas de ECG [2]. En las siguientes imágenes se pueden observar las colocaciones electrodos-cuerpo para la derivación I: IN+(rojo) & IN-(negro) en las muñecas y REF(blanco) en la cresta ilíaca. Adicionalmente, se observan las colocaciones BITalino-cables, al igual que electrodos-simulador.

</p>

<div align="center">

|  **Figura 3: Prueba con usuario**  | **Figura 4: Prueba con simulador de paro cardíaco** 
|:------------:|:---------------:|
|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/925752c6-bd24-4f0f-a469-47593b03ce60" width="60%" height="60%"></p>|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/9c875430-87de-4aeb-b7bb-d25da83601b4" width="60%" height="60%"></p>|

</div>

## **Videos de la señal** <a name="id5"></a>

### **Prueba con usuario**
<div align="center">

| **Antes de actividad (reposo)** | **Durante respiraciones rápidas** | **Durante actividad física** | **Después de actividad física** |
|:--------------------------------:|:---------------------------------:|:----------------------------:|:--------------------------------:|
| <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/5e95f0c3-f1d3-41bc-9e2d-58d7d24cf8b4"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/5d88b39e-38da-43da-a8d6-4046aef8e5ed"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/633e99b8-0350-4416-a4f2-8daf8bea16ef"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/03ed0916-50cb-4b50-b88d-55b8196b068e"></video> |

</div>

### **Prueba con simulador de paro cardíaco**
<div align="center">

|  **CVP (VI)**  | **Taq. vent. 160 lpm** | **Fib. vent. severa** | **Asistolia** |
|:------------:|:---------------:|:------------:|:------------:|
| <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/6635b400-6426-44e2-ae86-d348da1f3887"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/a48faa9a-92a5-4887-b891-336287c95599"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/d2614676-a40e-4211-8260-6377a6172635"></video> | <video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/9eec286f-0f4e-4b33-a9e2-5221e1e80f8c"></video> |

</div>

## **Ploteo de la señal en OpenSignals** <a name="id6"></a>
En esta sección presentaremos los gráficos de los datos recopilados mediante el uso de BITalino y OpenSignals.

* Antes de actividad (reposo):

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/0640e803-0752-4684-b347-e05737b1e874" width="700" height="350"> </p>
<p align="center"> <small>Figura 5: Ploteo de los datos en reposo.</small> </p>

* Durante respiraciones rápidas:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/53855182-b069-4fb8-abd2-af3e96019c27" width="700" height="350"> </p>
<p align="center"> <small>Figura 6: Ploteo de los datos durante respiraciones rápidas.</small> </p>

* Durante actividad física:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/8940821e-8eb5-408f-89b8-9582e3474791" width="700" height="350"> </p>
<p align="center"> <small>Figura 7: Ploteo de los datos durante actividad física.</small> </p>

* Despues de actividad física:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/579accd9-b6ea-4540-99f9-23cd08f1ebe9" width="700" height="350"> </p>
<p align="center"> <small>Figura 8: Ploteo de los datos despues de actividad física.</small> </p>

### Simulación de paro cardíaco
* CVP:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/c483d4c0-6a30-41af-b52c-e86847b17718" width="700" height="350"> </p>
<p align="center"> <small>Figura 9: Ploteo de los datos durante CVP.</small> </p>

* Taquicardia ventricular:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/b710cdcd-befa-4c41-9abc-b3fbb7cf95ee" width="700" height="350"> </p>
<p align="center"> <small>Figura 10: Ploteo de los datos durante taquicardia ventricular.</small> </p>

* Fibrilacion auricular:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/e844e987-2361-4d3e-8e15-76cbf404625a" width="700" height="350"> </p>
<p align="center"> <small>Figura 11: Ploteo de los datos durante fibrilación auricular.</small> </p>

* Asistolia

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/558dfba9-42a2-4728-8add-3f933c024d2c" width="700" height="350"> </p>
<p align="center"> <small>Figura 12: Ploteo de los datos durante asistolia.</small> </p>

## **Ploteo de la señal en Python** <a name="id7"></a>


## **Resumen y explicación de la señal ploteada** <a name="id8"></a>


## **Archivo de los datos de la señal ploteada** <a name="id9"></a>

* [Datos de las pruebas de ECG (.txt)](https://github.com/adri201022/ISB-Grupo-11/tree/main/Documentación/Laboratorios/L4_ECG/ECG_data)

## **Códido del ploteo de la señal en Python** <a name="id10"></a>


## **Referencias** <a name="id11"></a>
[1] R. Rhoades and D. R. Bell, Eds., Medical Physiology: Principles for Clinical Medicine, 6th ed, R. A. Rhoades and D. R. Bell, Eds. Lippincott Williams & Wilkins, 2022.

[2] M. Proença and K. Mrotzeck, vol. 2021. BITalino (r)Evolution Lab Guide, Home Guide 2—ECG. Available at: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

[3] J. G. Betts et al., 2013. Anatomy and Physiology. Houston, Texas: OpenStax. Available at: https://openstax.org/books/anatomy-and-physiology/pages/1-introduction

[4] E. A. Ashley and J. Niebauer. Chapter 3, Conquering the ECG, Cardiology Explained. London: Remedica, 2004. Available at: https://www.ncbi.nlm.nih.gov/books/NBK2214/
