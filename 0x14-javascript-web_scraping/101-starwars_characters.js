#!/usr/bin/node
// prints all characters of a Star Wars movie

const axios = require('axios');
const id = process.argv[2];

async function getNames () {
  try {
    const response = await axios.get('https://swapi-api.hbtn.io/api/films/' + id);
    for (const character in response.data.characters) {
      const responseC = await axios.get(response.data.characters[character]);
      console.log(responseC.data.name);
    }
  } catch (error) {
    console.log(error);
  }
}
getNames();
