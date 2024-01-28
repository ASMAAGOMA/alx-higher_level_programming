#!/usr/bin/node
function sorting (args) {
//get the numbers from line arguments and turn it into numeric values
  const numbers = args.slice(2).map(Number);
  const sorted = numbers.sort((a, b) => b - a);
  if (sorted.length >= 2) {
    return sorted[1];
  } else {
    return 0;
  }
}
console.log(sorting(process.argv));
