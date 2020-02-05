#!/usr/bin/node

const times = parseInt(process.argv[2]);
let count = 0;
if (!times) {
  console.log('Missing number of occurrences');
} else {
  while (count < times) {
    console.log('C is fun');
    count += 1;
  }
}
