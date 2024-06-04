from fastapi import FastAPI
from typing import Tuple
from urllib.parse import quote
import subprocess
import json
from cachetools import cached, TTLCache

# Crea una instancia de FastAPI
app = FastAPI()

cache = TTLCache(maxsize=128, ttl=3600)


@app.get("/coordinates/{city}")
def get_coordinates(city: str) -> Tuple[float, float]:
    """
    Function that returns the latitude and longitude of a given city

    Parameters:
    city (str): The city name to search for

    Returns:
    tuple: The latitude and longitude of the city

    Raises:
    Exception: If the city is not found
    """
    # Utiliza la caché para obtener las coordenadas si están disponibles
    if city in cache:
        return cache[city]

    encoded_city = quote(city)

    curl_command = f'curl "https://nominatim.openstreetmap.org/search?q={encoded_city}&format=json"'
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    data = json.loads(result.stdout)
    if data:
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])

        cache[city] = (latitude, longitude)

        return latitude, longitude
    else:
        raise Exception(f"No coordinates found for {city}")
