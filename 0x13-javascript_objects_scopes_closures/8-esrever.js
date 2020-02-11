#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  let i = list.length - 1;
  const rev = [];
  while (i >= 0) {
    rev.push(list[i]);
    i--;
  }
  return (rev);
};
