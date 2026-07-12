# python-for-ai

Proyecto de práctica con tres ejercicios de Python:

- **`hello.py`** — Lee variables de entorno desde un archivo `.env`.
- **`get_data.py`** — Descarga el clima de la última semana en Panamá (API Open-Meteo), lo grafica y guarda los resultados.
- **`sales-analysis/`** — Lee ventas desde un CSV, calcula totales y muestra un resumen.

## Requisitos

- Python 3.10 o superior

## Instalación

```bash
# 1. Crear y activar un entorno virtual
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt
```

## Configuración

Copia la plantilla de variables de entorno y completa tus valores:

```bash
# Windows:
copy .env.example .env
# Linux / macOS:
cp .env.example .env
```

El archivo `.env` no se sube a git porque puede contener datos privados.

## Uso

```bash
# Variables de entorno
python hello.py

# Clima de Panamá (genera data/clima_panama.png y data/clima_panama.csv)
python get_data.py

# Análisis de ventas
python sales-analysis/analyzer.py
```

Cada script se puede ejecutar desde cualquier carpeta: las rutas se resuelven
automáticamente respecto a la ubicación del archivo.

## Estructura

```
python-for-ai/
├── hello.py
├── get_data.py
├── requirements.txt
├── .env.example
└── sales-analysis/
    ├── analyzer.py
    ├── helpers.py
    └── data/
        └── sales.csv
```
