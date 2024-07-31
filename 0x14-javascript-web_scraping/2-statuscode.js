#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

//not all parameters are required

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});