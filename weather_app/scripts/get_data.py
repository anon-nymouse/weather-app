import requests
import json

def get_location():
    url = 'https://ipinfo.io/city'
    c = requests.get(url)
    city = c.text.replace(" ", "%20")
    return city

def get_data(city):
    api_key = 'c46121cc1ced83e6bc7281bcb5592ca0'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    data = requests.get(url).json()
    weather = []
    try:
        for i in range(len(data['list'])):
            temp =  data['list'][i]['main']['temp']
            feels_like = data['list'][i]['main']['feels_like']
            temp_min = data['list'][i]['main']['temp_min']
            temp_max = data['list'][i]['main']['temp_max']            
            w = data['list'][i]['weather'][0]['main']
            w0 = data['list'][i]['weather'][0]['description']
            time = data['list'][i]['dt_txt']
            weather_data = {
                'dt_txt': time,
                'temp' : temp,
                'feels_like': feels_like,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'w': w,
                'w0': w0  
                }
            weather.append(weather_data)
        return weather
    except:
        weather = None
    return weather

def get_data_from_lat_lon(lat, lon):
    api_key = 'c46121cc1ced83e6bc7281bcb5592ca0'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    data = requests.get(url).json()
    latt = data['lat']
    lonn = data['lon']
    temp =  data['current']['temp']
    feels_like = data['current']['feels_like']
    humidiy = data['current']['humidity']
    clouds = data['current']['clouds']            
    w = data['current']['weather'][0]['main']
    w0 = data['current']['weather'][0]['description']

    weather_data = {
        'url': url,
        'latt': latt,
        'lonn': lonn,
        'temp' : temp,
        'feels_like': feels_like,
        'humidity': humidiy,
        'clouds': clouds,
        'w': w,
        'w0': w0,
        }
    return weather_data




qdata = get_data_from_lat_lon(25.0513469, 88.7622938)
print(qdata)