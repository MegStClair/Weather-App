'use strict';


const showWeather = document.getElementById('button');
    
    showWeather.addEventListener('click', () => {
        const weather = document.getElementById('weather');
        
        if (weather.style.display === 'none') {
            weather.style.display = 'block';
        } else {
            weather.style.display = 'none';
        }
        });

const showAlert = document.getElementById('button');
    
    showAlert.addEventListener('click', () => {
        const alert = document.getElementById('footer-container');
        
        if (alert.style.display === 'none') {
            alert.style.display = 'block';
        } else {
            alert.style.display = 'none';
        }
        });
        

const weatherData = document.querySelector('.zipcode-form');

weatherData.addEventListener('submit', (evt) => {
  evt.preventDefault();
  const zipcode = document.querySelector('#zipcode').value;

  const queryString = new URLSearchParams({ zipcode: zipcode }).toString();
  const url = `/weather?${queryString}`;

  fetch(url)
    .then(response => response.json())
    .then(result => {
          
      document.querySelector('.city').innerHTML = 
        `<h1>${result['0']['city']}</h1>`

      document.querySelector('.current').innerHTML = 
        `
        <div id="date"><h1>${result['0']['date']}</h1></div>
        <h1>${result['0']['temp']} &#176;F </h1> 
        <div class="weather-details"> 
          <img class="side-by-side" id="icon" src='http://openweathermap.org/img/w/${result['0']['icon']}.png' style="height:45px; width:45px"></img>
          <div class="side-by-side" id="temp"><h3>${result['0']['weather']}</h3></div>
        </div>
        <div id="temp-details">
          <div class="side-by-side" id="temp-left"> 
            Low: <br>
            High: <br>
            Humidity:
          </div>
          <div class="side-by-side" id="temp-right">
            ${result['0']['temp_min']} &#176;F<br>
            ${result['0']['temp_max']} &#176;F<br>
            ${result['0']['humidity']} %
          </div>
        </div>
        <div class="weather-details">
          <div id="sun">
          ${result['0']['sunrise']} <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-sunrise" viewBox="0 0 16 16"><path d="M7.646 1.146a.5.5 0 0 1 .708 0l1.5 1.5a.5.5 0 0 1-.708.708L8.5 2.707V4.5a.5.5 0 0 1-1 0V2.707l-.646.647a.5.5 0 1 1-.708-.708l1.5-1.5zM2.343 4.343a.5.5 0 0 1 .707 0l1.414 1.414a.5.5 0 0 1-.707.707L2.343 5.05a.5.5 0 0 1 0-.707zm11.314 0a.5.5 0 0 1 0 .707l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zM8 7a3 3 0 0 1 2.599 4.5H5.4A3 3 0 0 1 8 7zm3.71 4.5a4 4 0 1 0-7.418 0H.499a.5.5 0 0 0 0 1h15a.5.5 0 0 0 0-1h-3.79zM0 10a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2A.5.5 0 0 1 0 10zm13 0a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z"/></svg>  
          <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-sunset-fill" viewBox="0 0 16 16"><path d="M7.646 4.854a.5.5 0 0 0 .708 0l1.5-1.5a.5.5 0 0 0-.708-.708l-.646.647V1.5a.5.5 0 0 0-1 0v1.793l-.646-.647a.5.5 0 1 0-.708.708l1.5 1.5zm-5.303-.51a.5.5 0 0 1 .707 0l1.414 1.413a.5.5 0 0 1-.707.707L2.343 5.05a.5.5 0 0 1 0-.707zm11.314 0a.5.5 0 0 1 0 .706l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zM11.709 11.5a4 4 0 1 0-7.418 0H.5a.5.5 0 0 0 0 1h15a.5.5 0 0 0 0-1h-3.79zM0 10a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2A.5.5 0 0 1 0 10zm13 0a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z"/></svg>
          ${result['0']['sunset']}
          </div>
        </div>`


      document.querySelector('#day1').innerHTML = 
        `<div id="date-day_1"><h2>${result['1']['date_1']}</h2></div>
        <div class="weather-details">
          <img class="side-by-side" id="icon-day_1" src='http://openweathermap.org/img/w/${result['1']['icon_1']}.png'></img>
          <div class="side-by-side" id="temp-day_1"><h3> ${result['1']['weather_1']}</h3></div>
        </div>
        <div id="temp-details-day_1">
            <div class="side-by-side" id="temp-left-day_1"> 
              Day: <br>
              Night:
            </div>
            <div class="side-by-side" id="temp-right-day_1">
              ${result['1']['day_1']} &#176;F<br>
              ${result['1']['night_1']} &#176;F
            </div>
        </div>`

      document.querySelector('#day2').innerHTML =
        `<div id="date-day_2"><h2>${result['1']['date_2']}</h2></div>
          <div class="weather-details">
            <img class="side-by-side" id="icon-day_2" src='http://openweathermap.org/img/w/${result['1']['icon_2']}.png'></img>
            <div class="side-by-side" id="temp-day_2"><h3> ${result['1']['weather_2']}</h3></div>
          </div>
            <div id="temp-details-day_2">
              <div class="side-by-side" id="temp-left-day_2"> 
                Day: <br>
                Night:
              </div>
              <div class="side-by-side" id="temp-right-day_2">
                ${result['1']['day_2']} &#176;F<br>
                ${result['1']['night_2']} &#176;F
              </div>
          </div>`
      
      document.querySelector('#day3').innerHTML =
        `<div id="day_3">
          <div id="date-day_3"><h2>${result['1']['date_3']}</h2></div>
          <div class="weather-details">
            <img class="side-by-side" id="icon-day_3" src='http://openweathermap.org/img/w/${result['1']['icon_3']}.png'></img>
            <div class="side-by-side" id="temp-day_3"><h3> ${result['1']['weather_3']}</h3></div>
          </div>
          <div id="temp-details-day_3">
              <div class="side-by-side" id="temp-left-day_3"> 
                Day: <br>
                Night:
              </div>
              <div class="side-by-side" id="temp-right-day_3">
                ${result['1']['day_3']} &#176;F<br>
                ${result['1']['night_3']} &#176;F
              </div>
          </div>`

      document.querySelector('#day4').innerHTML =
        `<div id="day_4">
          <div id="date-day_4"><h2>${result['1']['date_4']}</h2></div>
          <div class="weather-details">
            <img class="side-by-side" id="icon-day_4" src='http://openweathermap.org/img/w/${result['1']['icon_4']}.png'></img>
            <div class="side-by-side" id="temp-day_4"><h3> ${result['1']['weather_4']}</h3></div>
          </div>
          <div id="temp-details-day_4">
              <div class="side-by-side" id="temp-left-day_4"> 
                Day: <br>
                Night:
              </div>
              <div class="side-by-side" id="temp-right-day_4">
                ${result['1']['day_4']} &#176;F<br>
                ${result['1']['night_4']} &#176;F
              </div>
          </div>`
        ;

      document.querySelector('#alert').innerHTML =
        `<div><h3>ALERT: ${result['2']['event']}</h3>
        <b>${result['2']['start']} - ${result['2']['end']}: ${result['2']['sender']}</b> <br>
        ${result['2']['description']}
        </div>
        `
    })
});