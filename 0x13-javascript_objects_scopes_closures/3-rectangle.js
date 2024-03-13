#!/usr/bin/node

// the Rectangel class
class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0) || isNaN(w) || isNaN(h)) {
      return Object.create(Rectangle.prototype);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let mywidth = '';
    for (let i = 0; i < this.width; i++) {
      mywidth += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(mywidth);
    }
  }
}
module.exports = Rectangle;
