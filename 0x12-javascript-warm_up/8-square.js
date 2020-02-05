#!/usr/bin/node
const num = parseInt(process.argv[2]);
const sq = 'X';
let i = 0;
if (process.argv.length === 2 || isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    console.log(sq.repeat(num));
  }
}
