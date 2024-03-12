#!/usr/bin/node

function isDigite (value) {
  return /^\d+$/.test(value);
}

const { argv } = require('node:process');

if (isDigite(argv[2])) {
  const number = parseInt(argv[2]);
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
