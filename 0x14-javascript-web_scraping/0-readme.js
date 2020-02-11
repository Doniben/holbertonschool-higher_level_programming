#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (data === undefined) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
