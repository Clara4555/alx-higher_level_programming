#!/usr/bin/node
const SquareSub = require('./5-square');

class Square extends SquareSub {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let b = '';
      for (let d = 0; d < this.width; d++) {
        b = b + d;
      }
      console.log(b);
    }
  }
}

module.exports = Square;
