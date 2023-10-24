#!/usr/bin/node
// get request
const request = require('request');
const url = process.argv[2];
if (!url) process.exit();
request.get(url, (error, response, body) => {
  const character18URL = 'https://swapi-api.alx-tools.com/api/people/18/';
  if (!error && response.statusCode === 200) {
    let count = 0;
    const films = JSON.parse(body);
    for (let index = 0; index < films.count; index++) {
      for (const character of films.results[index].characters) {
        if (character === character18URL) count++;
      }
    }
    console.log(count);
  }
});
