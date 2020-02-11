#!/usr/bin/node
// Returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let sum = 0;
  for (x = 0; x < list.length; x++) {
    if (searchElement === list[x]) {
      sum++;
    }
  }
  return (sum);
};
