# 🏄 Surf Forecast MCP Server

An MCP server that provides comprehensive surf forecasts for any coastal location worldwide. Get current conditions and 5-day predictions including wave heights, periods, directions, wind conditions, and intelligent surf quality assessments.

## ✨ Features

- 🌊 **Current surf conditions** - real-time wave height, period, and direction
- 💨 **Wind conditions** - wind speed, direction, and gusts in knots
- 🌡️ **Temperature data** - air temperature for planning your session
- 📅 **5-day forecast** - daily predictions for planning your surf sessions
- 📍 **City name input** - simply provide a city name (e.g., "Livorno", "San Diego")
- 🎯 **Automatic geocoding** - converts city names to coordinates
- 📊 **Structured output** - clean pydantic models for easy integration
- ✅ **Data validation** - comprehensive pydantic validation for data quality
- 🏄 **Surf quality assessment** - intelligent interpretation of conditions for surfing

## 🚀 Quick Start

### local development

1. install dependencies:

```bash
pip install -r requirements.txt
```

2. run the server:

```bash
python server.py
```

3. connect with an mcp client (e.g., claude desktop, cline, MCP Client SDK, etc.)

### cloud deployment

deploy to fastmcp cloud in minutes:

1. create a [fastmcp cloud account](http://fastmcp.cloud/signup)
2. connect your github account
3. deploy this repository
4. your server will be available instantly to any mcp client

## 🔧 MCP Primitives

This server provides three MCP primitives:

### Tool
**`get_surf_forecast`** - get comprehensive surf forecast for any location

```python
# mcp tool call
get_surf_forecast("Livorno")

# returns validated SurfForecast object with:
# - location and coordinates
# - current wave, wind, and temperature conditions
# - 5-day daily forecasts
# - surf quality assessment
```

### Resource
**`surf://info`** - provides server information including capabilities, data sources, and usage guidelines

### Prompt
**`analyze_surf_conditions`** - generates a structured prompt for analyzing surf conditions at a specific location, guiding the llm to provide actionable recommendations including quality assessment, timing, trends, and skill level guidance

## 📁 Project Architecture

Clean separation of concerns with modular design:

```
surf-forecast-mcp/
├── server.py              # mcp server with tool definitions
├── models/
│   └── __init__.py       # pydantic data models with validation
├── api/
│   ├── __init__.py       # api client exports
│   ├── geocoding.py      # geocoding api client (nominatim)
│   ├── marine.py         # marine weather api client (open-meteo)
│   └── weather.py        # weather forecast api client (open-meteo)
├── services/
│   ├── __init__.py       # service exports
│   └── forecast.py       # surf forecast business logic
├── example.py            # usage examples
└── requirements.txt      # dependencies
```

**Separation of Concerns:**
- `models/` - data structures and validation rules
- `api/` - external integrations, api clients
- `services/` - business logic, data transformation
- `server.py` - mcp interface, tool definitions only

## 📊 Data Returned

### Tool: get_surf_forecast

Get comprehensive surf forecast for any location.

**Parameters:**
- `city_name` (str): name of the coastal city/location (e.g., "livorno", "biarritz", "san diego")

**Returns structured forecast with:**

#### Current Conditions (Hourly)
- wave height (meters)
- swell wave height (meters)
- wind wave height (meters)
- wave direction (degrees)
- swell wave direction (degrees)
- wave period (seconds)
- swell wave period (seconds)
- wind speed (knots)
- wind direction (degrees)
- wind gusts (knots)
- air temperature (celsius)

#### 5-Day Forecast (Daily)
For each day:
- maximum wave height (meters)
- maximum swell wave height (meters)
- maximum wind wave height (meters)
- dominant wave direction (degrees)
- dominant swell wave direction (degrees)
- maximum wave period (seconds)
- maximum swell wave period (seconds)
- maximum wind speed (knots)
- dominant wind direction (degrees)
- maximum wind gusts (knots)
- maximum temperature (celsius)
- minimum temperature (celsius)

#### Additional Info
- location coordinates (latitude/longitude)
- surf quality assessment and notes

### Example Output

The tool returns formatted text optimized for LLM context consumption:

```
# Surf Forecast: Livorno, Toscana, Italia
Location: 43.5484, 10.3116

## Current Conditions
Waves: 1.2m (9s period)
  - Swell: 0.9m from W
  - Wind waves: 0.3m
Wind: 9 knots from W (gusts 12 knots)
Temperature: 19°C

## Next Hours
03:00: 1.3m waves (swell 1.0m from W), 10kn wind from W
06:00: 1.4m waves (swell 1.1m from W), 11kn wind from W
09:00: 1.5m waves (swell 1.2m from WSW), 12kn wind from NW
12:00: 1.6m waves (swell 1.2m from WSW), 11kn wind from NW

## 5-Day Forecast
2025-11-10:
  Waves: 1.5m max (swell 1.1m from W)
  Wind: 12 knots from W
  Temp: 16-22°C
2025-11-11:
  Waves: 1.8m max (swell 1.4m from WSW)
  Wind: 10 knots from NW
  Temp: 15-21°C
2025-11-12:
  Waves: 1.6m max (swell 1.2m from W)
  Wind: 8 knots from N
  Temp: 14-20°C
2025-11-13:
  Waves: 1.4m max (swell 1.0m from WNW)
  Wind: 11 knots from NE
  Temp: 15-19°C
2025-11-14:
  Waves: 1.7m max (swell 1.3m from W)
  Wind: 13 knots from E
  Temp: 16-21°C

## Surf Quality
good wave height for most surfers | light breeze - good conditions | moderate period - decent wave quality | swell dominant - cleaner conditions
```

**Why this format?**
- ✓ Concise and human-readable
- ✓ Context-efficient (~200-300 tokens vs 2000+ for JSON)
- ✓ Easy for LLMs to parse and reason about

## ✅ Data Validation

All data is validated using Pydantic models.

## 🌐 Data Sources

This server combines data from two Open-Meteo APIs:

### Marine Weather API
[Open-Meteo Marine API](https://open-meteo.com/en/docs/marine-weather-api) provides:
- Global coverage at 5km resolution
- Hourly and daily wave forecasts
- Multiple wave parameters (significant height, swell, wind waves)
- Wave direction and period data

### Weather Forecast API
[Open-Meteo Weather API](https://open-meteo.com/en/docs) provides:
- Wind speed, direction, and gusts (in knots)
- Air temperature
- Hourly and daily forecasts

Both APIs are free for non-commercial use.

---

*built with [FastMCP](https://gofastmcp.com/) and powered by [Open-Meteo](https://open-meteo.com/)*