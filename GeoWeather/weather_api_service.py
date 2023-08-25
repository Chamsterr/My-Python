from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias

from coords import Coordinates
from enum import Enum

Celsius: TypeAlias = int

class WeatherType(Enum):
	THUNDERSTORM = "Гроза"
	DRIZZLE = "Изморось"
	RAIN = "Дождь"
	SNOW = "Снег"
	CLEAR = "Ясно"
	FOG = "Туман"
	CLOUDS = "Облачно"
        
@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius    
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(cordinates: Coordinates):
    """Requests weather in OpenWeather API and returns it"""
    ...

for w in WeatherType:
    print(w)