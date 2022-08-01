#!/usr/bin/node
/*  prints  */

const a = parseInt(process.argv[2]);
if (!a) {
  console.log('Not a number');
} else {
  console.log('My number: ', a);
}
