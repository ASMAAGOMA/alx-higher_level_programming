#!/usr/bin/node
if (typeof Process.argv[2] === 'undefined') {
  console.log('No argument');
} else {
  const firstArg = Process.argv[2];
  console.log('firstArg');
}