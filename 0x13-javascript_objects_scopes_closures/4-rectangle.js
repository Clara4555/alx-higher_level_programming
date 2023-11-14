#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let b = '';
      for (let c = 0; c < this.width; c++) {
        b = b + ' X';
      }
      console.log(s);
    }
  }

  rotate () {
    const switches  = this.width;
    this.width = this.height;
    this.height = switches;
  }

  double () {
    this.width = width * 2;
    this.height = width * 2;
  }
}
module.exports = Rectangle;
