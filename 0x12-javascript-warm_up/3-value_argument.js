#!/usr/bin/node
if (typeof process.argv[2] === 'undefined') {
  console.log('No argument');
} else {
  const firstArg = process.argv[2];
  console.log(firstArg);
}
