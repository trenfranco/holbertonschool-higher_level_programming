#!/usr/bin/node
/* omputes and prints a factorial  */

const num = parseInt(process.argv[2]);
if (!num) {
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return (factorial(num - 1) * num);
}
