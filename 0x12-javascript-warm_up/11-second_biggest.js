#!/usr/bin/node
const args = process.argv.slice(2);
function sb (arr) {
  arr = arr.map(Number);
  const x = arr.filter(element => element !== Math.max(...arr));
  return Math.max(...x);
}

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(sb(args));
}
