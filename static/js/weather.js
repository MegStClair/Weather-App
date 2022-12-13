'use strict';

const weatherData = document.querySelector('.zipcode-form');

weatherData.addEventListener('submit', (evt) => {
  evt.preventDefault();

  const zipcode = document.querySelector('#zipcode').value;
  console.log(zipcode)
});

