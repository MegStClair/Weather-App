from flask import Flask, render_template, request

import os
import requests

import math

from datetime import datetime

app = Flask(__name__)


@app.route('/weather')
def show_weather():
    """Show weather homepage."""

    return render_template('weather.html')


@app.route('/search', methods=['POST'])
def search_location():
    """Get location input."""

    zipcode = request.form.get('search')
    # export API_KEY='118df5d154ef4d25ebf3ec36bad1180e'
    key = os.environ['API_KEY']

    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={key}'

    response = requests.get(url)
    data = response.json()
    print(data)

    lat = data['lat']
    lon = data['lon']

    url_forecast = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,minutely&appid={key}'

    response_forecast = requests.get(url_forecast).json()
    print(response_forecast)

    city = data['name']
    print(city)

    temp = round(response_forecast['current']['temp'])
    print(temp)

    weather = response_forecast['current']['weather'][0]['description']
    print(weather)

    icon = response_forecast['current']['weather'][0]['icon']
    print(icon)

    temp_min = round(response_forecast['daily'][0]['temp']['min'])
    print(temp_min)

    temp_max = round(response_forecast['daily'][0]['temp']['max'])
    print(temp_max)

    humidity = response_forecast['current']['humidity']
    print(humidity)

    sunrise = response_forecast['current']['sunrise']
    sunset = response_forecast['current']['sunset']

    print(datetime.fromtimestamp(sunrise).strftime('%-I:%M %p'))
    print(datetime.fromtimestamp(sunset).strftime('%-I:%M %p'))

   
    
    

   
    return render_template('weather.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
