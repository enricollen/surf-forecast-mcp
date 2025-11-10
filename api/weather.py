"""
weather forecast api client
"""

import requests
from pydantic import ValidationError
from models import WeatherResponse


def fetch_weather_forecast(latitude: float, longitude: float) -> WeatherResponse:
    """
    fetch weather forecast data from open-meteo api with validation
    
    args:
        latitude: latitude coordinate
        longitude: longitude coordinate
    
    returns:
        validated weather response
    
    raises:
        requests.HTTPError: if api request fails
        ValidationError: if api response doesn't match expected schema
    """
    # open-meteo weather api endpoint
    url = "https://api.open-meteo.com/v1/forecast"
    
    # parameters for the api request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": [
            "temperature_2m",
            "windspeed_10m",
            "winddirection_10m",
            "windgusts_10m"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "windspeed_10m_max",
            "winddirection_10m_dominant",
            "windgusts_10m_max"
        ],
        "windspeed_unit": "kn",  # knots for surfing
        "timezone": "auto",
        "forecast_days": 7
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    # validate response
    try:
        return WeatherResponse(**response.json())
    except ValidationError as e:
        raise ValueError(f"invalid weather api response: {e}")
