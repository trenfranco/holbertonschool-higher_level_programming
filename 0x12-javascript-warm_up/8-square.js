#!/usr/bin/node
/* prints a square  */

const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
}
