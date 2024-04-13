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
6. [Resumen y explicación de la señal ploteada](#id6)
7. [Archivos](#id7)
8. [Ploteo de la señal en Python](#id8)

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

Se presenta el ploteo de los datos obtenidos por medio de los electrodos en OpenSignals.
### Ploteo del Usuario 1:
* En reposo:
   
![Rodrigo_Reposo](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/af4b6bd9-f27d-48ba-8d37-6bab68e4f9ae)
 
* Sin oposición:

![Rodrigo_SinOposicion](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/3a6bd5fd-b164-4500-9b26-f54753605719)

* Con oposición:

![Rodrigo_Oposicion](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/e204c362-a0ba-4119-ae41-a6f1fabea123)

### Ploteo del Usuario 2:
* En reposo:

![Adrian_Reposo](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/5045ebcb-3280-408c-a7a1-4c7187c812dd)

* Sin oposición:

![Adrian_SinOposicion](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/3239e1ec-42f5-48ef-ac5e-cdfe6482a8a4)

* Con oposición:

![Adrian_Oposicion](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/274cd343-fe7f-496f-aee9-e5fafb39eb84)

## **Resumen y explicación de la señal ploteada** <a name="id6"></a>

## **Archivos** <a name="id7"></a>

## **Ploteo de la señal en Python** <a name="id8"></a>
