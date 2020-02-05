#!/usr/bin/node
const num = parseInt(process.argv[2]);
const string = 'C is fun';
let i = 0;
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < num; i++) {
    console.log(string);
  }
}
