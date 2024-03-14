#!/usr/bin/node

const { argv } = require('node:process');
function add (a, b) {
  return a + b;
}
function isDigite (value) {
  return /^-?\d+$/.test(value);
}

if (argv.length < 4) {
  console.log('NaN');
} else {
  if (isDigite(argv[2]) && isDigite(argv[3])) {
    const result = add(Number(argv[2]), Number(argv[3]));
    console.log(result);
  } else {
    console.log('NaN');
  }
}
