#!/usr/bin/node

const secondBiggest = process.argv
  .slice(2)
  .map(Number)
  .sort((a, b) => b - a)[1];
console.log(secondBiggest === undefined ? 0 : secondBiggest);
