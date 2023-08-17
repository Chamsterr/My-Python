from exceptions import ApiServiceError, CantGetCoordinates
from coordinates import get_city_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from history import PlainFileWeatherStorage, JSONFileWeatherStorage, save_weather
from pathlib import Path

def main()->None:
    try:
        city = input("Введите название города: ")
        coordinates = get_city_coordinates(city)
    except CantGetCoordinates:
        print("Не смог получить GPS-координаты")
        exit(1)

    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print("Не смог получить погоду в API-сервисе погоды")
        exit(1)

    save_weather(
        weather,
        PlainFileWeatherStorage(Path.cwd() / "history.txt")
    )

    save_weather(
        weather,
        JSONFileWeatherStorage(Path.cwd() / "history.json")
    )


    print(format_weather(weather))

if __name__ == "__main__":
    main()