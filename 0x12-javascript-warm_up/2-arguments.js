#!/usr/bin/node
/* prints a message depending of the number of arguments passed  */

if (process.argv[2] == null) {
  console.log('No argument');
} else if (process.argv[2] != null && process.argv[3] == null) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
