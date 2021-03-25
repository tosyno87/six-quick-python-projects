import os
import requests
from pprint import pprint
from decouple import config

key = config('WEATHER_API_KEY')
city = input("Enter a city: ")
base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}"
weather_data = requests.get(base_url).json()

# pprint(weather_data)
print(weather_data['weather'][0]['description'])