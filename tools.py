import requests

API_KEY: str = "83fdb2621eb645fa8ed152414252911"  # твой ключ, можно оставить этот
BASE_URL: str = "http://api.weatherapi.com/v1/current.json"


def getWeather(city: str) -> str:
    """
    1. City name
    2. Temperature (°C)
    3. Condition (condition)
    4. Humidity
    5. Wind speed
    """
    if not isinstance(city, str) or len(city.strip()) == 0:
        raise ValueError("city must be non-empty string")

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no",
    }

    try:
        resp = requests.get(BASE_URL, params=params, timeout=5)
    except requests.RequestException as e:
        raise RuntimeError(f"Request error: {e}") from e

    try:
        data = resp.json()
    except ValueError as e:
        raise RuntimeError("Bad JSON from Weather API") from e

    if isinstance(data, dict) and "error" in data:
        msg = data["error"].get("message", "Unknown API error")
        raise ValueError(f"API error: {msg}")

    location = data.get("location", {})
    current = data.get("current", {})

    city_name = location.get("name", "Unknown city")
    country = location.get("country", "")

    temp_c = current.get("temp_c", "?")
    condition = (current.get("condition") or {}).get("text", "Unknown")
    humidity = current.get("humidity", "?")
    wind_kph = current.get("wind_kph", "?")

    result_lines = [
        f"City: {city_name}, {country}",
        f"Temperature: {temp_c} °C",
        f"Condition: {condition}",
        f"Humidity: {humidity}%",
        f"Wind speed: {wind_kph} kph",
    ]

    return "\n".join(result_lines)
