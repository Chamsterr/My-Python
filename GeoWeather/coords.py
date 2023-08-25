import requests
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Coordinates():
	longitude: float
	latitude: float

def get_gps_coordinates() -> Coordinates:
	response = requests.get("https://ipinfo.io/json")
	latitude, longitude = data["loc"].split(",")
	data = response.json()
	return Coordinates(longitude=longitude, latitude=latitude)
