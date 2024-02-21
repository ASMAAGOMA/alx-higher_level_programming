#!/usr/bin/node
// response
const req = require('request');
const link = process.argv[2];
req.get(link,
  function (error, response) {
    if (error) {
      console.log(error);
    } else {
        console.log('code: ' + response.statusCode);
    }
  });
