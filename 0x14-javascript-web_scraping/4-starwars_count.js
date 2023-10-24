#!/usr/bin/node
// get request
const request = require('request');
const url = process.argv[2];
if (!url) process.exit();
request.get(url, (error, response, body) => {
  const characterID = '/18';
  let count = 0;
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body);
    for (let index = 0; index < films.count; index++) {
      for (const character of films.results[index].characters) {
        if (character.search(characterID) !== -1) count++;
      }
    }
    console.log(count);
  }
});
