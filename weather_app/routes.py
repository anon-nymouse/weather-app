import re
from flask.helpers import url_for
import requests
from . import app
from flask import render_template
from flask import request, redirect, url_for
from weather_app.scripts.get_data import get_location, get_data

api_key = 'c46121cc1ced83e6bc7281bcb5592ca0'

@app.route('/')
@app.route('/index')
def index():
    #city = get_location()
    #data = get_data(city)
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        city = request.form.get('city')
        data = get_data(city)
        return render_template('results.html', city=city, data=data)
    return redirect(url_for('index'))

@app.route('/get_weather', methods=['GET', 'POST'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return render_template('res.html', lat=lat, lon=lon)