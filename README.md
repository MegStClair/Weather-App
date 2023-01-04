# Weather App
A weather application that provides current and forecasted weather utilizing user's zip code.

![weatherapp1](https://user-images.githubusercontent.com/110854972/210621861-2fa6c6ce-e4bd-4ec3-8bc5-437941b5af87.gif)
 

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


![weather-app-alert](https://user-images.githubusercontent.com/110854972/210629301-30b16235-5254-4bb1-89ec-0aec5e65f4b0.gif)

## Installation

In order to run the app locally on your machine: 

#### Create and activate a Python virtual enrivonment and install dependencies
````python
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
````
#### API utilization
Create a free account on https://openweathermap.org/ and generate an API Key
Input the following in your terminal: 
````python
export API_KEY='YOUR_API_KEY_HERE'
````

#### Run the server file
````python
python3 server.py
````
#### Verify the deployment by navigating to your server address in your preferred browser
```
localhost:5000
```




