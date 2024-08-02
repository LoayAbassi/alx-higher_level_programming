#!/usr/bin/node
const dict = require('./101-data').dict;
const newSort = {};
for (const user in dict) {
  const occ = dict[user];
  if (occ in newSort) {
    newSort[occ].push(user);
  } else {
    newSort[occ] = [user];
  }
}
console.log(newSort);
