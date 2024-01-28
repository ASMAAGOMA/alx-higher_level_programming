#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
let row = '';
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < number; j++) {
    for (let i = 0; i < number; i++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
}
