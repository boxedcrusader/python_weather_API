import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

try:
    city_name = input("\nEnter the city name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\nThe weather in {city_name} is currently {description} with a temperature of {temp}°C and humidity of {humidity}%.")
except KeyError:
    print(f"City '{city_name}' not found. Check the spelling.")
except requests.exceptions.ConnectionError:
    print("No internet connection.")