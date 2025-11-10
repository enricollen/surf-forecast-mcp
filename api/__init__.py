"""
api clients for external services
"""

from .marine import fetch_marine_forecast
from .weather import fetch_weather_forecast
from .geocoding import geocode_location

__all__ = [
    "fetch_marine_forecast",
    "fetch_weather_forecast",
    "geocode_location"
]