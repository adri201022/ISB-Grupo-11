# Laboratorio N°2 - Adquisión de señales y graficación en Arduino

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Objetivos específicos de la práctica
- Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
- Entender los criterios de selección de la frecuencia de muestreo.
- Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital;
Generador de señales y osciloscopio digital.

## Materiales y equipos

| Modelo | Descripción | Cantidad |
|:---------:|:---------:|:---------:|
| AFG1022      | Generador de señales      | 1      |
| TBS 1000C Series      | Osciloscopio digital      | 1     |
| -      | Cable BNC Male-Male      | 1      |
| -      | Punta de osciloscopio con conector BNC (Male)      | 1     |
| -      | Par de cables Male-Male      | 1     |
| SAMD    | Arduino 33 IoT     | 1     |

## Entregables
- Plotear al menos 3 señales en Arduino IDE provenientes del generador de señales.
- Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio.
## Fundamentos teóricos
   Para realizar el laboratorio correctamente se necesitaron conocimientos previos sobre la utilización de las herramientas mencionadas: Arduino, osciloscopio y genereador de ondas. Se explicará una descripción de conocimientos requeridos para usar estas herramientas.
   1.  Arduino nano 33 IoT:      
Es una placa de desarrollo compacta que esta basada en el microcontrolador ARM Cortex-M0+SAMD21 de 32 bits. Es una versió mejorada del calisco arduino nano que esta diseñada para proyectos de internet de las cosas (IoT). Además incorpora un módulo WI-FI y Bluetooth que permite la conexión inalambrica a redes locales y dispsitivos periféricos compatibles y cuenta con una diversa compatibiliadad con bibliotecas y herramientas de desarrollo para facilitar la creación de proyectos de IoT, como sería la integración con plataformas en la nube y servicios web.
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/2ec973ba-647f-40cb-87c0-01291fca391b"   width="50%">
  
   2.  Generador de Señales:
Es un instrumento que proporciona señales electricas. Se utiliza para poder obtener señales peridodicas controlando su periodo y su amplitud. Además de las ondas básicas como senoidal, cuadrada y triangular algunos generar ondas más complejas como rampa, puslo, diente de sierra, etc. Los controladores de señales tambien puede permitir ajustar la frecuencia de salida de manera precisa y en un amplio rango, desde frecuencias muy bajas hasta radiofrecuencia.
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/32ad1541-c87c-4f62-8dcb-3d1ac2932978"   width="50%">

   3.  Osciloscopio digital:
El osciloscopo es un instrumento de medición que es utilizado en el campo de electónica. Su función principal es representar graficamente señales electricas variables en el tiempo. Esta se ve representada en una pantalla donde el eje horizontal es el eje X, representa el tiempo, mientras que el eje vertical es el eje Y, representa la amplitud.
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/e376781c-009e-424a-aca7-eaa4da1855bf"   width="50%">

## Gráficas de señales obtenidas del osciloscopio
 El procedimiento que realizamos fue el siguiente:
 * Configuramos el generador de señales para poder obtener una señal sinusoidal de 1KHz de frecuencia con un voltaje pico-pico de 3.3V y y 1.5 V de offset, en en canal 1.
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/b202d4e7-0a91-453f-85fd-a7a8f00b2f81"   width="50%">

* Se procedió a colocar el cable BNC male - male entre el osciloscopio digital y el generador de señales, se hizo esto para poder observar en el osciloscopio digital que lso fatos colocados y la ubicación de la onda sea correcta.
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/9d761c48-99e8-454a-b9c0-ef11adfb6951"   width="50%">

* Una vez configruados eso procedimos a generar las señales en el osciloscopio digital con distintas frecuencias.

  - 1 KHz
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/c117a0cb-f5c1-471b-9aaf-94fc2da81253"   width="50%">
  
   - 100 Hz:
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/8f19fdeb-f78a-434e-95e8-b19dbbf8d556"   width="50%">   
  
   - 500 Hz
 
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/dce2dd66-3c01-43bc-a72b-af669f5e88ce"   width="50%">

   
## Ploteo de señales en Arduino
