# Laboratorio N°2 - Adquisión de señales y graficación en Arduino

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)
### Tabla de contenidos
1. [Objetivos específicos de la práctica](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#1-objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
2. [Materiales y equipos](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#2-materiales-y-equipos)
3. [Entregables](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#3-entregables)
4. [Fundamentos teóricos](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#4-fundamentos-te%C3%B3ricos)
5. [Gráficas de señales obtenidas del osciloscopio](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#5-gr%C3%A1ficas-de-se%C3%B1ales-obtenidas-del-osciloscopio)
6. [Ploteo de señales en Arduino](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#6-ploteo-de-se%C3%B1ales-en-arduino)
7. [Comparasión entre lás gráficas obtenidas del Arduino IDE y las gráficas obtenidas del osciloscopio](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#7-comparasi%C3%B3n-entre-las-gr%C3%A1ficas-obtenidas-del-arduino-ide-y-las-gr%C3%A1ficas-obtenidas-del-osciloscopio)
8. [Archivo de la señal ploteada en Arduino IDE](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#8-archivo-de-la-se%C3%B1al-ploteada-en-arduino-ide)
9. [Referencias bibliográficas](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/L2_OsciloscopioArduino.md#9-referencias-bibliogr%C3%A1ficas)

## 1. Objetivos específicos de la práctica
- Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
- Entender los criterios de selección de la frecuencia de muestreo.
- Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital;
Generador de señales y osciloscopio digital.

## 2. Materiales y equipos

| Modelo | Descripción | Cantidad |
|:---------:|:---------:|:---------:|
| AFG1022      | Generador de señales      | 1      |
| TBS 1000C Series      | Osciloscopio digital      | 1     |
| -      | Cable BNC Male-Male      | 1      |
| -      | Punta de osciloscopio con conector BNC (Male)      | 1     |
| -      | Par de cables Male-Male      | 1     |
| SAMD    | Arduino 33 IoT     | 1     |

## 3. Entregables
- Plotear al menos 3 señales en Arduino IDE provenientes del generador de señales.
- Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio.
## 4. Fundamentos teóricos
   Para realizar el laboratorio correctamente se necesitaron conocimientos previos sobre la utilización de las herramientas mencionadas: Arduino, osciloscopio y genereador de ondas. Se explicará una descripción de conocimientos requeridos para usar estas herramientas.
   1.  Arduino nano 33 IoT:      
Es una placa de desarrollo compacta que esta basada en el microcontrolador ARM Cortex-M0+SAMD21 de 32 bits. Es una versió mejorada del calisco arduino nano que esta diseñada para proyectos de internet de las cosas (IoT). Además incorpora un módulo WI-FI y Bluetooth que permite la conexión inalambrica a redes locales y dispsitivos periféricos compatibles y cuenta con una diversa compatibiliadad con bibliotecas y herramientas de desarrollo para facilitar la creación de proyectos de IoT, como sería la integración con plataformas en la nube y servicios web. [1]
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/2ec973ba-647f-40cb-87c0-01291fca391b"   width="50%">
<p align="center"><small>Figura 1: Arduino nano 33 IoT. [1]</small></p>


   2.  Generador de Señales:
Es un instrumento que proporciona señales electricas. Se utiliza para poder obtener señales peridodicas controlando su periodo y su amplitud. Además de las ondas básicas como senoidal, cuadrada y triangular algunos generar ondas más complejas como rampa, puslo, diente de sierra, etc. Los controladores de señales tambien puede permitir ajustar la frecuencia de salida de manera precisa y en un amplio rango, desde frecuencias muy bajas hasta radiofrecuencia. [2]
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/32ad1541-c87c-4f62-8dcb-3d1ac2932978"   width="50%">
<p align="center"><small>Figura 2: Generador de señales. [3]</small></p>

   3.  Osciloscopio digital:
El osciloscopo es un instrumento de medición que es utilizado en el campo de electónica. Su función principal es representar graficamente señales electricas variables en el tiempo. Esta se ve representada en una pantalla donde el eje horizontal es el eje X, representa el tiempo, mientras que el eje vertical es el eje Y, representa la amplitud. [4]
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/e376781c-009e-424a-aca7-eaa4da1855bf"   width="50%">
<p align="center"><small>Figura 3: Osciloscopio digital. [5]</small></p>

## 5. Gráficas de señales obtenidas del osciloscopio
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

   
## 6. Ploteo de señales en Arduino
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

Como se lográ observar cuando no se presenta un capacitor para que filtre el ruido, las señales que se muestran en el ploteo se asemejan a las formas de ondas que se desean , pero cuando se coloca el capacitor esas señales con las formas de ondas deseadas desaparecen y se empieza a formar como una señal erratica, pero esto en teoria no debería suceder ya que con el filtrado las gráficas se deberian ver mejor. Esto se debe al valor del capacitor que se esta usando el cual es de 470 uF, ya que cuando se utiliza un capacitor para filtrar la señal es necesario tomar en cuenta la constante de tiempo del circuito RC. Como en nuestro caso estamos usando un capacitor de 470 uF y una frecuencia de 500 Hz, nosotros debimos haber elegido una resistencia adecuada en serie con el capacitor, ya que si la resistencua es demasiado baja nuestra constente de tiempo sera muy pequeña y por ende el capacitor no tendra el tiempo suficiente para poder cargar o descargar completamente entre los ciclos de la señal de entrada y esto genera que la señal filtrasa sea distorsionada. En nuestro caso no usamos ninguna resistencia en paralelo por lo cual tuvimos ese error [6]. A continuación les mostraremos el cálculo del valor de resistencia aproximado que se debio colocar.

<p align="center">
<img src="Documentación/Material_adicional/Frecuencia de corte.png">
<p align="center"><small>Figura x: Fórmula [x]</small></p>

De la fórmula tenemos el valor de C, el valor de fc lo vamos a estimar de acuerdo a las diferentes mediciones realizadas en el laboratorio

## 7. Comparasión entre las gráficas obtenidas del Arduino IDE y las gráficas obtenidas del osciloscopio:
   - 500 Hz
 
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/dce2dd66-3c01-43bc-a72b-af669f5e88ce"   width="50%">

  - 500 Hz sinusoidal (sin capacitor) :
<p align="center">
<img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/a5ed9fa2-a4c7-4629-876c-890b1d637935"   width="50%">

Como se logra observar cuando la señal graficada del Arduino IDE no tiene el capacitor esta se asemeja mucho a la señal dada por el osciloscopio, no es del todo igual pero si mantiene una forma sinusoidal, si se colocará un capacitor correcto el filtrado lograría que  la señal graficada por el Arduino IDE sea casi identica a la del osciloscopio, pero como se contó un capacitor erróneo y no colocó una resistencia correcta es que se puede obervar que cuando se cuenta con este capacitor la señal se distorsiona y no se asemeja a nada a la señal del osciloscopio.

## 8. Archivo de la señal ploteada en Arduino IDE
- [Señal ploteada en Arduino IDE](https://github.com/adri201022/ISB-Grupo-11/blob/main/Documentaci%C3%B3n/Laboratorios/L2/codelab2.ino)

## 9. Referencias bibliográficas

[1] «Nano 33 IoT», Arduino. Disponible en: https://docs.arduino.cc/hardware/nano-33-iot/. [Accedido: 5 de abril de 2024]

[2] Javired, «Qué es un generador de señales: funcionamiento y sus aplicaciones», Electrositio, 23 de julio de 2022. Disponible en: https://electrositio.com/que-es-un-generador-de-senales-funcionamiento-y-sus-aplicaciones/. [Accedido: 5 de abril de 2024]

[3] «Generadores De Señales», Mapa Conceptual, 29 de abril de 2020. Disponible en: https://www.mapa-conceptual.net/generadores-de-senales/

[4] «Osciloscopio», Ingenierizando, 10 de octubre de 2022. Disponible en: https://www.ingenierizando.com/laboratorio/osciloscopio/. [Accedido: 5 de abril de 2024]


[5] «GW Instek GDS-2304A - Osciloscopio digital de banco 300 MHz», Cedesa. Disponible en: https://www.cedesa.com.mx/gw-instek/osciloscopios/digitales/GDS-2304A/. [Accedido: 5 de abril de 2024]

[6] «Filtro por condensador», Cienciasfera. Disponible en: https://cienciasfera.com/materiales/electrotecnia/tema20/4_filtro_por_condensador.html#:~:text=El%20condensador%20se%20cargar%C3%A1%20mientras%20la%20tensi%C3%B3n%20de,que%20volver%C3%A1%20a%20cargarse%20y%20repetir%20el%20ciclo. [Accedido: 5 de abril de 2024]




