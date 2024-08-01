#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(path, body, (err) => {
      if (err) {
        console.log(err);
      }
    }
    );
  }
});
