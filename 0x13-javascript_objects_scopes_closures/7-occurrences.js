#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      sum++;
    }
  }
  return sum;
};
