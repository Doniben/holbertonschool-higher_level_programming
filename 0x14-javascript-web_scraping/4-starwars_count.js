#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  } else {
  let count1 = 0;
  const results = JSON.parse(body).results;
  const count = JSON.parse(body).count;
  for (let i = 0; i < count; i++) {
    if (results[i].characters.includes('https://swapi.co/api/people/18/')) {
      count1++;
    }
  }
  console.log(count1);
  }
});
