from flask import Flask, render_template, request, jsonify

import os
import requests

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def show_weather():
    """Show weather homepage."""

    return render_template('weather.html')


@app.route('/weather')
def search_location():
    """Get weather data."""

    zipcode = request.args.get('zipcode')

    key = os.environ['API_KEY']

    # API call to  get lat & lon
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={key}'

    response = requests.get(url).json()
    
    lat = response['lat']
    lon = response['lon']

    # API call to get 4 day forecast
    url_forecast = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,minutely&appid={key}'

    response_forecast = requests.get(url_forecast).json()

    # Current day data
    city = response['name']
    temp = round(response_forecast['current']['temp'])
    weather = response_forecast['current']['weather'][0]['description']
    icon = response_forecast['current']['weather'][0]['icon']
    temp_min = round(response_forecast['daily'][0]['temp']['min'])
    temp_max = round(response_forecast['daily'][0]['temp']['max'])
    humidity = response_forecast['current']['humidity']
    sunrise = datetime.fromtimestamp(response_forecast['current']['sunrise']).strftime('%-I:%M %p')
    sunset = datetime.fromtimestamp(response_forecast['current']['sunset']).strftime('%-I:%M %p')
    date = datetime.fromtimestamp(response_forecast['current']['dt']).strftime('%A')

    current_day = {
        "city": city,
        "temp":temp,
        "weather": weather,
        "icon": icon,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "humidity":humidity,
        "sunrise": sunrise,
        "sunset": sunset,
        "date": date,
    }

    print(current_day)

    # Forecast data
    day_1 = round(response_forecast['daily'][1]['temp']['day'])
    night_1 = round(response_forecast['daily'][1]['temp']['night'])
    weather_1 = response_forecast['daily'][1]['weather'][0]['main']
    icon_1 = response_forecast['daily'][1]['weather'][0]['icon']
    date_1 = datetime.fromtimestamp(response_forecast['daily'][1]['dt']).strftime('%a')

    day_2 = round(response_forecast['daily'][2]['temp']['day'])
    night_2 = round(response_forecast['daily'][2]['temp']['night'])
    weather_2 = response_forecast['daily'][2]['weather'][0]['main']
    icon_2 = response_forecast['daily'][2]['weather'][0]['icon']
    date_2 = datetime.fromtimestamp(response_forecast['daily'][2]['dt']).strftime('%a')

    day_3 = round(response_forecast['daily'][3]['temp']['day'])
    night_3 = round(response_forecast['daily'][3]['temp']['night'])
    weather_3 = response_forecast['daily'][3]['weather'][0]['main']
    icon_3 = response_forecast['daily'][3]['weather'][0]['icon']
    date_3 = datetime.fromtimestamp(response_forecast['daily'][3]['dt']).strftime('%a')
    
    day_4 = round(response_forecast['daily'][4]['temp']['day'])
    night_4 = round(response_forecast['daily'][4]['temp']['night'])
    weather_4 = response_forecast['daily'][4]['weather'][0]['main']
    icon_4 = response_forecast['daily'][4]['weather'][0]['icon']
    date_4 = datetime.fromtimestamp(response_forecast['daily'][4]['dt']).strftime('%a')

    forecast = {
        "day_1": day_1,
        "night_1": night_1,
        "weather_1": weather_1,
        "icon_1": icon_1,
        "date_1": date_1,
        
        "day_2": day_2,
        "night_2": night_2,
        "weather_2": weather_2,
        "icon_2": icon_2,
        "date_2": date_2,

        "day_3": day_3,
        "night_3": night_3,
        "weather_3": weather_3,
        "icon_3": icon_3,
        "date_3": date_3,

        "day_4": day_4,
        "night_4": night_4,
        "weather_4": weather_4,
        "icon_4": icon_4,
        "date_4": date_4,
    }
    print(forecast)

    return jsonify([current_day, forecast])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
