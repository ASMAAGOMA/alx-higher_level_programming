#!/usr/bin/node
if (typeof process.argv[2] === 'undefined') {
    console.log('undefined is undefined');
  } else if (process.argv.length === 3) {
    const firstArg = process.argv[2] + ' is undefined';
    console.log(firstArg);
  } else {
    const twoArgs = process.argv[2] + ' is ' + process.argv[3];
    console.log(twoArgs);
  }
