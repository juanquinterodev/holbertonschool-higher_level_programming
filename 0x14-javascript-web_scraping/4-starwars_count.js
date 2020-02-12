#!/usr/bin/node
// Prints the number of movies where the character Wedge Antilles is present
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const ocu = JSON.parse(body).results;
    let sum = 0;
    for (let i = 0; i < ocu.length; i++) {
      const chars = ocu[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes('18')) {
          sum++;
        }
      }
    }
    console.log(sum);
  }
});
