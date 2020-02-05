#!/usr/bin/node
let i = 0;
exports.callMeMoby = function (x, theFunction) {
  for (i = 0; i < x; i++) {
    theFunction();
  }
};
