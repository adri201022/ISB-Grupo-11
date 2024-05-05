# Informe de Laboratorio 6: Filtrado de señales EMG, ECG y EEG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Filtros de señal EMG](#id3)
4. [Filtros de señal ECG](#id4)
5. [Filtros de señal EEG](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>
Los filtros digitales son un componente crucial en el procesamiento de señales biomédicas, ya que permiten eliminar el ruido, realzar características específicas y mejorar la calidad de las señales en diversas aplicaciones biomédicas como la electrocardiografía (ECG), la electromiografía (EMG) y la electroencefalografía (EEG) [1]. Los filtros se pueden clasificar de diversas maneras según sus características, como su comportamiento en el tiempo, su tipo de implementación (analógico o digital), y su respuesta al impulso (infinita o finita). Los filtros recursivos, también conocidos como IIR, utilizan conexiones de retroalimentación para lograr su función, mientras que los filtros FIR se basan en una respuesta al impulso de duración finita y no tienen retroalimentación. Estas diferencias en la estructura y el comportamiento hacen que cada tipo de filtro sea adecuado para diferentes aplicaciones [2].

### Filtros FIR
Esta sección se centra en los filtros de Respuesta Finita al Impulso (FIR). Un filtro FIR se construye con multiplicadores y sumadores, pudiendo ser implementado en hardware o software y ejecutarse en serie, paralelo o una combinación de ambos. Utiliza elementos de retardo, representados por registros con reloj, cruciales en el procesamiento de señales, y se denotan con el símbolo z1 en DSP debido a las propiedades matemáticas de la transformación Z. El número de "taps" o multiplicadores necesarios para calcular cada salida es un aspecto clave, coincidiendo en una implementación paralela con el número de taps, mientras que en serie, se utiliza un multiplicador secuencialmente para cada salida. La cantidad de taps puede variar según la complejidad del filtro, pudiendo alcanzar cientos en casos más complejos [3].

<div align="center";style="text-align:center;">
  <img width="400" height="400" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/156bcf55-a280-4bb2-904a-e1284ceb7b80">
  <br>
  <span style="font-style: italic;">Figura 1: Estructura de filtro de respuesta finita al impulso [3].</span>
</div>

#### Ventana Hanning
La forma de la ventana Hanning gradualmente atenúa tanto las señales principales como las regionales. En el dominio de la frecuencia, reduce significativamente el máximo lóbulo lateral, presenta una pendiente mucho más pronunciada en la atenuación del lóbulo lateral en función de la frecuencia y también minimiza la pérdida de festón, es decir, las fluctuaciones no deseadas en la respuesta de frecuencia [4].
<div align="center">
  <img width="300" height="100" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/60790e33-09f7-4368-bcf1-cd1f19e1670e">
</div>

<div align="center";style="text-align:center;">
  <img width="500" height="300" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/c73c2fef-1d43-4ddb-b486-155410460c41">
  <br>
  <span style="font-style: italic;">Figura 2: Ventana Hanning [5].</span>
</div>

#### Ventana Hamming
Podemos mitigar los efectos de las discontinuidades en la función temporal que generan anillos en la respuesta en frecuencia al reemplazar la ventana rectangular con una función de ventana que disminuye suavemente en ambos extremos. Esto ayudará a reducir la ondulación. La ventana de Hamming pertenece a este tipo de funciones de ventana [6]. 
<div align="center">
  <img width="400" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/dc931c09-e988-4811-af68-1278c3a3921e">
</div>

<div align="center";style="text-align:center;">
  <img width="500" height="300" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/e0babe14-c0d5-4cb9-8834-7be5f98ed70d">
  <br>
  <span style="font-style: italic;">Figura 3: Ventana Hamming [7].</span>
</div>

#### Ventana Rectangular
Una manera simple y directa de restringir la respuesta impulsional ideal d(k) implica mantener sus valores dentro de un rango específico, por ejemplo, de -M a M. Esto se logra multiplicando d(k) por una función rectangular, la cual tiene solo dos valores (0 o 1) en intervalos determinados, actuando como una especie de ventana que selecciona los valores deseados de d(k) [6].
<div align="center">
  <img width="300" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/541bd363-70c4-4fc1-973d-d011f36b3b5e">
</div>

<div align="center";style="text-align:center;">
  <img width="500" height="300" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/a192c53d-d199-432a-b210-59e54b28119d">
  <br>
  <span style="font-style: italic;">Figura 4: Ventana rectangular [8].</span>
</div>

#### Ventana Bartlett
La ventana de Bartlett, de longitud M + 1, adopta una forma triangular par en su distribución. Su espectro muestra un lóbulo principal más amplio en comparación con la ventana rectangular de la misma longitud. Sin embargo, los lóbulos laterales disminuyen en amplitud de manera más rápida a frecuencias más altas. Esta ventana produce una respuesta en frecuencia con una disminución monotónica de la magnitud [9].
<div align="center">
  <img width="400" height="200" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/a6b48a14-ef08-4b0f-bb2f-5ff4c2ddd96e">
</div>

<div align="center";style="text-align:center;">
  <img width="500" height="300" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/f64a0a3a-57d3-4c2b-b3e9-d5ee6a739cf3">
  <br>
  <span style="font-style: italic;">Figura 5: Ventana Bartlett [9].</span>
</div>

#### Ventana Blackman
La ventana Blackman, reconocida por su capacidad para reducir al mínimo la ondulación máxima en la banda de parada en comparación con la ventana Hamming, se define matemáticamente de la siguiente manera. Este diseño está dirigido a eliminar los lóbulos laterales tercero y cuarto, aunque mantiene una discontinuidad en los límites. A pesar de esta característica, se considera la ventana más precisa, ya que disminuye significativamente los lóbulos laterales [6].
<div align="center">
  <img width="400" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/df080cca-bfc5-4ce5-8a1e-b568126f54aa">
</div>

<div align="center";style="text-align:center;">
  <img width="500" height="300" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/9f303bcb-0c22-4e32-9158-28ad32d1e0f2">
  <br>
  <span style="font-style: italic;">Figura 6: Ventana rectangular [10].</span>
</div>

### Filtros IIR
Esta sección se centra en los filtros de Respuesta Infinita al Impulso (IIR), que son más complejos que los FIR. Mientras que un filtro FIR toma un flujo de datos de entrada y los multiplica por una serie de coeficientes para producir cada salida, un filtro IIR realiza este proceso y además retroalimenta el flujo de datos de salida a través de otra serie de multiplicadores y coeficientes. Esta retroalimentación elimina muchas de las propiedades lineales del filtro FIR, lo que hace que el filtro IIR sea mucho más difícil de analizar. Además, dependiendo de la elección de los coeficientes, puede generar comportamientos no deseados, como una respuesta al impulso de duración o magnitud infinita [11].

<div align="center";style="text-align:center;">
  <img width="400" height="400" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/82d4552f-adb3-4154-b023-9f24736867fc">
  <br>
  <span style="font-style: italic;">Figura 7: Estructura de filtro de respuesta infinita al impulso [11].</span>
</div>

#### Filtros Butterworth
Un filtro Butterworth, también conocido como filtro de máxima planicidad, es ampliamente utilizado en el ámbito de la frecuencia debido a sus características distintivas. Este filtro exhibe una atenuación aguda de frecuencias, una función de magnitud que varía de manera monótona con la frecuencia, ω, y una respuesta de fase más lineal en la banda de paso en comparación con otros filtros tradicionales. Por lo tanto, el filtro Butterworth puede ser definido por su respuesta de amplitud:
<div align="center">
  <img width="300" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/1dd2cee6-586a-4025-9db4-dca17535c1b6">
</div>
donde ωc representa la frecuencia de corte del filtro y n es el orden del filtro. A frecuencias bajas, la ganancia se aproxima a uno, disminuyendo a medida que aumenta la frecuencia. La transición entre estas regiones depende en gran medida del orden del filtro; con un orden bajo, se observa una disminución gradual, mientras que con un orden mayor, la curva puede mostrar un cambio abrupto, similar a una función escalonada, con una ganancia muy baja en frecuencias altas [12].

#### Filtros Bessel 
El filtro de Bessel, también conocido como filtro "Thomson", está diseñado específicamente para mantener un retardo de grupo constante dentro de la banda de paso del filtro, siendo utilizado en aplicaciones donde este retardo constante es crítico, como en el procesamiento de señales de vídeo analógico. A diferencia del filtro Butterworth, los polos del filtro de Bessel con una frecuencia de corte de 1 rad/s se encuentran fuera del círculo unitario, lo que resulta en una respuesta menos nítida tanto en la banda de paso como en la de parada, con una atenuación gradual [13].
<div align="center">
  <img width="400" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/a67363d0-421d-47b5-ba60-b5e2794c2e45">
</div>
<div align="center">
  <img width="400" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/6565cd95-c645-4603-ac4e-635e469be3da">
</div>

#### Filtros Chebyshev

El filtro Chebyshev Tipo I presenta una leve ondulación en la banda pasante, lo que permite un corte más abrupto en la banda de transición en comparación con el filtro Butterworth. Sin embargo, esta mejora en la atenuación de la banda de parada viene acompañada de una mayor variación en el retardo de grupo y un mayor sobreimpulso en la respuesta transitoria debido a la tolerancia del filtro hacia la ondulación en la banda pasante o de rechazo. A diferencia del Butterworth y del Chebyshev Tipo II, el Chebyshev Tipo I distribuye sus polos en una elipse en lugar de una circunferencia, lo que lo convierte en una aproximación más precisa a un filtro ideal, con una respuesta más rectangular en la región de corte y una disminución más abrupta en la banda de supresión. Por otro lado, el filtro Chebyshev Tipo II se caracteriza por mantenerse plano al máximo en la banda de paso, aunque exhibe un rizado de igual amplitud en la banda de parada. A diferencia del Chebyshev Tipo I, en el Tipo II se especifica la frecuencia de inicio de la banda de parada y la máxima amplitud del rizado [13].
<div align="center">
  <img width="300" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/ee830f01-df3b-42d9-a12c-2f8541db8f3e">
</div>

#### Filtros Elípticos
El filtro elíptico, también conocido como filtro "Cauer", presenta una oscilación tanto en la banda pasante como en la banda de parada. Para un filtro elíptico estándar, se especifican la banda de paso y la banda de parada, así como la atenuación mínima deseada. En el diagrama de polo-cero de un filtro elíptico genérico, se observan cuatro ceros en el eje imaginario. Este tipo de filtro destaca por su transición extremadamente nítida entre la banda pasante y la banda de parada, aunque esto conlleva una mayor variación en el retardo de grupo en comparación con otros filtros. Se logra esta estrechez en la zona de transición mediante un rizado constante en ambas bandas [13].
<div align="center">
  <img width="400" height="150" src="https://github.com/adri201022/ISB-Grupo-11/assets/164538327/3c07ae1a-4617-4305-9bad-a5312d54fa40">
</div>

## **Objetivos** <a name="id2"></a>
<ul>
  <li>Filtrar las señales EMG para eliminar ruido y artefactos, y aislar la actividad muscular efectiva.</li>
  <li>Diseñar y aplicar filtros óptimos, tanto IIR como FIR, para eliminar las frecuencias altas correspondientes a ruido en las señales de ECG utilizando un dataset previamente creado.</li>
  <li>Preprocesar señales EEG para reducir el ruido y extraer características de interés como ondas
cerebrales específicas.</li>
</ul>

## **Filtros de señal ECG** <a name="id4"></a>
A continuación se mostrará las gráficas de las señales con el uso de filtros FIR y IIR, cabe resaltar que se obtuvieron 3 señales del ecg que fueron en reposo, respiraciones rápidas y en actividad. Previamente antes de aplicar los filtros FIR y IIR se aplico un filtro notch para eliminar el ruido ambiental, el cual es 60 Hz. 

Encontramos en la bibliografía que las frecuecnias de corte bajas es de 0.5 Hz en ambos filtros que son el FIR y IIR. Primeramente, se presentará las respuestas en frecuencias de ambos filtros.[14]

| Respuesta en Frecuencia | Respuesta en Frecuencia  | 
|--------------------|---------------------------|
| Filtro FIR         | Filtro IIR                |
|                    |                           |
| ![Filtro FIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/799c7167-56c2-45a1-a706-a43124e90a79) | ![Filtro IIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/42d798ea-6672-42e2-b69a-e0cdeba16af7) |

 A continuación mostraremos el resultado luego del filtrado notch, que filtra el ruido ambiental

 |                     | Reposo                     | Respiraciones rápidas       | Actividad                    |
|---------------------|----------------------------|-----------------------------|------------------------------|
| Señal filtrado notch  | <img width="600" src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/c8617495-dcee-4c32-8beb-892e827524f5"> |  <img width="600" src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/58ab9afe-1e21-4e9b-a33b-05c9baed241e">  | <img width="600" src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/d6df02e2-3433-4155-a415-2e881b724a41">  |


Ahora presentaremos la señal de ECG en reposo,respiraciones y en actividad con sus respectivos filtros, como mencionamos anteriormente ambas frecuencias de cortes bajas son 0.5 Hz.[14]

|                   | Señal cruda | Filtro FIR (Butterworth) | Filtro IIR (Hanning) |
|-------------------|--------------|--------------------------|----------------------|
| Reposo            | ![Reposo sin filtrar](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/c08a27eb-da9a-4e9d-9e4e-ef4f7f8cefda) | ![Reposo FIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/a4f9c666-8bb8-4576-a2d7-b354ae2a5366) | ![Reposo IIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/7c7533ff-2cb3-4c91-9712-f8380116ebc9) |
| Respiraciones     | ![Respiraciones sin filtrar](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/7f5e5113-9f27-455e-bfcc-1d5087d5dd4f) | ![Respiraciones FIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/ea9f5374-46eb-4ef2-9d4e-860d058cb945) | ![Respiraciones IIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/850d4072-b5cb-447f-ac63-2170e484ac9e) |
| Actividad         | ![Actividad sin filtrar](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/b6c412d4-7608-4d68-bb10-9939a64d94b6) | ![Actividad FIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/3e8b1e95-c634-4532-93a5-7ca7810618c8) | ![Actividad IIR](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/829afebb-9053-4700-9f12-77d4987daad1) |

## **Filtros de señal EMG** <a name="id3"></a>

En esta sección filtraremos la señal EMG utilizando filtros digitales FIR e IIR. Dado que la señal EMG se encuentra típicamente entre frecuencias de 50 y 150 Hz, se eligio una frecuencia de corte de 180 Hz. [15]

| Respuesta en Frecuencia | Respuesta en Frecuencia  | 
|--------------------|---------------------------|
| Filtro FIR         | Filtro IIR                |
|                    |                           |
| ![FIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/8593e4e2-9cf8-478a-8825-64b70bc15625)| ![IIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/f10c2c48-8d95-4b61-b80c-e59f2d8bd2e0) |

|                   | Señal cruda | Filtro FIR (Butterworth) | Filtro IIR (Hanning) |
|-------------------|--------------|--------------------------|----------------------|
| Reposo            | ![Reposo_sinFiltrar](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/f7cb2485-357d-473b-b0e0-2758f9dd6ac8)| ![Reposo_FIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/b13a9407-2bfa-404c-92fe-55606df2b85c)|![Reposo_IIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/24b29ef2-6178-4505-8d96-b4e6c4cbb884)|
| Sin Oposición     | ![SinOposicion_sinFiltrar](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/8900594d-e7dd-438d-a2f6-764245e670e7)|![SinOposicion_FIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/2c30e05d-0e18-4f81-a68a-2c708b3999ad)| ![SinOposicion_IIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/587c7192-307a-4e7f-a353-45cfa7c97447)|
| Con Oposición     | ![ConOposicion_sinFiltrar](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/45539764-0962-422f-a661-8b7be2803e19)| ![ConOposicion_FIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/43638900-b700-4de6-8e15-6ddb6ca03907)| ![ConOposicion_IIR](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/4be61ac9-270f-4d5e-9aa7-a8b7aea99d33)|

## **Filtros de señal EEG** <a name="id5"></a>

La información será sacada del estudio "Reconocimiento de picos epilépticos en electroencefalograma utilizando autómatas finitos deterministas" [R1] después de la grabación de todos los datos se tiene la información de las gráficas usando el Bitalino y el OPENCBI.

Explicación general:

Después de la grabación, se analizaron todos los datos.
Para el preprocesado para eliminar el cambio de línea base y el pase de banda filtrado utilizando un filtro Butterworth de respuesta de impulso infinito (IIR) con un corte inferior de 0,25 Hz y un corte de 35 Hz [R1,R2]. Procedimientos experimentales completos en.Este estudio se realizó de conformidad con el "comité para el control y supervisión de experimentos con animales (CPCSEA)", India, así como con las normas internas.
políticas y lineamientos institucionales.

Evaluación en reposo


|                   | A | B | C |
|-------------------|--------------|--------------------------|----------------------|
| 1    | ![Captura1](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8bc9218e-b53f-460d-b628-90cc99ada2c8) | ![Captura4R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/1d02793b-ae23-429e-83fb-752561bcf392) | ![Captura5R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/2274ac5e-f36c-4451-b1f6-7ae9d4b1b85b) |
| 2    | ![Captura6R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/f758b6da-077e-4c91-a8b5-6bc5c3882614) | ![Captura7R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/12f991ec-871c-41e1-8bd4-92faf9110862) | ![Captura8R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8d689167-bf72-4a22-a078-232e81d64fa6)![Captura8R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8d689167-bf72-4a22-a078-232e81d64fa6) |
| 3    | ![Captura9R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/63371286-03b6-4de8-a690-2eb0d4586bed) | ![Captura10R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/c8bb67ea-23ef-4ec8-abb8-c59398b61af6) | ![Captura11R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8513e61f-c3ca-47f0-8991-146cd7ae379e) |

Primero colocamos un análisis espectral de señales para evaluar los picos que superan la frecuencia de 60Hz
![Captura1](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8bc9218e-b53f-460d-b628-90cc99ada2c8)


![Captura2](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/2456dcc3-9801-413b-bb15-a4337a404633)
![Captura3R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/f6524405-4833-4d63-81b9-bdb87c7cd1e1)
![Captura4R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/1d02793b-ae23-429e-83fb-752561bcf392)
![Captura5R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/2274ac5e-f36c-4451-b1f6-7ae9d4b1b85b)
![Captura6R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/f758b6da-077e-4c91-a8b5-6bc5c3882614)
![Captura7R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/12f991ec-871c-41e1-8bd4-92faf9110862)
![Captura8R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8d689167-bf72-4a22-a078-232e81d64fa6)
![Captura9R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/63371286-03b6-4de8-a690-2eb0d4586bed)
![Captura10R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/c8bb67ea-23ef-4ec8-abb8-c59398b61af6)
![Captura11R](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/8513e61f-c3ca-47f0-8991-146cd7ae379e)


Evaluación Ojos abiertos y cerrados

Se sigue el mismo procedimiento anterior

![Captura1O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/1896704a-e3ab-4218-bf66-f79319215daf)
![Captura2O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/ab8e348c-841d-46dc-b07e-8e2cfa63ade9)
![Captura3O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/3ca5e857-1259-46df-bd46-842dd909827d)
![Captura4O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/d005611a-4213-4ae7-a656-b821f0e98790)
![Captura6O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/66c9f2d4-7518-42dd-b52c-90ea35929abe)
![Captura7O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/52897b57-dd4f-46d2-b436-230ac0eaac9a)
![Captura8O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/998afb4b-31f8-410a-851b-fc029b53cbb9)
![Captura9O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/10c9f799-0b1e-4735-89ad-068112002ac0)
![Captura10O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/b57ff3fe-e75d-4460-9caf-05ad09e56b50)
![Captura11O](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/01c13e0e-66b3-4421-b16b-a0b8bb7ad6a4)


Evaluación de preguntas básicas y complejas

![Captura1P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/1f40c239-bcb3-44e2-9328-c1c0b2d37006)
![Captura2P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/2c74557a-5de4-4176-936c-3e432bf60563)
![Captura3P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/5bb4d121-cea2-444f-9c07-17c998955027)
![Captura4P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/5252b2ef-1edc-49cd-8e17-6be8521be320)
![Captura5P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/a2327e96-5a1e-4d42-8535-bfd2e4839e1d)
![Captura6P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/ab7d934b-7706-4ee5-8ed1-83524168fb1e)
![Captura7P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/9710e956-7455-429e-bf7a-af970ef34782)
![Captura8P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/388982db-392e-4807-a2f8-d7e8d252f66f)
![Captura9P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/17d75bd2-1d28-4baa-b90d-d4406c137c90)
![Captura10P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/cbdbb96e-528f-4a95-a5f4-c3f89aad33d1)
![Captura11P](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/ed8d62ba-2858-4b4d-8293-09b6feb328e5)



## **Conclusiones** <a name="id6"></a>
EMG:
-Como se puede apreciar en las graficas, los filtros FIR e IIR eliminaron eficazmente el ruido y las frecuencias no deseadas al aplicar un filtro pasa baja con la frecuencia de corte de 180 Hz, con lo cual ayuda a excluir las frecuencias altas relacionadas al ruido, conservando las frecuencias entre 50 y 150 Hz, donde reside la información relevante de la señal EMG. [15] Lo que se traduce en una mejora visual de las graficas filtradas a comparación de las graficas crudas.

ECG:
- Como se logra observar en la gráfica del espectro de la señal post filtrado de notch , las señales con frecuencias de 60 HZ, que son mayormente el ruido ambiental, han sido atenuadas. Además se logra observa que tanto el filtro IIR de butterworth y el filtro IFR de ventana hanning han logrado filtrar el ruido correctamente. Lo cual nos lleva a la conclusión que ambos filtros son utiles cuando se trata de filtrar señales de ECG cuando la persona se encuentra en reposo. Sin embargo para el caso de las respiraciones se puede apreciar que el filtrado em ambos tipos de filtros ha dejado un poco de ruido,por lo que el utilizar este tipo de filtro IIR butterwort y el filtro FIR de ventana Hanning no es el adecuado. Para el caso de la señal ECG en actividad se aprecia que el filtrado en ambos caso fue correcto ya que se logro filtrar correcta el ruido en ambos casos, lo que nos concluye a decir que el uso de estos tipos de filtros son adecuados para señales en ECG ena actividad.
## **Archivos de códigos** <a name="id7"></a>
[Señal filtrada de ECG reposo](https://github.com/adri201022/ISB-Grupo-11/blob/b9c788a4e056b9cc217754f752c74604851d501b/Documentaci%C3%B3n/Laboratorios/L6_Filtros_EMG_ECG_EEG/Se%C3%B1al%20ECG-filtros-Reposo.ipynb)

[Señal filtrada de ECG respiraciones rápidas](https://github.com/adri201022/ISB-Grupo-11/blob/b9c788a4e056b9cc217754f752c74604851d501b/Documentaci%C3%B3n/Laboratorios/L6_Filtros_EMG_ECG_EEG/Se%C3%B1al-ECG-filtros-Respiraciones.ipynb)

[Señal filtrada de ECG en actividad](https://github.com/adri201022/ISB-Grupo-11/blob/b9c788a4e056b9cc217754f752c74604851d501b/Documentaci%C3%B3n/Laboratorios/L6_Filtros_EMG_ECG_EEG/Se%C3%B1al-ECG-filtros-Actividades.ipynb)
## **Referencias** <a name="id8"></a>
[1] P. Podder, Md. Mehedi Hasan, Md. Rafiqul Islam, and M. Sayeed, “Design and Implementation of Butterworth, Chebyshev-I and Elliptic Filter for Speech Signal Analysis,” International Journal of Computer Applications, vol. 98, no. 7, 2014, doi: 10.5120/17195-7390.

[2] “COMPARISON OF FIR AND IIR FILTERS USING ECG SIGNAL WITH DIFFERENT SAMPLING FREQUENCIES,” International Research Journal of Modernization in Engineering Technology and Science, 2023, doi: 10.56726/irjmets35977.

[3] M. Parker, “Finite Impulse Response (FIR) Filters,” in Digital Signal Processing 101, 2017. doi: 10.1016/b978-0-12-811453-7.00005-6.

[4] S. Braun, “WINDOWS,” Encyclopedia of Vibration, pp. 1587–1595, Jan. 2001, doi: 10.1006/RWVB.2001.0052.

[5] “Hann or Hanning or Raised Cosine,” Stanford.edu, 2022. https://ccrma.stanford.edu/~jos/sasp/Hann_Hanning_Raised_Cosine.html#10436 (accessed May 04, 2024).

[6] E. Lai, “Finite impulse response filter design,” Practical Digital Signal Processing, pp. 98–144, Jan. 2003, doi: 10.1016/B978-075065798-3/50006-0.

[7] “Hamming Window,” Stanford.edu, 2022. https://ccrma.stanford.edu/~jos/sasp/Hamming_Window.html#10455 (accessed May 04, 2024).

[8] “The Rectangular Window,” Stanford.edu, 2022. https://ccrma.stanford.edu/~jos/sasp/Rectangular_Window.html (accessed May 04, 2024).

[9] “Signal Processing: Continuous and Discrete,”MIT OpenCourseWare, 2008. https://ocw.mit.edu/courses/2-161-signal-processing-continuous-and-discrete-fall-2008/b1566013ede775cece0ecb8f1bf945bb_lecture_16.pdf (accessed: May 04, 2024)

[10] “Spectrum Analysis of an Oboe Tone,” Stanford.edu, 2022. https://ccrma.stanford.edu/~jos/sasp/Spectrum_Analysis_Oboe_Tone.html (accessed May 04, 2024).

[11] M. Parker, “Infinite Impulse Response (IIR) Filters,” in Digital Signal Processing 101, 2017. doi: 10.1016/b978-0-12-811453-7.00008-1.

[12] N. AlHinai, “Introduction to biomedical signal processing and artificial intelligence,” Biomedical Signal Processing and Artificial Intelligence in Healthcare, pp. 1–28, Jan. 2020, doi: 10.1016/B978-0-12-818946-7.00001-9.

[13] M. T. Thompson, “Analog Low-Pass Filters,” Intuitive Analog Circuit Design, pp. 531–583, Jan. 2014, doi: 10.1016/B978-0-12-405866-8.00014-0. 

[14] A. Sharma, C. Saxena, H. Gupta, and R. Srivastav, (PDF) denoising of ECG signals using FIR & IIR Filter: A performance analysis, https://www.researchgate.net/publication/328293842_Denoising_of_ECG_signals_using_FIR_IIR_filter_A_performance_analysis (accessed May 5, 2024). 

[15] B. Gerdle, S. Karlsson, S. Day, y M. Djupsjöbacka, "Acquisition, Processing and Analysis of the Surface Electromyogram," en Modern Techniques in Neuroscience, U. Windhorst y H. Johanson, Eds. Berlin: Springer Verlag, 1999, pp. 705-755.


