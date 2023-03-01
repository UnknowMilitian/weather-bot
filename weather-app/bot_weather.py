from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
import requests
from pprint import pprint
import datetime


# Wetather token
from config import open_weather_token


# TODO ---------------------- Main variables ----------------------

bot = Bot(TOKEN_API)
dispatcher = Dispatcher(bot)


# ? List of Help commands for tg-bot
HELP_COMMAND = """
<b>/start</b> - <em>Hello welcome to my bot, start the working</em>
<b>/help</b> - <em>list commands</em>
<b>/description</b> - <em>Author: Umariy Jaloliddin</em>
<b>/photo</b> - <em>bot send picture</em>
"""


# ! ---------------------- Dispatcher functions ----------------------

async def on_startup(_):
    print('\nBot was launched successfully !!!\n')


@dispatcher.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello, welcome to my bot !!! \nYou can asck me about weather \nSend me name of city')


@dispatcher.message_handler()
async def get_weather(message: types.Message):
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
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
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

        await message.reply(
                f"*** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ***"
                f"\nWeather today in city '{city}'\nTemperature: {cur_weather} - C* {wd}\nHumidity: {humidity}\nPressure: {pressure}\nWind: {wind}\n"
                f"Sunrise: {sunrise_timestamp}\n"
                f"Sunrise: {sunset_timestamp}\n"
                f"Length of the day: {length_of_day_the_day}\n")

    except:
        await message.reply('Something was went wrong \U00002620 !!!')



# ? ---------------------- When loading the server ----------------------

if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=on_startup, skip_updates=True)