import requests
from pprint import pprint
import datetime
from config import open_weather_token


# ? -------- Weather coding ... --------

def get_weather(city, open_weather_token):

    code_to_smile = {
        'Clear': 'Sunny \U00002600',
        'Clouds': 'Clouds \U00002601',
        'Rain': 'Sunny \U00002614',
        'Drizzle': 'Sunny \U00002614',
        'Thunderstorm': 'Thunder \U000026A1',
        'Snow': 'Snow \U0001F328',
        'Mist': 'Mist \U0001F32B'
    }

    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data = r.json()

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Im dont know, watch to the mirrow"
        
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day_the_day = (datetime.datetime.fromtimestamp(data['sys']['sunset'])) - (datetime.datetime.fromtimestamp(data['sys']['sunrise']))

        print('\n-----------')
        print(f'\nWeather today in city: {city}\nTemperature: {cur_weather} C* {wd}\nHumidity: {humidity}\nPressure: {pressure}\nWind: {wind}\n'
              f"Sunrise: {sunrise_timestamp}\n"
              f"Sunrise: {sunset_timestamp}\n"
              f"Length of the day: {length_of_day_the_day}\n")

    except Exception as ex:
        print(ex)


def main():
    city = input('Write the city: ')
    get_weather(city, open_weather_token)



# ? ---------------------- When loading the server ----------------------

if __name__ == '__main__':
    main()