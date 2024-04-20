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
La colocación de los electrodos en el usuario de prueba se realiza conforme a la Guía de Inicio BITalino (r)evolution en casa para Electrocardiografía (ECG), diseñada para familiarizarse con las bioseñales específicas de ECG. En las siguientes imágenes se pueden observar las colocaciones electrodos-cuerpo y BITalino-cables, al igual que electrodos-simulador.
</p>

<div align="center">

|  **Prueba con usuario**  | **Prueba con simulador de paro cardíaco** 
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
<p align="center"> <small>Figura 3: Ploteo de los datos en reposo.</small> </p>

* Durante respiraciones rápidas:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/53855182-b069-4fb8-abd2-af3e96019c27" width="700" height="350"> </p>
<p align="center"> <small>Figura 4: Ploteo de los datos durante respiraciones rápidas.</small> </p>

* Durante actividad física:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/8940821e-8eb5-408f-89b8-9582e3474791" width="700" height="350"> </p>
<p align="center"> <small>Figura 5: Ploteo de los datos durante actividad física.</small> </p>

* Despues de actividad física:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/579accd9-b6ea-4540-99f9-23cd08f1ebe9" width="700" height="350"> </p>
<p align="center"> <small>Figura 6: Ploteo de los datos despues de actividad física.</small> </p>

### Simulación de paro cardíaco
* CVP:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/c483d4c0-6a30-41af-b52c-e86847b17718" width="700" height="350"> </p>
<p align="center"> <small>Figura 7: Ploteo de los datos durante CVP.</small> </p>

* Taquicardia ventricular:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/b710cdcd-befa-4c41-9abc-b3fbb7cf95ee" width="700" height="350"> </p>
<p align="center"> <small>Figura 8: Ploteo de los datos durante taquicardia ventricular.</small> </p>

* Fibrilacion auricular:

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/e844e987-2361-4d3e-8e15-76cbf404625a" width="700" height="350"> </p>
<p align="center"> <small>Figura 9: Ploteo de los datos durante fibrilación auricular.</small> </p>

* Asistolia

<p align="center"><img src="https://github.com/adri201022/ISB-Grupo-11/assets/100977549/558dfba9-42a2-4728-8add-3f933c024d2c" width="700" height="350"> </p>
<p align="center"> <small>Figura 10: Ploteo de los datos durante asistolia.</small> </p>

## **Ploteo de la señal en Python** <a name="id7"></a>


## **Resumen y explicación de la señal ploteada** <a name="id8"></a>


## **Archivo de los datos de la señal ploteada** <a name="id9"></a>

* [Datos de las pruebas de ECG (.txt)](https://github.com/adri201022/ISB-Grupo-11/tree/main/Documentación/Laboratorios/L4_ECG/ECG_data)

## **Códido del ploteo de la señal en Python** <a name="id10"></a>


## **Referencias** <a name="id11"></a>
