#!/usr/bin/node
//  prints the number of movies where the character Wedge Antilles is present
const axios = require('axios');

let count = 0;

axios
  .get(process.argv[2])
  .then(request => {
    const films = request.data.results;
    for (let i = 0; i < films.length; i++) {
      const chars = films[i].characters;
      for (let i2 = 0; i2 < chars.length; i2++) {
        if (chars[i2].includes('18')) { count++; }
      }
    }
    console.log(count);
  });
