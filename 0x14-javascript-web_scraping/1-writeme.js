#!/usr/bin/node
// write
const file = require('fs');
file.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
