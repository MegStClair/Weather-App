from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/weather')
def show_weather():
    """Show weather homepage."""

    return render_template('weather.html')


@app.route('/search', methods=['POST'])
def search_location():
    """Get location input."""

    location = request.form.get('search')

    return render_template('weather.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
