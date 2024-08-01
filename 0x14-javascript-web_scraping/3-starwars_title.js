#!/usr/bin/node

const request = require('request');
const endP = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(endP, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
