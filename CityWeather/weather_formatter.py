from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    """Formats weather in string"""
    return(f"{weather.city}, температура {weather.temperature}°C, "
           f"{weather.weather_type} \n"
           f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
           f"Закат: {weather.sunset.strftime('%H:%M')}\n")