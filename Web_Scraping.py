import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página de Monitores de Amazon
AMAZON_URL = "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
           'Acept-Language': 'en-US, en;q=0.5'}
PAGE_COUNT = 136
OUTPUT_FILE = 'productos.csv'

# Crear una lista vacía para almacenar los datos extraídos
productos = []

# Recorrer cada página de productos utilizando el parámetro "page=" en la URL
for i in range(1, PAGE_COUNT + 1):
    url_pagina = f"{AMAZON_URL}&page={i}&language=es&qid=1677807412&ref=sr_pg_{i}"
    response = requests.get(url_pagina, headers=HEADERS)

    # Verificar el estado de la respuesta antes de procesar el contenido de la página
    if response.status_code != 200:
        print(
            f'Error al cargar la página {url_pagina}. Estado de la respuesta: {response.status_code}')
        continue

    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los contenedores de productos en la página
    contenedores_productos = soup.find_all(
        'div', {'class': 's-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border'})

    # Extraer la información de cada producto
    for producto in contenedores_productos:
        # Get the title (if it exists)
        title_elem = producto.find(
            'span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
        title = title_elem.text.strip() if title_elem else ''

        # Get the rating (if it exists)
        rating_elem = producto.find('span', {'class': 'a-size-base'})
        rating = rating_elem.text.strip() if rating_elem else ''

        # Get the price (if it exists)
        price_elem = producto.find('span', {'class': 'a-price-whole'})
        price = price_elem.text.strip() if price_elem else ''

        # Get the price anterior (if it exists)
        price_anterior_elem = producto.find(
            'span', {'class': 'a-price a-text-price'})
        price_anterior = price_anterior_elem.text.strip() if price_anterior_elem else ''

        # Get the price (if it exists)
        votante_elem = producto.find(
            'span', {'class': 'a-size-base s-underline-text'})
        votante = votante_elem.text.strip() if votante_elem else ''

        # Get the demanda (if it exists)
        demanda_elem = producto.find(
            'span', {'class': 'a-size-base a-color-price'})
        demanda = demanda_elem.text.strip() if demanda_elem else ''

        # Agregar los datos extraídos a la lista de productos
        productos.append({'Title': title, 'Rating': rating,
                         'Price': price, 'Price_Anterior': price_anterior, 'Votante': votante, 'Demanda': demanda})

# Convertir la lista de productos en un dataframe de Pandas
df = pd.DataFrame(productos)

# Exportar el dataframe a un archivo CSV
df.to_csv('./data/productos.csv', index=False)
