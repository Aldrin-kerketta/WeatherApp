import requests
import math


def fetch_weather(city):
    api_key = 123
    url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'

    try:
        response = requests.get(url)
        data = response.json()
        weather = data['weather'][0]['description']
        curr_temp = data['main']['temp'] - 273.15
        city = data['name']
        return {'weather': weather,
                'curr_temp': float(str(curr_temp)[:5]),
                'city': city}
    except Exception as err:
        print('Error occurred !!', err)

# print(fetch_weather('Rourkela'))
