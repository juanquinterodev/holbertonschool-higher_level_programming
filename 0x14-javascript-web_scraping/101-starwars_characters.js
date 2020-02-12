#!/usr/bin/node
// Display one character name by line in the same order of the list characters in the /films/ response
const request = require('request');
const url = 'http://swapi.co/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body).characters;
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
