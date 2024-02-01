import requests
import sys

def get_coordinates(api_key, address):
    """
    Retrieves geographical coordinates (latitude and longitude) for a given address using the Google Maps Geocoding API.

    Parameters:
    api_key (str): API key for authenticating with the Google Maps Geocoding API.
    address (str): The address for which geographical coordinates are required.

    Returns:
    dict: A dictionary containing the latitude and longitude of the given address.
          Returns None if the API call is unsuccessful or no results are found.
    """
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": api_key}
    response = requests.get(endpoint, params=params)
    data = response.json()

    if response.status_code == 200 and data['results']:
        return data['results'][0]['geometry']['location']
    else:
        # You can print data here to inspect what's returned
        print("Error or no results:", data)
        return None

def get_weather(api_key, lat, lon):
    """
    Fetches the current weather data for a specified latitude and longitude using the OpenWeather API.

    Parameters:
    api_key (str): API key for authenticating with the OpenWeather API.
    lat (float): Latitude of the location for which weather data is required.
    lon (float): Longitude of the location for which weather data is required.

    Returns:
    json: The response from the OpenWeather API in JSON format, containing current weather data.
          Returns None if the API call is unsuccessful.
    """
    endpoint = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
