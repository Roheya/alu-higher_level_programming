#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body);
  let count = 0;

  films.results.forEach((film) => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count += 1;
    }
  });

  console.log(count);
});
