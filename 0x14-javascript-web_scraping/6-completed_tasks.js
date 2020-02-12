#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const ocu = {};
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed) {
        if (ocu[todos[i].userId] === undefined) {
          ocu[todos[i].userId] = 1;
        } else {
          ocu[todos[i].userId] += 1;
        }
      }
    }
    console.log(ocu);
  }
});
