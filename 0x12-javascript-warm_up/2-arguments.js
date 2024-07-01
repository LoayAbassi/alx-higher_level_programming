#!/usr/bin/node
/* this file counts arguments from terminal and returns number approximately */
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
