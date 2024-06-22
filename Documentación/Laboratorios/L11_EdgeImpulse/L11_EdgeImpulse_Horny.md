# Informe de Laboratorio 11: EdgeImpulse
## Micaela Horny
### Proyecto EMG
1. Captura de Pantalla
![captura_ei_emg](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/94df777c-619a-45e7-94ac-ab53b502a07c)

2. Link de EdgeImpulse
[Link a Proyecto de EMG en EdgeImpulse](https://studio.edgeimpulse.com/public/431214/live)

3. Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_0dd7d90a25cc36e65853a89d1aaefc6b4fcd7fde38555cf19dcc5f64389c05a4'
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
![Captura_ei_ecg](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/da9fd491-a1bc-498c-a426-5e1a38ceb82b)


2. Link de EdgeImpulse
[Link a Proyecto de ECG en EdgeImpulse](https://studio.edgeimpulse.com/public/431170/live)

3. Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_69811cb5c681962b13c318c4d6c55775648b4fef5585693310daea0f85f60c63'
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
![Captura_ei_eeg](https://github.com/adri201022/ISB-Grupo-11/assets/164538327/23ab35e0-dc10-4447-b9eb-d42b2609b148)

2. Link de EdgeImpulse
[Link a Proyecto de EEG en EdgeImpulse](https://studio.edgeimpulse.com/public/431218/live)

3. Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_70dad9e8acdd22a8aa8ee1e4a95c3a0607f122176058de04af00620981f44682'
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
