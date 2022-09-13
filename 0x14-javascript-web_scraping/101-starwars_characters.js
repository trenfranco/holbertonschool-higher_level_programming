#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    const characters = response.data.characters;
    for (let i = 0; i < characters.length; i++) {
      axios.get(characters[i])
        .then(function (response2) {
          console.log(response2.data.name);
        });
    }
  });
