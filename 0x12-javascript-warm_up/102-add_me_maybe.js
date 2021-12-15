#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const increment = ++number;
  theFunction(increment);
};
