#!/usr/bin/node
// star wars
const req = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req.get(link,
  function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }
    const film = JSON.parse(body);
    const characters = film.characters;
    let count = 0;
    const characterId = '18';
    characters.forEach(characterURL => {
      if (characterURL.includes(`/api/people/${characterId}/`)) {
        count++;
      }
    });
    console.log(count);
  });
