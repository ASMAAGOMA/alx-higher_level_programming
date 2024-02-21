#!/usr/bin/node
// star wars
const req = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req.get(link,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
