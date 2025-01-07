import requests
from dotenv import load_dotenv #get our env var value
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n***Get Current Weather conditions***\n')

    city=input("\nPlease enter a city name:\n")


    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API KEY")}&q={city}&units=metric'

    #print(request_url)

    weather_data = requests.get(request_url).json()

    pprint(weather_data)

get_current_weather()