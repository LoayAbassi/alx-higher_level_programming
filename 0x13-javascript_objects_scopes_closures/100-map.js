#!/usr/bin/node

const { list } = require('./100-data');

console.log(list);
const neww = list.map((e, i) => i * e);
console.log(neww);
