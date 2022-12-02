from flask import Flask, render_template, request

import os
import requests

app = Flask(__name__)


@app.route('/weather')
def show_weather():
    """Show weather homepage."""

    return render_template('weather.html')


@app.route('/search', methods=['POST'])
def search_location():
    """Get location input."""

    zipcode = request.form.get('search')

    key = os.environ['API_KEY']

    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode}&appid={key}'

    # url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={key}'

    # url = f'https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${key}&units=imperial)'

    # https://api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}

    response = requests.get(url)
    data = response.json()
    print(data)

    return render_template('weather.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
