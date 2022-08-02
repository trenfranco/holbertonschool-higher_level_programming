#!/usr/bin/node
/* Rectangle class  */

class Rectangle {
  constructor (w, h) {
    if (w && h && w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const flag = this.width;
    this.width = this.height;
    this.height = flag;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
