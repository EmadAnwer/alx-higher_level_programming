#!/usr/bin/node
const len = Number(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < len; index++) {
    console.log('C is fun');
  }
}
