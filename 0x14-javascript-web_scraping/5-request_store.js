#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const axios = require('axios');
const fs = require('fs');

axios
  .get(process.argv[2])
  .then(request => {
    const text = request.data;
    fs.appendFile(process.argv[3], text, { encoding: 'utf8' }, err => {
      if (err) { console.log(err); }
    });
  });
