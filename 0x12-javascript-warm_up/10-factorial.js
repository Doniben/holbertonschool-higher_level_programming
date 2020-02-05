#!/usr/bin/node

const arg = process.argv[2];

function Factorial (a) {
  if (a === 0) {
    return (1);
  }
  return a * Factorial(a - 1);
}

if (parseInt(arg)) {
  console.log(Factorial(parseInt(arg)));
} else {
  console.log('1');
}
