#!/usr/bin/node
// Writes a string to a file.

const fs = require('fs');

const write = process.argv[3];

fs.writeFile(process.argv[2], write, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
