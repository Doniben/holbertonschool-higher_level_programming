#!/usr/bin/node

const request = require('request');
let url = process.argv[2];

request.get(url, (error, responde, body) => {
  if(error) {
    return console.log(error);
  } else {
    const dic = {};
    const data = JSON.parse(body);
    for(i = 0; i < data.length; i++) {
      if(data[i].completed) {
	if(dic[data[i].userId]){
	  dic[data[i].userId]++;
	} else {
	  dic[data[i].userId] = 1;
	}
      }
    }
    console.log(dic)
  }
});
