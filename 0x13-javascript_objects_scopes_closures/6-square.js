#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the rectangle using the character c
const Square = require('./5-square');
let ch = 'X';
class Squares extends Square {
  charPrint (c) {
    if (c) {
      ch = c;
    }
    for (let x = 0; x < this.height; x++) {
      console.log(ch.repeat(this.width));
    }
  }
}
module.exports = Squares;
