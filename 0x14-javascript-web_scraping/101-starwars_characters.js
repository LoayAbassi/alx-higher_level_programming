#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url,(err,response,body)=>{
    if (err) {
        console.log(err);
    } else {
        const film = JSON.parse(response);
        console.log(film);
    }
});

/*
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tab = JSON.parse(body).characters;
    for (let i = 0; i < tab.length; i++) {
      request(tab[i], (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});*/
