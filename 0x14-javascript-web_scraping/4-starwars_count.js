#!/usr/bin/node
// get request
const request = require('request');
const url = process.argv[2];
if (!url) process.exit();
request.get(url, (error, response, body) => {
  const characterID = '18';
  let count = 0;
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const movies = data.results;
    let count = 0;

    for (const movie of movies) {
      if (
        movie.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/${characterID}/`
        )
      ) {
        count++;
      }
    }
    console.log(count);
  }
});
