#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2]).then(resp => {
  console.log('code: ' + resp.status);
});
