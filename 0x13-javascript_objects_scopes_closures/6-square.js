#!/usr/bin/node

const Hell = require('./5-square.js');

class Square extends Hell {
  constructor (size) {
  super(size, size);
  }
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log(Array(this.width + 1).join(c || 'X'));
    }
  }
}
module.exports = Square;
