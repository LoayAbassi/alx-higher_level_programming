#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) && w > 0 && !isNaN(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
}
module.exports = Rectangle;
