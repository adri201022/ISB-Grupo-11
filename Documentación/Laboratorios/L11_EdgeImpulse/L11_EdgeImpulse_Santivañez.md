# Informe de Laboratorio 11: EdgeImpulse
## Gian Santivañez

### Código Python para subir archivos a EdgeImpulse
```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_...'
# Add the files you want to upload to Edge Impulse
files = [
    '/archivos.csv',
]
# # Replace the label with your own.
label = 'Label'
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

* Api-Keys:
    - EMG: ei_da92a14a8b8d868e5cd8217ac103c659f0c72ecc57cd34de8bea503b03797426
    - ECG: ei_9c3c7baf3ad9c7ec14048335ca1a4f037708dc48a4ca56c97941ca71c1911bf5
    - EEG: ei_38b5dae8114553075007043394f92d63c923ebe3f5a524ea358a66b668384bb9


### Proyecto EMG
1. Captura de Pantalla
![SS](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/4bfdb5d2-5a1f-48bf-b84e-38c31195bcaf)

2. Link de EdgeImpulse
[Link a Proyecto de EMG en EdgeImpulse](https://studio.edgeimpulse.com/public/431189/live)

### Proyecto ECG
1. Captura de Pantalla
![SS_ECG](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/87937a65-f056-4240-b0ed-47b088e445ec)

2. Link de EdgeImpulse
[Link a Proyecto de ECG en EdgeImpulse](https://studio.edgeimpulse.com/public/431273/live)

### Proyecto EEG
1. Captura de Pantalla
![SS_EEG](https://github.com/adri201022/ISB-Grupo-11/assets/100977549/3e27dafe-a7a8-483c-9674-2e2c7c2e1d08)

2. Link de EdgeImpulse
[Link a Proyecto de EEG en EdgeImpulse](https://studio.edgeimpulse.com/public/431294/live)
