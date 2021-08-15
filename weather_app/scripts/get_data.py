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

city = 'patnitola'
data = get_data('london')
print(data)