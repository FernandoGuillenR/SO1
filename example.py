import subprocess
import json
from urllib.parse import quote


def get_coordinates(query):
    """
    Function that returns the latitude and longitude of a given query

    Parameters:
    query (str): The query to search for

    Returns:
    tuple: The latitude and longitude of the query

    Raises:
    Exception: If the query is not found
    """

    # Encode the query parameter
    encoded_query = quote(query)

    # Uses the curl to make the API request
    curl_command = f'curl "https://nominatim.openstreetmap.org/search?q={encoded_query}&format=json"'
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    data = json.loads(result.stdout)
    if data:
        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])

        return latitude, longitude

