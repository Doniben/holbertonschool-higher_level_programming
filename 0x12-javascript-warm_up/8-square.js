#!/usr/bin/node

const times = parseInt(process.argv[2]);
let count = 0;
const X = 'X';
let Xs = '';

if (!times) {
  console.log('Missing size');
}

while (count < times) {
  Xs = Xs + X;
  count += 1;
}

count = 0;

while (count < times) {
  console.log(Xs);
  count += 1;
}
