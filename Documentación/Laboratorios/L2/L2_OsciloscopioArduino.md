# Laboratorio N°2 - Adquisión de señales y graficación en Arduino

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)
### Tabla de contenidos
1. [Objetivos específicos de la práctica](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#1-objetivos-de-la-pr%C3%A1ctica-de-laboratorio)
2. [Materiales y equipos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#2-fotos-de-las-conexiones-usadas)
3. [Entregables](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#3-video-de-se%C3%B1al-en-silencio-el%C3%A9ctrico-o-reposo)
4. [Fundamentos teóricos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#4-imagen-del-emg-obtenido-en-python)
5. [Gráficas de señales obtenidas del osciloscopio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#5-imagen-del-emg-obtenido-en-open-signals)
6. [Ploteo de señales en Arduino](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#6-resumen-y-explicaci%C3%B3n)
7. [Comparasión entre lás gráficas obtenidas del Arduino IDE y las gráficas obtenidas del osciloscopio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#7-archivo-de-la-se%C3%B1al-ploteada-en-python-y-de-los-datos-de-la-se%C3%B1al-ploteada)
8. [Archivo de la señal ploteada en Arduino IDE](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L3_Uso%20de%20BiTalino%20para%20EMG/L3.md#7-archivo-de-la-se%C3%B1al-ploteada-en-python-y-de-los-datos-de-la-se%C3%B1al-ploteada)

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
* Ahora procederemos a mostrar las señales ploteadas en el Arduino IDE que vienen provenientes de nuestro generador de señales, mostraremos como salen las gráficas a 500 hz en sus formas sinusoidal, cuadrada y triangular. Además que como se ven cuando estas se les coloca un condesador como un filtro.
  
  - 500 Hz sinusoidal (sin capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/a5ed9fa2-a4c7-4629-876c-890b1d637935"   width="50%">
  
  - 500 Hz sinusoidal (con capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/a5a22e3f-d7a4-4fd8-b9f1-b8e899f76db4"   width="50%">
   
  - 500 Hz cuadrangular (sin capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/5f2f3eb4-0ca8-41ff-8877-de5fdd9e74a0"   width="50%"> 
   
  - 500 Hz cuadrangular (con capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/055af7c0-a590-421d-a9e3-6d08ccdf8b00"   width="50%">

  - 500 Hz triangular (sin capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/7ee717fd-1779-400c-a301-038d74cadeca"   width="50%">

  - 500 Hz triangular (con capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/7ec57c7b-699c-41e0-bd8a-49c1fdfe509e"   width="50%">

Como se lográ observar cuando no se presenta un capacitor para que filtre el ruido, las señales que se muestran en el ploteo se asemejan a las formas de ondas que se desean , pero cuando se coloca el capacitor esas señales con las formas de ondas deseadas desaparecen y se empieza a formar como una señal erratica, pero esto en teoria no debería suceder ya que con el filtrado las gráficas se deberian ver mejor. Esto se debe al valor del capacitor que se esta usando el cual es de 470 uF, ya que cuando se utiliza un capacitor para filtrar la señal es necesario toamr en cuenta la constante de tiempo del circuito RC. Como en nuestro caso estamos usando un capacitor de 470 uF y una frecuencia de 500 Hz, nosotros debimos habe elegido uan resistencia adecuada en serie con el capacitor, ya que si la resistencua es demasiado baja nuestra constente de tiempo sera muy pequeña y por ende el capacitor no tendra el tiempo suficiente para poder cargar o descargar completamente entre los ciclos de la señal de entrada y esto genera que la señal filtrasa sea distorsionada. En nuestro caso no usamos ninguna resistencia en paralelo por lo cual tuvimos ese error. A continuación les mostraremos el cálculo del valor de resistencia aproximado que se debio colocar.

## Comparasión entre lás gráficas obtenidas del Arduino IDE y las gráficas obtenidas del osciloscopio:
   - 500 Hz
 
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/dce2dd66-3c01-43bc-a72b-af669f5e88ce"   width="50%">

  - 500 Hz sinusoidal (sin capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/a5ed9fa2-a4c7-4629-876c-890b1d637935"   width="50%">

Como se logra observar cuando la señal graficada del Arduino IDE no tiene el capacitor esta se asemeja mucho a la señal dada por el osciloscopio, no es del todo igual pero si mantiene una forma sinusoidal, si se colocará un capacitor correcto el filtrado lograría que  la señal graficada por el Arduino IDE sea casi identica a la del osciloscopio, pero como se contó un capacitor erróneo y no colocó una resistencia correcta es que se puede obervar que cuando se cuenta con este capacitor la señal se distorsiona y no se asemeja a nada a la señal del osciloscopio.

## Archivo de la señal ploteada en Arduino IDE
- [Señal ploteada en Arduino IDE](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/codelab2.ino)



