"""
surf forecast mcp server - provides wave and surf conditions for any location
"""

from fastmcp import FastMCP
from models import SurfForecast
from api import geocode_location, fetch_marine_forecast, fetch_weather_forecast
from services import ForecastService

# create server
mcp = FastMCP("Surf Forecast Server")


@mcp.tool()
def get_surf_forecast(city_name: str) -> str:
    """
    get surf forecast for a location by city name.
    
    returns current conditions and 5-day forecast including:
    - wave heights (total, swell, wind waves) with directions
    - wind speed and direction (in knots) with gusts
    - air temperature
    - surf quality assessment
    
    the forecast is returned as formatted text optimized for llm context,
    with compass directions (n, s, e, w, etc) for easy interpretation.
    
    args:
        city_name: name of the city/location (e.g., "livorno", "san diego", "biarritz")
    
    returns:
        formatted surf forecast text optimized for llm consumption
    """
    # geocode the location
    latitude, longitude, full_location = geocode_location(city_name)
    
    # fetch marine and weather forecast data
    marine_data = fetch_marine_forecast(latitude, longitude)
    weather_data = fetch_weather_forecast(latitude, longitude)
    
    # parse and structure the data
    forecast = ForecastService.parse_forecast_data(
        marine_data,
        weather_data,
        full_location,
        latitude,
        longitude
    )
    
    # return as llm-optimized text format
    return forecast.to_llm_context()