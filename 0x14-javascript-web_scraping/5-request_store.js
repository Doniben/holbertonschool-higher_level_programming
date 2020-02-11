#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, responde, body) => {
  if (error) {
    return console.log(error);
  } else {
    fs.writeFile(file, body, error => {
      if (error) {
        console.log(error);
      }
    });
  }
});
