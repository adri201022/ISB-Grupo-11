# Informe de Laboratorio 9: Procesamiento de una señal ECG

## Integrantes
- Adrian Alberto Gutierrez Gonzales (adrian.gutierrez@upch.pe)
- Micaela Ivy Horny Insua (micaela.horny@upch.pe)
- Gian Pierre Santivañez Condor (gian.santivanez@upch.pe)
- Rodrigo Alfonso Gonzales Cabrera (rodrigo.gonzales@upch.pe)

## Tabla de contenidos
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Filtro de señal ECG](#id3)
4. [Picos de la onda R](#id4)
5. [HRV](#id5)
6. [Discusión](#id6)
7. [Archivos de códigos](#id7)
8. [Referencias](#id8)

## **Introducción** <a name="id1"></a>


## **Objetivos** <a name="id2"></a>


## **Filtro de señal ECG** <a name="id3"></a>

En el caso del filtrado de las señales, primero hemos utilizado un filtro notch para poder eliminar el ruido ambiental que aparece a menúdo en estos tipos de tomas. El segundo filtro que hemos usado es un filtro pasa baja bessel de tercer órden que tiene una frecuencia de corte de 30 Hz. Estamos usando este filtro ya que la bibliografía encontrada nos la recomienda para minimizar el efecto de ruido en altas frecuencias y artefactos en la detección de picos R.

### Señal en reposo
|                   | Señal cruda                          | Filtro Notch                          | Filtro Bessel                        |
|-------------------|--------------------------------------|---------------------------------------|--------------------------------------|
| Señal en reposo   | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/95c74016-64c6-4eba-a2e3-749bd6e51998" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/9ce09ca1-0489-4a25-92ea-8bf37ebd5d69" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/e5452472-3d28-4e90-a1fa-a24890f2d2b3" width="550" height="250"> |

### Señal en respiraciones rápidas
|                           | Señal cruda                          | Filtro Notch                          | Filtro Bessel                        |
|---------------------------|--------------------------------------|---------------------------------------|--------------------------------------|
| Señal en respiraciones rápidas  | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/151615a4-5692-4e0d-9358-9f96c15afee5" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/0fcfc928-bc34-4d07-ac5e-bdff7ecc383d" width="550" height="250"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/d513ed52-b307-44d4-9c64-6846a1c760d5" width="550" height="250"> |

### Señal durante actividad
|                     | Señal cruda                          | Filtro Notch                          | Filtro Bessel                        |
|---------------------|--------------------------------------|---------------------------------------|--------------------------------------|
| Señal durante actividad | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/72d0fa70-1499-4781-8ae3-04499caa4147" width="450" height="300"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/f6adc0aa-898f-49a7-810d-9ddd77e3ab36" width="450" height="300"> | <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/121294e7-3047-4f63-b310-40ad5827762e" width="450" height="300"> |


## **Picos de la onda R** <a name="id4"></a>
### Señal en reposo
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/1374a815-ce17-4b16-add7-4d67328f2b36" width="500" height="350">
</p>

### Señal en respiraciones rápidas
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/77455889-150d-4326-ada3-63f450c6635e" width="500" height="350">
</p>

### Señal durante actividad
<p align="center">
  <img src="https://github.com/adri201022/ISB-Grupo-11/assets/164541653/992b9f80-dddc-4443-959f-39f1300c4f82" width="500" height="350">
</p>

## **HRV** <a name="id5"></a>

Para esta parte hemos obtenido los datos importantes que destaca la bibliografía encontrada, las cuales son SDNN, rMSSD, SD1 y SD2.

### Señal en reposo
#### Resultados HRV
- **SDNN**: 33.85 ms
- **rMSSD**: 19.33 ms
- **SD1**: 0.09 s
- **SD2**: 0.04 s

### Señal en respiraciones rápidas
#### Resultados HRV
- **SDNN**: 122.54 ms
- **rMSSD**: 171.79 ms
- **SD1**: 0.29 s
- **SD2**: 0.12 s

### Señal durante actividad
#### Resultados HRV
- **SDNN**: 117.89 ms
- **rMSSD**: 172.71 ms
- **SD1**: 0.29 s
- **SD2**: 0.11 s
## **Discusión** <a name="id6"></a>


## **Archivos de códigos** <a name="id7"></a>

[Tratamiento de señal  ECG en colab](https://github.com/adri201022/ISB-Grupo-11/blob/4b4ce18e4fabbbc0655e8162bcf6cdbd4163f358/Documentaci%C3%B3n/Laboratorios/L9_Procesamiento_ECG/Tratamiento%20de%20ECG.ipynb)

## **Referencias** <a name="id8"></a>
