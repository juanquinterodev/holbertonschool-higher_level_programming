#!/usr/bin/node
// Prints all characters of a Star Wars movie
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
