import json
import urllib.request
from dataclasses import dataclass

WEATHER_API_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=40.7128&longitude=-74.006"
    "&current=temperature_2m,weather_code"
    "&daily=temperature_2m_max"
    "&timezone=America/New_York"
    "&forecast_days=1"
)


@dataclass
class WeatherData:
    current_temp: int
    max_temp: int
    weather_code: int


def fetch_weather() -> WeatherData | None:
    try:
        resp = urllib.request.urlopen(WEATHER_API_URL, timeout=10)
        data = json.loads(resp.read().decode())
        return WeatherData(
            current_temp=round(data["current"]["temperature_2m"]),
            max_temp=round(data["daily"]["temperature_2m_max"][0]),
            weather_code=int(data["current"]["weather_code"]),
        )
    except Exception:
        return None
