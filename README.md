# Weather App
A weather application that provides current and forecasted weather utilizing user's zipcode.

Live Site: 

## Features
- Utilizes OpenWeather API 
- Displays current day's weather details, including conditions, temperatures, humidity, and sunset/sunrise
- Provides 4 days forecast with weather conditions and day and night temperatures
- Provides user with any active emergency alerts from the National Weather Service

## Tech
- JavaScript
- Python
- HTML
- CSS
- Flask
- Jinja2

## Installation

In order to run the app locally on your machine: 

##### Create and activate a Python virtual enrivonment and install dependencies
````python
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
````
##### API utilization
Create a free account on https://openweathermap.org/ and generate an API Key
Input the following in your terminal: 
````python
export API_KEY='YOUR_API_KEY_HERE'
````

##### Run the server file
````python
python3 server.py
````
Verify the deployment by navigating to your server address in your preferred browser
```
localhost:5000
```




