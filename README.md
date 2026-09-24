# Informe de Regresión Lineal

## Análisis de transacciones inmobiliarias en Colombia

Proyecto académico de análisis y modelado mediante Regresión Lineal,
utilizando datos abiertos del Instituto Geográfico Agustín Codazzi (IGAC).

## Objetivo

Analizar en qué medida algunas características de las transacciones
inmobiliarias permiten explicar el valor registrado de las operaciones
de compraventa en Colombia.

## Fuente de datos

Los datos fueron obtenidos mediante la API de Datos Abiertos de Colombia,
a partir del conjunto de datos de registro de transacciones inmobiliarias
del IGAC.

Para el análisis se seleccionaron registros que:

- Corresponden a operaciones de COMPRAVENTA.
- Tienen un valor registrado.
- Presentan un valor mayor que cero.

Inicialmente se obtuvieron 5.000 registros. Después del proceso de
limpieza se utilizaron 4.997 registros para el modelado.

## Variables

### Variable objetivo

- `valor`: valor registrado de la transacción inmobiliaria.

### Variables predictoras

- `year_radica`: año de registro de la transacción.
- `count_a`: cantidad de receptores.
- `count_de`: cantidad de otorgantes.
- `tipo_predio_zona`: zona del predio.

La variable `tipo_predio_zona` fue transformada a una variable numérica
para su utilización en el modelo.

## Metodología

El proyecto incluye las siguientes etapas:

1. Recolección de datos mediante API.
2. Limpieza y preparación de los datos.
3. Análisis exploratorio de datos (EDA).
4. Selección y transformación de variables.
5. División de los datos en entrenamiento y prueba.
6. Ajuste de un modelo de Regresión Lineal.
7. Generación de predicciones.
8. Evaluación mediante MAE, MSE, RMSE y R².
9. Análisis de residuos.
10. Comparación entre valores reales y predichos.

## Tecnologías utilizadas

- Python 3.10+
- pandas
- numpy
- scikit-learn
- matplotlib
- requests
- python-dotenv

## Estructura del proyecto

```text
Informe_Regresion_Lineal/
│
├── Data/
│   └── raw/
│       └── transacciones_igac.csv
│
├── Figuras/
│
├── Notebooks/
│   └── 01_analisis_regresion.ipynb
│
├── Src/
│   └── recoleccion.py
│
├── .gitignore
├── README.md
└── requirements.txt