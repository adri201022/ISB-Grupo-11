# Informe de Laboratorio 11: EdgeImpulse
## Adrian Gutierrez
### Proyecto EEG

1. Captura de Pantalla
![eeg_prueba](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/e9864072-086f-4c3d-8580-23322e9a53e5)

2. Link de EdgeImpulse
[Link a Proyecto de EEG en EdgeImpulse](https://studio.edgeimpulse.com/studio/431536/acquisition/training)

3. Código Python para subir archivos a EdgeImpulse
```python
import requests
import os

api_key = 'ei_e219c6e877ef856c154937b04f819c156a2b78261bf228fbfe4a0f024bfca464'
# Add the files you want to upload to Edge Impulse
files = [
    'EEG_referencia.csv',
    'EEG_ojos_abiertos.csv',
    'EEG_preguntas.csv',
]
# Replace the label with your own.
label = 'Señales'

# Create a list of file tuples to upload
file_tuples = [('data', (os.path.basename(file), open(file, 'rb'), 'text/csv')) for file in files]

try:
    # Upload the files to Edge Impulse using the API, and print the response.
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                        headers={
                            'x-label': label,
                            'x-api-key': api_key,
                        },
                        files=file_tuples
                       )
    
    if res.status_code == 200:
        print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
    else:
        print('Failed to upload file(s) to Edge Impulse\n', res.status_code, res.content)
finally:
    # Ensure files are closed after the request
    for file_tuple in file_tuples:
        file_tuple[1][1].close()
 ```
### Proyecto ECG
1. Captura de Pantalla
![ecg_prueba](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/61a3c9e4-719d-4c99-ad6b-35d1d1709bf4)


2. Link de EdgeImpulse
[Link a Proyecto de ECG en EdgeImpulse](https://studio.edgeimpulse.com/studio/431535/acquisition/training?page=1)

3. Código Python para subir archivos a EdgeImpulse
```python
import requests
import os

api_key = 'ei_800dd7b0b9dda3e64d8b82e644f7fa67e67ad42e89057be23ea18db17447040f'
# Add the files you want to upload to Edge Impulse
files = [
    'Ecg_durante_actividad.csv',
    'Ecg_respiraciones.csv',
    'Ecg_reposo.csv',
]
# Replace the label with your own.
label = 'Señales'

# Create a list of file tuples to upload
file_tuples = [('data', (os.path.basename(file), open(file, 'rb'), 'text/csv')) for file in files]

try:
    # Upload the files to Edge Impulse using the API, and print the response.
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                        headers={
                            'x-label': label,
                            'x-api-key': api_key,
                        },
                        files=file_tuples
                       )
    
    if res.status_code == 200:
        print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
    else:
        print('Failed to upload file(s) to Edge Impulse\n', res.status_code, res.content)
finally:
    # Ensure files are closed after the request
    for file_tuple in file_tuples:
        file_tuple[1][1].close()
```

### Proyecto EMG
1. Captura de Pantalla
![emg_prueba](https://github.com/adri201022/ISB-Grupo-11/assets/164541653/4fac6888-7c21-41c2-86ae-1888b384ab8c)


2. Link de EdgeImpulse
[Link a Proyecto de EEG en EdgeImpulse](https://studio.edgeimpulse.com/studio/431164/acquisition/training?page=1)

3. Código Python para subir archivos a EdgeImpulse
```python
import requests
import os

api_key = 'ei_32bafc6757ec83fb6a4bb2b6297aba9c9fd0e08332be167bb5a53175778782d1'
# Add the files you want to upload to Edge Impulse
files = [
    'Emg_reposo.csv',
    'Emg_oposicion.csv',
]
# Replace the label with your own.
label = 'Señal'

# Create a list of file tuples to upload
file_tuples = [('data', (os.path.basename(file), open(file, 'rb'), 'text/csv')) for file in files]

try:
    # Upload the files to Edge Impulse using the API, and print the response.
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                        headers={
                            'x-label': label,
                            'x-api-key': api_key,
                        },
                        files=file_tuples
                       )
    
    if res.status_code == 200:
        print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
    else:
        print('Failed to upload file(s) to Edge Impulse\n', res.status_code, res.content)
finally:
    # Ensure files are closed after the request
    for file_tuple in file_tuples:
        file_tuple[1][1].close()
```
