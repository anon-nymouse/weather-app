import requests
from . import app
from flask import render_template
from flask import request
from weather_app.scripts.get_data import get_location, get_data
from weather_app.scripts.get_wdata import get_wdata


api_key = 'c46121cc1ced83e6bc7281bcb5592ca0'

@app.route('/')
def index():
    city = get_location()
    data = get_data(city)
    return render_template('index.html', data=data)

@app.route('/search', methods=['GET','POST'])
def search():
    city = request.args.get('city')
    data = get_wdata(city)
    return data
