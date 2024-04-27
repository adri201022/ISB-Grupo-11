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
  

</p>

<p align="center"><img src="" width="400" height="300"> </p>
<p align="center"> <small>Figura 1: .</small> </p>


### Adquisición de un EEG
<p style="text-align: justify;">
  

</p>


### Aplicaciones
<p style="text-align: justify;">
  

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

En la figura 1 se observa la colocación de los electrodos en el usuario de prueba que se realiza conforme a la Guía de Inicio BITalino (r)evolution en casa para Electroencefalografía (EEG), diseñada para familiarizarse con las bioseñales específicas de EEG [1]. En las siguientes imágenes se pueden observar las colocaciones electrodos-cuerpo para medir EEG en la posición FP1: pines de medición IN+/- (izquierda) y referencia (derecha) y las colocaciones BITalino-cables. En la figura 2 se observa la colocación del Ultracortex Mark IV en el usuario de prueba de acuerdo a lo indicado en sus instrucciones de uso [2].

</p>

<div align="center">

|  **Figura 1: Prueba con BITalino**  | **Figura 2: Prueba con Ultracortex** 
|:------------:|:---------------:|
|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/3ead35b7-7858-4e3b-bdb1-3955c5cfe5af" width="60%" height="60%"></p>|<p><img src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/3bb20da0-a6af-4bb9-8937-844391850a27" width="60%" height="60%"></p>|

</div>

## **Videos de la señal** <a name="id5"></a>

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
