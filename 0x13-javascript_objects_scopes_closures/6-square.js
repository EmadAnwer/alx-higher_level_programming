#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    if (c === undefined) c = 'X';
    console.log((c.repeat(this.width) + '\n').repeat(this.height).slice(0, -1));
  }
}
module.exports = Square;
