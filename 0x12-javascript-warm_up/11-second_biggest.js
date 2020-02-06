#!/usr/bin/node

const array = process.argv.lenght;

if (array < 4) {
  console.log('0');
} else {
  console.log(process.argv.slice(2).sort(tal));
}

function tal (a, b) {
  return (b - a);
}
