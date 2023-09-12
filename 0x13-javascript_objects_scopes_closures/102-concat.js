#!/usr/bin/node

const fs = require('fs');
let fileOne, fileTwo;

try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  fileOne = data;
} catch (err) {
  console.error(err);
}

try {
  const data = fs.readFileSync(process.argv[3], 'utf8');
  fileTwo = data;
} catch (err) {
  console.error(err);
}

try {
  fs.writeFileSync(process.argv[4], (fileOne + fileTwo));
} catch (err) {
  console.error(err);
}
