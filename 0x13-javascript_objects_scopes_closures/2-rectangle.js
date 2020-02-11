#!/usr/bin/node
// Take 2 arguments w and h. Create an empty object if w or h is 0 or not a positive integer, create an empty object

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
