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
    try:
        temp =  data['list'][0]['main']['temp']
        feels_like = data['list'][0]['main']['feels_like']
        temp_min = data['list'][0]['main']['temp_min']
        temp_max = data['list'][0]['main']['temp_max']
        City = data['city']['name']
        weather = {
            'City' : City,
            'temp' : temp,
            'feels_like': feels_like,
            'temp_min': temp_min,
            'temp_max': temp_max 
        }
    except:
        weather = "City Not Found"
    return weather
