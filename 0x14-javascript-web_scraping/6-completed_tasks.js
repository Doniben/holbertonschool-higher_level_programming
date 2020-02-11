#!/usr/bin/node

const request = require('request');
let url = process.argv[2];

request.get(url, (error, responde, body) => {
  if(error) {
    return console.log(error);
  } else {
    const data = JSON.parse(body);
    for(i = 0; i < data; i++) {
      (if )
    }
  }
})
