#!/usr/bin/node

const number1 = parseInt(process.argv[2]);
const number2 = parseInt(process.argv[3]);

const sum = add(number1, number2);
console.log(sum);

function add (a, b) {
  if (!a || !b) {
    return ('NaN');
  } else {
    return (a + b);
  }
}
