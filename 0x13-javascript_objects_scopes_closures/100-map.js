#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const list2 = list.map((item, index) => item * index);
console.log(list2);
