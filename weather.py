import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def get_curr_weather(city=''):
    if not bool(city.strip()):
        city = 'Mumbai'
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == '__main__':
    get_curr_weather()