#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  const size = list.length - 1;
  let i;
  for (i = size; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
