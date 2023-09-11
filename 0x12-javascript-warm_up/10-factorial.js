#!/usr/bin/node
const num = Number(process.argv[2]);
if (num >= 0 || isNaN(num)) console.log(fact(num));

function fact (number) {
  if (number === 0 || isNaN(number)) return 1;
  else return number * fact(number - 1);
}
