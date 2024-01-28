#!/usr/bin/node
if (Process.argv[2] === null) {
  console.log('No argument');
} else {
  firstArg = Process.argv[2]
  console.log(firstArg);
}