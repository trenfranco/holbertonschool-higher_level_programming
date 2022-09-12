#!/usr/bin/node

const fs = require('fs');

fs.appendFile(process.argv[2], process.argv[3], { encoding: 'utf8' }, function (err) {
  if (err) {
    console.log(err);
  }
});
