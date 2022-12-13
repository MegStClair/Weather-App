from flask import Flask, render_template, request, jsonify

import os
import requests

from datetime import datetime

app = Flask(__name__)


@app.route('/weather')
def show_weather():
    """Show weather homepage."""

    return render_template('weather.html')


@app.route('/search')
def search_location():
    """Get location input."""

    zipcode = request.args.get('search')
    print(zipcode)
    key = os.environ['API_KEY']

    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={key}'

    response = requests.get(url)
    data = response.json()
    print(data)

    lat = data['lat']
    lon = data['lon']
    print(lat, lon)

    # url_forecast = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,minutely&appid={key}'

    # response_forecast = requests.get(url_forecast).json()

    # print(response_forecast)

    # city = data['name']
    # print(city)

    # temp = round(response_forecast['current']['temp'])
    # print(temp)

    # weather = response_forecast['current']['weather'][0]['description']
    # print(weather)

    # icon = response_forecast['current']['weather'][0]['icon']
    # print(icon)

    # temp_min = round(response_forecast['daily'][0]['temp']['min'])
    # print(temp_min)

    # temp_max = round(response_forecast['daily'][0]['temp']['max'])
    # print(temp_max)

    # humidity = response_forecast['current']['humidity']
    # print(humidity)

    # sunrise = response_forecast['current']['sunrise']
    # sunset = response_forecast['current']['sunset']

    # print(datetime.fromtimestamp(sunrise).strftime('%-I:%M %p'))
    # print(datetime.fromtimestamp(sunset).strftime('%-I:%M %p'))

    # day_1 = round(response_forecast['daily'][1]['temp']['day'])
    # night_1 = round(response_forecast['daily'][1]['temp']['night'])
    # weather_1 = response_forecast['daily'][1]['weather'][0]['main']
    # icon_1 = response_forecast['daily'][1]['weather'][0]['icon']

    # print(datetime.fromtimestamp(response_forecast['daily'][1]['dt']))

    # day_2 = round(response_forecast['daily'][2]['temp']['day'])
    # night_2 = round(response_forecast['daily'][2]['temp']['night'])
    # weather_2 = response_forecast['daily'][2]['weather'][0]['main']
    # icon_2 = response_forecast['daily'][2]['weather'][0]['icon']

    # day_3 = round(response_forecast['daily'][3]['temp']['day'])
    # night_3 = round(response_forecast['daily'][3]['temp']['night'])
    # weather_3 = response_forecast['daily'][3]['weather'][0]['main']
    # icon_3 = response_forecast['daily'][3]['weather'][0]['icon']

    # day_4 = round(response_forecast['daily'][4]['temp']['day'])
    # night_4 = round(response_forecast['daily'][4]['temp']['night'])
    # weather_4 = response_forecast['daily'][4]['weather'][0]['main']
    # icon_4 = response_forecast['daily'][4]['weather'][0]['icon']

    # print('*******FORECAST*******')
    # print(day_1)
    # print(night_1)
    # print(weather_1)
    # print(icon_1)

    # return render_template('weather.html')
    return jsonify(data) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
