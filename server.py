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
    
    print(lat)
    print(lon)

    url_current = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

    response_current = requests.get(url_current).json()

    print(response_current)

    city = response_current['name']
    print(city)

    temp = response_current['main']['temp']
    temp = round((temp * 1.8) - 459.67)  # convert k to f
    print(temp)

    weather = response_current['weather'][0]['description']
    print(weather)

    icon = response_current['weather'][0]['icon']

    temp_min = response_current['main']['temp_min']
    temp_min = round((temp_min * 1.8) - 459.67)

    temp_max = response_current['main']['temp_max']
    temp_max = round((temp_max * 1.8) - 459.67)

    humidity = response_current['main']['humidity']

    sunrise = response_current['sys']['sunrise']
    sunset = response_current['sys']['sunset']

    print(datetime.fromtimestamp(sunrise).strftime('%-I:%M %p'))
    print(datetime.fromtimestamp(sunset).strftime('%-I:%M %p'))

    url_forecast = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely&appid={key}'

    response_forecast = requests.get(url_forecast).json()
    print(response_forecast)

   
    return render_template('weather.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
