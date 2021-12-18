#!/usr/bin/node
exports.converter = function (base) {
  // using closure
  return function (num) {
    return num.toString(base);
  };
};
