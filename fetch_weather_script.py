import requests
import math


def fetch_weather():
    city = 'hyderabad'
    api_key = '6299531ea6be344044a98940a5e8bb6c'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={17.40}&lon={78.47}&appid={api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        weather = data['weather'][0]['description']
        curr_temp = data['main']['temp'] - 273.15
        city = data['name']
        print(f'weather: {weather}\ncurrent temperature: {curr_temp:0,.2f}')

    except Exception as err:
        print('Error occurred !!')


fetch_weather()

