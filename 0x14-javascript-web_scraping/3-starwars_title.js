#!/usr/bin/node
// request get to get the data (json)
const axios = require('axios');

axios
  .get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(response => {
    console.log(response.data.title);
  });
