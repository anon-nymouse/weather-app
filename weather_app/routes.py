from . import app
from quart import render_template
from weather_app.scripts.get_data import get_location, get_data


api_key = 'c46121cc1ced83e6bc7281bcb5592ca0'

@app.route('/')
async def index():
    city = get_location()
    data = get_data(city)
    return await render_template('index.html', data=data)
