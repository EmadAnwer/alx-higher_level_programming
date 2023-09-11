#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction.call(theFunction, number);
};
