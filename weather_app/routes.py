from datetime import date
import json
from flask.helpers import url_for
import requests
from requests.api import get
from . import app
from flask import render_template
from flask import request, redirect, url_for
from weather_app.scripts.get_data import get_location, get_data

api_key = 'c46121cc1ced83e6bc7281bcb5592ca0'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        city = request.form.get('city')
        wdata = get_data(city)
        return render_template('results.html', city=city, wdata=wdata)
    return redirect(url_for('index'))

@app.route('/full_forcast/<city>')
def full_forcast(city):
    wdata = get_data(city)
    return render_template('full.html', wdata=wdata, city=city)

@app.route('/get_weather', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        data = {'lat': lat, 'lon': lon}
        return data
    else:
        return redirect(url_for('index'))