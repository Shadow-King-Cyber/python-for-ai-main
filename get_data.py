"""Descarga el clima de la última semana en Panamá, lo grafica y lo guarda."""
from datetime import datetime, timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests

# Carpeta de salida junto a este script (no depende del directorio actual)
DATA_DIR = Path(__file__).resolve().parent / "data"

# Panamá (latitud, longitud)
LATITUDE = 8.98
LONGITUDE = -79.52


def fetch_weather() -> dict:
    """Pide a Open-Meteo las temperaturas máx/mín de los últimos 7 días."""
    today = datetime.now()
    week_ago = today - timedelta(days=7)

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        f"&start_date={week_ago:%Y-%m-%d}&end_date={today:%Y-%m-%d}"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()  # lanza un error si el código HTTP no es 200
    return response.json()


def build_dataframe(data: dict) -> pd.DataFrame:
    """Convierte la respuesta de la API en un DataFrame con el promedio diario."""
    daily = data["daily"]
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(daily["time"]),
            "max_temp": daily["temperature_2m_max"],
            "min_temp": daily["temperature_2m_min"],
        }
    )
    df["avg_temp"] = (df["max_temp"] + df["min_temp"]) / 2
    return df


def plot_weather(df: pd.DataFrame, output_path: Path) -> None:
    """Genera y guarda la gráfica de temperaturas."""
    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["max_temp"], "r-o", label="Máx")
    plt.plot(df["date"], df["min_temp"], "b-o", label="Mín")
    plt.plot(df["date"], df["avg_temp"], "g--", label="Promedio")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.title("Clima de Panamá - Última semana")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    try:
        data = fetch_weather()
    except requests.exceptions.RequestException as error:
        print(f"No se pudo obtener el clima: {error}")
        return

    if "daily" not in data:
        print(f"Respuesta inesperada de la API: {data}")
        return

    df = build_dataframe(data)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    plot_weather(df, DATA_DIR / "clima_panama.png")
    df.to_csv(DATA_DIR / "clima_panama.csv", index=False)

    print(f"Temperatura promedio: {df['avg_temp'].mean():.1f}°C")
    print(f"Archivos guardados en: {DATA_DIR}")


if __name__ == "__main__":
    main()
