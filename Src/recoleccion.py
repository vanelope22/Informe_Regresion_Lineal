import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Cargar el token de la API
load_dotenv()

API_URL = "https://www.datos.gov.co/api/v3/views/7y2j-43cv/query.json"

APP_TOKEN = os.getenv("SOCRATA_APP_TOKEN")

# ---------------------------------------------------------
# CONSULTA DE DATOS
# ---------------------------------------------------------

query = """
SELECT
    year_radica,
    count_a,
    count_de,
    tipo_predio_zona,
    categoria_ruralidad_2024,
    valor
WHERE
    tiene_valor = 1
    AND valor > 0
    AND nombre_natujur = 'COMPRAVENTA'
LIMIT 5000
"""

headers = {
    "Accept": "application/json",
    "X-App-Token": APP_TOKEN
}

response = requests.post(
    API_URL,
    headers=headers,
    json={
        "query": query,
        "page": {
            "pageNumber": 1,
            "pageSize": 5000
        },
        "includeSynthetic": False
    }
)

print("Código de respuesta:", response.status_code)

if response.ok:

    data = response.json()

    df = pd.DataFrame(data)

    print("\nCantidad de registros:", len(df))

    print("\nColumnas:")
    print(df.columns.tolist())

    print("\nPrimeros registros:")
    print(df.head())

    # Guardar los datos
    ruta = "data/raw/transacciones_igac.csv"

    df.to_csv(ruta, index=False)

    print("\nArchivo guardado correctamente en:")
    print(ruta)

else:

    print("\nError:")
    print(response.text)