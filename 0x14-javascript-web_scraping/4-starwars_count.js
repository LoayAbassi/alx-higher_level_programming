#!/usr/bin/node

const wanted = 18;
const api = process.argv[2];

const request = require('request');

request(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    let nb = 0;
    const films = JSON.parse(body).results;
    let characters = [];
    for (let i = 0; i < films.length; i++) {
      characters = films[i].characters;
      console.log(characters);

      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes(wanted)) {
          nb++;
        }
      }
    }
    console.log(nb);
  }
});
