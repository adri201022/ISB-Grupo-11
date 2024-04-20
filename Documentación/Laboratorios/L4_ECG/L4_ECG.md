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


## **Ploteo de la señal en Python** <a name="id7"></a>


## **Resumen y explicación de la señal ploteada** <a name="id8"></a>


## **Archivo de los datos de la señal ploteada** <a name="id9"></a>


## **Códido del ploteo de la señal en Python** <a name="id10"></a>


## **Referencias** <a name="id11"></a>
