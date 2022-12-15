'use strict';

const weatherData = document.querySelector('.zipcode-form');

weatherData.addEventListener('submit', (evt) => {
  evt.preventDefault();
  const zipcode = document.querySelector('#zipcode').value;

  const queryString = new URLSearchParams({ zipcode: zipcode }).toString();
  const url = `/weather?${queryString}`;

  fetch(url)
    .then(response => response.json())
    .then(result => {
      console.log(result)
      document.getElementById('result').innerHTML = result['city'];
    })
  console.log('fetched')
});



