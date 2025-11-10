"""
geocoding api client for converting city names to coordinates
"""

from geopy.geocoders import Nominatim


def geocode_location(city_name: str) -> tuple[float, float, str]:
    """
    convert city name to latitude and longitude coordinates
    
    args:
        city_name: name of the city or location
    
    returns:
        tuple of (latitude, longitude, full_location_name)
    
    raises:
        ValueError: if location cannot be found
    """
    geolocator = Nominatim(user_agent="surf_forecast_mcp")
    location = geolocator.geocode(city_name)
    
    if location is None:
        raise ValueError(f"could not find location: {city_name}")
    
    return location.latitude, location.longitude, location.address
