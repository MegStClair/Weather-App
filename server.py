from flask import Flask, render_template

app = Flask(__name__)


@app.route('/weather')
def show_weather():

    return render_template('weather.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
