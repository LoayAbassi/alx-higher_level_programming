#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  const unbtc = {};
  tasks = JSON.parse(body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed == true) {
      if (unbtc.hasOwnProperty(tasks[i].userId)) {
        unbtc[tasks[i].userId] += 1;
      } else {
        unbtc[tasks[i].userId] = 1;
      }
    }
  }
  console.log(unbtc);
});
