#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movies = JSON.parse(body).results;
  const count = movies.filter(movie =>
    movie.characters.some(character => character.includes('/18/'))
  ).length;

  console.log(count);
});
