import requests

API_KEY = 'AIzaSyBC-dHC2Kh9uVabKOZtSy7Pu-fYLT5N4Dk'
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

params = {
    'query': 'ferreterías en Ciudad de México',
    'key': API_KEY,
    'type': 'hardware_store',
    'language': 'es'
}

response = requests.get(url, params=params)
results = response.json().get('results', [])

for business in results:
    name = business.get('name')
    address = business.get('formatted_address')
    phone = business.get('formatted_phone_number')
    print(f'Nombre: {name}, Dirección: {address}, Teléfono: {phone}')

def obtener_detalles(place_id, api_key):
    url = 'https://maps.googleapis.com/maps/api/place/details/json'
    params = {
        'place_id': place_id,
        'fields': 'website,formatted_phone_number',
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response.json().get('result', {})

# Ejemplo extendido con tu código
for business in results:
    place_id = business.get('place_id')
    detalles = obtener_detalles(place_id, API_KEY)

    name = business.get('name')
    address = business.get('formatted_address')
    phone = detalles.get('formatted_phone_number', 'No disponible')
    website = detalles.get('website', 'No disponible')

    print(f'Nombre: {name}, Dirección: {address}, Teléfono: {phone}, Website: {website}')

import requests
import re

def extraer_emails_desde_web(url_web):
    try:
        response = requests.get(url_web, timeout=5)
        html = response.text
        # Patrón básico para detectar emails
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
        # Eliminar duplicados
        emails = list(set(emails))
        return emails if emails else ['No encontrado']
    except Exception as e:
        return [f'Error al acceder a la web: {e}']

# Ejemplo completo con Google Places + extracción email
for business in results:
    place_id = business.get('place_id')
    detalles = obtener_detalles(place_id, API_KEY)

    name = business.get('name')
    address = business.get('formatted_address')
    phone = detalles.get('formatted_phone_number', 'No disponible')
    website = detalles.get('website', None)

    emails = []
    if website:
        emails = extraer_emails_desde_web(website)
    else:
        emails = ['No disponible']

    print(f'Nombre: {name}')
    print(f'Dirección: {address}')
    print(f'Teléfono: {phone}')
    print(f'Website: {website}')
    print(f'Emails encontrados: {emails}')
    print('-----------------------------')
