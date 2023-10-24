#!/usr/bin/node
// get request
const request = require('request');
const url = process.argv[2];
if (!url) process.exit();
request.get(url, (error, response, body) => {
  let count = 0;
  if (!error && response.statusCode === 200) {
    try {
      const films = JSON.parse(body);
      for (let index = 0; index < films.count; index++) {
        for (const character_url of films.results[index].characters) {
          const parts = character_url.split('/');
          console.log(parts);
          if (parts[parts.length - 2] === '18') count++;
        }
      }
      console.log(count);
    } catch (error) {
      console.log(error);
    }
  }
});
