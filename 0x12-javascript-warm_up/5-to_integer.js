#!/usr/bin/node
const myNumber = Number(process.argv[2]);
console.log(isNaN(myNumber) ? 'Not a number' : 'My number: ' + myNumber);
