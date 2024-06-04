from fastapi import FastAPI
from typing import Tuple
from urllib.parse import quote
import subprocess
import json

# Crea una instancia de FastAPI
app = FastAPI()

@app.get("/coordinates/{city}")
async def get_coordinates(city: str) -> Tuple[float, float]:
    """
    Function that returns the latitude and longitude of a given city

    Parameters:
    city (str): The city name to search for

    Returns:
    tuple: The latitude and longitude of the city

    Raises:
    Exception: If the city is not found
    """
    # Encode the city parameter
    encoded_city = quote(city)

    # Uses the curl to make the API request
    curl_command = f'curl "https://nominatim.openstreetmap.org/search?q={encoded_city}&format=json"'
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    data = json.loads(result.stdout)
    if data:
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])

        return latitude, longitude
    else:
        raise Exception(f"No coordinates found for {city}")
