#!/usr/bin/node
// get request
const request = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const filmsURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
const makeRequest = (url) =>
  new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else {
        console.log(JSON.parse(body).name);
        resolve();
      }
    });
  });
request.get(filmsURL, (error, response, body) => {
  if (!error) {
    const charactersInMovie = JSON.parse(body).characters;
    for (const char of charactersInMovie) {
      makeRequest(char);
    }
  } else console.log(error);
});
