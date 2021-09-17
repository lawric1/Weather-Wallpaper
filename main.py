import requests
import random
import datetime
import secrets

def getWeather():
    city = 'recife'
    apiKey = secrets.APIKEYS['open-weather']

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}'

    r = requests.get(url).json()['weather'][0]['main']

    return r

def getTimePeriod():
    now = datetime.datetime.now()

    if 5 <= now.hour < 12:
        return 'Morning'
    elif 12 <= now.hour < 18:
        return 'Noon'
    else:
        return 'Night'

def getRandomWallpaper():
    apiKey = secrets.APIKEYS['pexels']
    header = {
        'Authorization' : apiKey
    }

    weather = getWeather()
    period = getTimePeriod()
    page = random.randint(0,5)
    n = random.randint(0,80)

    url = f"https://api.pexels.com/v1/search?query={weather}%20{period}&orientation=landscape&size=large&page={page}&per_page=80"    

    r = requests.get(url, headers=header).json()['photos'][n]['src']['landscape']

    return r, weather, period

print(getRandomWallpaper())
