#!/usr/bin/node
// get request
const request = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const filmsURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
const responses = [];

function makeRequest (url, len, index) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      responses[index] = body;
    }
    if (responses.length === len) {
      responses.forEach((response) => {
        console.log(JSON.parse(response).name);
      });
    }
  });
}

request.get(filmsURL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const charactersInMovie = JSON.parse(body).characters;
    charactersInMovie.forEach((char, index) => {
      makeRequest(char, charactersInMovie.length, index);
    });
  }
});
