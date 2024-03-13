#!/usr/bin/node
const Test = require('./5-square');

class Square extends Test {
  charPrint (c) {
    let mywidth = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      mywidth += 'c';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(mywidth);
    }
  }
}
module.exports = Square;
