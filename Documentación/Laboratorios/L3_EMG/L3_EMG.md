# Informe de Laboratorio 3: Uso de BiTalino para EMG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Objetivos](#id1)
2. [Materiales y equipos](#id2)
3. [Fotos de conexión usada](#id3)
4. [Videos de la señal](#id4)
5. [Ploteo de la señal en OpenSignals](#id5)
6. [Ploteo de la señal en python](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L3_EMG/L3_EMG.md#ploteo-de-la-se%C3%B1al-en-python-)
7. [Resumen y explicación de la señal ploteada](#id6)
8. [Archivo de los datos de la señal ploteada*](#id7)
9. [Códido del ploteo de la señal en Python*](#id8)

## **Objetivos** <a name="id1"></a>
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution

## **Materiales y equipos** <a name="id2"></a>
<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>

## **Fotos de conexión usada** <a name="id3"></a>
<p style="text-align: justify;">
La colocación de los electrodos en el usuario de prueba se realiza conforme a la Guía de Inicio BITalino (r)evolution en casa para Electromiografía (EMG), diseñada para familiarizarse con las bioseñales específicas de EMG. En las siguientes imágenes se pueden observar las colocaciones electrodos-cuerpo y BITalino-cables para ambos usuarios de prueba.
</p>

<div align="center">

|  **Usuario de prueba 1**  | **Usuario de prueba 2** 
|:------------:|:---------------:|
|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/9849a554-d809-40de-9e8d-308abb3c09d9" width="60%" height="60%"></p>|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/889464c0-1196-4a90-b079-ade899835728" width="60%" height="60%"></p>|

</div>

## **Videos de la señal** <a name="id4"></a>

### **Prueba con el usuario 1**
<div align="center">

|  **Brazo en reposo**  | **Brazo sin oposición** | **Brazo con oposición** |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/c48cd691-d667-4692-9030-7ede53738d74"></video>|<video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/6cb87eb8-0054-42f9-87e4-87107d94e3ac"></video>|<video src= "https://github.com/adri201022/ISB-Grupo-11/assets/164538327/18525324-c704-40bf-8e5a-506fb8970c49"></video>|

</div>

### **Prueba con el usuario 2**
<div align="center">

|  **Brazo en reposo**  | **Brazo sin oposición** | **Brazo con oposición** |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/6ececc85-96b9-4806-8a99-0acdefeb3112"></video>|<video src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/de2c7ee9-e73b-452b-b10b-cb37625330d8"></video>|<video src= "https://github.com/adri201022/ISB-Grupo-11/assets/164538327/b3042135-7c77-4097-a587-9714cbf989bc"></video>|

</div>

## **Ploteo de la señal en OpenSignals** <a name="id5"></a>

Se presentan los gráficos de los datos recopilados mediante el uso de BITalino y OpenSignals de cada uno de los usuarios, a través de los electrodos correspondientes.
### Gráficos del Usuario 1:
* En reposo:
  
<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/af4b6bd9-f27d-48ba-8d37-6bab68e4f9ae" width="700" height="350"> </p>
<p align="center"> <small>Figura 3: Ploteo de los datos en reposo.</small> </p>
 
* Sin oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/3a6bd5fd-b164-4500-9b26-f54753605719" width="700" height="350"> </p>
<p align="center"> <small>Figura 4: Ploteo de los datos sin oposición.</small> </p>
* Con oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/e204c362-a0ba-4119-ae41-a6f1fabea123" width="700" height="350"> </p>
<p align="center"> <small>Figura 5: Ploteo de los datos con oposición.</small> </p>

### Gráficos del Usuario 2:
* En reposo:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/5045ebcb-3280-408c-a7a1-4c7187c812dd" width="700" height="350"> </p>
<p align="center"> <small>Figura 6: Ploteo de los datos en reposo.</small> </p>

* Sin oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/3239e1ec-42f5-48ef-ac5e-cdfe6482a8a4" width="700" height="350"> </p>
<p align="center"> <small>Figura 7: Ploteo de los datos sin oposición.</small> </p>

* Con oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/274cd343-fe7f-496f-aee9-e5fafb39eb84" width="700" height="350"> </p>
<p align="center"> <small>Figura 8: Ploteo de los datos con oposición.</small> </p>

## **Ploteo de la señal en Python** <a name="id5"></a>
Se mostraran las gráficas obtenidas de python, algunas de las imágenes se le ha hecho zoom para que logre apreciar mejor la señal.
### Gráficos del Usuario 1:
* En reposo:
  
<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/2fe54a39-91d9-4557-9bc3-7e6eee0c6608" width="650" height="350"> 
<p align="center"> <small>Figura 3: Ploteo de los datos en reposo.</small> </p>
 
* Sin oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/453e8c5b-6fd2-4f14-a1c5-305d0a98ae46" width="650" height="350"> 
<p align="center"> <small>Figura 4: Ploteo de los datos sin oposición.</small> </p>
* Con oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/f47af37d-cd66-4fc1-a70b-ddc76afa7351" width="650" height="350"> </p>
<p align="center"> <small>Figura 5: Ploteo de los datos con oposición.</small> </p>

### Gráficos del Usuario 2:
* En reposo:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/daff1997-6c1e-4134-8f28-17facd22859f" width="650" height="350"> </p>
<p align="center"> <small>Figura 6: Ploteo de los datos en reposo.</small> </p>

* Sin oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/58460092-705b-4b59-8f98-3385a113a702" width="650" height="350"> </p>
<p align="center"> <small>Figura 7: Ploteo de los datos sin oposición.</small> </p>


* Con oposición:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/1c8a982f-2026-4f30-af7b-7aaa905aaeac" width="650" height="350"> </p>
<p align="center"> <small>Figura 8: Ploteo de los datos con oposición.</small> </p>

## **Resumen y explicación de la señal ploteada** <a name="id6"></a>
### Técnica del estudio de conducción nerviosa motora del nervio mediano en el músculo bíceps braquial:

#### Electrodos de registro:
Se hicieron uso de 3 electrodos (G1, G2 y tierra)

- Electrodo activo (G1): Se coloca sobre el vientre muscular del músculo bíceps braquial (posición anterior), aproximadamente a una tercera parte de la distancia entre el pliegue del codo y el acromion (hueso del hombro). 

- Electrodo de referencia (G2): Se sitúa en un punto cercano al electrodo activo G1, en el mismo músculo bíceps braquial, pero un poco más distal del codo siguiendo la posición del mismo eje que la del electrodo G1.

- Electrodo tierra: Colocado en una ubicación neutral en la zona posterior del antebrazo, alejado del hueso del carpo (hueso pisiforme), para proporcionar una referencia común para las mediciones así como evitar posibles interferencias en la medición.

#### Mediciones:

Se registran y analizan las siguientes mediciones:

- Distancias: Se miden las distancias entre los puntos de estimulación (G1 y G2) para calcular la longitud del segmento de conducción nerviosa.

- Latencias: Se registran los tiempos transcurridos desde la estimulación hasta la aparición de la respuesta muscular, tanto en el punto distal como en el proximal.

- Amplitudes: Se mide la magnitud de la respuesta muscular registrada por los electrodos, lo que proporciona información sobre la integridad de la conducción nerviosa.

- Velocidad de conducción: Se calcula la velocidad de conducción nerviosa entre los puntos de estimulación distal y proximal, lo que indica la eficiencia con la que el impulso nervioso se transmite a lo largo del nervio mediano en el segmento evaluado.

### Explicación de la señal ploteada:
#### Del usuario 1:
##### En reposo:
Se observa una gráfica casi lineal donde las amplitudes de los picos son bajas, esto por el ruido que se puede estar detectando, no se observa ningún estímulo en reposo.
##### Sin oposición:
Se observa una gráfica con algunos intervalos de amplitud, esto corresponde al estímulo que se genera en el músculo por el propio peso del brazo que al levantarse o comenzar a levantarlo se generarlo
##### Con oposición:
Se observa una gráfica con varios picos de amplitud, en el 1er caso la fuerza de oposición fue bastante por lo que se necesitó mucho esfuerzo para levantar el brazo y ahí en ese forcejeo se producieron varios picos altos y por el tambaleo del movimiento hubo un poco de contaminación en la señal

#### Del usuario 2:
##### En reposo:
Se observa una gráfica casi lineal donde las amplitudes de los picos son bajas, esto por el ruido que se puede estar detectando, no se observa ningún estímulo en reposo. No se presentan diferencias respecto al usuario 1
##### Sin oposición:
Se observa una gráfica con algunos intervalos de amplitud, esto corresponde al estímulo que se genera en el músculo por el propio peso del brazo que al levantarse o comenzar a levantarlo se generarlo, en este caso el peso del brazo es menor por lo que se emplea una menor fuerza que se ve reflejado en picos de amplitud ligeramente menores
##### Con oposición:
Se observa una gráfica con varios picos de amplitud, en el 1er caso la fuerza de oposición fue bastante por lo que se necesitó mucho esfuerzo para levantar el brazo; sin embargo, en este caso el brazo quedó un poco inmovilizado por la fuerza de oposición lo que impidió al músculo estar en una posición adecuada para ejercer la mayor fuerza

## **Archivo de los datos de la señal ploteada** <a name="id7"></a>
* [Datos de las pruebas de EMG (.txt)](https://github.com/adri201022/ISB-Grupo-11/tree/main/Documentaci%C3%B3n/Laboratorios/L3_EMG/EMG_data)

## **Códido del ploteo de la señal en Python** <a name="id8"></a>
* [Código del ploteo en python (.py)](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L3_EMG/Ploteo%20de%20se%C3%B1ales%20en%20python.py)
