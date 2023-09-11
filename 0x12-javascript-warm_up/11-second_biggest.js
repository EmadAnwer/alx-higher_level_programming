#!/usr/bin/node

const secondBiggest = process.argv.slice(2).sort().reverse()[1];
console.log(secondBiggest === undefined ? 0 : secondBiggest);
