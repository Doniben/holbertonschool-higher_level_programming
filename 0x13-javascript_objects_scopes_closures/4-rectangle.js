#!/usr/bin/node

module.exports =
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h)) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    while (this.height) {
      console.log('X'.repeat(this.width));
      this.height--;
    }
  }

  rotate () {
    const cambio = this.height;
    this.height = this.width;
    this.width = cambio;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
