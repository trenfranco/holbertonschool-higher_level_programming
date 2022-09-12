#!/usr/bin/node
//  prints the number of movies where the character Wedge Antilles is present
const axios = require('axios');

let count = 0;

axios
  .get(process.argv[2])
  .then(request => {
    const films = request.data.results;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  });
