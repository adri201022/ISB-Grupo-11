# Informe de Laboratorio 11: EdgeImpulse
## Rodrigo Gonzales
### Proyecto EMG
1. Captura de Pantalla
![image](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/87c369f2-15e2-4979-a22c-1509a6cd275f)

2. Link de EdgeImpulse
[Link a Proyecto de EMG en EdgeImpulse](https://studio.edgeimpulse.com/studio/431509/acquisition/training?page=1)

3. Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_dbd192bf9e35efa378c3b3b406522ed71a4ffffe9927de455ec0a3f8eb49b88f'
# Add the files you want to upload to Edge Impulse
files = [
    '/Emg_reposo.csv',
    '/Emg_oposicion.csv',
]
# # Replace the label with your own.
label = 'emg_reposo'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'application/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
 ```
### Proyecto ECG
1. Captura de Pantalla
![image](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/97e1da70-0cf3-4ee0-a500-a13d123ea81f)

2.  Link de EdgeImpulse
[Link a Proyecto de ECG en EdgeImpulse](https://studio.edgeimpulse.com/studio/431215)

3. Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_97b89d8315deac85c85905db66a45ae39079a0beb3ca0bbe7862121f912ed43a'
# Add the files you want to upload to Edge Impulse
files = [
    '/Ecg_reposo.csv',
    '/Ecg_respiraciones.csv',
    '/Ecg_durante_actividad.csv',
]
# # Replace the label with your own.
label = 'ecg'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'application/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
```

### Proyecto EEG
1. Captura de Pantalla
![image](https://github.com/adri201022/ISB-Grupo-11/assets/42382650/82396a6a-d3ac-4b09-b21e-cfb82cf473cd)

2. Link de EdgeImpulse
[Link a Proyecto de EEG en EdgeImpulse](https://studio.edgeimpulse.com/studio/431547)

3. Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_719f34fd8dee1d91add320ccc66608f3cbe548e85dcb0f741bd3f01c745f6c20'
# Add the files you want to upload to Edge Impulse
files = [
    '/Eeg_referencia.csv',
    '/Eeg_preguntas.csv',
    '/Eeg_ojos_abiertos_cerrados.csv',
]
# # Replace the label with your own.
label = 'eeg'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'application/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
```
   
