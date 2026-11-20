
import requests


def get_weather_description(code):
    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Heavy Drizzle",
        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Slight Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Rain Showers",
        81: "Moderate Rain Showers",
        82: "Heavy Rain Showers",
        95: "Thunderstorm",
        96: "Thunderstorm with Hail",
        99: "Heavy Thunderstorm with Hail"
    }

    return weather_codes.get(code, "Unknown Weather")


def get_weather(city):
    try:
        # Step 1: Find the city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 10,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url, params=geo_params, timeout=10
        )
        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            print("City not found. Please try again.")
            return

        # Prefer an Indian city when there are multiple matches
        location = next(
            (
                place for place in geo_data["results"]
                if place.get("country_code") == "IN"
            ),
            geo_data["results"][0]
        )

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "Unknown")

        # Step 2: Fetch current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url, params=weather_params, timeout=10
        )
        weather_response.raise_for_status()

        weather_data = weather_response.json()
        current = weather_data["current"]

        # Step 3: Get weather description
        code = current["weather_code"]
        description = get_weather_description(code)

        # Step 4: Display weather report
        print("\n========== WEATHER REPORT ==========")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {current['temperature_2m']} °C")
        print(f"Feels Like: {current['apparent_temperature']} °C")
        print(f"Humidity: {current['relative_humidity_2m']} %")
        print(f"Wind Speed: {current['wind_speed_10m']} km/h")
        print(f"Weather: {description}")
        print("====================================")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Internet connection error. Check your network.")

    except requests.exceptions.HTTPError:
        print("Weather service returned an error.")

    except requests.exceptions.RequestException as error:
        print("Unable to fetch weather information.")
        print("Error:", error)

    except (KeyError, IndexError, TypeError, ValueError):
        print("Unable to process weather information.")


# Main program
def main():
    print("\n================================")
    print("       WELCOME TO WEATHER APP")
    print("================================")

    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
