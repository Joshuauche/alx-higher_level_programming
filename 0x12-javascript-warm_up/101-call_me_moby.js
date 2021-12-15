#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (x > i) {
    i++;
    theFunction();
  }
};
