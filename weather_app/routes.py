from datetime import date
import json
import geocoder
from flask.helpers import url_for
import requests
from requests.api import get
from . import app
from flask import render_template
from flask import request, redirect, url_for, jsonify, make_response
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
        if wdata != None:
            return render_template('results.html', city=city, wdata=wdata)
        else:
            return 'City Not Found!'
    return redirect(url_for('index'))

@app.route('/full_forcast/<city>')
def full_forcast(city):
    wdata = get_data(city)
    return render_template('full.html', wdata=wdata, city=city)

@app.route('/get_weather', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        lat = req['lon']
        lon = req['lat']
        data = geocoder.google([lat, lon], method='reverse')
        print('I have got a requests!', data)
        res = make_response(jsonify(data), 200)
        return res
    else:
        return redirect(url_for('index'))

key = 'AIzaSyCvGDh1g1f-PhndHdg6SBWd_qxeT_XmwKY'