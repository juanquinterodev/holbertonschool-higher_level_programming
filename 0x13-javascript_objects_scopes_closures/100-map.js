#!/usr/bin/node
// Imports an array and computes a new array.
const init = require('./100-data').list;
console.log(init);
const newlist = init.map(function (x, y) { return (x * y); });
console.log(newlist);
