# API ner_recognition
API para el reconocimiento de entidades nombradas en Español.

## Objetivo:

 Reconocer entidades nombradas para oraciones en Español

## Prerequisitos

- Python instalado, versión 3.8.2 o superior .
- Instalar librería Flask: `pip install Flask`
- Instalar liberería Spacy y descargar el modelo 'es_core_news_sm': `pip install spacy && python -m spacy download es_core_news_sm`

## Ejecución del API

1. Clonar este reporitorio en su computadora.
2. Ubicarse en el directorio donde se encuentra el proyecto.
3. Ejecutar la aplicación Flask :  `python app.py `
4. El API se encontrará corriendo en `http://127.0.0.1:5000`

## Uso y prueba

Para realizar una prueba sobre este proyecto puede utilizar el siguiente ejemplo:
 ```
import json
import requests
from pprint import pprint

api_url = 'http://127.0.0.1:5000/ner_recognition/'  
headers = {
    'Content-Type': 'application/json',
}
pay_load = {
    "sentences": ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera"]
}
result = requests.post(api_url, data=json.dumps(pay_load), headers=headers)
pprint(result.json())
 ```
 ```
#Output
{
    'results': [
        {
            'entities': {'Apple': 'ORG', 'Reino Unido': 'LOC'},
            'sentence': 'Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.'
        },
        {
            'entities': {'San Francisco': 'LOC'},
            'sentence': 'San Francisco considera prohibir los robots de entrega en la acera'
        }
    ]
}
```
