#!/usr/bin/node
// star wars
const req = require('request');
let count = 0;
const link = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req.get(link,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body);
      films.results.forEach(film => {
        film.characters.forEach((character) => {
          if (character.includes(18)) {
            count += 1;
          }
        });
      });
      console.log(count);
    }
  });
