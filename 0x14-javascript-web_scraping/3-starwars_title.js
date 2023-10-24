#!/usr/bin/node
// get request
const request = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const move = JSON.parse(body);
    console.log(move.title);
  }
});
