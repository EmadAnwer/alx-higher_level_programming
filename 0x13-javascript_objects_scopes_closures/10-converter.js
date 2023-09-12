#!/usr/bin/node
exports.converter = function (base) {
  return function (decimal) {
    return decimal.toString(base);
  };
};
