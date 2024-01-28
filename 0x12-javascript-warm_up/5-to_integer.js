#!/usr/bin/node
if (typeof process.argv[2] === 'undefined' || process.argv.length !== 3) {
  console.log('Not a number');
} else {
  const number = Math.floor(Number(process.argv[2]));
  if (isNaN(number)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${number}`);
  }
}
