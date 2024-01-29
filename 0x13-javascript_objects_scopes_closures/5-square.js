#!/usr/bin/node
Rec = require('./4-rectangle.js');
class Square extends Rec{
  constructor (size) {
    super(size, size);
  }
}

module.exports(Square);
