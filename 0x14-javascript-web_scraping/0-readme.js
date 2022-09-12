#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], { encoding: 'utf8' }, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
