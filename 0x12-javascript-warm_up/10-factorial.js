#!/usr/bin/node
const num = parseInt(process.argv[2]);
function fact (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  } else {
    return fact(num - 1) * num;
  }
}
console.log(fact(num));
