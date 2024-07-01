#!/usr/bin/node
const args = process.argv;
console.log(fact(args[2]));

function fact (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
