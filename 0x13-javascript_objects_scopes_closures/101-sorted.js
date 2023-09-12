#!/usr/bin/node
const dict = require('./101-data').dict;
const myNewDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (myNewDict[value] === undefined) {
    myNewDict[value] = [key];
  } else {
    myNewDict[value].push(key);
  }
}

console.log(myNewDict);
