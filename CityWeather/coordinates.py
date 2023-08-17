import geocoder # type: ignore

from dataclasses import dataclass
from exceptions import CantGetCoordinates

from exceptions import CantGetCoordinates

@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_city_coordinates(city: str) -> Coordinates:
    g = geocoder.arcgis(city)

    if g.latlng:
        latitude, longitude = g.latlng
        return Coordinates(longitude, latitude)
    else:
        raise CantGetCoordinates


if __name__ == "__main__":
    city = input("Введите название города: ")
    print(get_city_coordinates(city))